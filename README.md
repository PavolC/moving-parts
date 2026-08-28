# Moving Parts

The index for a series of interactive courses you finish by building the thing they
are about. Published to GitHub Pages from `site/`, which is one static file plus its
social card.

- **The page:** `site/index.html`
- **Live at:** https://pavolc.github.io/moving-parts/ once this repository is public
  and **Settings > Pages > Source** is set to **GitHub Actions**. Both need repository
  admin rights, so the workflow cannot turn itself on.
- **Something already depends on it.** The first course has set `SERIES.homeUrl` to
  that URL, so its masthead and its footer both link here on every page. Until Pages
  is switched on, those are links to a 404.

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
- The two `course-meta` items are what the reader writes and what the course assumes.
  These are counts, and counts are what go stale — check them against the course rather
  than against the last card.

## One width, and everything centred on it

Everything on this page is read as text, the course cards included, so there is one width
and everything sits on one axis. `--column` is derived rather than chosen: it is the
measure plus a card's own padding and borders, so the lines inside a card land on the same
axis, at the same width, as the paragraphs above and below it.

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
courses' shared brand layer (`src/brand/brand.css` in any course repo), because this page
has no bundler to import through. That is the one duplication the series accepts.

A duplicated palette with no guard is a palette that drifts, so `tools/brand_palette.py`
recomputes the family from its seed and `--check` fails if this file has moved. That
matters more than it sounds: the derivation is not quite the sentence people repeat.
Teal's chroma is lower than the other eight because the full chroma falls outside sRGB at
that hue, and the stop at 288 degrees is skipped because it comes out an olive, so moss
sits at 324 and the family is nine hues over ten stops. Regenerating an even nine from
the summary gives a different last colour.

The same tool checks the two greys the page sets text in against AA. It carried a third,
`#767a77`, for the card meta lines and the count: 4.28:1 on the page ground, below AA at
the 0.78rem those are set in, and nothing here would have said so.

Two strings are the kit's rather than this page's, and are worth keeping equal to it by
hand: the eyebrow is `SERIES.note` and the tagline opens with `SERIES.what`. A reader who
crosses over from a course should not meet a third phrasing of what the series is.

Light only, matching the courses. That is their standing decision rather than an omission
here: an index that inverted while its courses did not would be the odd one out.

## The social card

`site/og-image.png`, 1200x630, which is the slot both Open Graph and Twitter's
`summary_large_image` render; anything else is letterboxed or cropped. Without it every
share of this page — the page most likely to be the one that gets pasted — renders as a
line of grey text.

It is a rendered HTML page (`tools/og_card.html`, screenshotted by
`bash tools/make_og_image.sh`) rather than a drawn image, so the card stays made of the
same things as the page: the family, the mark and the type roles. Two things about it
fail silently and are checked rather than trusted:

- **Every URL in the card's meta tags is absolute.** A share is unfurled by a crawler
  that has no page to resolve `./og-image.png` against, so the deployed origin is a
  literal in `index.html`, spelled four times.
- **The image carries no counts.** A card that said "one course" would be a second
  hand-maintained list, in a PNG, where nothing can see it go stale.

The card renders in a headless Chromium, which has no Georgia, so DejaVu leads both font
stacks. It is the one surface whose type is resolved at author time.

## The checks

Both are stdlib-only Python and run in under a second.

```
python3 tools/brand_palette.py --check   # the nine hues, and the inks, against the arithmetic
python3 tools/check_brand.py             # the mark, the title and the social card agree
```

The mark exists in four drawings and every one of them is a literal: the favicon, the
masthead, and the card's tile and artwork. A favicon and a screenshot are copies no
component can generate, which is the whole reason for the second script.

## Where the kit is, and when it moves here

The shared conventions, the process, the casebook and the brand files currently live in
the first course, at
[PavolC/neural-nets/course-kit](https://github.com/PavolC/neural-nets/tree/main/course-kit).

They stay there until the second course starts, for two reasons. They are still being
refined **by** building that course, and every refinement so far was discovered by writing
a module rather than by thinking about the kit: moving them out now would turn each of
those into a pair of cross-repository changes. And `tools/check_brand.py` in that repo
enforces byte-equality between the course's live brand layer and the kit's copy of it,
which is a working guard that has nothing to replace it across repositories yet.

That course's `check_brand.py` and the one here share a name and not a job: there, the
mark is generated by two components and the literals are the favicon and the theme
colour; here there are no components, so every copy of the mark is a literal.

At course two the kit belongs above both courses, and this is where it comes.
