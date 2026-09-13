#!/usr/bin/env python3
"""Fail if the protected reviewer-material navigation disappears or breaks.

The root README intentionally duplicates the canonical reviewer-package index so
an external reviewer can reach the current papers without knowing repository
internals.  This guard makes accidental deletion during full-file status rewrites
visible in CI.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "releases" / "REVIEW_READY_INDEX.md"
START = "<!-- REVIEW-MATERIALS:START -->"
END = "<!-- REVIEW-MATERIALS:END -->"

REQUIRED_CURRENT = [
    "START_HERE_FOR_REVIEWERS.md",
    "releases/REVIEW_READY_INDEX.md",
    "releases/n25-reviewer-v2/README.md",
    "releases/n27-reviewer-v2/README.md",
    "releases/n28-reviewer-v2/README.md",
    "releases/n29-reviewer-v4/README.md",
    "releases/n30-reviewer-v3/README.md",
    "releases/n31-reviewer-v1/README.md",
    "releases/n32-reviewer-v1/README.md",
    "releases/n33-reviewer-v1/README.md",
    "releases/n34-reviewer-v2/README.md",
    "releases/n35-reviewer-v1/README.md",
    "releases/general-7-12-reviewer-v1/README.md",
    "releases/general-stepback-v1/README.md",
    "releases/general-joint-clipping-reviewer-v1/README.md",
    "releases/general-heavy-load-reviewer-v1/README.md",
    "releases/general-joint-routing-reviewer-v1/README.md",
    "releases/general-routing-tail-reviewer-v1/README.md",
    "releases/general-compatible-routing-reviewer-v1/README.md",
    "releases/general-compatible-catalogue-reviewer-v1/README.md",
    "releases/general-closed-compatible-reviewer-v1/README.md",
    "releases/general-arc-realisation-reviewer-v1/README.md",
]


def fail(msg: str) -> None:
    print(f"README_REVIEW_GUARD_FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    text = README.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        fail("protected review-material markers must each occur exactly once")
    a = text.index(START) + len(START)
    b = text.index(END, a)
    section = text[a:b]
    if "## Papers and review materials" not in section:
        fail("protected section heading is missing")

    missing = [x for x in REQUIRED_CURRENT if x not in section]
    if missing:
        fail("current reviewer links missing from protected section: " + ", ".join(missing))

    # Every repository-relative Markdown link in the protected section must resolve.
    broken = []
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", section):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target and not (ROOT / target).exists():
            broken.append(target)
    if broken:
        fail("broken repository-relative links in protected section: " + ", ".join(sorted(set(broken))))

    # The canonical index must continue to advertise the fixed-order current editions.
    idx = INDEX.read_text(encoding="utf-8")
    index_tokens = [
        "n25-reviewer-v2", "n27-reviewer-v2", "n28-reviewer-v2",
        "n29-reviewer-v4", "n30-reviewer-v3", "n31-reviewer-v1",
        "n32-reviewer-v1", "n33-reviewer-v1", "n34-reviewer-v2",
        "n35-reviewer-v1", "general-7-12-reviewer-v1",
    ]
    absent = [x for x in index_tokens if x not in idx]
    if absent:
        fail("canonical review index lost current package identifiers: " + ", ".join(absent))

    print("README_REVIEW_GUARD_OK")
    print(f"protected_section_links={len(re.findall(r'\[[^\]]*\]\(([^)]+)\)', section))}")


if __name__ == "__main__":
    main()
