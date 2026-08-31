# The stuck button

Notes on a learner-facing "I'm stuck" button: what the series already has, what it does
not, and the three questions that decide whether it ships at all. A brainstorm rather
than a design doc. It follows the kit's Phase 0 convention of **append, never revise**:
when an open question below gets answered, annotate it in place rather than editing the
question away.

The one-line version: the artifact already knows almost everything the button needs, the
transport for a portable dossier is already built and already a file, and the expensive
part is neither of those. It is that answering well removes the data this method runs on.

---

## The button already exists, pointed the other way

`course-kit/.claude/commands/stuck.md` is this product, written for the author instead of
the learner. It runs at authoring time, in a repo, with Claude Code, and its contract is
better than anything a support chatbot would be given:

> This is a comprehension bug report, not a style note. Treat my words as the evidence.
> **Do not defend the passage.** Find the mechanism of the failure, not a nicer wording.

That is the spec. The learner-facing button is `/stuck` shipped to the other side of the
page, and the design work is mostly about what changes when the person pressing it wants
to be unblocked in ninety seconds rather than to fix the chapter.

Those two goals conflict, and that conflict is the whole product. Held together, the
button is the method at scale. Split apart, it is a chatbot that quietly makes the course
worse.

## What is free

Six things the courses already do that a stuck button would otherwise have to invent.

**An exact address, already tracked.** Section ids are unique across chapters and prefixed
with the chapter (`c4-`), and each chapter mounts one on-this-page nav that discovers its
own section headers from the DOM and scrollspies them. The scrollspy already computes
"which section is the reader in" on every scroll and throws the answer away. "Reference an
exact location in the course" is a read of a value that exists.

**Structured attempt history, not scroll depth.** The exercise contract says tests run in
definition order, fail by raising with a teaching message, and take their display title
from the first docstring line. So the runtime can already say: this learner ran the chapter
6 suite eleven times, `test_gradient_matches_numeric` has never passed, and the message it
raises names the misconception it was written to catch. That is an order of magnitude
better than any signal a general tutor gets, and it is the difference between a dossier and
a reading log.

**A flagship proof per course.** The kit requires each course to name its one automated
proof that the learner's implementation is right, and to celebrate it in the UI. Whether
that test has ever gone green is the single most informative bit in the dossier.

**Export and import, already shipping.** `state/progress.ts`, `state/storage.ts` and
`state/workbenchDoc.ts` carry no chapter ids, no exercise ids and no topic knowledge, and
the index already promises the learner "you can save it to a file and load it back."
Portability is not a feature to add. The dossier is a superset of a file format that
exists, and the courses already have the code that reads and writes it.

**A per-course concept registry, maintained under a hard rule.** The notation reference is
one folded lookup carrying, per row: the symbol, one line of meaning, the field's name for
it, and the chapter that introduced it, in the order a reader meets them. Adding notation
means adding a row in the same change. That is a machine-readable list of every concept the
course names, with the field's word attached, kept current by an existing rule rather than
by goodwill.

**A ready-made rule for what may cross a course boundary.** The vocabulary handover sorts
every coined word into three tiers: **switch** (the field's word becomes primary),
**run both** (the plain word stays primary and the field's word rides along), and
**local only** (scaffolding for one beat, with no counterpart anywhere). A cross-course
answer may reach for switch and run-both words. It must never use a local-only word,
because that word means nothing outside the course that coined it. The constraint that
makes cross-course explanation safe is already written down, for a different reason.

## What is not free

**A cross-course concept spine.** Two notation references do not join themselves. Saying
"this is the same slope you computed by hand in Neural Networks chapter 3" needs a shared
id behind both rows, and nothing produces one today.

Where it lives is already settled by an argument in the README, though. A course links
**up** to the index and never across to a sibling, because the alternative means editing N
repositories to ship the N+1th and any one of them forgotten shows a stale list forever.
The same logic applies exactly: courses publish concept rows up to this repository, and no
course ever reads another course's registry. If the spine lives anywhere else it is the
sibling coupling the series already rejected.

**Addresses that survive revision.** METHOD.md measured about five revision commits per
new chapter, overwhelmingly additive, chapters growing three to four times longer. An
address stored as "section `c4-receipts`, third paragraph" is wrong after the next pass. The
series has met this before: renaming course one's modules to chapters needs `#m1` to `#c1`
hash aliases because those addresses live in bookmarks and shared links. A dossier is a
bookmark file. It wants the same alias discipline, decided before the first one is written
rather than after ten thousand exist.

**Interactive state.** The most useful thing the button can do is often not prose (below),
and doing it needs interactives to be addressable and settable by URL. They are not today.

**Somewhere for the answer to come from.** The one genuinely new piece of infrastructure.

## Three questions that decide it

### 1. The no-backend, no-account stance is load-bearing copy

The index says it in the front door: everything runs in the browser, "with no account to
create and nothing to install," and your work is stored locally. The kit offers "anything
with accounts or a backend" as the example non-goal a course fills in. Neither is a
throwaway line: the same section is why the courses are self-sufficient, which is goal two
in the kit's priority order.

A paid button needs a key that cannot ship to a browser, which needs a server, which needs
an identity to bill. There is no version of this that does not touch that claim.

The way out that costs least: **split the dossier from the answering.** The dossier stays
local, free, and a file, an extension of `state/progress.ts` that never requires an
account. The paid thing is the answering, which takes the dossier as input. Then the
sentence on the index changes from a promise to a scope: the course needs no account, and
the optional tutor does. A lapsed subscription strands nobody, because the asset the
learner built is on their own disk in a format the free course still reads.

Do not sell the dossier. It is the learner's record of their own confusions and their own
code. Charging rent on it is the version of this that would be hard to defend.

### 2. Course one may not be allowed to carry it

`course-kit/CLAUDE.md` records that course one shipped saying "this project" inherits
CC BY-NC, and states the consequence flatly: a NonCommercial spine "is survivable if the
goal is reach; it is fatal if the goal ever becomes revenue."

A paid button on the Neural Networks course sends that course's adapted chapter prose into
a paid service as context. Whether that is commercial use of the source is a question for
someone who reads licences for a living, and the honest planning assumption is that it is.
Notably, the same rule already establishes that the engine, the brand layer and the tooling
contain none of the source and carry none of its terms, so the button's machinery is clean
even if course one's content is not.

Two consequences worth deciding early. The button may have to ship on Transformers first
and never on course one, which makes it a per-course capability rather than a series one,
which the index will have to show. And source licence moves from a footnote in a course's
Phase 0 to a commercial gate: pick CC0, CC BY, MIT or public domain, as the kit already
advises, and now for a second reason.

### 3. Answering well destroys the input to the method

This is the one that matters, and it is not obvious.

METHOD.md is blunt about where the course's quality comes from: "you are not writing a
course, you are debugging one against a reader," the learner is the test suite, and 20 of
course one's 64 non-merge commits either attribute their change to the reader or record his
words as a rule. Nineteen casebook incidents are nineteen times someone got lost and said
so. The two most valuable sentences anyone said during course one were "over my head" and
"we're just talking about curves..... why??"

A stuck button that answers well intercepts every one of those sentences. The learner is
unblocked, is grateful, and the chapter stays broken for everyone after them. The button
privatizes the fix. Run at scale, it is a machine for converting comprehension bugs into
support tickets that nobody reads, on a method whose engine is comprehension bugs reported
verbatim.

The same fact inverted is the strongest argument for building it. The loop currently needs
a named friend willing to read ten chapters out loud and stop when he is lost, which is why
it has run once, with n=1. A button is that instrument for every reader: the exact section,
the failing test, and the learner's own words for what went wrong, at the moment it went
wrong, which is the window METHOD.md says the whole thing depends on ("a reading session
followed by two to five commits within a few hours, while the confusion is still
articulable").

So the requirement, and it is a requirement rather than a nice-to-have: **every press is a
comprehension bug report first and an answer second.** Presses cluster by section id. A
section with a cluster is a chapter to restructure, and the aggregate flows back into
`/stuck` at authoring time with the reader's own words attached. A button that answers and
records nothing is a regression against the method, however good its answers are.

Which also means the button's success metric is not satisfaction. It is presses per section
falling after a revision pass.

## What the dossier can honestly claim

The kit already bans the tempting version. "A score gets a breakdown": any aggregate number
reported to the learner gets its decomposition beside it, never the single number alone.
And casebook 14 is the standing warning about inferring understanding from completion, a
learner who "could explain it and could not use it," found only by a review of the finished
course.

So: **the dossier records evidence, with receipts, and never a mastery score.** "Passed
`test_gradient_matches_numeric` on the fourth attempt, after two runs that raised the
shape error" is a fact the artifact observed. "Understands backpropagation: 82%" is a
fabrication, and a course that spent five days deleting unearned claims from its prose
should not ship one in a file.

What it can hold, all of it observed rather than inferred:

- chapters opened, and the furthest section the scrollspy reached in each
- exercises attempted, per named test: passes, failures, attempt counts, and the raised
  message
- whether the flagship test has ever gone green
- the learner's current code, which they already own and can already export
- notation rows encountered, by the chapters they were introduced in
- every stuck press: section id, their words, and what was on screen
- interactives touched and with what parameters, once interactives report it

The last two are new instrumentation. The rest is a projection of state that exists.

## What actually travels between courses

The flashy version of portability is cross-course analogy. It is the low-value half, and
the kit's own rules say why. "A callback earns prose only if it removes work or carries the
argument," and one that only says "remember this from before" costs attention and returns
nothing. Most cross-course references fail that test. Worse, "assume weeks pass between
chapters, never lean on a bare name from an earlier chapter as a load-bearing reference"
applies double across courses and across months, so any cross-course callback has to
restate the thing in plain words anyway, at which point the dossier saved nothing.

The high-value payload is duller and much better: **the measured learner floor.**

Phase 1 asks for the floor as a list of what the learner does not know, then insists on
confirming it by writing two paragraphs at that floor and reading them, because a floor
that is wrong makes every chapter written against it wrong. Today that floor is authored
once per course as a careful guess about one named person.

A dossier makes it measured. Course two opens knowing this person has written a gradient
descent loop by hand and got it green, has met nabla and can pronounce it, has never seen a
tensor or an attention score, and needed four attempts and the "log first" figure before
the chain rule landed. That is checkable, mundane, cheap, and it is the input the method
says is most expensive to get wrong. It needs no concept graph, only notation rows and test
outcomes.

Lead the portability story with the floor. The analogies can come later, if the spine ever
justifies itself.

## The button's best answer is usually not prose

Casebook says which fixes worked, across nineteen incidents: "the fixes that worked in
course one were reorderings, figures and worked examples, not adjectives." Move the
interactive earlier. Log the numbers first. Draw the thing. Pick an example where the
mechanism is visible. Name the pattern and sort the instances into kinds.

A chatbot cannot reorder a chapter at runtime. It can do the other four, and this is where
the product stops being "an LLM with course context in its prompt":

- **Route backward to the interactive, with parameters set.** Casebook 3 is a learner told
  that changing something by 0.01 changed the result by 0.01, on the one hop whose partner
  was 1.0: "so what?" The fix was to lead with the times-2 wire, where the effect shows.
  A button that opens chapter 3's interactive preset to the case where the mechanism is
  visible is applying the course's own best fix, not describing it.
- **Generate the receipts table from the learner's own numbers.** The runtime can execute
  code strings and return a structured verdict, so the button can re-run this learner's
  actual code and produce the before/after/change log first, then explain each stage as a
  rule that predicts the next logged number. That is "log first, explain second" performed
  rather than quoted, on their numbers rather than the chapter's.
- **Name which rule the passage broke.** The authoring `/stuck` demands this, and it turns
  a vague complaint into a routable one. It is also the field that makes the aggregate
  useful at authoring time.

The generated prose is the fallback, not the feature.

And it is gated prose. `/house-style` measures per chapter: median sentence length, cleft
and abstract-first openers as a share of sentences, paragraphs opening with a pronoun,
parentheticals, callbacks per paragraph, and em dashes, which must be zero. The bands are
written down: clefts at or under 5 percent, pronoun aphorisms at or under 5 percent, median
sentence length 19 to 23 words, callbacks 0.4 to 1.2 per paragraph. The register test is one
sentence: could this appear unchanged in a careful colleague's explanation email?

That is unusual and worth exploiting. The series has a measurable style spec and a script
that computes it, which means generated answers can be linted the way chapters are, instead
of being trusted. Without it the button will sell, promise, flatter and narrate, because
that is the house style of every model, and the course spent five days deleting exactly
those sentences. Casebook 15 prices the retrofit: a register fix over four finished chapters
that then did not hold, chased through four further commits, with the same drift found again
in the final pass. A runtime generator would reintroduce it on every press.

## Packaging

The recommendation, in order of what it protects:

1. **The dossier is free, local, and a file.** No account. It is the learner's own record,
   an extension of a format the courses already read and write.
2. **The stuck report is free.** The button assembles the exact section, the recent reading
   path, the failing test names and their raised messages, the code, and the notation rows
   in play, into one structured block the learner can copy into whatever assistant they
   already have, or send to the author with one tap. Zero infrastructure, zero licence
   exposure, no identity, and it is the authoring `/stuck` command's input, formatted by the
   artifact instead of typed by a friend.
3. **The answering is the paid layer**, on courses whose licence permits it, priced per
   course rather than per seat if the catalogue stays small.

Two notes on copy, because this repository is strict about it. The pricing surface inherits
the social card's discipline: "the only thing on a card that reads as credible is a fact,
and if there is no room for facts then quiet is the next best thing." And the button's
placement inherits casebook 18, "a reader who reaches an exit door takes it." A prominent
help affordance beside a hard passage is an exit door. It belongs where a stuck reader will
find it and not where a reading reader will be offered it.

## Build order

Cheapest first, and each step is worth shipping alone.

1. **Record the presses.** The stuck report, free, local, copy-to-clipboard. No model, no
   server, no account. It answers the only two questions that matter before spending
   anything: do learners press it, and is the assembled context actually enough for a
   competent assistant to help? If the pasted report does not produce good help from a
   model the learner already pays for, no backend will fix that.
2. **Promote progress to a dossier.** Extend the existing export with the attempt history,
   the reading path and the presses. Decide the address alias scheme here, before there are
   files to migrate.
3. **Publish concept rows up to this repository.** One file per course, generated from its
   notation reference by a committed script, so the spine is derived rather than
   hand-maintained and cannot go stale silently. Courses never read each other.
4. **Then the answering service**, whose first job is dispatch (route to an interactive,
   re-run their code, produce the receipts table) and whose second is prose, linted against
   the house-style bands before it renders.
5. **Close the loop.** Presses aggregate by section id and land in the authoring `/stuck`
   flow with the learner's words attached. Watch presses per section fall after a revision
   pass. That number is the product working.

Steps 1 through 3 need no backend, no account, and no licence conversation, and step 1 is
useful the day it ships whether or not step 4 ever does.

## What will go wrong

- **The button becomes an adjective machine.** It will be asked for help exactly where the
  course is hardest, which is where course one needed four restructures in one day and a
  live tutoring session, and a model handed that passage will produce a nicer wording. The
  authoring command forbids that in its first instruction for a reason. A wrong answer at
  the hardest passage is worse than no button.
- **The dossier leaves the browser.** A record of one named person's confusions and their
  code, sent to a service, is a confusion record on someone else's disk. "No account" was a
  privacy property, not only a convenience one. Whatever the answer is, it should be a plain
  sentence on the page rather than a policy page.
- **Paying creates an expectation the free course never carried.** The first "the button
  explained softmax wrong" is a refund conversation about a free course.
- **The ending stays the least reviewed part.** Casebook's own summary: three of nineteen
  incidents are the end of the course, all three found by a reader who had finished it
  rather than by any chapter review, because the ending is written last by an author who
  has read everything too recently to skim. Press data will land there first and hardest.
  That is the button earning its keep, and it will not feel like it.

## Open questions

- Per-course pricing or series subscription, given two courses and one of them possibly
  ineligible?
- Does the free stuck report send to the author by default, on request, or never? The
  method wants the data; the learner did not ask to be a test suite.
- Who is the button for: the learner who will not otherwise message anyone, or the author
  who currently has one reader? The answers rank the build order differently past step 3.
- Does the index show which courses carry it, and how, without adding a second
  hand-maintained list that can go stale?
