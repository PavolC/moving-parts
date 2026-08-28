#!/usr/bin/env python3
"""Check that every copy of the series mark and every spelling of the deployed
origin agrees with every other one.

The courses have tools/check_brand.py for the same job, and it is not the same
script: there, the mark is generated from brand.ts by two components and the
literals are the favicon and the theme colour. Here there are no components, so
the mark is a literal in all three of the places it appears, and the social
tags spell the origin out four times. Nothing in the page can notice when one
of them moves.

What is checked:

  * the three-band mark, in the favicon, in the masthead, and in both drawings
    of it on the social card, is the same three hues of the family in the same
    order, and the two 32-unit tiles are geometrically identical;
  * those three hues are the ones the section marks walk, in that order;
  * the social tags are absolute, name one origin, and agree in the pairs that
    have to agree;
  * the image they promise exists in site/ at the size they declare, which is
    the 1200x630 the summary_large_image slot renders;
  * the page title agrees in the three places it is spelled;
  * theme-color is a colour the page defines.

    python3 tools/check_brand.py

Exit status is 0 when everything agrees. Stdlib only, like brand_palette.py.
"""

import pathlib
import re
import struct
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "site" / "index.html"
CARD = ROOT / "tools" / "og_card.html"

# The mark is three bands of the family. Which three is a decision, not an
# accident: they are spread across the nine so the mark reads as the family
# rather than as a neighbourhood of it, and the section marks walk the same
# three in the same order so the page and its tab carry one mark.
MARK = ["hue-green", "hue-blue", "hue-plum"]


def tokens(text: str) -> dict[str, str]:
    """Every `--token: #hex;` in a stylesheet, keyed without the dashes."""
    return {
        m.group(1): m.group(2).lower()
        for m in re.finditer(r"--([a-z-]+):\s*(#[0-9a-fA-F]{6});", text)
    }


def banded_groups(svg: str) -> list[list[str]]:
    """The fills inside each clipped group, in document order.

    Every drawing of the mark bands a clipped rounded rect, so this finds the
    bands without caring how big the tile is or whether its fills are hex
    literals or var() references."""
    out = []
    for group in re.findall(r"<g clip-path=[^>]*>(.*?)</g>", svg, re.S):
        fills = re.findall(r'fill=["\'](#[0-9a-fA-F]{6}|var\(--[a-z-]+\))["\']', group)
        if fills:
            out.append([f.lower() for f in fills])
    return out


def resolve(fill: str, palette: dict[str, str]) -> str:
    """A fill as a hex value, whether it was written as one or as a var()."""
    var = re.fullmatch(r"var\(--([a-z-]+)\)", fill)
    return palette.get(var.group(1), fill) if var else fill


def geometry(svg: str) -> list[tuple[str, str, str]]:
    """Each band's x, width and the tile's rx, as written."""
    rx = re.search(r'rx=["\'](\d+)["\']', svg)
    bands = re.findall(r'<rect width=["\'](\d+)["\'] height=["\']32["\'] x=["\'](\d+)["\']', svg)
    return [(x, w, rx.group(1) if rx else "?") for w, x in bands]


def main() -> int:
    problems: list[str] = []
    page = PAGE.read_text()
    palette = tokens(page)
    want = [palette[t] for t in MARK if t in palette]
    if len(want) != len(MARK):
        missing = ", ".join(f"--{t}" for t in MARK if t not in palette)
        print(f"the page does not define {missing}", file=sys.stderr)
        return 1

    # --- the mark, in each of the places it is drawn --------------------------

    icon = re.search(r'rel="icon"\s*\n?\s*href="data:image/svg\+xml,([^"]+)"', page)
    if not icon:
        problems.append("site/index.html has no inline data-URI favicon")
        favicon = ""
    else:
        favicon = urllib.parse.unquote(icon.group(1))

    masthead = re.search(r'<svg class="brand-monogram".*?</svg>', page, re.S)
    if not masthead:
        problems.append("site/index.html does not draw the mark in its masthead")

    if not CARD.exists():
        problems.append("tools/og_card.html is missing, so the social card cannot be redrawn")
        card = ""
    else:
        card = CARD.read_text()

    # The card draws the mark twice, as the brand-row tile and as the artwork,
    # and both are clipped groups, so they come out of banded_groups directly.
    card_groups = banded_groups(card)

    for label, svg in {
        "the favicon": favicon,
        "the masthead mark": masthead.group(0) if masthead else "",
    }.items():
        if not svg:
            continue
        groups = banded_groups(svg)
        if not groups:
            problems.append(f"{label} draws no clipped band group")
            continue
        got = [resolve(f, palette) for f in groups[0]]
        if got != want:
            problems.append(
                f"{label} is banded {', '.join(got)}\n"
                f"    but the mark is {', '.join(want)} (--{', --'.join(MARK)})"
            )

    if card:
        if not card_groups:
            problems.append(
                "tools/og_card.html draws no banded group, so the card carries no mark"
            )
        # However many times the card draws the mark, every one of them has to
        # be the mark. The count is deliberately not asserted: how the card is
        # composed is a design decision that changes, and the version of this
        # check that pinned it to two had to be edited the first time the card
        # was redrawn.
        for i, bands in enumerate(card_groups):
            got = [resolve(f, palette) for f in bands]
            if got != want:
                problems.append(
                    f"the social card's drawing {i + 1} is banded {', '.join(got)}\n"
                    f"    but the mark is {', '.join(want)}"
                )

    # The two 32-unit tiles are the same drawing at two sizes, so they have to
    # agree exactly. The card's artwork is the same mark scaled up, and its
    # geometry is checked only by its hues above.
    if favicon and masthead:
        a, b = geometry(favicon), geometry(masthead.group(0))
        if a != b:
            problems.append(
                f"the favicon's bands are {a}\n    but the masthead's are {b} (x, width, rx)"
            )
        elif len(a) != 3:
            problems.append(f"the mark should be three bands, the tiles draw {len(a)}")

    # The section marks walk the same three hues in the same order.
    walked = re.findall(r"h2(?::nth-of-type\(\d\))?::before \{[^}]*?background: var\(--([a-z-]+)\)", page, re.S)
    if walked != MARK:
        problems.append(
            f"the section marks walk {', '.join('--' + w for w in walked)}\n"
            f"    but the mark is banded {', '.join('--' + m for m in MARK)}"
        )

    # --- the title, in the three places it is spelled ------------------------

    spellings = {
        "<title>": re.search(r"<title>([^<]+)</title>", page),
        "og:title": re.search(r'property="og:title"\s+content="([^"]+)"', page),
        "twitter:title": re.search(r'name="twitter:title"\s+content="([^"]+)"', page),
    }
    missing = [k for k, v in spellings.items() if not v]
    if missing:
        problems.append(f"site/index.html is missing {', '.join(missing)}")
    else:
        got = {k: v.group(1) for k, v in spellings.items()}
        if len(set(got.values())) != 1:
            spelled = ", ".join(f"{k} -> {v!r}" for k, v in sorted(got.items()))
            problems.append(f"the title is spelled more than one way: {spelled}")

    # --- theme-color ---------------------------------------------------------

    theme = re.search(r'name="theme-color"\s+content="(#[0-9a-fA-F]{6})"', page)
    if not theme:
        problems.append("site/index.html has no theme-color meta tag")
    elif theme.group(1).lower() not in palette.values():
        problems.append(
            f"theme-color is {theme.group(1)}, which is not a colour the page defines. "
            f"A course sets it to its accent; the series has no one accent, so this one "
            f"is --ink."
        )

    # --- the social card -----------------------------------------------------

    # Four spellings of one origin, which go stale independently, so the check
    # is that they agree with each other rather than with a copy kept here.
    social = {
        "og:url": re.search(r'property="og:url"\s+content="([^"]+)"', page),
        "og:image": re.search(r'property="og:image"\s*\n?\s*content="([^"]+)"', page),
        "twitter:image": re.search(r'name="twitter:image"\s*\n?\s*content="([^"]+)"', page),
        "canonical": re.search(r'rel="canonical"\s+href="([^"]+)"', page),
    }
    missing = [k for k, v in social.items() if not v]
    if missing:
        problems.append(f"site/index.html is missing {', '.join(missing)}")
    else:
        got = {k: v.group(1) for k, v in social.items()}
        for key, value in got.items():
            if not value.startswith("https://"):
                problems.append(
                    f"{key} is {value!r}, which a crawler cannot resolve: it must be absolute"
                )
        # Four segments, not three: every project site on GitHub Pages shares
        # one host, so comparing hosts alone would pass a tag that had drifted
        # to a sibling project's path.
        origins = {k: "/".join(v.split("/")[:4]) for k, v in got.items()}
        if len(set(origins.values())) != 1:
            spelled = ", ".join(f"{k} -> {v}" for k, v in sorted(origins.items()))
            problems.append(f"the social tags point at more than one origin: {spelled}")
        if got["og:url"] != got["canonical"]:
            problems.append(f"og:url is {got['og:url']!r} but canonical is {got['canonical']!r}")
        if got["og:image"] != got["twitter:image"]:
            problems.append(
                f"og:image is {got['og:image']!r} but twitter:image is {got['twitter:image']!r}"
            )

        # The image has to exist under the name the tag promises, in site/,
        # which is the only directory the deploy workflow uploads. A crawler
        # that fetches a 404 renders the share as bare text, and the page
        # itself gives no sign of it.
        image = ROOT / "site" / got["og:image"].rsplit("/", 1)[-1]
        if not image.exists():
            problems.append(f"og:image names {image.name}, which is not in site/")
        else:
            data = image.read_bytes()
            if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
                problems.append(f"site/{image.name} is not a PNG")
            else:
                width, height = struct.unpack(">II", data[16:24])
                declared = (
                    re.search(r'property="og:image:width"\s+content="(\d+)"', page),
                    re.search(r'property="og:image:height"\s+content="(\d+)"', page),
                )
                if not all(declared):
                    problems.append("site/index.html declares og:image but not its width and height")
                elif (width, height) != (int(declared[0].group(1)), int(declared[1].group(1))):
                    problems.append(
                        f"site/{image.name} is {width}x{height}, but the tags declare "
                        f"{declared[0].group(1)}x{declared[1].group(1)}"
                    )
                if (width, height) != (1200, 630):
                    problems.append(
                        f"site/{image.name} is {width}x{height}; the summary_large_image "
                        f"slot wants 1200x630"
                    )
        if not re.search(r'property="og:image:alt"\s*\n?\s*content="[^"]+"', page):
            problems.append("og:image has no og:image:alt")

    # A token that is declared and never used is a decoration, and on a page
    # whose palette is a copy it is also the first sign that the copy and its
    # source have parted company. Two greys and a radius sat here unused.
    declared = set(re.findall(r"--([a-z-]+):\s*[^;]+;", page))
    referenced = set(re.findall(r"var\(--([a-z-]+)", page))
    # --hue is set per card, on the element, rather than declared at :root.
    for token in sorted(declared - referenced - {"hue"}):
        problems.append(f"--{token} is declared in site/index.html and never used")
    for token in sorted(referenced - declared - {"hue"}):
        problems.append(f"--{token} is used in site/index.html and never declared")

    if problems:
        print(f"{len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1

    print(
        f"Brand agrees: the mark is {', '.join('--' + m for m in MARK)} in "
        f"{2 + len(card_groups)} drawings, the title in 3 places, and the social "
        f"tags name one origin and an image that exists at the size they declare."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
