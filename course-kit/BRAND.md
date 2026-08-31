# The series brand

A visual identity meant to carry across several courses on unrelated topics, published as
separate GitHub Pages sites, so a reader who lands on one recognizes the others as siblings.

Design constraint: plain and readable, with identity. Not a design system, and no
dependency a course has to install. The whole thing is five files: a stylesheet, the file
that names the series and the course, and three small components.

---

## What makes it a set

Five things, and only these five, have to hold across courses.

**1. The accent family.** Nine hues at one OKLCH lightness (0.478) and one chroma (0.0975),
the values of the first course's green, held fixed while the hue turns 36 degrees at a time.
Same lightness and chroma means siblings read as a set: only the hue tells them apart, so no
course looks louder than its neighbour, and none can pick an accent that is off-brand by
being darker or more saturated.

Contrast is a consequence rather than a hope. Every hue lands between 6.1:1 and 6.9:1
against the page ground and between 6.2:1 and 6.9:1 under white ink, so any one of them
works as text, as a rule, and as a button fill. AA wants 4.5:1.

| token           | hex       | on the ground | under white ink |
| --------------- | --------- | ------------- | --------------- |
| `--hue-green`   | `#0b6e4f` | 6.14          | 6.25            |
| `--hue-teal`    | `#016a70` | 6.25          | 6.37            |
| `--hue-blue`    | `#12648d` | 6.38          | 6.50            |
| `--hue-indigo`  | `#4b5894` | 6.60          | 6.72            |
| `--hue-violet`  | `#6d4d87` | 6.73          | 6.86            |
| `--hue-plum`    | `#83456a` | 6.82          | 6.94            |
| `--hue-crimson` | `#8c4445` | 6.81          | 6.94            |
| `--hue-oxide`   | `#864d1e` | 6.66          | 6.79            |
| `--hue-moss`    | `#4c6726` | 6.30          | 6.41            |

`tools/brand_palette.py` regenerates the family and prints these ratios; `--check` fails if
`brand.css` has drifted from what it computes. One stop on the circle is deliberately
skipped: the hue between oxide and moss comes out an olive that reads as a mistake rather
than as a choice.

Washes are mixed from whatever the accent is, so a course that changes one line gets a
matching set instead of hand-picked near-whites that now clash:

```css
--accent-wash: color-mix(in oklab, var(--accent) 6%, var(--bg)); /* tinted paper */
--accent-panel: color-mix(in oklab, var(--accent) 14%, var(--bg)); /* a visible panel */
--accent-rule: color-mix(in oklab, var(--accent) 30%, var(--bg)); /* a visible rule */
```

All three mix with `--bg`, which is one reason the ground, the inks and the rules are
declared in `brand.css` rather than in a course's own stylesheet. They were the other way
round once, referenced in the layer and declared in the course, which meant the layer
worked only by load order: a sibling that dropped the folder into an empty repo got three
invalid mixes and lost every surface painted from them.

```css
--bg: #fdfdfb;
--ink: #1a1a1a;
--muted: #5a5a5a;
--rule: #e2e2e2; /* a container's edge, deliberately faint at 1.27:1 */
--rule-strong: #c4cac2; /* a boundary that marks something as a control */
```

The courses have exactly two inks and no third. The series index carried a lighter grey
beside `--muted` once, `#767a77`, for its card meta lines: 4.28:1 on the ground, below AA
at the 0.78rem those are set in, and nothing in the repository would have said so. The
weight of the label idiom does the work that grey was doing. Unlike the family, both inks
are hand-picked rather than computed, so `brand_palette.py --check` measures them against
the ground instead: `--ink` at 17.09:1 and `--muted` at 6.77:1.

**2. The rule across the top.** Three pixels of the course's own hue, at the very top of
every page. It is on `body` rather than fixed, so it never fights a sticky bar or a
fullscreen editor for the top three pixels.

**3. The type pairing.** A serif for everything read in sentences, a sans for everything
that is chrome. The contrast between them is what tells a reader that a piece of text is
machinery rather than prose, and it costs nothing:

```css
--font-prose: Georgia, "Times New Roman", serif;
--font-ui: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--font-display: var(--font-ui);
--font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

Georgia is a choice, not a fallback: the most consistently available serif with a real
italic, and a large enough x-height to survive the 19px root at the sizes figures need.
Nothing is downloaded, which keeps a promise the courses make about what leaves the
reader's machine. If a course ever ships a display face, it replaces `--font-display`
alone and nothing else moves.

The label idiom is the sans doing its most visible job: small, uppercase, letterspaced.
It marks the series wordmark, the aside and nav labels, the passed badge, and every
"this is a kind of thing" marker.

```css
--label-size: 0.72rem;
--label-tracking: 0.09em;
--label-weight: 600;
```

**4. The reading measure, and one axis.** Two widths on a page, and only two. Everything
read as text runs to `--measure` (34rem, about 69 characters at a 19px root): prose,
headings, captions, the cards, and the display equations. Everything that is an
illustration keeps the whole column: figures, tables, panels, the editor, the blocks that
hold code. That is the single change that does most for how designed a long reading page
looks.

Resist a third width in between. The first course gave equations their own 42rem, on the
grounds that they centre themselves and cannot re-wrap, and the result was three widths
on one page, which reads as an accident rather than as a rule; it also failed the four
equations that were wider than 42rem anyway. Splitting a long equation over two or three
lines is what a typesetter does with it regardless. A card's box carries the measure plus
its padding AND its borders, so the lines inside it land on the same axis at the same
width as the paragraphs above and below it.

**Centre the measured content in the column; do not left-align it.** This is the part that
is easy to get wrong, and the first course got it wrong first. Left-aligned, every block
wider than the prose hangs off to its right and the page reads as lopsided; centred, the
prose, the equations and the figures share one centre line and an equation sits dead centre
over the paragraph that introduces it. The masthead, the headings and the figure captions
belong on that axis too: a title starting at the column edge while the prose under it starts
113px further in reads as a misalignment, not as a wider header.

Keep the column itself centred at every width. A column shifted off centre to open a gutter
for a sidebar charges every page that has no sidebar, including the front page, which is the
first thing anyone sees.

Apply the measure with direct-child selectors on the reading column, never on `p` globally:
in a stylesheet with two dozen interactives in it, a paragraph inside a panel or a control
row must not inherit a prose measure. And watch for rules further down the file that set a
`margin` shorthand, which resets the horizontal `auto` that does the centring.

**Figures: one number in the markup, every width derived from it.** A figure carries its
viewBox width into CSS as a custom property (`--fig-units`, set by the same helper that
writes the viewBox), and every width rule is `calc()` on that. Otherwise a stylesheet ends
up with `min(490px, 100%)` written out beside a viewBox that says 490, in eight places, and
tightening a viewBox leaves the two disagreeing.

Keep each viewBox tight to what the figure draws, about eight units of margin a side. A
padded viewBox is not free: the figure reserves that width in the column, starts shrinking
as if it were that wide, and on a phone the reader pans across the empty margins. Centring
the ink inside a padded box, which is the tempting fix, leaves all of that in place.

Diagrams that belong to a set should render at one scale, so a diagram with fewer boxes in
it is narrower rather than differently drawn. Calibrate that scale so the widest of them
fills the column exactly, and have a check fail if a new one exceeds it.

**Two CSS traps, both found by measuring rather than by looking.** A custom property that
references another is substituted **where it is declared**: `--cover: var(--ground)` at
`:root` freezes the root's value and inherits that down, so a card with a ground of its own
still gets the page's. Read the token on the element that paints. And an invalid `var()`
makes the whole declaration invalid at computed-value time, so a width built that way
silently falls back to `auto`, which for an SVG with a viewBox means 100 percent. That
scaled every plot figure to twice its drawn size, and the page looked _better_, not broken.
Compare drawn sizes before and after a change like this; a screenshot will not tell you.

**Labels on lines need clearance, not a halo.** A background-coloured stroke behind the
glyphs (`paint-order: stroke`) covers the line beside each glyph and not in the gaps
between them, so a line running through a label still reads through it. Move the label
clear, remembering that an offset moves the _baseline_ while the glyphs stand above it, and
draw every label in a pass after every line or a later line paints over an earlier label.

**Phones: the header is the thing to cut.** Measured on the first course at 390x844, the
masthead and tab strip came to 329px and the first line of prose sat at 892px, past the
bottom of the screen. Three changes, in order of what they bought:

- **A picker instead of a panning strip.** A row of tabs that does not fit is usually made
  to pan sideways, and that is the worst way to offer a list: the active tab is centred, so
  a phone shows three of them and the reader has to discover that the rest exist. Fold the
  same list into one line that names where you are and opens the rest vertically. Wrapping
  is not the alternative it looks like: eleven tabs wrap to six rows on a 390px screen.
- **A compact masthead on inner pages.** Give the masthead a `compact` flag and let the
  application pass it for every page but the front door. On a phone, compact drops the
  tagline and sizes the title to a running head. The tagline summarizes the course's
  concrete arc, which belongs on the front door rather than above every inner page.
- **Fold the page's opening card.** Anything that sits between the title and the first
  sentence is a wall on a phone. A `<details>`, open above the phone breakpoint and closed
  below it, keeps the promise and gives back a third of the screen. Read the state once at
  mount rather than watching the media query, so a reader who opens it is not shut out by a
  rotation.

**Touch, and two traps.** 44px is the smaller of the two platform minimums and a good floor
below the width where a phone layout takes over. An unstyled `input[type="range"]` is 16px
tall: `min-height` grows its box while the browser keeps the track centred, so the
affordance looks unchanged and the whole box is live. And a `<summary>` is
`display: list-item`; setting `display: flex` on it to centre it in a taller target removes
the disclosure marker, which is the one thing saying the block folds.

**In-page jumps should be instant.** A browser's smooth scroll animates toward the offset it
computed when it started. If the page mounts anything as it comes into view, the document
grows in flight and the jump overshoots: measured at 971px of growth and a heading 189px
above the viewport, repeatably, on a phone, while the same jump on a desktop was exact.
Nothing is lost, because a jump of thousands of pixels animates a blur with nothing readable
in it. Sections also need `scroll-margin-top` clearing whatever sticky bar is on screen, or
the heading lands behind the bar it was chosen from.

**5. The lockup.** The series mark, the series wordmark, and the course subject on the
line below:

```
[series mark]  MOVING PARTS  |  BUILD-IT-YOURSELF COURSES
Neural Networks
Build a neural network from its smallest parts, then teach it to recognize handwritten digits.
```

**The tagline is one plain-language sentence about the learner's concrete arc.** Name
the thing they build in words that make sense before the course, then name something a
stranger can see it do. Do not classify the page ("A course on..."), advertise that the
reader will finish, or pack the sentence with implementation and delivery details. Those
details, such as Python, the browser and no setup, belong in supporting copy.

The sentence is canonical, not a fresh line for each surface. Reuse it verbatim in
`COURSE.tagline`, the front door's opening, the README lead, the social card, the page's
description metadata and the course's card on the series index. A surface may follow it
with its own factual detail. The current pair shows the shared method without becoming a
template with blanks:

- Build a neural network from its smallest parts, then teach it to recognize handwritten
  digits.
- Build a small language model from its smallest parts, then teach it to write.

**The series name is an imprint, not a prefix.** The courses are "Neural Networks" and
"Transformers", published under one name, so the wordmark sits above the heading rather than in
front of it, and a sibling reads the same two lines with only the heading changed. Pick a
series name that works this way. A name that has to be prefixed stops being grammatical
the moment the subject is a plural or a noun phrase ("Grokking Neural Networks" is a
phrase, not a title), and it puts a word in front of the heading that every page in the
series already carries.

The heading needs no hidden prefix, because the wordmark right above it is text: a screen
reader reaches the series name first and then the course. The document title reverses them
("Neural Networks · Moving Parts"), since the subject is the word that has to survive being
one tab of eight.

The monogram beside Moving Parts is the series mark: three bands sampled across the accent
family. It stays the same in every course because the adjacent name is the series name.
The course has a separate glyph for places that identify the course itself: its favicon,
its social card, and its card on the series index. **Pick something the course itself
draws.** The first course uses the sigmoid curve, which is the first figure in its chapter
1 and the shape every unit in the course is built from. A glyph that means nothing is worse
than a letter.

## Three details that carry more than they look like

**A section title wears a short accent rule above it.** 26 by 2 pixels, in the course's
hue. On a long single-scroll page it is the only thing that says a new section started, and
because it is drawn from the accent it is the one piece of structural furniture a sibling
course inherits already recoloured.

**Hover is declared per variant, never on `button`.** A bare `button:hover` outranks
`.tab:hover` and every other variant that sets its own transparent background, and fills
them solid. The first course shipped that bug and had to revert the whole hover pass. The
primary treatment is reached as `button:not([class])`: every variant carries a class, so
the selector cannot reach one.

**The width where the nav strip folds has headroom in it.** The first course's eleven tabs
wrap to two rows down to 881px and to a third row at 854, and the fold to the picker is
set at 880 rather than at 854. The labels are set in `system-ui`, which is a different
face on every platform, and a sans a few percent wider moves that boundary up into the
band. Folding early gives up 26px of widths where the strip would still have fit; getting
it wrong the other way puts three rows of navigation above the course on somebody else's
machine. Neither navigation pans at any width: below the fold it is the picker, not a row
dragged sideways.

## The code editor

If the course has an in-page editor, theme it: a stock editor theme is the most visible
surface on the page that nobody chose. Two halves, both in the editor component rather
than the stylesheet, because the editor generates its own class names:

- **Chrome** from the surfaces and the accent: the card surface behind the code, the sunken
  surface behind the gutter, the accent as the caret, the 6 percent wash as the active line,
  the 14 percent panel as the selection.
- **Token colours from the accent family.** Do not hand-pick syntax colours. Every hue in
  the family sits at the one lightness that clears 6:1 on the page ground, so taking
  keywords from violet, strings from moss, numbers from oxide and definitions from blue
  gives a syntax theme that is legible by construction and unmistakably the same brand.

## The files

| file               | what a course changes                                 |
| ------------------ | ----------------------------------------------------- |
| `brand.css`        | one line: which hue `--accent` points at              |
| `brand.ts`         | the four `COURSE` fields: id, subject, tagline, glyph |
| `Monogram.tsx`     | nothing                                               |
| `Masthead.tsx`     | nothing                                               |
| `SeriesFooter.tsx` | nothing                                               |

The stylesheet is most of the volume, comments included, and the three components run 25 to
50 lines each. Run `wc -l src/brand/*` for the current figures rather than quoting a number
from here: this table carried per-file counts for a while and they went 250 lines stale,
because `brand.css` grew 70 percent after they were written and nothing tied the two
together.

The rest of `brand.ts` is `SERIES`, and a course copies it unchanged: the name, the note,
the one-sentence what, and `homeUrl`. There is deliberately no list of siblings in it, and
adding one is the failure the whole design exists to prevent; see "link up, never across"
below.

`brand.css` is loaded first, so a course can still override anything in it:

```css
@import "./brand/brand.css";
:root {
	/* the course's own tokens */
}
```

The footer's legal text arrives as children rather than from `brand.ts`, because every
course carries different obligations and a shared component holding them would end up
either wrong or empty.

## Wiring it into a course

1. Copy `brand/` to `src/brand/`.
2. Edit `brand.ts`: the course's id, subject, canonical tagline and glyph path. Reuse the
   tagline verbatim in the front-door opening, README lead, social card, description
   metadata and series-index card. Keep runtime and setup facts in separate supporting
   copy. All of `SERIES` is copied from a sibling unchanged, `homeUrl` included, because
   every course carries the same series name, the same descriptor and the same index.
   There is deliberately no list of siblings to add the course to; see "link up, never
   across" below for why not.
3. Edit the one `--accent` line in `brand.css` to an unused hue.
4. `@import "./brand/brand.css";` at the top of the course stylesheet, and delete whatever
   it already had for `h1`, the tagline, the nav strip and the footer, so the two do not
   fight over specificity.
5. Render `<Masthead nav={...} />` and `<SeriesFooter>{attribution}</SeriesFooter>`.
6. Put the same glyph in `index.html`'s inline favicon, tile filled with the accent and the
   path stroked white, and set `theme-color` to the accent.
7. Copy `tools/check_brand.py` and `tools/brand_palette.py` from a sibling course and run
   both.

Step 6 is the one that goes stale, which is what `check_brand.py` is for: the favicon is
the only copy of the mark that no component can generate, because a tab needs its icon
before any JavaScript runs.

## When a new course ships: link up, never across

**A course links up to the series index. It does not list its siblings.**

The obvious design is the other way round: each course carries the list of courses and
links across to the others. It is a trap. Shipping the fourth course then means editing and
redeploying four repositories, and any one of them forgotten shows a stale list forever.
That is the hand-maintained-list failure in its purest form, multiplied by the number of
courses, and the first course in this series shipped a smaller version of the same bug: a
front page claiming ten modules over a list of eight, because the list was written before
two of them existed.

So: `SERIES.homeUrl` is set once when a course is created and never touched again, and the
index is the one thing that knows what exists. Shipping a course edits exactly one
repository. Nothing anywhere else can go stale, because nothing anywhere else knows.

The index is a single static page, one card per course, each card in that course's own hue.
It wants no build step: with a handful of courses, a hand-maintained list in the one place
that is allowed to have one is correct.

`homeUrl` stays `null` until the index is actually published, which leaves the wordmark as
plain text rather than as a link to a 404.

## The social card

A course with no `og:image` is invisible in every place a link is pasted: Slack, Discord,
LinkedIn, X, iMessage and Bluesky all render it as a line of grey text, which is the
weakest possible showing for work whose whole argument is that it is worth looking at.
The card is the one piece of the identity that is seen by people who have not arrived yet.

Course one draws it as a rendered HTML page (`tools/og_card.html`, screenshotted to
`public/og-image.png` by `tools/make_og_image.sh`) rather than as a drawn image, for the
same reason the rest of the identity is tokens: the card is then made of the accent, the
course glyph and the type roles, and a rebrand reaches it. Copy both files, put the
course's own subject and canonical tagline in them without rewriting either, and run the
script.

**It is type and one rule, and it makes no argument.** Every claim on the card is one the
page already makes. The series index's card began as three colour-coded pills of benefits,
an accent-coloured phrase in the middle of the tagline, and the mark blown up with two
empty tiles fanned behind it to suggest more were coming, which is a landing page drawn by
someone with one course to show. A course this new has nothing to gain from asserting and
everything to lose: the only thing on a card that reads as credible is a fact, and where
there is no room for facts, quiet is the next best thing. Keep counts off it for the same
reason they are kept off everything else: a number inside a PNG is a hand-maintained
number that nothing can see go stale.

Two things a sibling course must get right, because both fail silently:

- **Every URL in the card's meta tags is absolute.** `base: "./"` makes the build
  subpath-safe for the browser, and does nothing for a crawler, which has no page to
  resolve `./og-image.png` against. The deployed origin is a literal in `index.html`,
  alongside the favicon and the theme colour, and for the same reason.
- **The image is 1200x630.** That is the slot both `summary_large_image` and Open Graph
  render. Anything else is letterboxed or cropped, usually through the title.

`check_brand.py` carries the check: the four URLs name one origin, the file they name
exists in `public/`, and it is the size the tags declare.

## Deliberately not here

- **Dark mode.** Every colour is already a token, so a dark palette is a later drop-in
  rather than a rewrite. It was left out because the interactives carry dozens of hand-tuned
  SVG palettes that would each need a second reading, and that is a project rather than a
  pass.
- **A type scale sweep.** The tokens name the scale the chrome uses. Rewriting every
  `font-size` in an existing course's stylesheet is churn with no visible return; new
  courses should use the tokens from the start.
