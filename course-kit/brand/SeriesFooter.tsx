import type { ReactNode } from "react";
import { SERIES } from "./brand";
import { Monogram } from "./Monogram";

/**
 * The bottom of every course in the series: what the series is, a link up to
 * its index, and then the course's own legal text.
 *
 * Up, not across. A course does not list its siblings, because that list would
 * have to be maintained in every course's copy of brand.ts and redeployed
 * everywhere on each new course. The index is the one thing that knows what
 * exists; see SERIES.homeUrl.
 *
 * The legal text arrives as children rather than from brand.ts, because every
 * course carries different obligations and a shared component that tried to
 * hold them would end up either wrong or empty. This one is only responsible
 * for putting them below a rule, where a reader looking for the licence knows
 * to find them.
 */
export function SeriesFooter({ children }: { children: ReactNode }) {
	return (
		<footer className="series-footer">
			<div className="series-band">
				<span className="series-lockup">
					<Monogram />
					<span>
						{SERIES.homeUrl ? <a href={SERIES.homeUrl}>{SERIES.name}</a> : <b>{SERIES.name}</b>}
						{"."}
					</span>
				</span>
				<span className="series-what">{SERIES.what}</span>
				{SERIES.homeUrl && (
					<span className="series-siblings">
						<a href={SERIES.homeUrl}>Every course in the series</a>
					</span>
				)}
			</div>
			<div className="series-legal">{children}</div>
		</footer>
	);
}
