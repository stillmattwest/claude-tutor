# Infer scope (before locking a course or track)

Follow this file **before** writing `curriculum/CURRICULUM.md` or `curriculum/MASTERTRACK.md`. Do not lock the path until the student has answered any scope question this file requires.

Applies to `curriculum` and `mastertrack`. Skip when writing a **mapped** live course (intake already happened; the map item is the scope).

Stay encouraging. No gatekeeping. No jargon until you have defined it.

## When the goal is “get a job”

“I just want to get a job,” “I want to be a professional X,” or a job title with no programming background is very common. Handle it carefully and kindly:

1. **Be honest without crushing hope.** You cannot guarantee anyone a job. Landing an entry-level role as a self-taught coder is hard and competitive—say so plainly, without scare tactics or false promises.
2. **Say what this path *can* do.** Real skills, senior-correct habits, and projects that demonstrate ability. A first course or even a full mastertrack is a meaningful stretch—not the whole road to employment.
3. **Invite building later.** After they finish, they can extend (portfolio, interview prep, deeper stack). Do not pretend one course or one track equals a job.
4. **Then infer material scope** (below). A job-title ask is not enough to lock topics.

## Infer the real outcome

Named **tools**, **buzzwords**, and **job titles** are often a proxy—especially early in the journey.

1. **Infer the likely real outcome** from their ask, background, and project idea.
   - Tool example: a new programmer asking for FastAPI often wants to **ship a working website or web app**, not an API-only specialty. An experienced backend engineer asking for the same may want FastAPI depth only.
   - Role example: a new programmer who wants to be a **professional AI engineer** often heard “train models.” In practice that job is still **software engineering**: something other people can use (an app, API, or site), not only notebooks, training, and evaluation. An experienced researcher asking for the same may want modeling depth only.
2. **Map the gap** between what they named and what that outcome usually requires (missing layers: programming foundations, shipping a product, data, models, deploy, etc.).
3. **With beginners, explain the basics before asking about scope.** One or two plain sentences per idea the question needs (e.g. training a model vs putting a program on the internet that other people can use). Do not ask “ML-only vs full-stack” until those words mean something.
4. **Propose the fuller scope and ask**—do not silently inflate or silently omit.
   - Early learners: outcome language only, after the definitions (“Do you want a path that includes building something people can actually use, or focus on training and judging models first—knowing you would not yet be able to ship a product?”).
   - Experienced learners: sharper tradeoffs (“Modeling and eval only, or include serving and a small product around the model?”).
5. **Wait for their answer** before locking the curriculum or map. If they decline adjacent topics, design a coherent narrower path and **write what it will not cover** (see below) so expectations stay honest.
6. Still apply the senior-correct bar inside whatever scope they choose.

## Ship test (required for professional / product / role goals)

If the stated goal is a **job**, a **professional** role, **engineer** in the title, or building products, run this test on the draft path:

- After this path, could they **ship** something another person can use (run, click, or call)—not only complete exercises or notebook experiments?

If the honest answer is **no** (Python + data + train/eval and stop; frontend with no way to deploy; and similar):

1. **Stop.** Do not write the map or `CURRICULUM.md` yet.
2. Say so in outcome language: what they *would* be able to do, and that they would **not** yet be able to ship a product.
3. Propose the missing shipping layer at the right depth (foundations, a small service or app, deploy as needed)—justified by *their* goal, not a generic extra stack.
4. **Wait.** Lock only after they choose fuller (include shipping) or narrower (specialty only).

For **no programming background** plus **professional [role]**, recommend the fuller path that includes shipping. Do not lock a specialty-only track unless they explicitly accept “cannot ship a product yet.”

## Protect them from what they don't know

- Prefer the **current default good path** for the language, framework, and project type (packaging, project layout, testing, env/config, version control, and other norms seniors expect). Example: prefer `uv` for new Python projects over ad-hoc `pip` unless the domain truly requires otherwise.
- Include **foundation topics they did not ask for** when those are prerequisites for doing the desired skill well (e.g. Git, tests, project structure before a web API or ML course). Keep those lean and justified by the end goal—do not pad.
- If they request an approach a senior would consider outdated, fragile, or misleading for learning, **do not silently adopt it**. Briefly say what you recommend instead and why (one or two sentences), then design on the sound path unless they insist after hearing the tradeoff.
- Optimize for **transfer**: habits that still look right on the next project, not tutorial magic that only works in this repo.
- Sequence so each new tool appears when it first matters, with a plain-language “what / why” in that lesson or track-skill end goal.

## Write what it will not cover

After they choose:

- **Map** (`curriculum/MASTERTRACK.md`): include an **Out of scope** section (plain language, a short list). If they chose the fuller path, list only what is still genuinely outside (e.g. this track still does not guarantee a job; it does not include X specialty). If they chose narrower, the first bullet must be the honest gap (e.g. they will not yet be able to ship a product).
- **Single course** (`curriculum/CURRICULUM.md`): same idea in a short **Out of scope** note under the title (after `# Current lesson:`), so later chats do not “forget.”

Do not hide out-of-scope in tutor-only files. The student should be able to see it.
