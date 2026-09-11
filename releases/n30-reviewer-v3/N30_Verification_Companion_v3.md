---
title: "N30 verification companion"
subtitle: "Reviewer edition 3 - dependencies, replay and review obligations"
author: "Paul Lenz research project - developed with ChatGPT/Geeps"
date: "11 September 2026"
documentclass: article
fontsize: 10pt
geometry: [a4paper, margin=23mm]
toc: true
toc-depth: 1
colorlinks: true
linkcolor: black
urlcolor: blue
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
header-includes:
  - \usepackage{amsmath,amssymb,mathtools,booktabs,microtype,pdflscape,etoolbox,fvextra}
  - \setlength{\emergencystretch}{3em}
  - \AtBeginEnvironment{longtable}{\fontsize{8}{9.4}\selectfont}
  - \fvset{fontsize=\small,breaklines=true,breakanywhere=true}
  - \setcounter{tocdepth}{1}
---

# N30 reviewer-v3: verification and review guide

**Claim under review:** every finite simple diameter-two edge-critical graph on thirty vertices has at most 225 edges, with equality exactly for K(15,15).

**Status:** complete candidate argument. Exact internal arithmetic is REPRODUCED. Independent specialist mathematical review and external computational reproduction remain OPEN. Separate implementations by ChatGPT/Geeps do not constitute external independence. No governed theorem-ledger promotion or unrestricted conjecture claim is made.

## What the reviewer receives

The manuscript includes the full proof and all proof-critical integer tables. Its appendices contain the universal bridge, the twelve-label lemma, the 100-profile classification, every five- and six-lift interval, the residual-tail reconstruction, all eight 226-edge source inequalities, the four 225-edge envelopes and every one of the 211 positive-gap rows. Review does not require following links to assemble missing mathematical premises.

The ZIP preserves the PDFs, Markdown, build source, exact original mathematical inputs, arithmetic audit source and saved outputs. Paths inside the ZIP mirror the repository so that the audit scripts run without alteration. Historical inputs appear as source evidence; their earlier status prose is not the current edition's dependency map. Read the reviewer-v3 manuscript for that map.

## The dependency change from reviewer-v2

| Branch | Reviewer-v3 argument | Remaining review obligation |
|---|---|---|
| Delta at most 14, m at least 225 | Degree sum | Elementary arithmetic |
| Delta=15, m=225 | Regularity, common-neighbor count, criticality, complete bipartite equality | Short graph argument |
| Delta=16, m at least 227 | Q at most 21, Q at least 16+2t | Bridge and hand classification |
| Delta=16, m=226 | Seven profiles, nine residual rows, one ledger contradiction and eight source inequalities | Complete finite reconstruction and eight tables |
| Delta=16, m=225 | 100 profiles, 272 rows, 61 ledger contradictions and 211 envelope contradictions | Complete finite reconstruction and all envelope tables |
| Delta=17 through 28, m at least 225 | Twelve-label Q at most 18 and zero-padding | Hand transfer and universal bridge |
| Delta=29 | A universal vertex forces a star | Elementary criticality argument |

The hand transfer proves the stronger m at most 221 at Delta=17. It also yields the candidate corollary `e(G)<=Delta(n-Delta)` whenever `1<=n-1-Delta<=12` and `Delta>=17`; no uniqueness or novelty claim for that corollary is made.

Reviewer-v3 needs neither Fan's density theorem nor the published dominating-edge reduction. The isolated-C strengthening, higher-degree charging scans, large historical profile/residual scans, grouped LPs and Farkas rays are no longer premises. They remain historical evidence. **Finite arithmetic has not disappeared:** the printed classification and endpoint tables remain proof-critical.

## What the internal audit established

The preceding assembly was preserved at commit `01d1fb03d5b68ea4494a4ff29cedd0b49cb5dc16`, with its receipt at `81f37b80f643dd12f371680e673a95f6de793df2`. All six relevant GitHub workflows passed. The new implementation's run was [34649839054](https://github.com/paullenz/MurtySimon742/actions/runs/34649839054).

| Internal check | Result |
|---|---|
| Thirteen-label full-domain regression | 5,200,300 multisets; maximum Q=21; exactly 100 high-score profiles |
| Thirteen-label clipping regression | 20,801,200 comparisons; no failure |
| Twelve-label unbounded-threshold regression | 1,352,078 multisets; maximum Q=18 |
| Twelve-label clipping regression | 5,371,184 comparisons; no failure; exceptional all-fives case handled directly |
| Independent 225-edge reconstruction | 272 total rows, 61 ledger exclusions, 211 tight rows |
| Independent envelope arithmetic | 12,772 local states; all 844 per-template row gaps match |
| Assigned envelope cover | B1:195, B2:13, B3:2, C1:1; minimum integer gap 1 |
| Independent 226-edge arithmetic | Nine rows, one ledger exclusion, eight source contradictions; 859 source states |

The C++ full-domain regressions corroborate the written clipping proofs. They are not logical premises. The Python checker imports neither predecessor acceptance code nor discovery code. It uses a separate residual reconstruction and literal potential formulas; no numerical solver or floating point is used. Its agreements are internal evidence, not a substitute for human review of the deductions and printed arithmetic.

## Reproduce from the ZIP or repository

After extracting the ZIP, change into its top directory, `N30_Reviewer_Package_v3`. Alternatively run from the repository root. Python 3.12 and a C++17 compiler suffice for the mathematical checks; no third-party Python packages or solver are required.

```bash
python3 -I -B project/reviews/n30/2026-09-11-reviewer-v3/replay_bundle.py
```

This command verifies all bundled file hashes, compiles the preserved C++ regression into a temporary directory, regenerates both profile sweeps, compares the regenerated JSON with its saved counterpart, and runs the exact endpoint audit and written twelve-label payment-table check. It leaves original evidence files unchanged and prints a compact PASS report. A mismatch fails the command. The endpoint auditor reads the saved profile JSON only after it has been reproduced exactly in this replay.

To regenerate the PDF source and PDFs in a full repository checkout, use Python, Pandoc, XeLaTeX, the DejaVu Serif/Sans/Mono fonts and the supplied build script:

```bash
python3 project/reviews/n30/2026-09-11-reviewer-v3/build_package.py
```

Rendering is editorial; exact PDF bytes can vary with toolchain metadata and font versions. The committed manifest pins the reviewed outputs. SHA checks and exact arithmetic do not depend on visual rendering. The manuscript's mathematical input hashes are in SOURCE_MAP.json; BUNDLE_CONTENTS.json pins the files inside the ZIP, and MANIFEST.json pins the release PDFs and ZIP without recursive self-hashing.

## Editorial corrections and preservation

The new manuscript uses the canonical bridge's correct source-degree identity `(rho+q)+(b-1-q-p)=rho+b-1-p`, giving `p<=rho+b-a-1`. It correctly identifies z as the unique exception of `uj->z` in the residual forcing argument. These repair wording/display issues already documented in older copies; the old copies remain preserved.

Positive demand alone implies `s_i=d_i-R_i`; ledger tightness is not an extra premise for excluding the positive-slack 226-edge row. The manuscript states this directly. At zero-demand labels, the different equality-of-sums argument is written explicitly before the envelope proof.

Local equation and section references are qualified by appendix. Source statements that an already completed later task was still open have been removed from the new exposition. Every mathematical source and table remains hash-pinned; the editorial record explains the selected sections and these clarifications. All prior reviewer-v2 files and the governed ledger are preserved unchanged.

## Highest-value external review

1. Check the complement equivalence, unique selected representatives, residual forcing and all-source activity. A flaw here overrides downstream arithmetic.
2. Check the threshold-capacity unordered-pair count and both clipping arguments, especially unbounded gamma, the all-fives exception and reverse lifts.
3. Check completeness of all 100 profiles and both residual frontiers from the printed rules, then the sign of each envelope/resource inequality and all finite minima.
4. Check the elementary equality branch and the final degree assembly. Record any counterexample, missing case or hidden premise with a precise location.

A useful report distinguishes a mathematical gap, an arithmetic mismatch, a rendering error and an expository improvement. The supplied review report template can be used without accepting any project status label. A clean internal run does not pre-judge the result of that review.

\clearpage

# Included internal bridge audit

The following audit is preserved from the pre-edition assembly. Its references to a supplementary route and frozen reviewer-v2 describe that earlier checkpoint; reviewer-v3 now packages that route. No new external review is implied.


**No blocking flaw identified in the reviewed implications. This is internal same-assistant mathematical review, not independent specialist acceptance.**

The proof surface used by this assembly is the canonical parameterized bridge (Appendix A). The audit followed every implication needed by the N30 supplementary route: Sections 1-9 and 11 of that bridge, the two tail arguments, the profile/row classifications, and the two endpoint certificate arguments. Charging, isolated-C and the general h-index corollary are not required by the new assembly.

## 1. Criticality and selected representatives

For distinct vertices x,y, distance greater than two in G is equivalent to an adjacent total-dominating pair in its complement H: adjacency in H means xy is absent in G, and total domination means there is no vertex adjacent to both x and y in G. Open neighborhoods include both endpoints precisely when the pair is adjacent in H.

Adding a missing B-pair uw changes only the H-neighborhoods of u and w, so any newly total-dominating pair uses at least one endpoint. It cannot be uw itself because both endpoints still miss the root v. An existing pair ui must therefore become total dominating by covering its unique former exception w. Its auxiliary i lies in A to dominate v.

A selected cross-edge uniquely determines its source and its sole undominated B-vertex. It therefore identifies its indexing missing unordered B-pair. Selecting one representative per unordered pair gives an injection and prohibits opposite orientations. At a fixed source both labels and supplements are distinct. These facts are needed later; selecting one edge per orientation instead would invalidate the pair counts.

## 2. Ledger and demand

Selected edges plus H[B]-edges count each unordered B-pair once. Substitution into the complement edge count gives exactly `e(F)=r+t`. Minimum complement degree gives `x_i>=d_i-R_i`; hence `s_i=max(0,d_i-R_i)` satisfies `x_i>=s_i` and `S>=r+2t`.

This uses only the minimum-degree root and simple-graph counting. No stronger isolated-C conclusion is being inserted into the label degree cap: F has a vertices, so the direct bound is `d_i<=a-1`.

## 3. Forced residual edges and positive-surplus activity

For selected `ui->w`, each F-neighbor j of i forces an H-edge uj. If it is residual, it is counted at u. If selected `uj->z`, then z differs from w, `uz` is absent, and `iz` is forced. Both i and z miss the A-vertex j; therefore iz cannot be a selected edge, whose only exception lies in B. Distinct supplements make these forced residual incidences injective. This proves `d_i<=rho_u+R_i` and `s_i<=rho_u`.

The analogous count at supplement w gives `d_i<=rho_u+rho_w`; the assembly does not need that stronger second residual inequality, but its injection has the same valid disjointness mechanism.

For residual activity, suppose some rho_u=0 and partition A into its cross-neighbors U and nonneighbors T. Every u-to-U edge is selected, so an F-edge between U and T would leave an A-vertex undominated, impossible. Each F[U]-edge forces two distinct residual cross-edges with A-endpoints in U. Each F[T]-edge, when added in H, forces a cross quasi-edge with exception in A: the pair cannot use both T-endpoints because they miss u; an A-auxiliary would force a forbidden F-edge between U and T. Its unique exception identifies the original F[T]-edge, so this is injective into residual edges with A-endpoint in T. The two families are disjoint. Thus `r>=2e(F[U])+e(F[T])>=e(F)=r+t`, contradicting t>0.

The proof is universal in a,b and does not assume t is one or two. That is essential for the new Delta=17 transfer.

## 4. Source, supplement and endpoint capacities

Every F-neighbor of label i is an A-neighbor of its selected source u, different from i itself; hence `d_i<=rho_u+q_u-1`. Other selected labels at u force distinct cross-neighbors of the supplement w, giving `rho_w+q_w>=q_u-1`.

The exact degree calculation is

$$
d_H(u)=(\rho_u+q_u)+(b-1-q_u-p_u)=\rho_u+b-1-p_u\ge a.
$$

Thus `p_u<=rho_u+b-a-1`; at a=13,b=16 this is `p<=rho+2`. Together with `q<=a-rho`, it already implies `q+p<=15`. The endpoint box must include the boundary `p=rho+2`. No `rho+1` tightening is valid here.

For a selected ui, label i is adjacent to u, the other outward supplements of u, and all inward sources to u. The two latter families cannot collide because that would select opposite orientations of one unordered pair. Hence `R_i+x_i>=q_u+p_u`.

Individual label and source caps follow from distinct simple-graph incidences and `s_i<=rho_u`: `x_i<=#{rho>=s_i}` and `q_u<=#{s_i<=rho_u}`. These are upper bounds on actual degrees, not assumptions of independent realizability of relaxed vertex states.

## 5. Threshold capacity and the transfer

At threshold h, call selected labels heavy when their demand is at least h. A source with more than h heavy labels has every heavy supplement in Z_h: the other heavy labels force at least h cross-edges at that supplement; either all are residual, or a selected one already forces rho>=h.

For j such sources among z_h vertices, unordered-pair injection bounds their arcs by `j*z_h-j(j+1)/2`. Other sources contribute at most h each. The difference between `h*z_h+C(z_h-h,2)` and that combined bound is `(z_h-h-j)(z_h-h-j-1)/2`, nonnegative for every integer j. This yields the stated capacity without a source-count-specific constant.

Defining the inverse capacity without an upper cutoff therefore preserves the graph implication for any b. A profile whose inverse exceeded b would simply be impossible for an actual graph. Padding at most twelve labels with zeros leaves Q unchanged. The twelve-label hand proof has no step requiring b=16, so it legitimately gives the N30 Delta>=17 exclusion.

## 6. Ledger equality, potentials and signs

If every s_i is positive, its definition already forces `s_i=d_i-R_i`; summing gives `S=r+2t`. If the ledger is tight but a label has s_i=0, equality of `sum max(0,d_i-R_i)` and `sum(d_i-R_i)` forces `d_i=R_i` there too. Thus all tight rows satisfy `d_i=R_i+s_i`, including all four zero-demand m225 rows.

Combining source-degree forcing and endpoint load gives the three coordinate inequalities used by the monotone potentials. Their coordinates are nonnegative on the full local boxes. Every potential coefficient is nonnegative; `s*v`, threshold indicators and rectangles are coordinatewise nondecreasing. Summing incidence inequalities counts each label x_i times and each source q_u times, giving the correct sign.

The four-envelope sum cancels the c and mu terms using `sum x=sum q=sum p`. Nonnegative supplement-tail weights multiply nonpositive H_k. Therefore the summed lower envelopes cannot exceed lambda*r. Strictly positive reported gaps contradict the graph. The independent evaluator matches all 844 gaps, not only the first successful certificate per row.

At m226, the alpha bound is exactly three. The elementary inequality `(s+e)min(e,3)<=(s+3)e` is valid for all nonnegative integer s,e. The source inequalities, after subtracting nonpositive Hall-tail terms, give the required lower bound on `B0-cE`; no sign reversal was found.

## 7. Historical wording clarifications

Two errors in older copies do not change the mathematical implications used here:

1. Section 4.1 of the frozen N29 reviewer-v3 bridge says that j is the unique exception of `uj->z`. The exception is **z**. What is needed is that jz is absent, which follows because z is that exception. Canonical Section 6.1 states this correctly.
2. The frozen N29 bridge and the older `2026-09-11-universal-selected-residual-bridge-v1/UNIVERSAL_BRIDGE.md` omit q_u in an intermediate source-degree display. The correct formula is printed in Section 4 above and canonical Section 7. The already-stated supplement bound remains correct. The earlier [source-degree erratum](https://github.com/paullenz/MurtySimon742/blob/81f37b80f643dd12f371680e673a95f6de793df2/project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md) remains applicable.

The m226 endpoint note also describes the positive-demand implication imprecisely using the word “tight”. Positivity alone gives `s_i=d_i-R_i`; no tightness assumption is required to exclude its one positive-slack row. The assembled proof uses the direct implication.

Historical proof sources are left unchanged and hash-accounted in the publication. These are wording/display clarifications, not new missing lemmas or repaired numerical exclusions.

## 8. Limits

No blocking flaw was found in the reviewed chain, but the main risk remains a universal graph argument, not a floating-point calculation. The exhaustive regressions test arithmetic demand vectors, not all thirty-vertex graphs, and do not prove the bridge. Independent specialist scrutiny remains essential. This audit does not certify unrelated earlier discovery models, and no governed theorem-ledger status is promoted.

\clearpage

# Source and integrity inventory

The build records SHA-256 hashes for every input in SOURCE_MAP.json and packages the original input bytes. Sections were consolidated as described in EDITORIAL_REVIEW.md; historical sources remain unchanged.

- `project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md`

  SHA-256: `c87068f40785baa790495aa5811b92370012845c0e592cfeacd6c03a3976dcd2`

- `project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLED_PROOF.md`

  SHA-256: `d2a0b37ddccfa51204a817f0e9fff1537f58c4a0c789fc76e3681c9f6017f8ad`

- `project/research/n30/2026-09-11-assembled-hand-route-v1/BRIDGE_AUDIT.md`

  SHA-256: `042bd5113e2b3bd82dc3aa5e5625be3d537800b5d7220cf9a3e0bebe96d94395`

- `project/research/n30/2026-09-11-assembled-hand-route-v1/TWELVE_LABEL_TRANSFER.md`

  SHA-256: `3eaf4b64c6e388823a0eca47fbdf646f6f7e0a71197124525a84651caf22512c`

- `project/research/n30/2026-09-11-m225-hand-classification-v1/HAND_CLASSIFICATION.md`

  SHA-256: `2c410a2a9c939441579d1d9ea1e899a18b79a2ed150ff112b2fb13dceae8ed70`

- `project/research/n30/2026-09-11-m225-hand-classification-v1/PREIMAGE_ARITHMETIC.md`

  SHA-256: `8fe4a58f3c472c1f3964f403be2a07f0e8fb574a4e3033f50d9b0f03a3950648`

- `project/research/n30/2026-09-11-m225-resource-envelope-v1/EXACT_APPENDIX.md`

  SHA-256: `c658de4f40e6382c48c71d16f438c093eb750388e3705e3a59b379ceca7a206a`

- `project/research/n30/2026-09-11-m225-resource-envelope-v1/FOUR_ENVELOPE_REDUCTION.md`

  SHA-256: `be1c5025c359a223ab8023a5940b07c96adf6132feb012156a1d55459ff945f7`

- `project/research/n30/2026-09-11-threshold-tail-v1/N30_M225_THRESHOLD_SLACK_REDUCTION.md`

  SHA-256: `641e300abea1959327b7f86c87863e91924e800b4ea8ca86ca949d4a5a5260dd`

- `project/research/n30/2026-09-11-threshold-tail-v1/N30_M226_HAND_ENDPOINT_REDUCTION.md`

  SHA-256: `1bcd6da2e687149315461446c90a613ff7c54a6e7f369a2a4ac4fdd9575bb2c2`

- `project/reviews/n30/2026-09-11-reviewer-v3/VERIFICATION_COMPANION.md`

  SHA-256: `18caec8c93fb0410e05ba6ffce2ff8f134d6f3936e00d7ebe8aff150d252e956`

