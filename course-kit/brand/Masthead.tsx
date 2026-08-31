import type { ReactNode } from "react";
import { COURSE, SERIES } from "./brand";
import { Monogram } from "./Monogram";

/**
 * The top of every course in the series: the accent rule (drawn by brand.css
 * on body), the series row, the course title, its tagline, and whatever
 * navigation the course passes in.
 *
 * The wordmark sits above the title rather than in front of it, because the
 * series name is an imprint and not a prefix: the courses are "Neural Networks"
 * and "Ciphers", published under one name, so a sibling reads the same two lines
 * with only the heading changed. The heading is the subject alone, and needs no
 * hidden prefix: the wordmark immediately above it is text, so a screen reader
 * reaches the series name first and then the course.
 *
 * `compact` marks an inner page, and on a phone it drops the tagline and sizes
 * the title down. The tagline is the course's pitch, which is what the front
 * door is for; on page seven of a course the reader has bought it already, and
 * on a 390px screen it costs four lines, a fifth of the first screenful. The
 * flag changes nothing above 560px, where the masthead costs nothing.
 */
export function Masthead({ nav, compact }: { nav?: ReactNode; compact?: boolean }) {
  const wordmark = (
    <>
      <Monogram />
      <span className="brand-wordmark">{SERIES.name}</span>
    </>
  );
  return (
    <header className={compact ? "masthead masthead-compact" : "masthead"}>
      <p className="brand-row">
        {SERIES.homeUrl ? (
          <a className="brand-mark" href={SERIES.homeUrl}>
            {wordmark}
          </a>
        ) : (
          <span className="brand-mark">{wordmark}</span>
        )}
        <span className="brand-series-note">{SERIES.note}</span>
      </p>
      <h1 className="masthead-title">{COURSE.subject}</h1>
      <p className="masthead-tagline">{COURSE.tagline}</p>
      {nav}
    </header>
  );
}
