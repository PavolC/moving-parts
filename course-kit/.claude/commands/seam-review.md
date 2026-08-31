---
description: Reconcile a chapter against its neighbours. Vocabulary, numbers, cross-references.
---

Chapter: $ARGUMENTS

Read the chapter, the one before it, and the one after it. Report contradictions, not style
opinions, and cite file and line for each.

Check:

- **Vocabulary.** Any word used with two meanings across the three chapters. Any term this
  chapter coins that an earlier one already names differently. Any word used before the
  section that defines it.
- **Numbers.** Every number this chapter quotes from another one, verified against the
  source chapter. Every measured number, verified against its bench. Any number quoted from
  one engine for a measurement the reader makes with another.
- **Backward claims.** Every "chapter N taught X", checked against chapter N.
- **Ownership.** Anything that files a thing with the wrong owner per the anatomy in
  `CLAUDE.md`, including counts, tables and figure captions.
- **Notation.** Every symbol and coined term introduced here, present in the notation
  reference with the right chapter.
- **Callbacks.** Density against the band in `CLAUDE.md`, and whether each callback removes
  work or carries the argument. Cut the ones that only say "remember this".
- **Figures.** Whether each joins an established geometry family, and what it does at the
  narrowest supported viewport.

Then fix what you found, in one commit per kind of problem.
