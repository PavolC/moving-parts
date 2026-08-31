# Course kit

Everything needed to build another interactive, self-contained course that teaches a
technical topic to one named learner by making them build the thing. The series is Moving
Parts, and `METHOD.md` opens with its canonical description of itself plus the five-point
fit test a topic has to pass. Read that before deciding what the new course is; those
words are the series', not the new course's to reword.

Extracted from the first one ([Neural Networks](https://github.com/PavolC/neural-nets), in the Moving Parts series:
five days, 70 commits, ten chapters, nine coding exercises, a real network training in the
browser), and specifically from the parts of it that were not about neural networks.

## Start here

Drop this folder's contents into an empty repo and say:

```
/new-course music theory, for someone who plays guitar by ear
```

That command interviews you, tests your stated floor before believing it, writes the design
doc, and builds the day-one scaffold. Everything else is what it reads while doing that.

Without Claude Code slash commands, the equivalent is: read `METHOD.md`, then work through
`DESIGN-DOC-TEMPLATE.md`, then close every `FILL:` in `CLAUDE.md`.

## What is in the box

| file | what it is | when to read it |
|---|---|---|
| `CLAUDE.md` | the portable rules, with topic-shaped holes marked `FILL:` | every session |
| `METHOD.md` | what a Moving Parts course is and the fit test, then the process: phases, the feedback loop, the end passes | once, first |
| `CASEBOOK.md` | the incidents from course one and the rules they produced | once |
| `DESIGN-DOC-TEMPLATE.md` | the plan to write before any code | once, at the start |
| `BRAND.md` | the shared visual identity, and how to wire it in | once |
| `brand/` | five files, a stylesheet and three components: the identity itself | copy it |
| `.claude/commands/` | six slash commands that run the loop | they run themselves |

`CLAUDE.md` is the deliverable. The other files exist because two things it cannot contain
turned out to matter as much as its rules: **the loop that generates new rules**
(`METHOD.md`) and **the evidence that the existing ones are load-bearing** (`CASEBOOK.md`).
A rule with no incident behind it gets bent; a rule with a quote behind it does not.

## The six commands

| command | what it does |
|---|---|
| `/new-course <topic>` | interview, floor test, design doc, day-one scaffold, one chapter |
| `/chapter <n>` | seam check, beat plan, then draft or revise to the playbook |
| `/stuck <what happened>` | fix the passage, write the rule, log the incident, sweep for the same bug |
| `/seam-review <n>` | reconcile a chapter against its neighbours: vocabulary, numbers, claims |
| `/house-style` | measure every chapter on countable prose features against the bands |
| `/teaching-review` | read the finished course for what no single chapter can show |

`/stuck` is the important one. About a third of course one's commits exist because a
real reader said something like "over my head" or "we're just talking about curves.....
why??" and that got turned into a fix plus a rule in the same commit.

## What this method assumes

**You do not know the topic.** The engine is your own confusion, reported fast and quoted
verbatim. If you already know the material, this is the wrong method: there is nothing to
drive the revisions, and the revisions are the project.

**You will read every chapter, in one sitting, and stop where you get lost.** Not push
through to be polite. The stopping point is the data.

**The rewriting is the work.** Course one committed its machine and first drafts of three
chapters inside two hours, then spent five days making them teach. Of its 64 non-merge
commits, 8 added a new chapter and 38 revised chapters that already existed: about five
revision commits per new chapter. Those passes were mostly additive, so the chapters got
three to four times longer rather than being replaced. Budget four or five revision passes
for every unit of new content.

## Code worth copying, if the new course has code exercises

The kit is deliberately docs and brand rather than a second application scaffold: a generic
scaffold for a topic that does not exist yet is a guess. But roughly 2,900 of course one's
21,700 lines under `src/` are topic-free, and the dependency direction never inverts
(nothing in `components/`, `runtime/` or `state/` imports a chapter), so they lift cleanly.
Worth cribbing from course one's `src/`:

- `runtime/messages.ts` and `runtime/workerClient.ts`: the run-tests exchange itself is two
  opaque code strings in, one structured verdict out, and that shape transfers to any
  language. The files around it do not: the same `messages.ts` also carries this course's
  MNIST training protocol, and the client hardcodes the Pyodide worker and names Python in
  its error strings. Copy the shape, delete the rest.
- `python/harness.py` (98 lines of pure stdlib): runs the learner's code as a `submission`
  module, collects every `test_*` callable in definition order, titles each from its
  docstring's first line, and returns a JSON verdict. A second entry point runs the editor
  with no tests at all. It carries no topic vocabulary, but it is not free of the course
  either: it hardcodes the exercise contract (the module name, the filename, the `test_*`
  convention, the result shape), and it cannot run the course's own tests until the caller
  registers the shared-helpers module first. It is the one place the Python assumption
  lives, which is what a non-Python course reimplements.
- `components/Workbench.tsx` and `components/WorkbenchProvider.tsx` (the panel and its
  state), `components/ExerciseCard.tsx` (what stays in the chapter page) and
  `components/DockShell.tsx` (the column-and-panel geometry): no reference to MNIST,
  neurons, digits or the source text anywhere in them. Their couplings are a handful of
  small named seams: two runtime-side names in the run-my-code path, the exception name a
  skeleton raises, three spots of Python-flavored copy, a pointer at the notation
  reference, and the flagship-test banner. The accumulated UX fixes are the expensive
  part, and none of them are topic-bound. `DockShell` in particular carries the one
  measurement worth stealing outright: publish the reading column's content width as a
  custom property and derive every figure scale from it, so a resizable panel cannot
  break a diagram system calibrated for one column width.
- `components/CodeEditor.tsx`: three lines couple it to Python. Swap one language package.
- `components/ModuleBits.tsx`: the chapter building blocks, including a table of contents
  that discovers its own sections from the DOM and needs no configuration.
- `state/workbenchDoc.ts`, `state/workbench.ts`, `state/storage.ts`, `state/progress.ts`
  and `exercises/types.ts`: no chapter ids, no exercise ids and no topic knowledge at all,
  which makes them the cleanest lift in the repo. The document format (one marker regex,
  one join rule, one parse that never throws), the lending rule, the prefix projections and
  progress export and import all come along free.
- The section table (`exercises/sections.json`): one file the app and the tools both read,
  which is what stops the format from being written down twice. Copy the shape, not the
  rows.
- The per-exercise folder convention: one directory per exercise holding the skeleton, the
  tests, the reference solution and the prompt metadata.
- `tools/check_exercises.py` and `tools/check_panels.py`: the invariants are the reusable
  part. Solutions pass, untouched skeletons fail for their own reason, no section rebinds
  an earlier section's name, and a sabotaged provider is noticed by its consumer.
- `App.tsx` and the `ModuleDef` registry: a complete tabbed course shell with lazy chapters
  and preloading, in under 200 lines.
- `tools/check_brand.py` and `tools/brand_palette.py`: copy both with `brand/`.

What does not transfer: the chapter prose, the interactives, the exercise Python, the
datasets and their loaders, and every bench. The benches carry a discipline rather than
code, and it is cheap to re-establish.

If the new topic has **no** code exercises, about 1,100 of those lines go dead and what is
left is a themed article shell with saved progress. At that point `CLAUDE.md` is the whole
asset, which is fine: it is the part that took five days.
