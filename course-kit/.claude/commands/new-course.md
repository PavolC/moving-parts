---
description: Start a new course in this series from the kit. Interviews me, then writes the design doc and day-one scaffold.
---

Read `METHOD.md`, `CLAUDE.md` and `DESIGN-DOC-TEMPLATE.md` first. Then start a new
course on: $ARGUMENTS

Do it in this order and stop for my answers where it says to stop.

**1. Interview me.** Ask only what you cannot decide yourself, one round, and give your
recommendation with each question. You need:

- what I want to be able to DO at the end, not what I want to know;
- **the floor**: what I do not know, as a list. Push me here. "Intermediate programmer"
  is not an answer; "I have never seen a grammar or a stack machine" is;
- the canonical source text or paper series, if there is one;
- the one thing that has to run in a browser tab for this to work at all;
- roughly how many chapters, and what the summit is (the chapter where I build the real
  thing).

Then **stop** and let me answer.

**2. Test the floor before believing it.** Write two paragraphs of real teaching prose at
the floor I gave you, on the topic's first idea, and show me. If they land, the floor is
right. If they are over my head, the floor is wrong, and every chapter written against it
would have been too. Do not proceed until we agree on it.

**3. Write the design doc** from the template. Fill every section. Propose the chapter list
with what I write in each one, including the two closing chapters the template requires.
Show it to me before writing code.

**4. Day one, in one commit each:**

- `CLAUDE.md` from the kit, with every `FILL:` closed. Leave nothing marked FILL.
- the feasibility spike: the riskiest runtime constraint proved end to end with a reference
  implementation, with its measurement recorded and the runtime pinned to it;
- the exercise pipeline on one exercise as the guinea pig;
- the exercise checker (solutions pass, untouched skeletons fail for their own reason);
- the bench harness, so the first measured number in prose is already reproducible;
- the notation reference on the front page, empty;
- `src/brand/` copied from `brand/`, edited per `BRAND.md`, with an
  unused hue and a glyph the course itself draws;
- the deploy workflow, green.

Also decide now, and record in `CLAUDE.md`'s Decisions section: the component vocabulary,
the figure geometry families and their phone behaviour, and what a first-time visitor sees.

**5. Then one chapter only.** Write it, and hand it to me to read. Do not write the rest.
