# Moving Parts

The index for Moving Parts, a series of build-it-yourself courses for understanding
complicated technical systems by rebuilding their essential machinery — and, since
course two, the home of the course kit the courses are built from. The site is published
to GitHub Pages from `site/`, which is one static file plus its social card.

- **The page:** `site/index.html`
- **The kit:** `course-kit/` — the method, the casebook, the commands and the brand
  layer. Its licence travels inside it, at `course-kit/LICENSE`.
- **Licence:** MIT for everything outside the kit (see `LICENSE`); the kit is governed
  by its own file. The series name and the marks are granted by neither.
- **Live at:** https://pavolc.github.io/moving-parts/, published by
  `.github/workflows/deploy.yml` on every push to `main`.
- **The URL is load-bearing.** The first course has `SERIES.homeUrl` set to it, so its
  masthead and its footer link here on every page. That line is set once when a course
  is created and never touched again, which is the whole design — and it means this URL
  cannot move without editing every course in the series.
- **The workflow cannot turn Pages on**, only publish through it. Pages needs the
  repository public, or a plan that allows Pages on a private one, and **Settings >
  Pages > Source** set to **GitHub Actions**; both need repository admin rights. The
  first deploy here failed for exactly that reason, so it is worth knowing if this
  repository is ever moved or recreated.

## Brand and method

- **Short descriptor:** Build-it-yourself courses.
- **Positioning:** Understand complicated technical systems by rebuilding their
  essential machinery.
- **Core idea:** Moving Parts makes complicated technical things understandable by
  taking them apart and rebuilding them.
- **Method:** read a little → manipulate the mechanism → build part of it → assemble
  the real thing.

Future courses can explore different technical systems and ideas. They do not all have
to require code, but each one must let the learner build, manipulate, simulate or inspect
the mechanism itself. The tone stays understated: explain what the learner does and let
the work make the case.

### Moving Parts fit test

1. There is a real mechanism to expose.
2. The learner can build, simulate, manipulate, or inspect meaningful parts of it.
3. The course removes abstraction progressively.
4. What is built is recognizably related to the real thing, not just an analogy.
5. The learner finishes with a concrete mental model of how the thing works.

## Why the list of courses lives here and nowhere else

A course links **up** to this index and never across to a sibling. The obvious design is
the other way round, with each course carrying the list and linking to the others, and it
is a trap: shipping the fourth course would mean editing and redeploying four
repositories, and any one of them forgotten shows a stale list forever.

So shipping a course is two edits. Add its card to `site/index.html` here, and set
`SERIES.homeUrl` in that course's `src/brand/brand.ts` once, at creation. Nothing else
anywhere knows what the series contains, so nothing else can go stale.

## Adding a course

One `<li>` in `site/index.html`:

- `--hue` picks the course's colour from the nine-hue family. Use one no other course has.
  It sets the card's left edge, its hover border and its wash in one line: the wash is
  mixed from `--hue` on the element itself, so there is no second colour to choose.
- The glyph is the same single path that course's `brand.ts` draws, so the card and the
  course's own masthead carry the same mark.
- The two `course-meta` items are what the learner builds or manipulates and what the
  course assumes. These are counts when a course has useful counts to show, and counts
  are what go stale — check them against the course rather than against the last card,
  and against its checks rather than its prose. For Neural Networks that is
  `grep -h "^def test_" src/exercises/*/tests.py | wc -l` in the course repo, the same
  total `python3 tools/check_exercises.py` prints there.

A course can be teased before it ships. The teaser is the same `<li>` with everything a
link would promise left out: no `href` — the card is a `div` with the `course-soon`
class, so it takes no underline and answers no hover — no glyph path, because a course
draws its mark at creation and the tile stays empty until then, and no counts or CTA,
just a "Coming soon" label in the head row. The one claim a teaser makes is its
`--hue`: teasing is what reserves that segment of the family. Shipping the course means
filling in that same `<li>`, not adding a second one beside it.

## One width, and everything centred on it

Everything on this page is read as text, the course cards included, so there is one width
and everything sits on one axis. `--column` is derived rather than chosen: it is the
measure plus a card's own padding and a hairline per side. A card's left edge is 2px
wider than the hairline opposite it and its left padding is short by the same 2px, so
border-plus-padding comes out even and the lines inside a card land on the same axis, at
the same width, as the paragraphs above and below it.

The measure used to be left-aligned inside a wider column, which is the arrangement the
first course tried and reverted: every block wider than the prose hangs off to its right
and the page reads as lopsided. The courses do keep a second, wider width, because they
have figures, an editor and tables to put in it. This page has none of those, so a wider
column here would be slack rather than a second width.

Each measured element carries its horizontal `auto` inside its own `margin` shorthand.
That is not style: a shorthand written later in the file resets the auto that does the
centring, so keeping the two in one declaration is what stops it being undone.

## The tokens are copied, not imported

The palette, the type roles and the measure in `site/index.html` are duplicated from the
series brand layer — `course-kit/brand/brand.css`, in this repository since the kit was
promoted — because this page has no bundler to import through. That is the one
duplication the series accepts.

A duplicated palette with no guard is a palette that drifts, so `tools/brand_palette.py`
recomputes the family from its seed and `--check` fails if either file has moved. That
matters more than it sounds: the derivation is not quite the sentence people repeat.
Teal's chroma is lower than the other eight because the full chroma falls outside sRGB at
that hue, and the stop at 288 degrees is skipped because it comes out an olive, so moss
sits at 324 and the family is nine hues over ten stops. Regenerating an even nine from
the summary gives a different last colour.

The same tool checks the two greys the page sets text in against AA. It carried a third,
`#767a77`, for the card meta lines and the count: 4.28:1 on the page ground, below AA at
the 0.78rem those are set in, and nothing here would have said so.

The eyebrow is `SERIES.note`. The positioning statement, core idea and four-step method
above are the canonical description of the series, including across courses about
different technical systems and ideas. A reader who crosses over from a course should
not meet a competing description of what the series is.

Light only, matching the courses. That is their standing decision rather than an omission
here: an index that inverted while its courses did not would be the odd one out.

## The social card

`site/og-image.png`, 1200x630, which is the slot both Open Graph and Twitter's
`summary_large_image` render; anything else is letterboxed or cropped. Without it every
share of this page — the page most likely to be the one that gets pasted — renders as a
line of grey text.

It is a rendered HTML page (`tools/og_card.html`, screenshotted during deployment by
`bash tools/make_og_image.sh`) rather than a drawn image, so the card stays made of the
same things as the page: the family, the mark and the type roles.

**It is type and one rule, and it makes no argument.** Every claim on it is one the page
already makes. The first version had three colour-coded
pills of benefits, an accent-coloured phrase in the middle of the tagline, and the mark
blown up with two empty tiles fanned behind it to suggest more were coming — which is a
landing page, drawn by someone with one course to show. A series this small has nothing
to gain from asserting and everything to lose: the only thing on a card that reads as
credible is a fact, and if there is no room for facts then quiet is the next best thing.

Two things about it fail silently and are checked rather than trusted:

- **Every URL in the card's meta tags is absolute.** A share is unfurled by a crawler
  that has no page to resolve `./og-image.png` against, so the deployed origin is a
  literal in `index.html`, spelled four times.
- **The image carries no counts.** A card that said "one course" would be a second
  hand-maintained list, in a PNG, where nothing can see it go stale.

The card renders in a headless Chromium, which has no Georgia, so DejaVu leads both font
stacks. It is the one surface whose type is resolved when the deployment renders it.

## The checks

Both are stdlib-only Python and run in under a second.

```
python3 tools/brand_palette.py --check   # the hues in the kit and the page, and the inks, against the arithmetic
python3 tools/check_brand.py             # the mark, the title and the social card agree
```

Every copy of the mark is a literal: the favicon, the masthead, and the card's tile. A
favicon and a screenshot are copies no component can generate, which is the whole reason
for the second script, and it finds the drawings rather than being told how many to
expect.

## The course kit

The shared conventions, the process, the casebook and the brand files live here, in
[`course-kit/`](course-kit/), extracted from the first course and promoted out of it now
that the second is underway — which was the standing rule: at course two the kit belongs
above both courses.

What the move changed, and what it did not:

- The kit came over byte-for-byte except for its own pointers: the few links and phrases
  that located it inside the course now name the course explicitly. Its licence moved
  with it — `course-kit/LICENSE`: the documents CC BY 4.0, `brand/` MIT, the series name
  and the mark granted by neither.
- The course's `tools/check_brand.py` enforced byte-equality between its live brand layer
  and its kit copy, a guard that cannot reach across repositories. The replacement here
  works at the token level: `tools/brand_palette.py --check` reads both
  `course-kit/brand/brand.css` and `site/index.html` against the same arithmetic, so the
  canonical palette and the page's duplicate cannot drift apart inside this repository.
  The kit's components have no duplicate here to drift against; a course guards its own
  copies with its own tools.
- The first course keeps its live `src/brand/` — a course always owns its copy — and,
  until a cleanup lands in that repository, the kit copy it grew up with. The canonical
  kit is this one, and it is the one the index links to.

That course's `check_brand.py` and the one here still share a name and not a job: there,
the mark is generated by two components and the literals are the favicon and the theme
colour; here there are no components, so every copy of the mark is a literal.
