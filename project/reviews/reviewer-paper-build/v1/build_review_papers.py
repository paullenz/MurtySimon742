#!/usr/bin/env python3
"""Build canonical reviewer manuscripts and verification companions.

The script does not alter canonical proof/audit sources. It creates editorial
reviewer editions, renders them with the repository's audited Pandoc/XeLaTeX
settings, and rebuilds the review-ready index.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
TODAY = "9 September 2026"
FILTER = "project/reviews/reviewer-paper-build/v1/fix_aligned_tags.lua"


@dataclass(frozen=True)
class Spec:
    key: str
    release_dir: str
    manuscript_name: str
    companion_name: str
    title: str
    subtitle: str
    abstract: str
    proof: str
    companion_sources: tuple[str, ...]
    status: str
    claim: str


SPECS = (
    Spec(
        key="n27",
        release_dir="releases/n27-reviewer-v1",
        manuscript_name="N27_Reviewer_Manuscript_v1",
        companion_name="N27_Verification_Companion_v1",
        title="A candidate proof of the Murty-Simon conjecture at order 27",
        subtitle="Reviewer edition 1 - independent mathematical review pending",
        abstract=("We present the current candidate argument that every simple diameter-2 edge-critical graph on 27 vertices has at most 182 edges, with equality exactly for K(13,14). The proof combines published reductions, witness counting, residual/quasi-edge structure and complete finite arithmetic. The computational terminal cases have been replayed internally, but the graph-theoretic reductions and the whole argument remain open to independent mathematical and computational review."),
        proof="project/reviews/n27/2026-09-07-candidate-v1/PROOF.md",
        companion_sources=(
            "releases/n27-candidate-v1/README.md",
            "project/reviews/n27/2026-09-08-redteam-v1/REPORT.md",
        ),
        status="complete candidate; independent mathematical and computational review OPEN",
        claim="e(G) <= 182, with equality exactly K(13,14)",
    ),
    Spec(
        key="n29",
        release_dir="releases/n29-reviewer-v1",
        manuscript_name="N29_Reviewer_Manuscript_v1",
        companion_name="N29_Verification_Companion_v1",
        title="A candidate proof of the Murty-Simon conjecture at order 29",
        subtitle="Reviewer edition 1 - independent mathematical review pending",
        abstract=("We present the current candidate argument that every simple diameter-2 edge-critical graph on 29 vertices has at most 210 edges, with equality exactly for K(14,15). The difficult maximum-degree-16 case is reduced to a small trusted computational kernel with exact integer Farkas verification. The manuscript preserves the full current proof; the companion assembles the graph-to-model bridge, hostile audits and replay guidance. Independent specialist review remains open."),
        proof="project/reviews/n29/2026-09-08-candidate-v1/PROOF.md",
        companion_sources=(
            "project/reviews/n29/2026-09-08-candidate-v1/README.md",
            "project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md",
            "project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md",
            "project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md",
        ),
        status="complete candidate; independent mathematical review OPEN",
        claim="e(G) <= 210, with equality exactly K(14,15)",
    ),
    Spec(
        key="n30",
        release_dir="releases/n30-reviewer-v1",
        manuscript_name="N30_Reviewer_Manuscript_v1",
        companion_name="N30_Verification_Companion_v1",
        title="A candidate proof of the Murty-Simon conjecture at order 30",
        subtitle="Reviewer edition 1 - independent mathematical review pending",
        abstract=("We present the current candidate argument that every simple diameter-2 edge-critical graph on 30 vertices has at most 225 edges, with equality exactly for K(15,15). Published reductions leave a small set of maximum-degree cases; the difficult degree-16 and degree-17 frontiers are closed by exact finite kernels and integer Farkas certificates. The companion records the hostile assembly audit and replay boundary. Independent specialist review remains open."),
        proof="project/reviews/n30/2026-09-09-candidate-v1/PROOF.md",
        companion_sources=(
            "project/reviews/n30/2026-09-09-candidate-v1/README.md",
            "project/reviews/n30/2026-09-09-candidate-v1/ASSEMBLY_AUDIT.md",
        ),
        status="complete candidate; independent mathematical review OPEN",
        claim="e(G) <= 225, with equality exactly K(15,15)",
    ),
    Spec(
        key="general-293-500",
        release_dir="releases/general-293-500-reviewer-v1",
        manuscript_name="General_293_500_Reviewer_Manuscript_v1",
        companion_name="General_293_500_Verification_Companion_v1",
        title="A profile-integral maximum-degree bound for diameter-2 edge-critical graphs",
        subtitle="Reviewer edition 1 - retained candidate general structural theorem",
        abstract=("We present the retained candidate profile-integral argument establishing its original surplus bound and the rational maximum-degree threshold 293/500. This result is superseded in threshold strength by the later 7/12 profile-integral strengthening, but remains preserved as an independently reviewable development checkpoint. Independent mathematical review and novelty assessment remain open."),
        proof="project/research/general_n/2026-09-08-profile-integral-v1/PROOF.md",
        companion_sources=(
            "project/research/general_n/2026-09-08-profile-integral-v1/README.md",
            "project/research/general_n/2026-09-08-profile-integral-v1/AUDIT.md",
        ),
        status="retained candidate hand argument; superseded in threshold strength by 7/12; independent review OPEN",
        claim="n >= 6 and Delta(G) >= (293/500)n imply e(G) < floor(n^2/4)",
    ),
    Spec(
        key="general-7-12",
        release_dir="releases/general-7-12-reviewer-v1",
        manuscript_name="General_7_12_Reviewer_Manuscript_v1",
        companion_name="General_7_12_Verification_Companion_v1",
        title="A strengthened profile-integral maximum-degree bound for diameter-2 edge-critical graphs",
        subtitle="Reviewer edition 1 - current strongest profile-integral candidate",
        abstract=("We present a strengthened candidate profile-integral argument. A sharper elementary square-root minorant improves the universal surplus estimate, and an exact finite threshold certificate completes the degree assembly at the rational threshold 7/12. Two separately written standard-library checkers agree on the scalar arithmetic and every finite exception. The argument remains candidate mathematics: independent specialist review, novelty assessment and external computational reproduction are open."),
        proof="project/research/general_n/2026-09-09-profile-integral-7-12-v1/PROOF.md",
        companion_sources=(
            "project/research/general_n/2026-09-09-profile-integral-7-12-v1/README.md",
            "project/research/general_n/2026-09-09-profile-integral-7-12-v1/AUDIT.md",
            "project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/EXACT_CHECK.json",
            "project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/INDEPENDENT_AUDIT.json",
            "project/research/general_n/2026-09-09-profile-integral-7-12-v1/evidence/run-34355073705/RECEIPT.json",
        ),
        status="complete candidate hand argument; internal exact audits green; independent review and novelty assessment OPEN",
        claim="n >= 6 and Delta(G) >= (7/12)n imply e(G) < floor(n^2/4)",
    ),
    Spec(
        key="general-13-22",
        release_dir="releases/general-13-22-reviewer-v1",
        manuscript_name="General_13_22_Reviewer_Manuscript_v1",
        companion_name="General_13_22_Verification_Companion_v1",
        title="A layer-sum residual bound for diameter-2 edge-critical graphs",
        subtitle="Reviewer edition 1 - retained candidate general structural theorem",
        abstract=("We present the retained candidate layer-sum argument yielding a cubic residual inequality, its resulting surplus bound, and the rational maximum-degree threshold 13/22. The result remains useful structural history even though later profile-integral arguments improve the threshold. Independent mathematical review remains open."),
        proof="project/research/general_n/2026-09-08-layer-sum-v1/PROOF.md",
        companion_sources=(
            "project/research/general_n/2026-09-08-layer-sum-v1/README.md",
            "project/research/general_n/2026-09-08-layer-sum-v1/CONSTRUCTION_AUDIT_2026-09-08.md",
            "project/research/general_n/2026-09-08-layer-sum-v1/LAYER_AGGREGATION_AUDIT_2026-09-08.md",
            "project/research/general_n/2026-09-08-layer-sum-v1/RED_TEAM_2026-09-08.md",
            "project/research/general_n/2026-09-08-layer-sum-v1/RECONCILIATION.md",
        ),
        status="retained candidate hand proof; independent mathematical review OPEN",
        claim="n >= 6 and Delta(G) >= (13/22)n imply e(G) < floor(n^2/4)",
    ),
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def yaml_front(title: str, subtitle: str) -> str:
    return f'''---\ntitle: "{title}"\nsubtitle: "{subtitle}"\nauthor: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"\ndate: "{TODAY}"\ndocumentclass: article\nfontsize: 11pt\ngeometry: [a4paper, margin=25mm]\ncolorlinks: true\nlinkcolor: "black"\nurlcolor: "blue"\n---\n\n'''


def manuscript_front(spec: Spec) -> str:
    return yaml_front(spec.title, spec.subtitle) + f'''\\begin{{abstract}}\n{spec.abstract}\n\\end{{abstract}}\n\n**Reviewer status.** {spec.status}. This reviewer edition is an editorial rendering of the canonical source proof listed below. It does not convert same-assistant checking into external independence, does not make a novelty or priority claim, and does not claim the unrestricted Murty-Simon conjecture unless the source proof itself proves such a statement.\n\n**Canonical claim.** `{spec.claim}`.\n\n**Canonical proof source.** `{spec.proof}`. The source is reproduced in full below; substantive mathematical changes must be made in the canonical proof first and then rebuilt into this edition.\n\n---\n\n'''


def companion_front(spec: Spec) -> str:
    srcs = "\n".join(f"- `{p}`" for p in spec.companion_sources)
    return yaml_front(spec.title + " - verification companion", "Reviewer edition 1 - replay, audit and provenance") + f'''\\begin{{abstract}}\nThis companion collects the principal replay instructions, audits, graph-to-model bridges and provenance documents supporting the reviewer manuscript. It is not a substitute for reading the mathematical proof. Exact arithmetic or certificate verification is identified as such in the underlying sources; same-assistant reconstructions are not represented as external independent review.\n\\end{{abstract}}\n\n## Reviewer orientation\n\n**Claim under review.** `{spec.claim}`.\n\n**Status.** {spec.status}.\n\n**Sources assembled verbatim below:**\n{srcs}\n\nA failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.\n\n---\n\n'''


def run_pandoc(md: Path, pdf: Path) -> None:
    cmd = [
        "pandoc", str(md),
        "--from=markdown+raw_tex+tex_math_single_backslash",
        f"--lua-filter={FILTER}",
        "--pdf-engine=xelatex",
        "-V", "geometry:a4paper",
        "-V", "geometry:margin=25mm",
        "-V", "fontsize=11pt",
        "-V", "mainfont=FreeSerif",
        "-V", "sansfont=FreeSans",
        "-V", "monofont=FreeMono",
        "-V", "colorlinks=true",
        "-V", "urlcolor=blue",
        "-o", str(pdf),
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)


def build(spec: Spec) -> dict:
    proof = ROOT / spec.proof
    if not proof.exists():
        raise FileNotFoundError(proof)
    for p in spec.companion_sources:
        if not (ROOT / p).exists():
            raise FileNotFoundError(ROOT / p)

    out = ROOT / spec.release_dir
    out.mkdir(parents=True, exist_ok=True)
    manuscript_md = out / f"{spec.manuscript_name}.md"
    manuscript_pdf = out / f"{spec.manuscript_name}.pdf"
    companion_md = out / f"{spec.companion_name}.md"
    companion_pdf = out / f"{spec.companion_name}.pdf"

    manuscript_md.write_text(manuscript_front(spec) + proof.read_text(encoding="utf-8"), encoding="utf-8")
    companion_parts = [companion_front(spec)]
    for p in spec.companion_sources:
        companion_parts.append(f"\n\n\\newpage\n\n# Included source: `{p}`\n\n")
        companion_parts.append((ROOT / p).read_text(encoding="utf-8"))
    companion_md.write_text("".join(companion_parts), encoding="utf-8")

    run_pandoc(manuscript_md, manuscript_pdf)
    run_pandoc(companion_md, companion_pdf)

    readme = f'''# {spec.title}\n\n**Reviewer package v1 - {TODAY}.**\n\nCanonical claim: `{spec.claim}`.\n\nStatus: **{spec.status}.**\n\nStart with [{spec.manuscript_name}.pdf]({spec.manuscript_name}.pdf). For computational scope, replay instructions, hostile audits and provenance, read [{spec.companion_name}.pdf]({spec.companion_name}.pdf). The Markdown sources are committed beside the PDFs.\n\nCanonical mathematical source: `{spec.proof}`. This package is editorial: it does not silently alter the underlying proof, and it does not represent internal or same-assistant checking as external independent verification.\n'''
    (out / "README.md").write_text(readme, encoding="utf-8")

    files = [manuscript_md, manuscript_pdf, companion_md, companion_pdf, out / "README.md"]
    manifest = {
        "schema": "murty-simon-reviewer-package-v1",
        "built": TODAY,
        "key": spec.key,
        "claim": spec.claim,
        "status": spec.status,
        "canonical_proof": spec.proof,
        "companion_sources": list(spec.companion_sources),
        "files": [{"path": str(p.relative_to(ROOT)), "sha256": sha256(p), "bytes": p.stat().st_size} for p in files],
        "editorial_only": True,
        "external_review_complete": False,
    }
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def build_index(manifests: list[dict]) -> None:
    lines = [
        "# Review-ready proof index\n",
        f"Updated {TODAY}. This index identifies the canonical reviewer-facing paper for every current theorem-level candidate claim in the top-level project status. Historical failed or superseded development checkpoints remain preserved rather than silently rewritten.\n",
        "| Scope | Claim | Reviewer manuscript | Verification companion | Status |\n",
        "|---|---|---|---|---|\n",
        "| n=25 | `e(G) <= 156`, equality `K(12,13)` | [PDF](n25-reviewer-v1/N25_Reviewer_Manuscript_v1.pdf) | package audit material in [n25 reviewer release](n25-reviewer-v1/README.md) | independent review open |\n",
        "| n=28 | `e(G) <= 196`, equality `K(14,14)` | [PDF](n28-reviewer-v1/N28_Reviewer_Manuscript_v1.pdf) | [PDF](n28-reviewer-v1/N28_Verification_Companion_v1.pdf) | independent review open |\n",
    ]
    for spec in SPECS:
        d = Path(spec.release_dir).name
        lines.append(f"| {spec.key} | `{spec.claim}` | [PDF]({d}/{spec.manuscript_name}.pdf) | [PDF]({d}/{spec.companion_name}.pdf) | {spec.status} |\n")
    lines += [
        "\n## Scope rule\n\n",
        "This index covers the project's current **theorem-level candidate claims**: the fixed-order candidates at n=25,27,28,29,30 and the retained general structural candidates 13/22, 293/500 and 7/12. The 7/12 profile-integral strengthening is the strongest current maximum-degree threshold among these three. Earlier residual-h-index, v9/v10/v11 and other development checkpoints remain available in their original directories as history and supporting lemmas. The ongoing RX-Hall / pairwise-staircase programme is research in progress and is not yet a theorem paper.\n\n",
        "No item in this index is represented as externally accepted. Same-assistant independent implementations are not external independent verification.\n",
    ]
    (ROOT / "releases/REVIEW_READY_INDEX.md").write_text("".join(lines), encoding="utf-8")


def main() -> None:
    manifests = [build(s) for s in SPECS]
    build_index(manifests)
    report = {
        "schema": "review-ready-build-report-v1",
        "built": TODAY,
        "packages": [m["key"] for m in manifests],
        "existing_review_ready": ["n25", "n28"],
        "all_current_theorem_level_claims_have_reviewer_papers": True,
        "external_review_complete": False,
    }
    report_path = ROOT / "project/reviews/reviewer-paper-build/v1/BUILD_REPORT.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
