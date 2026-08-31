# Design doc: <topic> (working title: "<name>")

Write this with Claude in one sitting, before any code. Two maintenance rules, both
learned the hard way:

- **Append, never revise.** When an open question gets answered, annotate it in place
  rather than editing the question away, so the document stays a record of intent plus
  divergence rather than a retconned spec.
- **Section 10 grows as you build.** Every deliberate departure from this plan gets
  recorded there. Six months later it is how a reader tells a decision from an accident.

---

## 1. What this is

Two paragraphs. What the learner does, what runs where, what they end up owning.

### Goals, in priority order

1. The primary learner (<name>) understands <X> deeply by implementing <Y> themselves.
2. The artifact is self-sufficient: a colleague opens a link and finishes it with no book,
   no setup, no author involvement.
3. It is demoable in under two minutes: open link, show a live figure, show the thing
   running.

### Non-goals

What this deliberately is not. Be specific enough that a future session can tell whether it
is about to violate one.

## 2. Source, licensing and attribution

The canonical text or paper series the sequence follows, its licence, what attribution is
required and on which surfaces, and what licence this derivative inherits.

Prose policy: original explanations structured for interactivity; verbatim borrowing rare
and deliberate. Code policy: what may be adapted from where.

Also settle here: **the per-chapter "go deeper" target.** Choosing the canonical source
early is what fixes the chapter order, including any deliberate reordering of the source's
own sequence.

## 3. Architecture

- **Frontend:** framework, single-page or multi, static build, where it deploys.
- **In-page runtime:** the thing that executes the learner's code, and where it is pinned.
- **Editor:** which one, and the language mode.
- **Execution model:** what runs off the main thread, and what streams back (stdout, test
  results, live metrics).
- **Visualizations:** what draws them and why not a chart library.
- **State:** what persists, where, and how a learner moves it between browsers.

### Data

Every dataset: what it is, its licence, how big, what shape it arrives in, and the
committed script that produces it. At least one dataset should arrive **raw** if the course
means to teach preparation.

### The canonical representation

The one data representation the whole project obeys, stated exactly. Fill this in here and
copy it into `CLAUDE.md`. Drift between chapters is a bug.

### Exercise and test contract

Per exercise: the skeleton's contract, the tests, the reference solution, the hint ladder.
State the invariants: deterministic, hardcoded fixtures, teaching failure messages, no
solution logic in skeletons.

Then decide, and write down which: are the exercises **many isolated files** or **one file
the learner grows**? Many means each chapter is handed its predecessors' work as a library,
and a bug in chapter 1 can never block chapter 9. One file means the learner's own earlier
code is what the later code calls, and at the end they hold something. Retrofitting either
way is a course-wide change, and one file adds three invariants the other does not need:
the untouched file must implement nothing, no section may rebind a name an earlier one
owns, and a section that has not been written yet must still let the chapter run.

Name **the flagship automated proof** that the learner's implementation is right, and say
where it is celebrated in the UI.

## 4. Chapters

Per chapter: what it covers, its interactives, its exercise (or an explicit note that it has
none, and why), and its go-deeper link.

Two chapters to plan from the start, because a course that omits them finishes with a
learner who can explain the topic and cannot use it:

- **Assembly.** The learner writes the loop that runs their own parts, unaided, plus an
  honest list of what the course did not teach, plus the list of words that were only ever
  this course's own. The translations into the field's vocabulary are not here: each one is
  handed over in the chapter that earned the idea.
- **Their own input.** The artifact meets data the course did not curate.

Say which chapter is last, and put the where-to-go-next reading list on that one. A chapter
added after it takes the list with it.

## 5. Content conventions

Prose beat length, voice, notation policy, the register rules, the chapter template. Keep
this short here and canonical in `CLAUDE.md`; say which file wins.

## 6. Repo layout

The tree, with one line per directory.

## 7. `CLAUDE.md` seed content

What the working conventions file starts with. Use `CLAUDE.md` from the kit and list the
holes this project has to close.

## 8. Build milestones

Each one ends in a deployable state.

- **M0, feasibility spike (do first).** The riskiest runtime constraint, proved end to end
  with a reference implementation, before any content exists. State the budget it has to
  fit inside and what happens if it does not.
- **M1, exercise pipeline.** Editor to runtime to tests to results, with the hint ladder and
  persistence, built on one chapter's exercise as the guinea pig. Also day one: the exercise
  checker, the bench harness, the empty notation reference, and a green deploy.
- **M2, one chapter, read by the learner, rules written down.** Do not skip to M3.
- **M3, the spine.** The chapters up to and including the summit.
- **M4, the tail.**
- **M5, handoff polish.** Front door, demo path, progress export, cross-browser check,
  colleague dry-run, then the three end passes (teaching review, house style,
  reproducibility).

Deploy from M1 onward so the demo link exists before there is content on it.

## 9. Open questions

List them. Answer them in place as they resolve, in bold, rather than deleting them.

## 10. What the build actually produced

Empty at first. Add an entry for every deliberate departure from the plan above, with its
reason.
