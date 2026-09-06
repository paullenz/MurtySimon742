# Literature and attribution check

Checked 6 September 2026. This is a targeted public-source check, not an exhaustive bibliographic review or a priority determination.

**Finding:** no published resolution of the complete order-25 case was located in the sources inspected. This does not establish novelty. The reviewer edition should be described as a candidate for examination, without a “39-year-old problem solved” announcement.

## Mathematical inputs

| Source | Exact use in the candidate | Check and limitation |
|---|---|---|
| Genghua Fan, *On diameter 2-critical graphs*, Discrete Mathematics 67 (1987), 235–240, [DOI](https://doi.org/10.1016/0012-365X(87)90174-9) | Strict numerical bound implies e(G)≤157 at n=25. | The formula was checked against the publisher abstract and Wang's primary manuscript, p.2. Fan's full publisher text was unavailable; no full-paper audit is claimed. |
| Tao Wang, *On Murty-Simon Conjecture*, [arXiv:1205.4397v1](https://arxiv.org/pdf/1205.4397v1), 2012 | Fan's exact formula; Theorem 2.1 covers the complement-diameter-three strict inequality at odd orders. | Primary manuscript consulted. It is cited as an arXiv manuscript; no unverified journal publication is asserted. |
| Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs*, 2014, [primary PDF](https://d-nb.info/1372516379/34) | Theorems 3.1, 3.2 and 3.6(a): complement correspondence, complete-bipartite exception and δ(H)≤0.3n bound. | The minimum-degree inequality points toward small δ. At n=25, δ≤7 gives e(H)≥145. Stars are handled separately. The odd-order diameter-three point is cross-checked using Wang. |
| Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142–3159, [DOI](https://doi.org/10.1016/j.disc.2019.06.023), [primary manuscript](https://arxiv.org/pdf/1812.08420) | Theorem 4 excludes a dominating edge in a non-bipartite order-25 graph with 156 or 157 edges. | The bound is floor(n²/4)-2, with a six-vertex exception that cannot occur at order 25. |

## Recent and adjacent work inspected

- Kirchweger, Manrique and Szeider, *Formally Verified Graph Generation with SAT Modulo Symmetries and Lean*, IJCAR 2026, first online 24 July 2026. Section 5 explicitly reports formal confirmation through 13 vertices. It does not report an order-25 resolution. [Primary publisher text](https://link.springer.com/chapter/10.1007/978-3-032-32589-1_8)
- Kirchweger, Xia, Peitl and Szeider, *Smart Cubing for Graph Search: A Comparative Study*, arXiv:2501.17201, submitted January 2025 and subsequently appearing in CP 2026. Its diameter-critical-graph benchmarks and computational methodology are relevant background; it is not an input to this proof. [Primary manuscript](https://arxiv.org/html/2501.17201v1), [conference record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2026.33)
- The 2016 manuscript *Improving the bound for maximum degree on Murty-Simon Conjecture* states a high-degree threshold of 0.6756n, which at order 25 only reaches integer degree 17. Its Theorem 2.6 reverses the minimum-degree inequality when restating the 2014 result. This candidate therefore cites the original 2014 text directly and does not depend on the 2016 manuscript. [Primary manuscript](https://arxiv.org/html/1610.00360v2)
- A 2025 publisher result on a restricted class of diameter-2-critical graphs was found in search, but the full abstract/text could not be retrieved. Its title is insufficient to establish coverage of all order-25 graphs, so it is not used as a novelty conclusion. [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0166218X25003439)

The Erdős Problems page for 742 returned an access error during this check. Search results also surfaced recent experimental repositories and restricted symmetry exclusions; inaccessible repository pages and search snippets were not treated as proof of either a complete solution or the absence of one. No source here justifies declaring the general Murty–Simon conjecture solved.

Searches included the exact problem name with “25”, “n=25”, “proof”, “2025” and “2026”, followed by the primary papers and author pages. Before public submission, an expert should confirm the precise novelty claim and check Fan's original full paper and any more recent specialized results.

## Contribution and evidence disclosure

Paul Lenz initiated and directed this research project and supplied the earlier project material. ChatGPT/Codex produced substantial mathematical arguments, implementation code, internal audits and the assembled candidate text. Both arithmetic implementations and the separate certificate checker were produced with the same assistant; their agreement is a software cross-check, not independent mathematical authorship or review.

Published inputs remain attributed to their original authors. The frozen project dossier and new generalizations have separate, preserved provenance. This reviewer edition does not assign final scholarly authorship, assert independent expert endorsement, or claim Lean/formal-kernel verification. A publication byline and contribution statement should be settled explicitly before submission.

The original mathematical evidence remains byte-identical to the archived version. This edition adds typography, navigation, a top-level verification/replay wrapper, literature notes and review materials; it does not promote the governed theorem ledger.
