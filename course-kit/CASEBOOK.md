# Casebook

Sixteen incidents from course one (neural networks), each a place where a chapter failed a
real reader, and each the reason a rule exists in `CLAUDE.md`. Read this once. The rules
are what you follow; these are what makes them credible, and what tells you whether a rule
you are tempted to bend is load-bearing.

Every quote is the learner's own. The cost column is the commit that fixed it, so you can
see what a late-settled convention actually costs.

---

## 1. "Over my head", then "lost the concept and got math heavy"

**Chapter:** backpropagation, the idea. The hardest conceptual chapter in the course.

**What was wrong.** The first draft put nine equations and 1,200 words before its
centerpiece interactive, and taught the four formal statements with abstract layer indices
after pages of concrete language. The learner stopped.

**The fix.** Teach the one genuinely new idea in prose with concrete numbers; reach the
interactive by the page's midpoint; present the equations after it as "what you just
watched, written down", written with the interactive's own layer numbers, each paired with
a number the learner had already computed by hand in a receipts table. Direction-of-use and
sign-reading got their own beat, because neither is visible in the symbols.

A second draft of the same section failed again on the numbers: claims-first prose ("nudge
w and z moves by x times that amount") floated past the reader, and what landed was showing
the full log of before/after/change values first, then explaining each stage as a rule that
predicts the next logged number from the previous one.

**Rules:** "Interactives carry the algorithm; the formalism recaps it" and "Log first,
explain second".

**Cost:** two restructures of the same chapter (4 files, +213/-157, then 3 files, +73/-22),
inside a chapter that was rewritten four times in one day.

## 2. "A neuron is a straight line trying to divide data up" to "pairs of them making bars"

**Chapter:** universality.

**What was wrong.** The chapter re-derived three artifacts the learner had already built by
hand in chapters 1 and 2, without saying so. He read new machinery and asked why the ground
had moved.

**The fix.** Name each identity explicitly, with the numbers restated: this switchover is
chapter 1's decision boundary with one input removed; this bump is chapter 1's own network
with the squash taken off; this thresholding unit is chapter 1's output unit doing what its
bias did. The same commit found a silent axis swap: two identical-looking square plots
that meant entirely different things.

**Rule:** "Recognize, do not rebuild."

**Cost:** 2 files, +106/-19, on day five, on a chapter shipped on day three.

## 3. "Changing by 0.01 changes it by 0.01, so what?"

**Chapter:** backpropagation, the idea.

**What was wrong.** The chapter proved "the change comes out multiplied by the partner" on
the one hop whose partner happened to be 1.0. A worked example whose value makes the key
effect a no-op teaches that nothing happened.

**The fix.** Lead with the times-2 wire, where the effect shows, and explain 1.0 afterwards
as the special case it is.

**Rule:** "Demonstrate where the mechanism is visible." Watch for multiply by 1, add 0, gap
of 0, modulus 1, transposition by a unison.

## 4. Five correct derivations that read as five separate proofs

**Chapter:** backpropagation, the idea.

**What was wrong.** Five factors along a chain, each derived position by position. Every
line checked out and the learner lost the thread anyway.

**The fix.** Name the pattern once, in a concept already taught ("every factor is a slope,
chapter 3's kind of number"), sort the five into their few kinds, give each kind one
plain-words why plus an extreme case, and colour-code the kinds in the figure so the picture
carries the grouping.

**Rule:** "Teach kinds, not instances."

**Cost:** 3 files, +178/-51.

## 5. The symbol with no spoken name

**Chapters:** 3 onward.

**What was wrong.** The course said the gradient is written with an upside-down delta, and
never said the symbol is read "nabla". Every later prompt and skeleton then used `nabla_w`
and `nabla_b`, which read as an unrelated word.

**The fix.** Name the glyph where it first appears, then bridge to the code names at their
own first use.

**Rule:** "Name the glyph, not just the meaning, whenever code borrows that name." This
generalizes to any topic whose identifiers come from its notation.

**Cost:** small (4 files, +19/-4) and only because it was caught mid-course. The same class
of bug, left until the end, is incident 8.

## 6. "Why is the weight on the wire and not the neuron?" and "Is this a single neuron per layer?"

**Chapters:** 1, 2 and 4, then 6.

**What was wrong.** Two bugs, one question each. First, the prose filed weights with
neurons in some places (counts, matrix rows) and with wires in others, so ownership was
never settled. Second, a chapter placed values by hand to build a small network and never
drew it: the shape had to be inferred from a plot of curves, and the prose coined "output
weight", a term the course never established, which filed a weight with a neuron again.

**The fix.** One anatomy, stated everywhere ownership comes up, and reconciled in place
wherever prose violated it, including counts and figure captions. Any hand-built example
gets its structure drawn in the idiom the earlier chapters taught, with its parts named the
way those chapters name them.

**Rules:** "One anatomy, stated everywhere ownership comes up" and "A hand-built example
gets its structure drawn".

**Cost:** 9 files, +549/-34 (bundled with the section-navigation retrofit).

## 7. "We're just talking about curves..... why??"

**Chapter:** universality. The learner stopped five sections in.

**What was wrong.** The chapter delivered a *fact* rather than a capability, and it opened
in a new world: continuous input, a 0-to-10 rating, no training, no exercise, with its only
connection to the course in the closing beat. Every previous chapter had handed over a thing
the learner then owned.

**The fix.** Open with a number the learner produced, name the competing explanations for
it, say which one this page settles and which it leaves standing, and at the end spend the
result back on the learner's own artifact. Name the shrink (one input instead of 784,
hand-placed values instead of trained ones) as deliberate in the opener, with its reason,
plus the sentence that the small case is a sub-case and not a detour.

**Rules:** "Chapters that deliver a fact rather than a capability" and the requirement that
the running world can carry the last chapter, not just the first.

**Cost:** 3 files, +384/-196, a full reframe of a finished chapter, 23 minutes after the
rule was written down.

## 8. The notation reference that arrived last

**Chapter:** all of them.

**What was wrong.** The course's own rule said weeks pass between chapters. Nothing acted
on it: symbols were defined once, thousands of words before a returning reader would want
them, with no lookup anywhere.

**The fix.** A folded reference on the front page: symbol, one line of meaning, the chapter
that introduced it, in the order a reader meets them. Plus the rule that introducing
notation means adding its row in the same change.

**Cost:** 36 rows back-filled in one commit (8 files, +429/-7) after all ten chapters were
written, and 7 more rows in the pass after that. Creating it empty on day one is free.

## 9. Numbers published before the code that produces them

**Chapters:** 6, 7 and 8.

**What was wrong.** Every measurement two chapters quoted came from a throwaway script that
no longer existed, so nothing could be re-verified when a helper changed.

**The fix.** A committed bench per chapter that runs the artifact's own code path, each
section printing the prose sentence it backs.

**What it found on its first run:** three numbers that no longer reproduced. Two traps
worth knowing, both discovered here: the initializer drew every weight and then every bias,
so a bench that interleaved them built a different network from the same seed; and the
gradient step summed per-example contributions in a loop, so a vectorized bench rounded
differently, which a deep network amplified into a two-point divergence after seven epochs.

**Rule:** "Every measured number comes from a committed bench that runs the artifact's own
code path", including the clause that the bench must match **exactly, not just
mathematically**.

**Cost:** 7 files, +651/-18, four chapters too late. Every bench added in this project
found errors on its first run.

## 10. Numbers and backward claims written from memory

**Chapters:** several.

**What was wrong.** "Both numbers I first wrote from memory were wrong (the worst digit is
8, not 5, and the 7 was read as a 2, not a 1), which is what the bench is for." Elsewhere,
a first draft claimed a score and two behaviours that the bench disproved, and a table was
factually wrong about where two of the four equations fire.

**The fix.** No number is written from memory, ever. And the other half, which nothing had
covered: every "chapter N taught X" claim, every cross-reference, and every outside-world
fact gets checked against the source before commit.

**Rule:** "Backward claims get checked like numbers." A course that quotes its own earlier
chapters constantly grows this class of bug faster than it grows content.

## 11. Nothing checked the exercises until seven of them existed

**What was wrong.** "Nothing verified the exercises except a person clicking through seven
of them in a browser, so a change to a test, a skeleton or a solution could break an
exercise silently."

**The fix.** A script that asserts both halves: every reference solution passes every test,
and every untouched skeleton fails every test for the skeleton's own reason.

**Cost to build:** 122 lines, one commit, on day four. It then gated every content change
after it. This is a day-one artifact.

## 12. "Dense, backwards, vague, clippy"

**Chapter:** universality, again.

**What was wrong.** Four things at once. Cleft and abstract-first openers that front a
placeholder and delay the content. Four consecutive paragraphs opening with a pronoun whose
antecedent was five paragraphs away. Meta-narration of the exposition itself. And
telegraphese: the chapter had been through two rounds of word-cutting, which is exactly
what made it clippy.

**The fix.** Give every sentence a concrete subject and a verb, in that order. Name the
subject each time, even at the cost of a longer sentence. Describe the thing, not the plan
for describing it. And **rejoin clauses instead of cutting them** when prose reads badly.

**Rule:** "Three sentence shapes to keep out", with the measurable bands (cleft openers and
pronoun aphorisms at or under 5 percent of sentences, median sentence length 19 to 23 words)
so the taste becomes an audit.

**Cost:** part of the 20-file house-style pass (+1096/-491), the largest revision commit in
the project.

## 13. Figure geometry decided at diagram thirty

**What was wrong.** Diagrams had accumulated one at a time, each sized to look right on its
own, so no two shared a width and none had a defined behaviour on a phone.

**The fix.** Exactly two families: a box-and-arrow family sharing one fixed viewBox width
rendered at full column width (a narrower layout is centred by shifting the viewBox, never
by scaling), and a plot family rendered at natural scale, capped and centred. On narrow
screens the box family keeps a minimum width and pans inside a scroll wrapper rather than
shrinking its labels. New diagrams join a family.

**Cost:** 6 files, +51/-16 to retrofit, and free to decide on day one.

## 14. The learner who could explain it and could not use it

**Found by:** a teaching review of the finished course.

**Two gaps, both invisible from inside a chapter.**

*Assembly.* The learner owned seven functions and had never assembled them: every training
run in the course was started by a course-written panel. The other 37 tests checked parts.
He also finished speaking a private language, since the course had deliberately invented
its own vocabulary and never translated it back.

*Curated input.* Every dataset in the course arrived numeric, scaled, complete, labelled
and split. A learner finished able to explain the technique and unable to point it at
anything.

**The fix.** Two closing chapters. One where the learner writes the loop that runs their
own parts, carrying a translation table into the field's vocabulary and an honest list of
what the course did not teach. One where the artifact meets a second dataset chosen for its
defects: words, holes, unequal classes, and measurements 245 times apart in scale, where
skipping one preprocessing step drops the network to the majority-class baseline and a 73.5
percent score turns out to hide a class it never once predicts.

**Cost:** two whole chapters (16 files +1154, and 17 files +1569) and a change to the
project's stated goals, at the very end. Both are designable from the start.

## 15. The narrator, muted four chapters late

**What was wrong.** The prose sold, promised, gave stage directions, and pointed at its own
storytelling. Verdict punchlines, promises about the reader's future experience, moralized
vocabulary for algorithms, flattery.

**The fix.** The whole register section in `CLAUDE.md`, with the operational test: could
this sentence appear unchanged in a careful colleague's explanation email?

**Cost:** a retrofit over four finished chapters (7 files, +97/-75) that then did not hold.
The drift had to be chased in four further commits, and the final house-style pass found the
same drift again from chapter 6 onward. Voice is the cheapest thing to settle first and the
most expensive to retrofit, because it touches every sentence and cannot be enforced
mechanically.

---

## 16. Nine editors, and nothing to hold at the end

**What was wrong.** The learner, after finishing most of the course: "it would be awesome
for there to be a side panel/workbench where every exercise simply allows me to add on code
so that by the end of it i have a single piece that i understand and have built up ... might
feel more cohesive throughout instead of a random embedded window on each module."

Two complaints in one sentence, and the second is the sharper. The editor sat several
thousand pixels into each chapter, so reading the prompt and typing the answer meant
scrolling between them. And the nine exercises were nine isolated files: each opened with a
line handing it the previous chapters' work out of a shared library, so the learner's own
function was never what their next function called. By the last chapter, the capstone's own
call map had to admit in a caption that three of the names in it ran the course's code.

**The fix.** One panel docked beside the reading column, and one growing file: a section per
exercise, in course order, plus two marked "written for you" so the file needs nothing but
the language's array library. A section the learner has not written yet is filled in from
the course's copy for the run, and the panel names what it borrowed, so a reader who opens
the last chapter first still gets a run.

**What made it expensive was not the panel.** It was that the isolated model had been
hiding a live bug. Concatenating the nine untouched skeletons in their old state passed
**19 of 52 tests**: the library import in a later section rebound a name an earlier section
defined, and the harness executes the whole document before the tests import from it, so the
last binding won retroactively for every suite. A learner pressing Run tests before writing
anything would have been told five functions were already finished. Running the suites
cannot detect this, because everything is green. Only a mutation check can: sabotage a
provider, require its consumer's suite to notice.

**Cost to fix:** a course-wide change touching the exercises, the harness, the worker
protocol, every payoff panel, the stylesheet, the app shell, both checkers and the prose in
seven chapters. Deciding it on day one costs nothing.

**The rule it bought.** Decide in the design doc whether the exercises are one file or many,
and if one file, write down the three invariants it needs from the first commit: the
untouched file implements nothing, no section rebinds an earlier section's name, and an
unwritten section still lets its chapter run.

## The pattern behind all sixteen

Four of them (2, 6, 7, 12) are the same chapter, and it is the one chapter authored outside
the playbook, in a single 25-file commit that also touched the stylesheet, the app shell and
the runtime. Two regressions landed in that commit as well, in files nobody was reviewing
for UI.

That chapter also had, at birth, every structural component the conventions required:
section headers, the on-this-page nav, an aside box, a recap. **Structural conformance is
not playbook conformance.** A chapter can carry every component and still fail the reader
completely.
