# Casebook

Twenty-four incidents from the courses built so far, each a place where the work failed a
real reader, and each the reason a rule exists in `CLAUDE.md`. Read this once. The rules
are what you follow; these are what makes them credible, and what tells you whether a rule
you are tempted to bend is load-bearing.

Incidents 1 to 18 come from course one (neural networks), 19 to 23 from course two
(transformers), and 24 from the series itself. Every entry says which course and which
surface, because the first question to ask about somebody else's incident is whether it
can happen to you. A chapter-craft failure travels to any topic. A workbench, runtime or
tooling failure travels to every course that lifts the same code, which is all of them.
Two of the entries here are in code both courses share: one of those was live in both at
once, and the other had already happened in the first course and was re-broken in the
second.

Every quote is the learner's own. The **Cost** line is what the fix actually took, so you
can see what a late-settled convention costs; most of them end with what the same decision
would have cost on day one.

An entry that came out of the `/stuck` loop also records **what the misunderstanding
turned out to be**, which is frequently not what the learner's quote pointed at, and
**which re-explanation landed**, which is the part a later chapter can reuse. When the loop
was skipped, because the report was a defect with a known mechanism, because the learner
said to just fix it, or because two re-explanations died, the entry says that instead of
guessing at either.

Not everything that changes a rule belongs here. **This file holds failures that were paid
for**, and that price is what tells you whether a rule you are tempted to bend is
load-bearing; a rule adopted before its failure has no price to record and no incident to
attribute. The `/stuck` diagnosis loop is the standing example: it rewrote the command and
the second half of rule zero without an entry in this file, and `METHOD.md` phase 3 carries
its reasoning instead.

The numbers are load-bearing: each course's `CLAUDE.md` cites these incidents as
`[casebook: N]`. Append new ones, and never renumber an entry without fixing every rule
that cites it.

---

## 1. "Over my head", then "lost the concept and got math heavy"

**Course:** one (neural networks), the backpropagation chapter, the hardest conceptual
chapter in it.

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

**Course:** one (neural networks), the universality chapter.

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

**Course:** one (neural networks), the backpropagation chapter.

**What was wrong.** The chapter proved "the change comes out multiplied by the partner" on
the one hop whose partner happened to be 1.0. A worked example whose value makes the key
effect a no-op teaches that nothing happened.

**The fix.** Lead with the times-2 wire, where the effect shows, and explain 1.0 afterwards
as the special case it is.

**Rule:** "Demonstrate where the mechanism is visible." Watch for multiply by 1, add 0, gap
of 0, modulus 1, transposition by a unison.

## 4. Five correct derivations that read as five separate proofs

**Course:** one (neural networks), the backpropagation chapter.

**What was wrong.** Five factors along a chain, each derived position by position. Every
line checked out and the learner lost the thread anyway.

**The fix.** Name the pattern once, in a concept already taught ("every factor is a slope,
chapter 3's kind of number"), sort the five into their few kinds, give each kind one
plain-words why plus an extreme case, and colour-code the kinds in the figure so the picture
carries the grouping.

**Rule:** "Teach kinds, not instances."

**Cost:** 3 files, +178/-51.

## 5. The symbol with no spoken name

**Course:** one (neural networks), chapter 3 onward.

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

**Course:** one (neural networks), chapters 1, 2 and 4, then 6.

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

**Course:** one (neural networks), the universality chapter. **Found by:** the primary
learner, who stopped five sections in.

**What was wrong.** The chapter delivered a _fact_ rather than a capability, and it opened
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

**Course:** one (neural networks), all of its chapters.

**What was wrong.** The course's own rule said weeks pass between chapters. Nothing acted
on it: symbols were defined once, thousands of words before a returning reader would want
them, with no lookup anywhere.

**The fix.** A folded reference on the front page: symbol, one line of meaning, the chapter
that introduced it, in the order a reader meets them. Plus the rule that introducing
notation means adding its row in the same change.

**Cost:** 36 rows back-filled in one commit (8 files, +429/-7) after all ten chapters were
written, and 7 more rows in the pass after that. Creating it empty on day one is free.

## 9. Numbers published before the code that produces them

**Course:** one (neural networks), chapters 6, 7 and 8.

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

**Course:** one (neural networks), several chapters.

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

**Course:** one (neural networks), its exercises and their tests.

**What was wrong.** "Nothing verified the exercises except a person clicking through seven
of them in a browser, so a change to a test, a skeleton or a solution could break an
exercise silently."

**The fix.** A script that asserts both halves: every reference solution passes every test,
and every untouched skeleton fails every test for the skeleton's own reason.

**Cost to build:** 122 lines, one commit, on day four. It then gated every content change
after it. This is a day-one artifact.

## 12. "Dense, backwards, vague, clippy"

**Course:** one (neural networks), the universality chapter, again.

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

**Course:** one (neural networks), its diagrams.

**What was wrong.** Diagrams had accumulated one at a time, each sized to look right on its
own, so no two shared a width and none had a defined behaviour on a phone.

**The fix.** Exactly two families: a box-and-arrow family sharing one fixed viewBox width
rendered at full column width (a narrower layout is centred by shifting the viewBox, never
by scaling), and a plot family rendered at natural scale, capped and centred. On narrow
screens the box family keeps a minimum width and pans inside a scroll wrapper rather than
shrinking its labels. New diagrams join a family.

**Cost:** 6 files, +51/-16 to retrofit, and free to decide on day one.

## 14. The learner who could explain it and could not use it

**Course:** one (neural networks), the whole of it. **Found by:** a teaching review of the
finished course.

**Two gaps, both invisible from inside a chapter.**

_Assembly._ The learner owned seven functions and had never assembled them: every training
run in the course was started by a course-written panel. The other 37 tests checked parts.
He also finished speaking a private language, since the course had deliberately invented
its own vocabulary and never translated it back.

_Curated input._ Every dataset in the course arrived numeric, scaled, complete, labelled
and split. A learner finished able to explain the technique and unable to point it at
anything.

**The fix.** Two closing chapters. One where the learner writes the loop that runs their
own parts, carrying a translation table into the field's vocabulary (the table was the
wrong shape, which is incident 17) and an honest list of what the course did not teach. One
where the artifact meets a second dataset chosen for its defects: words, holes, unequal
classes, and measurements 245 times apart in scale, where skipping one preprocessing step
drops the network to the majority-class baseline and a 73.5 percent score turns out to hide
a class it never once predicts.

**Cost:** two whole chapters (16 files +1154, and 17 files +1569) and a change to the
project's stated goals, at the very end. Both are designable from the start.

## 15. The narrator, muted four chapters late

**Course:** one (neural networks), its prose, everywhere.

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

**Course:** one (neural networks), the exercises and the editors that held them.
**Found by:** the primary learner, most of the way through the course.

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

## 17. "A big brain dump of all of these terms that I now need to swap in my head"

**Course:** one (neural networks), the assembly chapter and every chapter before it.

**Found by:** the primary learner, having finished the whole course.

**What was wrong.** The course invented plain words on purpose, so that each idea could
arrive before its name, and then translated all of them at once: a twenty-row table on the
closing page, after the final exercise. That page asks for the highest-effort operation in
the course, re-indexing twenty concepts learned under other names, at its lowest-energy
moment, and there is nothing downstream to use the new words on.

The sharper half was invisible from inside any one chapter. The course was already
bilingual and silent about it. Its equation glosses used the field's words while the prose
beside them used the coined ones: "the weight matrix" in one chapter's gloss, "the layer's
wire ledger" twenty lines below it, seven uses each before the closing table arrived. The
field's vocabulary was reaching the reader unlabelled all along, so withholding the names
had bought nothing and had cost the reader the equivalence.

**The fix.** One short paragraph per chapter, at the first use of the thing, saying what
everyone else calls it, after which both words are in play. Unlabelled: seven of the eight
opened with "this chapter's naming note is" in the first draft, which is meta-narration and
a formula a reader skips after the second one. None of them wears an aside box either,
because a shaded box says the lesson pauses here, and this paragraph's whole job is to put
a word into the reader's working vocabulary.

Three tiers decide how much prose changes downstream, and the point of having tiers is that
most of the prose does not change: **switch** (the field's word becomes primary in the
formal registers only), **run both** (the plain word stays primary and the field's word
rides along in equations and code), **local only** (scaffolding for one beat, never handed
over). The closing page keeps the inverted table, six rows: these words are ours, there is
nothing to go looking for.

**Rules:** "A coined word hands over to the field's word in the chapter that earned the
idea", and the "also called" line in the notation reference.

**Cost:** naming notes back-filled into eight finished chapters, 17 "also called" lines
added to a 56-row notation reference, and the closing chapter's central section replaced.
The commit that fixed this and incident 18 together is 15 files, +533/-280, on a course
that was finished. One paragraph written at the moment the word is coined costs nothing.

## 18. The exit door one chapter before the exit

**Course:** one (neural networks), its last two chapters.

**Found by:** the primary learner, who reported skimming both of them and internalizing
nothing from either.

**What was wrong.** The assembly chapter closed with a five-item reading list one chapter
before the end, so it had to open that list by telling the reader that another chapter was
still ahead of them. A page that has to explain why its own exit is not the exit is in the
wrong place, and a reader who reaches an exit door takes it.

The list had been in the right place twice already: it ended chapter 8 when chapter 8 was
last, and moved to chapter 9 when chapter 9 was added. Then chapter 10 arrived and it did
not move again, and both closing chapters were written around it while it sat in the middle.

**The fix.** The reading list belongs to the last page in the course, whichever that is,
and adding a chapter after it moves the list in the same change. Its section id and CSS
class are named for the course rather than for a chapter, so the next move is free.

**Rule:** "The reading list belongs to the last page in the course, whichever that is."
It generalizes: anything that says "this is the end" gets re-checked when the end moves,
and in a course whose last chapters are discovered in a review (incident 14) the end moves
at least twice.

**Cost:** the same commit as 17, and free at any point if the question is asked when a
chapter is added.

## 19. "start page width leaked out"

**Course:** two (transformers), its front door, on day one. **Found by:** the learner, on
the deployed site.

**What was wrong.** The front door's prose ran the full page width instead of the reading
measure, so the page read lopsided against its own centred masthead. The cause was one
word: the article was written `className="start"`, and nothing in the stylesheet selects
`.start`. Course one's front door carries two classes and both are load-bearing, one that
the measure rules select and one that the front door's own headings select. The invented
name selected neither, and nothing said so.

The same mistake had already been made twice that week, both times by inventing a name
instead of reading the stylesheet: a control row built out of three classes that did not
exist, which let a slider overlap its own buttons, and a figure marked with a made-up
family name, which kept it out of its figure family's one scale. A repository whose
Decisions section already said "component vocabulary: course one's names, kept so cribbed
code stays readable" got it wrong three times in three days, which is what makes this a
tooling problem rather than a discipline problem.

**Why nothing caught it.** Every check was green. The build compiles unknown class names
happily, the typechecker has no opinion about strings, and the page still looks like a
page: prose, headings, a footer, all present and all painted. Only a reader comparing it
against its sibling course saw it, and the chapter pages were fine throughout, which is
what made the front door's version look plausible.

**The fix.** A checker: every class a component states outright must have a rule in the
stylesheet, with a short allow-list of deliberately unstyled hooks carrying a reason each.
It reads only the unambiguous forms, a plain `className="a b"` and a template's static
text, because a first version that also read ternaries reported `?`, `===` and a
comparison string as missing classes, and **a checker with false positives gets switched
off**. All three real bugs were plain literals, so the narrow rule loses nothing that has
ever broken a page. Verified by reintroducing the defect and watching the checker name it.

**Rule:** "Never invent a class name", in the hard rules, plus the checker in the
pre-commit list and in CI.

**Cost:** the fix was one word; finding it took a reader on a deployed site, and the
checker that makes it impossible again is 120 lines written the same day. It is a day-one
artifact for any course that lifts a stylesheet it did not write, which is every course
after the first.

## 20. "where is the text i'm counting. what am i counting? what are ids?"

**Course:** two (transformers), chapter 1's first exercise. **Found by:** the learner on
the day it shipped, one exercise into a twelve-chapter course.

**What was wrong.** The learner called the prompt "very unclear" and asked three
questions. Each one names something the page never said.

_Where is the input._ The prompt opened on the function's signature and never mentioned
that the data is handed in by the caller, so the obvious reading is that the exercise
expects you to go and find it yourself.

_What am I computing._ The thing being counted had been concrete in the chapter's prose,
where the reader counted some by hand, and turned abstract in the prompt, which stated the
contract precisely and never said the plain version of it.

_What is this noun._ The load-bearing one. The chapter's prose never used the word. The
exercise's contract was written in the representation the code works in, the design doc
had planned that representation for the following chapter, and so the first exercise of
the course was written in the vocabulary of the chapter after it. The notation reference
had a row for it, which is no help: that lookup exists for a reader returning weeks later,
not for first use.

**Why nothing caught it.** Every check was green, and the exercise itself is correct: the
tests pass, the solution passes, the skeleton fails for its own reason. **A contract can
be complete and still be unreadable, because completeness is measured against somebody who
already knows the nouns.** A prompt that opens with its contract is written for the person
who has already done the exercise.

**The fix.** A beat in the chapter at the point the story first needs that representation,
shown on the chapter's own small case and named as the small version of what the later
chapter builds properly, however late in the chapter the beat has to sit. Then every
prompt and skeleton rewritten to open with where the input comes from, what is being
computed in plain words, and what each argument means, before any shape.

**Rules:** "A prompt opens by answering where the input comes from, what the thing being
computed is, and what every argument means", and "A word the exercise cannot avoid is
taught in the chapter, in the same commit as the exercise".

**Cost:** one chapter beat, one figure, two prompts and two skeletons, on a chapter that
was hours old. The generalizable half is cheap and mechanical: before shipping an exercise,
grep the chapter's prose for every noun its contract uses. Deliberately not a script, since
a checker comparing contract names to prose flags every internal parameter and gets
switched off.

## 21. The output the chapter showed and the output the exercise printed

**Course:** two (transformers), chapter 1. **Found by:** the author, re-reading the prompts
the day after writing them.

**What was wrong.** The chapter quotes a generated string out of its committed bench. The
exercise after it hands the reader a snippet that generates the same way, and the snippet
printed the chapter's string with its first character missing: the bench seeds its output
with the item it starts from and the snippet did not. The prompt then quoted the snippet's
output, typed by hand from a run rather than imported, so the repository held two strings
for one process and nothing connected them.

The same off-by-the-starting-item sat in the bench's own record, a count written beside a
string one longer than it, because the number counts steps and the string counts items.
The chapter read that key out and told the reader "here is N characters of it" above a
block holding N plus one.

**Why nothing caught it.** Every check was green and every number was real. The bench ran,
the chapter imported it, the exercise's tests pass, and both strings are correct outputs of
correct code: outputs of two runs that disagree about whether the thing you start from is
part of what the run produced. The prompt's hand-typed copy was the only place the
disagreement was visible, and it was on the wrong side of it. It matched the snippet, so a
reader checking the prompt against the code it ships would find them consistent and the
chapter, three screens up, wrong.

**The fix.** The snippet seeds its output the way the bench does, so it prints the
chapter's string exactly, and the prompt quotes the bench's own field instead of a typed
prefix. The bench records a count of steps and a count of items separately, under names
that say which is which, along with what each run started from.

**Rules:** "Generated output is a number" and "An experiment the reader re-runs prints what
the chapter printed", both under Numbers.

**Cost:** four lines, before a reader reached it. The class is what makes it worth an
entry: a course whose method is "now run this yourself" puts a snippet beside every quoted
output, and every one of those is a place where two programs can disagree by one item with
every check green.

## 22. "screatch pad didn't work right after exercise 1"

**Course:** two (transformers), chapter 1, the workbench and the runtime under it.
**Found by:** the learner on the day it shipped, one exercise into the course.

**What was wrong.** The learner finished the first exercise, pressed Send to the scratch
pad on the experiment the prompt hands them, ran it, and got a FileNotFoundError on line 1.
Every prompt in the course opens its experiment by loading the dataset.

The worker fetches a dataset when the request carries a URL for one, and the scratch pad's
request read that field off the exercise belonging to whichever section the caret sat in.
No exercise sets it. **The field had been lifted from course one along with the runtime,
where its comment records the same bug one course earlier**, naming that course's own
dataset and the prompt that asked for it. The mechanism was there, unused, with the
incident that created it written on it, and the second course re-broke it anyway.

Running the snippets turned up two more. One experiment computed over the whole dataset
while the chapter's table computed over the training split, so a reader checking their own
function against the table read one number where the page said another, with nothing to
explain the gap. And that table's shares were rounded twice, once into the bench and once
by the component that renders them, which moved the last digit.

Behind all of that sat a fourth failure, found by clicking through the fix rather than by
any check. The dataset URL was relative, because the build's base is `./` so the site works
from any subpath. **A relative URL inside a web worker resolves against the worker
script's own directory, not against the page**, so the worker fetched a path that does not
exist, the static host answered the miss with the app's own `index.html` and a 200, and the
worker wrote that HTML into the dataset file. With the first fix in and this one still open,
the scratch pad ran happily and reported a vocabulary 19 characters larger than the real
one and a colon most often followed by a slash: the tally of an HTML file, printed without
an error anywhere.

**Why nothing caught it.** The prompts' snippets are the one kind of code in the repository
that nothing ran. The pre-commit list builds the app, runs every exercise's tests against
its solution and its skeleton, runs the panels' code outside the browser, and checks the
classes, the brand and the palette. **A copyable code block was prose to all of it.** The
type system had no opinion either, because the dataset field was optional on a request
whose only sensible value is the course's one dataset.

**The fix.** The URL is resolved against `document.baseURI` on the main thread, the only
side that knows where the page is, and the fetch refuses a URL that is not absolute with a
message naming the worker-relative trap. The field is required on the scratch-pad request,
so the compiler asks for it: reverting the fix fails the typecheck. The scratch pad sends
the dataset always, rather than reading it off the current section, and a missing file
becomes a sentence saying the workbench rather than the learner's code is at fault. The
bench stores unrounded and the page formats.

A checker now lifts every code block out of every prompt, runs it against the solved
document with the data in place, and asserts that the chapter's own committed values appear
in what it printed. It named two further defects on its first run, before it had ever
guarded anything.

**Rules:** "Every snippet the course hands the reader is run by a checker, in the
environment the reader runs it in", "A run path that takes the learner's code loads the
course's data unconditionally", "A URL handed to a worker is absolute", and "Round once,
where the number is displayed".

**Cost:** two lines of runtime wiring, found by the learner rather than by CI. The checker
that makes the class impossible is 90 lines. The worker-relative failure cost more than all
of it: it needed a real browser, a real worker and a local copy of the pinned runtime to
see at all, because every check in the repository stands in for the fetch it broke.

## 23. "sometimes it does on the first try but then repeated tries don't work"

**Course:** two (transformers), chapter 1, the same button as incident 22 and hours after
that fix landed. Ported to course one the same day, where the defect was identical.
**Found by:** the learner.

**What was wrong.** Send to the scratch pad wrote the appended text to local storage and
told the panel to open the pad. The panel opened it, scrolled it into view, and never
touched the editor. The editor takes its document once, when it mounts, so:

- the first send of a session arrived, because it was the thing that mounted the editor,
  and the editor read storage on the way up;
- every send after it stopped at storage, with the pad on screen showing the old text;
- and the reader's next keystroke ran the editor's change handler, which writes the
  editor's whole document to storage, so the stale copy overwrote the appended snippet and
  took it out of the pad's own Run as well as out of view.

Measured in a headless browser against the built site: two sends, then one keystroke, and
storage fell from 2,139 characters to 1,416. The snippet was gone from the one place the
reader could still have run it.

The panel had the fix already, ten lines above, for the same reason on the other editor:
"Follow an import or a splice that happened somewhere else. Without this the always-mounted
editor keeps the text it had and the next keystroke writes it back over what was just
loaded." One editor was guarded and its neighbour was not.

A second defect sat behind it, invisible while the first one held: the pad shows about six
lines at a time, so a snippet appended below a pad that already holds one is off screen.
Sending needs a scroll as well as a write, which means the position the text landed at has
to travel with the request rather than a bare counter.

**Why nothing caught it.** **No check in either repository mounted an editor.** One runs
the exercises' Python, one runs the prompts' snippets outside the browser, one reads the
components' class names, and the build only typechecks; all of them were green through both
defects, in both courses. The failure also needs three interactions in order, open then
send then type, and leaves no trace in any file, so reading the diff would not have shown
it either.

**The fix.** The provider computes the appended text, writes it, and reports where the
snippet landed; the panel pushes that text into the editor and scrolls to the offset. Both
paths are covered: the pad already open, where the editor exists and gets the text pushed
in, and the pad closed, where the editor mounts holding it and gets scrolled once it
reports ready. A sequence number rather than a timestamp, and a ref holding the last one
applied, so a send is applied exactly once and opening the pad by hand does not move the
reader.

Both courses now have a browser check that presses the button twice and then types, in the
docked layout and the phone sheet, with the pad seeded with filler lines so that "did it
scroll to the new snippet" has an unambiguous answer: no filler line may be on screen
afterwards. Verified by putting the defect back, which turns four cases red per layout in
each course.

**Cost:** three files and about sixty lines in each of two courses, plus the browser checks.
Found by the learner, on the button that had been fixed hours earlier. The class is worth
naming once: **an always-mounted editor is not the same object as the storage under it**,
and any control that seeds one has to write to both.

## 24. "The promotional materials across these courses 'taglines' are cringy"

**Course:** the series, and both courses in it: the mastheads, front doors, social cards,
metadata and series-index cards.

**Found by:** the primary learner, while comparing the courses as a pair.

**What was wrong.** The social cards used the same sentence with blanks: "A course on
[topic] that you finish by building [artifact], in Python, in your browser." The title had
already named the topic, and the series descriptor had already said build-it-yourself, so
half the sentence repeated the furniture around it. "That you finish" advertised the
course rather than describing the work. The final stack of Python and browser details read
like keywords added to a slogan. Seeing the Transformers version beside the Neural
Networks version exposed the Mad Lib underneath both.

The mastheads used different feature lists again. That left each surface trying to invent
its own pitch, although they all described the same course.

**The fix.** Give each course one plain-language sentence that names a concrete arc: what
the learner builds, then something visible it does. Neural Networks now goes from the
smallest parts to recognizing handwritten digits; Transformers goes from the smallest
parts to writing. Python, the browser and no setup remain useful facts, but they sit in
supporting copy. The same sentence opens the masthead, front door, README, social card,
description metadata and series-index card.

**Rule:** "The tagline is one plain-language sentence about the learner's concrete arc."
It is written once in the design doc and reused verbatim everywhere promotional copy needs
it.

**Cost:** two existing courses, the series index, both generated social images and the
course kit all had to change. Written before the scaffold, the rule costs one sentence.

---

## The patterns behind the twenty-four

Four of course one's (2, 6, 7, 12) are the same chapter, and it is the one chapter authored
outside the playbook, in a single 25-file commit that also touched the stylesheet, the app
shell and the runtime. Two regressions landed in that commit as well, in files nobody was
reviewing for UI.

That chapter also had, at birth, every structural component the conventions required:
section headers, the on-this-page nav, an aside box, a recap. **Structural conformance is
not playbook conformance.** A chapter can carry every component and still fail the reader
completely.

**Incidents cluster at the two ends of a course.** Three of course one's (14, 17, 18) are
its ending, all three found by a reader who had finished it rather than by a review of a
chapter, and two of them are the first fix failing: the closing chapters of incident 14
were the right chapters, and both of the things they were asked to carry were wrong on
them. Four of course two's (20 to 23) are chapter one's exercises and the scratch pad they
run in, all four found within hours of that chapter shipping. Neither end is reviewed the way the middle is. The ending is
written last, by an author who has read every earlier chapter too recently to skim
anything. The first exercise ships before any of the machinery under it has met a reader,
and it is the first thing a reader touches with their own hands. Everything in between gets
reviewed by the act of writing what follows it.

**Every check was green, every time.** All five of course two's entries carry a "why
nothing caught it" paragraph, and in every one of them the whole pre-commit list passed.
That is structural rather than unlucky: a check suite grows around the classes that have
already bitten, so the next incident is by construction outside it. What those five have in
common is the response rather than the cause. Each bought either a checker or a rule that a
checker enforces; each checker was written the same day; and the one that lifts the prompts'
snippets and runs them named two further defects on its first run, before it had ever
guarded anything. **Write the checker while the incident is still warm, and expect it to
pay for itself immediately.**

**Lifted code carries its traps, and a comment is not a check.** Incidents 22 and 23 are
both in the workbench and the runtime that the second course lifted whole from the first,
and 23 was live in both courses at once. In 22, the mechanism that broke had a comment on
it recording the same failure one course earlier, in the first course's own words, and the
second course broke it anyway. In 23, the same file held the guard, ten lines above the
code that needed it. Reading is not a control. A course that lifts a subsystem inherits its
traps, so the check that would have caught the first occurrence belongs in this kit rather
than in whichever course happened to find it.

**Every incident here was first noticed by a person.** A learner reading, a learner
clicking, an author re-reading their own prompt the next day, one teaching review of a
finished course, and one comparison of two courses side by side. The benches and checkers
found plenty afterwards, several on their first run, but never the first instance of a
class. That is the honest reason this playbook is long: the failures it prevents are not
the failures that a type checker or a test suite finds.
