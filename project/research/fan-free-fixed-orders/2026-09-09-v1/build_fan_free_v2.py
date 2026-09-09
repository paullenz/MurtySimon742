#!/usr/bin/env python3
"""Build Fan-free v2 fixed-order proof editions from frozen historical sources.

The historical v1 proofs are never modified. This script performs only explicit,
asserted editorial/logical replacements:
  * replace Fan as the upper-range logical dependency with FAN_FREE_REDUCTION.md;
  * clarify one-representative-per-unordered-B-pair selection;
  * clarify why the forced residual cross-edge cannot itself be selected;
  * update the final assembly sentence.
"""
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parents[4]
FF='project/research/fan-free-fixed-orders/2026-09-09-v1/FAN_FREE_REDUCTION.md'


def once(text,old,new,label):
    n=text.count(old)
    if n!=1:
        raise SystemExit(f'{label}: expected exactly one anchor, found {n}')
    return text.replace(old,new,1)


def sha256_text(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def common_selection_patch(text,label):
    old=("For each missing unordered pair bw in H[B], this observation applies because the pair misses v. Choose one cross-edge bi→w, where i is in A since it must dominate v. Different missing B-pairs select different cross-edges: a cross-edge fixes its B-endpoint and its unique exception. Call these edges selected and all other A–B edges residual. At a fixed B-source, supplements of different selected edges are distinct, since only one edge was selected for each unordered B-pair.")
    new=("For each missing **unordered** pair {b,w} in H[B], this observation applies because the pair misses v. Fix that unordered pair first, and designate exactly one corresponding cross-edge bi→w after interchanging b and w if necessary; i lies in A because the edge must dominate v. If both orientations happen to be available as possible quasi-edges, only one is designated selected for this unordered pair. Thus the map from selected edges to missing unordered B-pairs is injective by construction: a selected edge fixes its B-source and its unique B-exception, and opposite orientations of the same pair can never both be selected. Call these designated edges selected and all other A–B edges residual. At a fixed B-source, supplements of different selected edges are distinct, since there is only one selected representative for each unordered B-pair.")
    return once(text,old,new,label+' selected-pair clarification')


def common_residual_patch(text,label):
    old=("Since bw_i is absent, jw_i is an edge. It is residual because j and w_i both miss the A-vertex i. Similarly iw_j is residual.")
    new=("Since bw_i is absent, jw_i is an edge. It is residual: j and w_i both miss the A-vertex i, so jw_i cannot be one of the selected representatives of a missing B–B pair, because every selected edge has its unique exception in B and therefore must dominate every A-vertex. Similarly iw_j is residual.")
    return once(text,old,new,label+' forced-residual clarification')


def build_n25():
    src=ROOT/'project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md'
    text=src.read_text()
    frozen_hash=sha256_text(text)
    prefix=("# N=25 Murty–Simon: Fan-free reviewer proof, edition 2\n\n"
            "9 September 2026. Built deterministically from the frozen 6 September candidate proof.\n\n"
            "**Status:** complete candidate argument with internally checked exact arithmetic; independent mathematical and computational review OPEN. This edition removes Fan's theorem as a logical dependency while preserving and citing the historical Fan-based v1 proof.\n\n"
            f"**Historical source preserved:** `project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md` (SHA-256 `{frozen_hash}`).\n\n"
            f"**Fan-free replacement component:** `{FF}`.\n\n---\n\n")
    # Drop original title/date/status preamble but keep from Section 1 onward.
    marker='## 1. Statement and scope\n'
    if marker not in text: raise SystemExit('n25 section-1 marker missing')
    text=prefix+marker+text.split(marker,1)[1]

    old=("Fan's bound, valid for n at least 25, is\n\n"
         "\\[\n"
         "e(G)<\\frac{n^2}{4}+\\frac{n^2-16.2n+56}{320}.\n"
         "\\]\n\n"
         "At n=25 its right side is 157.1125 = 12569/80. Thus integrality gives e(G) at most 157: a counterexample to the upper bound has **exactly 157 edges**. This is a direct numerical reduction and requires no deletion of edges while preserving criticality. The formula appears in the primary publisher abstract of G. Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, [DOI 10.1016/0012-365X(87)90174-9](https://www.sciencedirect.com/science/article/pii/0012365X87901749), and is explicitly stated on page 2 of [Tao Wang, *On Murty-Simon Conjecture*](https://arxiv.org/pdf/1205.4397).")
    new=("### Fan-free upper-range reduction\n\n"
         "Historically, the v1 proof used G. Fan's 1987 theorem (*On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, DOI 10.1016/0012-365X(87)90174-9) to reduce an above-target graph to 157 edges. Fan is retained here for attribution, but **his theorem is not a logical dependency of this edition**.\n\n"
         f"The replacement is proved in `{FF}`. Briefly: the degree sum excludes `Delta<=12`; the existing complement maximum-degree theorem excludes `Delta>=17`; the Section 3 witness inequality at `Delta=13` is monotone stronger as `m=e(G)` increases and therefore excludes every `m>=157`; the frozen residual proof below excludes `m=157` for `Delta=14,15,16`; and a new exact necessary-condition scan covers every larger degree-sum-possible edge count, namely `m=158..175` at `Delta=14`, `158..187` at `Delta=15`, and `158..200` at `Delta=16`. Across those 91 scopes it enumerates 128,754 outer numerical states and leaves **zero** survivors. Hence every above-target graph has exactly 157 edges before the original dense-case analysis below is invoked.\n\n"
         "The old Fan-based reduction remains available in the frozen v1 proof for historical comparison.")
    text=once(text,old,new,'n25 Fan block')
    text=common_selection_patch(text,'n25')
    text=common_residual_patch(text,'n25')
    text=once(text,
        "Fan reduces any upper-bound counterexample to 157 edges. The degree-sum bound covers Δ≤12; Section 3 covers Δ=13; the original reviewed finite argument covers Δ=14; Sections 4–7 cover Δ=15,16; and the published maximum-degree input covers Δ≥17.",
        "The Fan-free upper-range reduction above excludes every edge count `m>=158`, while the dense-case analysis in this manuscript excludes `m=157`. The degree-sum bound covers Δ≤12; Section 3 covers Δ=13; the original reviewed finite argument covers Δ=14; Sections 4–7 cover Δ=15,16; and the published complement maximum-degree input covers Δ≥17.",
        'n25 assembly')
    out=ROOT/'project/reviews/n25/2026-09-09-fan-free-v2'
    out.mkdir(parents=True,exist_ok=True)
    (out/'PROOF.md').write_text(text)
    (out/'HISTORY.md').write_text(f"""# n=25 proof history for Fan-free edition 2

The canonical historical v1 proof remains unchanged at
`project/reviews/n25/2026-09-06-full-chain-candidate-v1/PROOF.md`.

Its SHA-256 at v2 build time is `{frozen_hash}`.

Edition 2 changes only:

1. Fan's 1987 theorem is moved from logical dependency to historical attribution and replaced by `{FF}`;
2. the selected-edge convention now says explicitly that exactly one representative is designated per missing unordered B-pair, so reverse orientations cannot collide;
3. the Section 5 forced cross-edge is explicitly shown non-selected before being counted residual;
4. the final assembly sentence points to the Fan-free reduction.

No frozen v1 evidence, source, hash or theorem ledger entry is overwritten.
""")


def build_n27():
    src=ROOT/'project/reviews/n27/2026-09-07-candidate-v1/PROOF.md'
    text=src.read_text(); frozen_hash=sha256_text(text)
    prefix=("# Murty–Simon at n=27: Fan-free candidate proof, edition 2\n\n"
            "9 September 2026. Built deterministically from the frozen 7 September candidate proof.\n\n"
            "**Status:** complete candidate argument with internally replayed exact arithmetic; independent mathematical and computational review OPEN. This edition removes Fan's theorem as a logical dependency while preserving and citing the historical Fan-based v1 proof.\n\n"
            f"**Historical source preserved:** `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md` (SHA-256 `{frozen_hash}`).\n\n"
            f"**Fan-free replacement component:** `{FF}`.\n\n---\n\n")
    marker='## 1. Statement\n'
    if marker not in text: raise SystemExit('n27 section-1 marker missing')
    text=prefix+marker+text.split(marker,1)[1]
    old=("Fan's strict bound, as stated on page 2 of [Wang, On Murty-Simon Conjecture](https://arxiv.org/pdf/1205.4397), gives\n\n"
         "\\[\n"
         "e(G)<\\frac{n^2}{4}+\\frac{n^2-16.2n+56}{320}.\n"
         "\\]\n\n"
         "At n=27 the right side is exactly 146669/800=183.33625. Thus an upper-bound counterexample has exactly 183 edges. We separately examine equality at 182 edges. We do not delete edges and assume criticality is preserved. Fan's original source is [On diameter 2-critical graphs, Discrete Mathematics 67 (1987), 235–240](https://www.sciencedirect.com/science/article/pii/0012365X87901749); its full proof was not re-audited here.")
    new=("### Fan-free upper-range reduction\n\n"
         "Historically, the v1 proof used G. Fan's 1987 theorem (*On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, DOI 10.1016/0012-365X(87)90174-9) to reduce an above-target graph to 183 edges. Fan is retained here for attribution, but **his theorem is not a logical dependency of this edition**.\n\n"
         f"The replacement is proved in `{FF}`. Briefly: the degree sum excludes `Delta<=13`; the existing complement maximum-degree theorem excludes `Delta>=18`; the Section 3 witness inequality at `Delta=14` is monotone stronger as `m=e(G)` increases and therefore excludes every `m>=183`; the frozen dense-case proof below excludes `m=183` at `Delta=15,16,17`; and a new exact necessary-condition scan covers every larger degree-sum-possible edge count. `Delta=16` contributes 8,880 outer states and zero survivors; `Delta=17` has an empty numerical domain. At `Delta=15`, all `m>=186` die at the outer layer; the only 661 outer survivors occur at `m=184,185`, and their 49,461 canonical residual columns (representing 1,185,130 labelled columns) are all rejected by the existing column/source-cap/subset machinery with independent check-mode replay. Hence every above-target graph has exactly 183 edges before the original dense-case analysis below is invoked.\n\n"
         "The old Fan-based reduction remains available in the frozen v1 proof for historical comparison.")
    text=once(text,old,new,'n27 Fan block')
    text=common_selection_patch(text,'n27')
    text=common_residual_patch(text,'n27')
    text=once(text,
        "Its unordered source/supplement pair is different from every other selected edge's pair, by Section 4. This gives the stated injection.",
        "By the Section 4 selection convention, each selected edge is the unique designated representative of its missing unordered B-pair. Therefore two selected edges cannot be opposite orientations of the same pair, and their unordered source/supplement pairs are distinct. This gives the stated injection.",
        'n27 fixed-column pair clarification')
    text=once(text,
        "Fan leaves only 183 edges above the target. The degree sum covers Δ≤13; Section 3 covers Δ14; Sections 4–11 cover Δ15,16,17; the published complement bound covers Δ≥18.",
        "The Fan-free upper-range reduction excludes every edge count `m>=184`, while Sections 3–11 exclude `m=183`. The degree sum covers Δ≤13; Section 3 covers Δ14; Sections 4–11 cover Δ15,16,17; the published complement bound covers Δ≥18.",
        'n27 assembly')
    out=ROOT/'project/reviews/n27/2026-09-09-fan-free-v2'
    out.mkdir(parents=True,exist_ok=True)
    (out/'PROOF.md').write_text(text)
    (out/'HISTORY.md').write_text(f"""# n=27 proof history for Fan-free edition 2

The canonical historical v1 proof remains unchanged at
`project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`.

Its SHA-256 at v2 build time is `{frozen_hash}`.

Edition 2 changes only:

1. Fan's 1987 theorem is moved from logical dependency to historical attribution and replaced by `{FF}`;
2. the selected-edge convention explicitly designates exactly one representative per missing unordered B-pair;
3. the Section 5 forced cross-edge is explicitly shown non-selected before being counted residual;
4. Equation (10.1)'s unordered-pair injection explicitly rules out reverse-orientation collisions;
5. the final assembly sentence points to the Fan-free reduction.

The 8 September red-team report and the later cross-cutting feedback audit remain preserved separately. No frozen v1 evidence, source, hash or theorem ledger entry is overwritten.
""")


if __name__=='__main__':
    build_n25(); build_n27(); print('FAN_FREE_V2_BUILD_OK')
