# CLAUDE.md

Working conventions for building an interactive, self-contained course that teaches a
technical topic to one named learner by making them build the thing.

This file is read at the start of every session. It is the rules only. The incidents
that produced them are in `CASEBOOK.md`, the process that generates new ones is in
`METHOD.md`, and the visual system is in `BRAND.md`. Read this one every time; read the
others once.

Every `FILL:` below is a hole this project has to close before the first chapter is
written. A hole left open is not a style question, it is a bug that will be paid for
later at ten to twenty times the cost (`CASEBOOK.md` prices six of them).

---

## Rule zero

**A fix that does not leave a rule behind will be re-learned.** Every time the learner is
confused, the same commit does three things: fixes the passage, adds a rule to this file
in the learner's own words, and adds the incident to `CASEBOOK.md`. One file, one commit,
provoking quote included. This is the single practice that produced everything below.

## What this project is

FILL: two sentences. What the learner will be able to do at the end, and what they build
to get there.

Goals, in priority order:

1. FILL: the primary learner understands X deeply by implementing Y themselves.
2. The artifact is self-sufficient: a colleague opens a link and finishes with no book,
   no setup, no author involvement.
3. Demoable in under two minutes: open link, show a live figure, show the thing running.

Non-goals: FILL: what this deliberately is not (a production tool, a full port of the
source text, anything with accounts or a backend).

## The learner floor

FILL: one short line for what the learner can already do, then the list of what they have
never seen. "Knows Python and high-school algebra; has never seen a grammar, a stack
machine, or asymptotic notation." The absences are the load-bearing half, because a
paragraph can be checked against them; "intermediate programmer" cannot be checked against
anything.

The floor is binding on every chapter, including the last one. Everything above the floor
is built here, in the order the story needs it and never before.

## Hard rules

- **Never write solution logic into a skeleton file.** Solutions live only in
  `solution.py` (or its equivalent). Skeletons hold stubs, docstrings and contracts.
- FILL: the attribution and licence obligations, naming every surface that carries them
  (app footer, README, LICENSE). If the sequence is adapted from a book, a paper series or
  a curriculum, its terms are an unremovable hard rule.
  **Scope the restriction to the material it actually covers, and write that scope down
  before the first chapter.** A course adapted from a NonCommercial source contains two
  kinds of material: the content, which carries the source's terms, and the engine, the
  brand layer and the tooling, which contain none of the source and carry none of its
  terms. Course one shipped saying "this project" inherits CC BY-NC, in the README, the
  app footer and LICENSE, which gave away rights over the one asset that transfers to
  every later course in the series. Note also that BY-NC and BY have no ShareAlike clause,
  so matching a source's licence in the adapted content is a choice rather than an
  obligation that spreads.
  **Prefer a source that is CC0, CC BY, MIT or public domain.** Check before committing to
  a spine, because the licence is chosen once and lived with forever, and BY-NC-ND forbids
  derivatives outright. A NonCommercial spine is survivable if the goal is reach; it is
  fatal if the goal ever becomes revenue.
  **If any source code is redistributed, its notice ships with the build.** A permissive
  licence like MIT asks that the copyright and permission notice travel with the code, and
  a bundler will happily inline the code and leave the notice in the repository. Emit the
  licence file into the build output and link it from the footer. Course one shipped this
  defect.
- **No em dashes in any user-facing prose.** Commas, colons or parentheses.
- **No number is written from memory.** See "Numbers" below.

## The canonical representation

FILL: the one data representation the whole project obeys, stated exactly, with the shape
or type rules that follow from it. A compiler course fixes its IR; a music course fixes
its pitch encoding; a modelling course fixes its state vector and time unit.

Drift between chapters is a bug, not a preference. This is the cheapest rule to settle on
day one and the most expensive to retrofit.

## The running world

FILL: one story, with named recurring artifacts, that can carry the LAST chapter as well
as the first. New material connects explicitly to prior artifacts instead of opening
fresh abstractions.

Check the last chapter against it before writing the first. A chapter that opens a new
world has to be re-anchored, which is a rewrite, not an edit. [casebook: 7]

## The exercise and test contract

FILL the language and runtime; the rest is fixed:

- Tests import the learner's code under one fixed name. Work from earlier chapters
  arrives as an importable library, so a skeleton never contains a previous answer.
- Build the shared library with a **seam** where a later chapter will vary (a swappable
  argument defaulting to the earlier behaviour), so later exercises are one-line diffs
  rather than rewrites. Decide which axis varies before the ladder is built.
- The shared library carries later chapters' functions too, and a capstone patches the
  learner's own saved versions over them, so the final run really is theirs.
- Tests are deterministic: fixed seeds, no wall-clock assertions. Fixtures are hardcoded
  literals, never regenerated at test time, so results cannot drift with library versions.
- Tests run in definition order and fail by raising with a teaching message. The first
  docstring line is the test's display title.
- **Failure messages are teaching content.** Each says what was expected, what was
  received, and the likely misconception behind the gap.
- **Skeleton docstrings freeze into the learner's saved copy.** The editor persists their
  code, so improving a skeleton never reaches anyone who already opened the exercise.
  Anything essential to the contract must also live in the prompt, which always re-renders.
  This applies to every artifact seeded into a learner's workspace.
- Name the course's **one flagship automated proof** that the learner's implementation is
  right, and celebrate it in the UI when it passes. FILL: here it is X (a numerical
  gradient check; differential testing against a reference implementation; a closed-form
  solution the solver is checked against).

Day one, not day four: a script that runs every exercise's tests against its reference
solution (all must pass) and against its untouched skeleton (all must fail, for the
skeleton's own reason). It is about a hundred lines and it gates every later content
change. [casebook: 11]

## Numbers

- Every number in the prose is derived in front of the reader, quoted from an earlier
  chapter, or labelled a free design choice with its trade-off. An unexplained constant
  is a bug.
- **Every measured number comes from a committed bench that runs the artifact's own code
  path**, with each bench section printing the prose sentence it backs. Write the bench
  before the prose, not after. Every bench added to course one found errors on its first
  run. [casebook: 9]
- The bench must match the artifact **exactly, not just mathematically**. Same draw
  order, same summation order. Two mathematically identical runs can agree for a while
  and then diverge.
- Two engines (say a JS panel and a Python runtime) produce two sets of numbers from two
  generators. They are not meant to agree: never quote one engine's number for a
  measurement the reader makes with the other, and say which panel a table came from.
- Prefer statistics that hold still: the mean and middle 90 percent of 200 draws
  reproduce; the extremes of that stream do not. Where a run is still moving at the end,
  quote an average over the last several steps.
- **Backward claims get checked like numbers.** Every "chapter N taught X", every
  cross-reference, and every outside-world fact is verified against the source before
  commit. [casebook: 10]

## Chapter template

Each chapter opens with "What you'll be able to do after this" (2 to 3 items), then 5 to
8 titled sections of short prose beats (150 to 400 words, one idea each) interleaved with
interactives, and closes with a recap and a "go deeper" link to FILL: the canonical
source for this topic. Every equation is followed by a one-sentence plain-language gloss.
Each chapter mounts exactly one on-this-page nav that discovers its own section headers
and scrollspies them. Section ids are unique across chapters and prefixed with the
chapter (`c4-`).

## The authoring playbook

Write every chapter to the floor above. These are ordered roughly as they bite.

### Reaching the reader

- **Numbers before notation.** Compute a concrete instance by hand, then name the
  operation and its shorthand. Never the reverse.
- **Interactives carry the algorithm; the formalism recaps it.** Teach the one genuinely
  new idea in prose with concrete numbers, reach the interactive by the page's midpoint,
  and present the formal statements after it as "what you just watched, written down".
  Recap means instantiated: say the job is recognition rather than derivation, write the
  formalism with the interactive's own concrete values (general indices wait until the
  implementation needs them), pair each statement with a number the learner already
  computed (a receipts table), and give direction-of-use and sign-reading their own beat.
  This is the highest-value structural rule here. [casebook: 1]
- **Log first, explain second.** For any multi-stage numeric process, show the full log of
  concrete values (before, after, change) as one figure or table FIRST, then explain each
  stage as a rule that predicts the next logged number from the previous one. Run the
  check in the multiplying direction (factor times change gives the next change), never
  the dividing direction. Claims-first prose floats past a reader; prediction-against-a-log
  lands. [casebook: 1]
- **Draw every conceptual jump.** Never ask the reader to imagine a picture; put the
  figure in the page. Before any interactive the reader gets a how-to-read key. Captions
  state counts and label which parts of the figure are the object of study and which are
  scaffolding.
- **Succeed before failing.** The learner solves the easy cases before meeting the one
  that breaks. "Press Show a solution, break it one piece at a time, then rebuild" is a
  valid on-ramp for a fiddly interactive.
- **Demonstrate where the mechanism is visible.** A worked example whose value makes the
  key effect a no-op (multiply by 1, add 0, gap of 0, modulus 1) teaches that nothing
  happened. Lead with an instance where the effect shows, then explain the no-op value as
  the special case it is. [casebook: 3]
- **Teach kinds, not instances.** When several facts repeat one pattern, position-by-
  position derivations read as N separate proofs and lose the reader even when each line
  checks out. Name the pattern once in a concept already taught, sort the instances into
  their few kinds, give each kind one plain-words why plus an extreme case, and colour-code
  the kinds in the figure so the picture carries the grouping. [casebook: 4]
- **State what a section buys before proving it.** Open a stretch of verification with the
  one-sentence payoff it earns, and close by cashing it out. Checks without stated stakes
  read as arithmetic for its own sake.
- **Tally explicitly.** Count the cost in the text: it is why the next chapter exists.
  FILL: the countable quantity each chapter's technique reduces.
- **A score gets a breakdown.** Any aggregate number reported to the learner gets its
  decomposition beside it (per-class counts, the specific confident mistakes, the
  residuals by stratum), never the single number alone.

### Chapters that deliver a fact rather than a capability

A chapter that hands over a property instead of a working artifact has to work harder, in
this order: open with a number the learner produced, name the competing explanations for
it, say which one this page settles and which it leaves standing, and at the end spend the
result back on the learner's own artifact. Anything that looks like a departure (a shrunken
case, hand-placed values, no exercise) is named as a deliberate shrink in the opener, with
its reason, plus the sentence that the small case is a sub-case and not a detour.
[casebook: 7]

### Notation and vocabulary

- **Notation down to the punctuation.** Anything that could read as a typo is notation to
  explain at first use: a trailing comma in a shape, a bare decimal point, an operator
  glyph, slice colons. Language idioms count as much as symbols. Flag order reversals
  explicitly and teach the mechanical check that catches them.
- **Name the glyph, not just the meaning,** whenever code borrows that name. A symbol the
  reader cannot pronounce becomes an unrelated word the moment it appears in an
  identifier. [casebook: 5]
- **Every new symbol and coined term goes in the notation reference in the same change.**
  One folded lookup on the front page: symbol, one line of meaning, the chapter that
  introduced it, in the order a reader meets them. Weeks pass between chapters, and a
  symbol defined once four thousand words ago is not defined for that reader.
  [casebook: 8]
- **One word, one meaning.** Reserve the topic's load-bearing words and never reuse them.
  Before coining a noun, check what earlier chapters already call the thing. No word may
  appear before the section that defines it.
- **One anatomy, stated everywhere ownership comes up.** FILL: the topic's ownership
  ontology (what lives on what). Any prose that files a thing with the wrong owner gets
  reconciled in place, including counts, tables and figure captions, which is where the
  violation hides. [casebook: 6]

### Backward references

- **Assume weeks pass between chapters.** Never lean on a bare name from an earlier
  chapter as a load-bearing reference. Restate the thing in a few plain words or drop the
  callback.
- **A callback earns prose only if it removes work or carries the argument.** Removing
  work means the reader has nothing new to learn because it is the same object. Carrying
  the argument means the page's conclusion depends on it. A callback that only says
  "remember this from before" costs attention and returns nothing; cut it. Two callbacks
  to the same earlier figure in one section are clutter.
- **Recognize, do not rebuild.** When a chapter re-derives something the learner already
  built by hand, say so, with the numbers restated. A reader who is not told sees new
  machinery and asks why the ground moved. Watch for silent axis swaps the same way: two
  identical-looking figures that mean different things need saying. [casebook: 2]
- **Say the implicit connections** where the reader will wonder about them, not later.

### Sentences

- **One inference per sentence.** Unpack chains; three steps compressed into one sentence
  loses the reader even when all three are true.
- **Arithmetic goes in display math.** Any tally with more than two terms, and any product
  of more than two factors, becomes display math with labelled braces or a small table
  (knob, value, read off as), never an inline prose sentence of times-and-plus. More
  display math reads lighter than fewer inline products.
- **Three sentence shapes to keep out:** clefts and abstract-first openers ("What no part
  of the argument provides is..."); short pronoun aphorisms, especially as paragraph
  openers; and meta-narration of the exposition ("this section makes X, the next turns it
  into Y"). Give every sentence a concrete subject and a verb, in that order. Describe the
  thing, not the plan for describing it.
- Measurable signature, to audit against the chapters that worked: cleft openers at or
  under 5 percent of sentences, pronoun aphorisms at or under 5 percent, median sentence
  length 19 to 23 words, callbacks 0.4 to 1.2 per paragraph.
- **Cutting words is not the fix when prose reads badly.** Two rounds of cutting turn
  full sentences into telegraphese. Rejoin clauses instead. [casebook: 12]

### Departures and borrowed worlds

- **Departures wear the Aside box.** Anything that pauses the main thread (a borrowed
  analogy, a scope note, a why-digression) goes in the shared `<Aside>` component, never
  in a long parenthetical. The shaded box tells the reader the lesson pauses and resumes.
- **A borrowed mini-world is allowed when the home story has no carrier** for a concept.
  Three constraints: one beat plus one figure, every element mapped back by name, and the
  borrowed vocabulary allowed to run through the section it serves and no further.

### Interactives

- **Interactives carry their own keys.** Each chart's how-to-read key lives on the
  interactive (section titles, one-line legends at the point of use). The prose before it
  keeps only what sections cannot say: the connection to earlier material and the single
  carrying idea. Prose that narrates an interactive's own labels is duplication to delete.
- **Interactives must not jump.** Fixed-basis flex columns (wrap depends on window width,
  never content), reserved heights for changing status text, statuses on their own
  full-width line inside control rows, range inputs allowed to shrink. Live readouts tie
  manipulation to meaning.
- **A hand-built example gets its structure drawn**, in the visual idiom the earlier
  chapters taught the reader to read, with its parts named the way those chapters name
  them. Any chapter that places values by hand rather than deriving them owes this.
  [casebook: 6]
- **Figure geometry is a small closed set.** FILL: pick two or three families before
  drawing many figures (a fixed-width box-and-arrow family at full column width; a plot
  family at natural scale), and decide once what each does on a phone (pan inside a scroll
  wrapper rather than shrink labels). New diagrams join an existing family. Deciding this
  at diagram 30 costs a course-wide retrofit. [casebook: 13]

### Exercises

- **Exercises are visible.** The output panel shows everything printed, tagged by source.
  A "run my code" path executes the editor without tests. The test source is viewable in
  the page. Hidden test code breeds guessing.
- **Every prompt carries a concrete experiment** tied back to an earlier chapter's
  numbers, shipped as a copyable code block with Copy and Send-to-the-scratch-pad buttons.
  Never woven into a prose sentence: an experiment the reader must retype is an experiment
  they will not run.
- **Decide early whether the exercises are one file or many, because retrofitting is a
  course-wide change.** Many is simpler and isolates failure: a bug in chapter 1 can never
  block chapter 9. One file is what a learner asks for once they have written five of
  them, because it is the only shape where the thing they hold at the end is a thing.
  If you choose one file, the invariant to protect from the first commit is that the
  untouched file implements nothing: hand a chapter its predecessor's work through an
  import and the import wins retroactively for every suite, so untouched skeletons start
  passing. Running the suites cannot detect that. A mutation check can: sabotage a
  provider, require its consumer's suite to notice. [casebook: 16]

### The two closing chapters

Design for both from the start; course one discovered them in a review at the end.

1. **Assembly.** The learner writes the loop that runs their own parts. Every earlier run
   was started by scaffolding, so this is the only assessment of assembly the course has.
   It carries a translation table from the course's invented vocabulary into the field's,
   and an explicit list of what the course did not teach.
2. **Their own input.** The artifact meets data the course did not curate: words, holes,
   unequal classes, wrong scales. Every dataset before it arrived clean, so a learner who
   stops earlier finishes able to explain the technique and unable to use it. [casebook: 14]

## Register: plotted, narrator muted

Plot chapters like a story (setup, tally, payoff, callbacks). Remove the audible
narrator: the voice that sells, promises, and points at its own storytelling.

- Motivate with numbers, not verdicts. Let the tally be the drama. A judgment is allowed
  once, in plain words, never as a punchline and never twice for rhythm.
- No promises about the reader's future experience ("it will be short", "you will beat
  this later").
- No stage directions that command attention or feelings ("watch the clock, and count",
  "remember this feeling"). Directing perception at content is fine ("watch how the steps
  shrink as the ground flattens").
- Never narrate the course's own storytelling. Devices stay, labels go: a callback works
  without being announced.
- No flattery or possession theatrics. No moralized vocabulary for algorithms ("the
  honest way", "X cheats").
- Replace aphorisms with their literal content. Punchlines compress by discarding
  information.
- **The test:** could this sentence appear unchanged in a careful colleague's explanation
  email? If not, rewrite it.
- Exception: a chapter's final beat may carry one slightly hot sentence.

Write this section before the first chapter. It touches every sentence, cannot be
enforced mechanically, and retrofitting it is the most expensive pass in the project.
[casebook: 15]

## Before you commit

FILL the commands; the list is fixed.

- [ ] Typecheck and production build pass.
- [ ] The exercise checker passes (solutions green, skeletons red for their own reason,
      and if the exercises are one file: nothing passing when it is untouched).
- [ ] Every panel that runs the learner's code has been run outside the browser.
- [ ] Every bench whose numbers you touched has been re-run, and the prose matches it.
- [ ] You looked at every string you added **in the real artifact**, not just in the diff.
- [ ] Nothing scrolls sideways at FILL: the narrowest supported viewport (375px).
- [ ] Every new symbol or coined term has a row in the notation reference.
- [ ] Every backward claim in the new prose was checked against the chapter it cites.
- [ ] If this commit fixes a confusion: this file has the new rule and `CASEBOOK.md` has
      the incident.

## Pinned versions

FILL: the one runtime whose performance the whole design depends on, pinned exactly, with
where the version string lives, and the measurement that justifies the pin. It may not be
bumped without re-running the feasibility spike.

FILL: every content-critical library, pinned exactly.

## Repo layout

```
/                    README (what, why, how to run, licence, attribution)
/CLAUDE.md           this file
/CASEBOOK.md         the incidents behind the rules
/METHOD.md           the process
/BRAND.md            the visual system
/<topic>-design-doc.md
/src/brand/          the series brand layer (shared, see BRAND.md)
/src/chapters/       one folder or file per chapter, plus interactives/
/src/exercises/      per exercise: skeleton, tests, solution, prompt metadata
/src/exercises/sections.json  the section table, if the exercises are one file
/src/runtime/        the in-page language runtime (worker, protocol, client)
/src/components/     shared UI: editor, workbench, exercise card, chapter blocks
/src/state/          the document format, and progress persistence
/public/data/        committed datasets
/tools/              build-time scripts, benches, and the exercise checker
```

## Commands

FILL. Every generated artifact names the committed script that regenerates it, and every
entry says what it needs. This section is how a stranger reproduces the numbers.

## Decisions

Append an entry when something is chosen: what was chosen, when, why, and what was
rejected. Never relitigate an entry; add a superseding one. Include decisions that exist
only to keep two subsystems consistent, since those are the ones a later session breaks
without knowing.

## Known non-bugs, do not chase

FILL. Rendering artifacts and stack quirks that look like bugs and are not, so a future
session does not spend a day on one.
