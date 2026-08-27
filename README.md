# Moving Parts

The index for a series of interactive courses you finish by building the thing they
are about. Published to GitHub Pages from `site/`, which is one static file.

- **The page:** `site/index.html`
- **Live at:** https://pavolc.github.io/moving-parts/ once this repository is public
  and **Settings > Pages > Source** is set to **GitHub Actions**. Both need repository
  admin rights, so the workflow cannot turn itself on.

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
- The glyph is the same single path that course's `brand.ts` draws, so the card and the
  course's own masthead carry the same mark.
- The two `course-meta` items are what the reader writes and what the course assumes.

## The tokens are copied, not imported

The palette, the type roles and the measure in `site/index.html` are duplicated from the
courses' shared brand layer (`src/brand/brand.css` in any course repo), because this page
has no bundler to import through. That is the one duplication the series accepts, and the
comment at the top of the file carries the derivation so the numbers can be checked
against their source rather than trusted.

Light only, matching the courses. That is their standing decision rather than an omission
here: an index that inverted while its courses did not would be the odd one out.

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

At course two they belong above both courses, and this is where they come.
