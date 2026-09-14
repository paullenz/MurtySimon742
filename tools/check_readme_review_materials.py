#!/usr/bin/env python3
"""Fail if protected reviewer navigation or red-team history disappears or breaks.

The root README intentionally duplicates the canonical reviewer-package index and
retains a concise but substantive adversarial-audit history. These are durable
review surfaces, not disposable status prose. This guard makes accidental
deletion or over-compression during full-file status rewrites visible in CI.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INDEX = ROOT / "releases" / "REVIEW_READY_INDEX.md"
REVIEW_START = "<!-- REVIEW-MATERIALS:START -->"
REVIEW_END = "<!-- REVIEW-MATERIALS:END -->"
REDTEAM_START = "<!-- REDTEAM-HISTORY:START -->"
REDTEAM_END = "<!-- REDTEAM-HISTORY:END -->"

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

# These tokens protect not just navigation but the historical substance: real
# defects, corrections, hostile-review consequences and the routes hardened by
# those audits. Removing them requires an intentional guard update.
REQUIRED_REDTEAM = [
    "## Hostile / red-team audit history and resulting proof hardening",
    "real normalization bug",
    "v1 cumulative-threshold certificates are therefore **invalid as proof evidence**",
    "blind external red-team follow-up",
    "non-blocking sign/order typo",
    "Fan dependency removed",
    "hostile coverage/integrity audit",
    "project/reviews/n25/2026-09-08-reaudit-v1/README.md",
    "project/reviews/n27/2026-09-08-redteam-v1/REPORT.md",
    "project/reviews/n28/2026-09-07-redteam-v1/REPORT.md",
    "project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md",
    "project/reviews/n29/2026-09-11-blind-external-ai-redteam-v1/FOLLOWUP.md",
    "project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md",
    "project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md",
    "project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_AUDIT.md",
    "project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md",
]


def fail(msg: str) -> None:
    print(f"README_REVIEW_GUARD_FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def protected_section(text: str, start: str, end: str, name: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        fail(f"protected {name} markers must each occur exactly once")
    a = text.index(start) + len(start)
    b = text.index(end, a)
    return text[a:b]


def broken_relative_links(section: str) -> list[str]:
    broken = []
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", section):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if target and not (ROOT / target).exists():
            broken.append(target)
    return sorted(set(broken))


def main() -> None:
    text = README.read_text(encoding="utf-8")

    review = protected_section(text, REVIEW_START, REVIEW_END, "review-material")
    if "## Papers and review materials" not in review:
        fail("protected review-material heading is missing")
    missing = [x for x in REQUIRED_CURRENT if x not in review]
    if missing:
        fail("current reviewer links missing from protected section: " + ", ".join(missing))
    broken = broken_relative_links(review)
    if broken:
        fail("broken repository-relative links in review section: " + ", ".join(broken))

    redteam = protected_section(text, REDTEAM_START, REDTEAM_END, "red-team-history")
    missing_redteam = [x for x in REQUIRED_REDTEAM if x not in redteam]
    if missing_redteam:
        fail("protected red-team history lost required substance: " + ", ".join(missing_redteam))
    broken_redteam = broken_relative_links(redteam)
    if broken_redteam:
        fail("broken repository-relative links in red-team section: " + ", ".join(broken_redteam))

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
    print(f"protected_review_links={len(re.findall(r'\[[^\]]*\]\(([^)]+)\)', review))}")
    print(f"protected_redteam_links={len(re.findall(r'\[[^\]]*\]\(([^)]+)\)', redteam))}")


if __name__ == "__main__":
    main()
