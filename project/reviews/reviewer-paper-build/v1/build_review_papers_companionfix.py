#!/usr/bin/env python3
"""Reviewer-paper entry point with corrected companion source-list layout.

Imports the canonical builder and replaces only companion_front so the source
list begins after a Markdown blank line. The mathematical and package-building
logic remains in build_review_papers.py.
"""
import build_review_papers as base


def companion_front(spec):
    srcs = "\n".join(f"- `{p}`" for p in spec.companion_sources)
    return base.yaml_front(
        spec.title + " - verification companion",
        "Reviewer edition 1 - replay, audit and provenance",
    ) + f'''\\begin{{abstract}}\nThis companion collects the principal replay instructions, audits, graph-to-model bridges and provenance documents supporting the reviewer manuscript. It is not a substitute for reading the mathematical proof. Exact arithmetic or certificate verification is identified as such in the underlying sources; same-assistant reconstructions are not represented as external independent review.\n\\end{{abstract}}\n\n## Reviewer orientation\n\n**Claim under review.** `{spec.claim}`.\n\n**Status.** {spec.status}.\n\n**Sources assembled verbatim below:**\n\n{srcs}\n\nA failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.\n\n---\n\n'''


base.companion_front = companion_front

if __name__ == "__main__":
    base.main()
