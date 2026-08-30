"""Layer 1 — static checks on the skill set. No API calls; runs in milliseconds.

Catches the classes of breakage that are easy to introduce while editing skills:
malformed frontmatter, name/directory drift, dangling skill references, broken
relative links, leftover Cursor artifacts, README/skill mismatch, and step
renumbering slips.
"""

from __future__ import annotations

import re

from common import (
    REPO_ROOT,
    SKILLS_DIR,
    Result,
    iter_skill_docs,
    parse_frontmatter,
    skill_names,
)

# Files outside the skill dirs that still participate in the skill vocabulary.
EXTRA_DOCS = [REPO_ROOT / "CLAUDE.md", REPO_ROOT / "README.md"]

# `foo` immediately followed by "skill", or "skill" followed by `foo`.
_SKILL_REF = re.compile(r"`([a-z][a-z0-9-]{2,})`\s+skill\b|\bskill\s+`([a-z][a-z0-9-]{2,})`")

# Domain words that appear as `word` next to "skill" but are adjectives/status
# values, not skill names.
_NOT_A_SKILL = {
    "this", "that", "the", "a", "an", "same", "one", "each", "any", "new",
    "current", "next", "later", "shaky", "mastered", "learning", "retired",
    "track", "track-level", "lesson-level", "first", "last",
}
_MD_LINK = re.compile(r"\]\(([^)]+)\)")
_CURSOR = re.compile(r"\.cursor\b|\.mdc\b|cursorignore", re.IGNORECASE)
_README_CMD = re.compile(r"^\|\s*`/([a-z][a-z0-9-]+)`\s*\|", re.MULTILINE)
_STEP = re.compile(r"^(\d+)\.\s")
_HEADING = re.compile(r"^#{1,6}\s")


def _check_frontmatter_and_names(results: list[Result]) -> None:
    names = skill_names()
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        fields, body = parse_frontmatter(skill_md.read_text())
        rel = skill_md.relative_to(REPO_ROOT)
        if not fields.get("name"):
            results.append(Result(f"{rel}: has frontmatter `name`", False))
        elif fields["name"] != skill_dir.name:
            results.append(
                Result(
                    f"{rel}: name matches directory",
                    False,
                    f"name={fields['name']!r} dir={skill_dir.name!r}",
                )
            )
        else:
            results.append(Result(f"{rel}: name matches directory", True))
        if not fields.get("description"):
            results.append(Result(f"{rel}: has frontmatter `description`", False))
        if not body.strip():
            results.append(Result(f"{rel}: has a body", False))
    results.append(Result(f"{len(names)} skills discovered", True, ", ".join(sorted(names))))


def _check_skill_references(results: list[Result]) -> None:
    names = skill_names()
    docs = list(iter_skill_docs()) + [p for p in EXTRA_DOCS if p.exists()]
    dangling: list[str] = []
    for doc in docs:
        text = doc.read_text()
        for m in _SKILL_REF.finditer(text):
            token = m.group(1) or m.group(2)
            if token not in names and token not in _NOT_A_SKILL:
                dangling.append(f"{doc.relative_to(REPO_ROOT)}: `{token}` skill")
    results.append(
        Result(
            "all `x` skill references resolve",
            not dangling,
            "; ".join(sorted(set(dangling))),
        )
    )


def _check_relative_links(results: list[Result]) -> None:
    broken: list[str] = []
    for doc in iter_skill_docs():
        for m in _MD_LINK.finditer(doc.read_text()):
            target = m.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("/"):
                resolved = REPO_ROOT / target.lstrip("/")
            else:
                resolved = (doc.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{doc.relative_to(REPO_ROOT)} -> {target}")
    results.append(Result("all relative markdown links resolve", not broken, "; ".join(broken)))


def _check_no_cursor_artifacts(results: list[Result]) -> None:
    hits: list[str] = []
    roots = [SKILLS_DIR, *[p for p in EXTRA_DOCS if p.exists()]]
    files = list(SKILLS_DIR.rglob("*.md")) + [p for p in EXTRA_DOCS if p.exists()]
    for f in files:
        for i, line in enumerate(f.read_text().splitlines(), 1):
            if _CURSOR.search(line):
                hits.append(f"{f.relative_to(REPO_ROOT)}:{i}")
    results.append(Result("no .cursor / .mdc / cursorignore references", not hits, "; ".join(hits)))


def _check_readme_commands(results: list[Result]) -> None:
    readme = REPO_ROOT / "README.md"
    names = skill_names()
    missing = [c for c in _README_CMD.findall(readme.read_text()) if c not in names]
    results.append(
        Result("README command table maps to real skills", not missing, ", ".join(missing))
    )


def _check_step_numbering(results: list[Result]) -> None:
    bad: list[str] = []
    for doc in iter_skill_docs():
        expected = 0  # 0 means "not currently in a numbered block"
        for i, line in enumerate(doc.read_text().splitlines(), 1):
            if _HEADING.match(line):
                expected = 0
                continue
            m = _STEP.match(line)
            if not m:
                continue
            n = int(m.group(1))
            if expected == 0:
                expected = n + 1  # start of a block; accept whatever it opens with
            elif n == expected:
                expected += 1
            elif n == expected - 1:
                pass  # a sibling list restarting is rare; tolerate a repeat
            else:
                bad.append(f"{doc.relative_to(REPO_ROOT)}:{i} expected {expected}, got {n}")
                expected = n + 1
    results.append(Result("numbered instruction steps are sequential", not bad, "; ".join(bad)))


def _check_claude_router(results: list[Result]) -> None:
    """Every skill named in CLAUDE.md's 'Which skill to use' table must exist."""
    claude_md = REPO_ROOT / "CLAUDE.md"
    text = claude_md.read_text()
    start = text.find("Which skill to use")
    if start == -1:
        results.append(Result("CLAUDE.md has a 'Which skill to use' router table", False))
        return
    end = text.find("\n## ", start)
    block = text[start : end if end != -1 else len(text)]
    names = skill_names()
    referenced = set(re.findall(r"`([a-z][a-z0-9-]{2,})`", block))
    unknown = sorted(tok for tok in referenced if tok not in names and tok not in _NOT_A_SKILL)
    results.append(
        Result("CLAUDE.md router table skills all resolve", not unknown, ", ".join(unknown))
    )


def run_lint() -> list[Result]:
    results: list[Result] = []
    _check_frontmatter_and_names(results)
    _check_skill_references(results)
    _check_claude_router(results)
    _check_relative_links(results)
    _check_no_cursor_artifacts(results)
    _check_readme_commands(results)
    _check_step_numbering(results)
    return results


if __name__ == "__main__":
    import sys

    rs = run_lint()
    for r in rs:
        print(r.line())
    sys.exit(0 if all(r.ok for r in rs) else 1)
