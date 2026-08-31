# Claude Tutor

This folder turns Claude Code into a coding tutor. You say what you want to learn. It builds a course around you, then walks you through it one lesson at a time. You write the code. It explains, checks that you understand, and only moves on when you can actually do the thing that lesson was for.

You do not need to know how to program already. You do not need to design the course yourself.

## Get started

1. Copy this project to a place you will keep your learning work.
2. Open a terminal in that folder and run `claude`.
3. Type one of these, then say what you want in your own words:

```
/curriculum I want to learn Python
```

```
/short-course give me the essentials of Git
```

```
/mastertrack I have no programming background and I want to be a professional web developer
```

Use **`/curriculum`** when you want one course (a few weeks of focused lessons).

Use **`/short-course`** when you just want a quick footing in one topic — five lessons or fewer, taught properly, not a rushed survey. At the end the tutor points you at what to do next: a full course, another short course, or going off to build.

Use **`/mastertrack`** when the goal is bigger — several full courses, short projects you build from scratch, and a larger capstone at the end. If you start with `/curriculum` and the goal is clearly that big, the tutor will offer a mastertrack and wait for you to choose.

It will ask what to call you, what you already know, and what you are aiming for. Then it writes the plan. Read the introduction, ask questions, and say when you are ready for the first lesson.

## Talking to it

After the plan is written, you just chat — type your exercises in the `workspace/` folder and tell the tutor what is going on. It picks the right thing to do from what you say:

- "I'm stuck" → a hint, not the answer
- "Can you look at this?" (paste your code) → one thing that is working, one thing to improve
- "Quiz me" → a few questions on the current lesson
- "This is going too fast" / "I already know loops" → it reworks the plan
- "Call me Sam" / "show me an example first, then let me try" → it remembers

You do not need to memorise commands. These are the only ones you need, and only to *start* something:

| Command | What it is for |
|---------|----------------|
| `/curriculum` | Start (or fully redo) one course |
| `/short-course` | A quick footing in one topic — five lessons or fewer, then you are pointed at what is next |
| `/mastertrack` | Start a longer path: several courses, build projects, and a capstone |

There are `/`-command versions of the rest (`/review`, `/adjust-curriculum`, and so on) if you would rather be explicit, but plain words work just as well.

## Where your files are

| Folder | What it is |
|--------|------------|
| `workspace/` | Your projects — this is where you type |
| `curriculum/` | Your course plan, and short summaries after each lesson. If you have a mastertrack, the map of the whole path is here too |

That is enough to begin. Run `claude` and say what you want to learn.
