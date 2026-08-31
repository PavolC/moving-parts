import { useId } from "react";

/**
 * The series mark: three bands sampled across the shared accent family.
 * Decorative in every place it is used, because the series name beside it
 * carries the identity in text.
 *
 * Sized by --monogram-size, which the footer lowers, so one component serves
 * both placements.
 */
export function Monogram() {
	const clipId = useId();
	return (
		<svg className="brand-monogram" viewBox="0 0 32 32" aria-hidden="true" focusable="false">
			<clipPath id={clipId}>
				<rect width="32" height="32" rx="7" />
			</clipPath>
			<g clipPath={`url(#${clipId})`}>
				<rect width="11" height="32" x="0" fill="var(--hue-green)" />
				<rect width="11" height="32" x="11" fill="var(--hue-blue)" />
				<rect width="10" height="32" x="22" fill="var(--hue-plum)" />
			</g>
		</svg>
	);
}
