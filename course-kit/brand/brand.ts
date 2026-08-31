/**
 * The series identity, and this course's slot in it.
 *
 * This is the one file in the brand folder a course edits. Nothing else here
 * knows the subject, so a course that changes its name, its hue and its glyph
 * below is fully rebranded. The other change is one line in brand.css, marked
 * COURSE ACCENT.
 *
 * Everything marked FILL has to be closed before the first chapter ships.
 */

/**
 * A course's mark, used where the course itself needs identifying: the
 * favicon, the social card, and the course's card on the series index. The
 * masthead and footer use the separate Moving Parts mark beside the series
 * name. tools/check_brand.py asserts that this repository's two course-mark
 * copies still carry this exact path.
 *
 * Pick something the course itself draws. The first course used the sigmoid
 * curve, which is the first figure in its chapter 1 and the shape every unit in
 * the course is built from. A glyph that means nothing is worse than a letter.
 */
export interface Glyph {
	viewBox: string;
	/** A single stroked path. No fills, so the tile works at 16px. */
	d: string;
	strokeWidth: number;
}

export const SERIES = {
	/** An imprint rather than a prefix: the courses are "Neural Networks" and
	 *  "Ciphers", published under this name, not "Moving Parts Neural Networks".
	 *  That is why the masthead puts the wordmark above the title instead of in
	 *  front of it, and why COURSE_TITLE below reads subject first. */
	name: "Moving Parts",
	/** Uppercased into the masthead beside the wordmark. Keep it to four words. */
	note: "build-it-yourself courses",
	/** One sentence, in the footer, under the series name the way the index
	 *  sets it under the wordmark. It is the series' positioning statement, so
	 *  it is series-level like the note above and the URL below: a sibling
	 *  course copies it unchanged rather than rewording it, because a reader
	 *  who crosses over from one course to another should not meet two
	 *  descriptions of what the series is. */
	what: "Understand complicated technical systems by rebuilding their essential machinery.",
	/** The series index, which is the only place that knows what else exists.
	 *
	 *  A course links UP to it and never across to a sibling. The obvious design
	 *  was the other way round, with each course carrying the list and linking
	 *  to its siblings, and it is a trap: shipping the fourth course would mean
	 *  editing and redeploying four repositories, and any one of them forgotten
	 *  shows a stale list forever. This is the same hand-maintained-list failure
	 *  that once let the front page claim ten modules over a list of eight,
	 *  multiplied by the number of courses. Linking up means shipping a course
	 *  edits exactly one repository, and nothing anywhere else can go stale.
	 *
	 *  Set once when a course is created, then never touched. Series-level
	 *  rather than course-level: every course in the series points at the same
	 *  index, so a sibling copies this line unchanged and never edits it again.
	 *  Null leaves the wordmark as plain text rather than a link to a 404, which
	 *  is where it should sit until the index is actually published. */
	homeUrl: "https://pavolc.github.io/moving-parts/" as string | null,
};

export const COURSE = {
	/** FILL: the slug, not the display name. It is the stem of the progress
	 *  file's name and the series index's key for this course, so pick one that
	 *  survives the subject being reworded. */
	id: "FILL",
	/** FILL: the subject. It is the page's heading and the first word of the
	 *  document title, so it should be the words a reader would search for. */
	subject: "FILL",
	/** FILL: one sentence, in the masthead under the title. What the reader does
	 *  here, not what the topic is: the heading already carries the topic. */
	tagline: "FILL",
	/** FILL: see the Glyph docstring above. The default below is the first
	 *  course's sigmoid: flat, steepest in the middle, flat. */
	glyph: {
		viewBox: "0 0 32 32",
		d: "M5 24C12 24 15 19 16 16C17 13 20 8 27 8",
		strokeWidth: 3,
	} as Glyph,
};

/** The document title. Subject first, because that is the word a reader needs
 *  when eight tabs are open, then the series as the imprint.
 *
 *  This is the canonical spelling, and index.html has to repeat it as a
 *  literal, because a tab needs its title before any JavaScript runs.
 *  tools/check_brand.py asserts that the two agree, which is what stops a
 *  rename from reaching the masthead and leaving the tab behind. */
export const COURSE_TITLE = `${COURSE.subject} · ${SERIES.name}`;
