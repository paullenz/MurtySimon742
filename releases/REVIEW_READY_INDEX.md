# Review-ready proof index
Updated 12 September 2026. This index identifies the canonical reviewer-facing paper or source package for every current theorem-level candidate claim in the top-level project status. Historical failed or superseded development checkpoints remain preserved rather than silently rewritten.

The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. Source-first reviewer-v1 packages cover `n=31,32,33,34`, including complete candidate bound and equality classification at n=34. The 12 September step-back programme also has a source-first general-theory package collecting the new balanced-degree, `a=14`, fifteen-label and sixteen-label structural results.

**Current review notes:** reviewers of the frozen N29 bridge appendix should apply the [source-degree display erratum](../project/reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md). N30 reviewer-v3 incorporates the corrected canonical bridge and the [assembled route](../project/research/n30/2026-09-11-assembled-hand-route-v1/ASSEMBLED_PROOF.md). Internal arithmetic and same-assistant hostile audits are not external validation.

| Scope | Claim | Reviewer manuscript / package | Verification / audit | Status |
|---|---|---|---|---|
| n=25 | `e(G) <= 156`, equality `K(12,13)` | [PDF](n25-reviewer-v2/N25_Reviewer_Manuscript_v2.pdf) | [PDF](n25-reviewer-v2/N25_Verification_Companion_v2.pdf) | **Fan-free v2**; independent review open; [v1 history](n25-reviewer-v1/README.md) |
| n=27 | `e(G) <= 182`, equality `K(13,14)` | [PDF](n27-reviewer-v2/N27_Reviewer_Manuscript_v2.pdf) | [PDF](n27-reviewer-v2/N27_Verification_Companion_v2.pdf) | **Fan-free v2**; independent review OPEN; [v1 history](n27-reviewer-v1/README.md) |
| n=28 | `e(G) <= 196`, equality `K(14,14)` | [PDF](n28-reviewer-v2/N28_Reviewer_Manuscript_v2.pdf) | [PDF](n28-reviewer-v2/N28_Verification_Companion_v2.pdf) | **Fan-free v2 + analytic hardening**; internal hostile audit PASS; independent review open |
| n=29 | `e(G) <= 210`, equality `K(14,15)` | [PDF v4](n29-reviewer-v4/N29_Reviewer_Manuscript_v4.pdf) | [PDF v4](n29-reviewer-v4/N29_Verification_Companion_v4.pdf) | **Reviewer-v4 hand-reduced + hostile audit PASS**; no proof-critical N29 computation; independent review OPEN |
| n=30 | `e(G) <= 225`, equality `K(15,15)` | [PDF v3](n30-reviewer-v3/N30_Reviewer_Manuscript_v3.pdf) | [PDF v3](n30-reviewer-v3/N30_Verification_Companion_v3.pdf) | **Reviewer-v3 hand lemmas + explicit integer tables**; internal arithmetic REPRODUCED; independent review OPEN |
| n=31 | `e(G) <= 240`, equality `K(15,16)` | [source package](n31-reviewer-v1/README.md) | [hostile audit](../project/research/n31/2026-09-11-hand-route-v1/HOSTILE_AUDIT.md) | **Reviewer-v1 source-first hand route**; no blocking flaw found internally; independent review OPEN |
| n=32 | `e(G) <= 256`, equality `K(16,16)` | [source package](n32-reviewer-v1/README.md) | [exact equality ledger](../project/research/n32/2026-09-12-equality-v1/CERTIFICATION_LEDGER.md) | **Reviewer-v1 hand + exact finite replay**; hostile internal audit found no blocking flaw; independent review OPEN |
| n=33 | `e(G) <= 272`, equality `K(16,17)` | [source package](n33-reviewer-v1/README.md) | [hostile audit](../project/research/n33/2026-09-12-candidate-v1/HOSTILE_AUDIT.md) | **Reviewer-v1 compact hand + exact 25-state replay**; 21 demand profiles / 29 states at the sole new equality frontier; no blocking flaw found internally; independent review OPEN |
| balanced-degree general theorem | `Delta=ceil(n/2) => e(G)<=floor(n^2/4)`, equality only balanced complete bipartite; any counterexample has `Delta>=ceil(n/2)+1` | [source package](general-stepback-v1/README.md) | [hostile audit](../project/reviews/general-theory/2026-09-12-stepback-v1/HOSTILE_AUDIT.md) | **New all-order structural candidate**; symbolic witness-capacity proof; independent review OPEN |
| `a=14` high-b family | `a=14,b>=17 => t<=1`; `a=14,b>=20 => t<=0` | [source package](general-stepback-v1/README.md) | [exact boundary verifier](../project/research/general_n/2026-09-12-a14-high-b-v1/check_a14_high_b.py) | **New infinite-family candidate**; one common graph-level potential + hand boundary cases; independent review OPEN |
| fifteen-label tail | `a=15 => Q<=26`, equality `3^2 4^13` or `4^15`; hence `b+2t<=26` | [source package](general-stepback-v1/README.md) | [exact checker](../project/research/general_n/2026-09-12-fifteen-label-tail-v1/check_fifteen_label_tail.py) | candidate structural theorem; exhaustive 77,558,760-profile scan retained as corroboration only; independent review OPEN |
| sixteen-label tail | `a=16 => Q<=29`, equality `4^16` or `5^16`; hence `b+2t<=29` | [source package](general-stepback-v1/README.md) | [exact checker](../project/research/general_n/2026-09-12-sixteen-label-tail-v1/check_sixteen_label_tail.py) | candidate structural theorem; first safe-clipping obstruction beyond this range explicitly documented; independent review OPEN |
| joint tail bounds a=17..23 | sharp Q bounds `32,35,39,42,46,49,54`; compatible-tail recurrence and adaptive terminal cap | [source package](general-joint-clipping-reviewer-v1/README.md) | [independent integer verifier](../project/research/general_n/2026-09-12-joint-clipping-v1/verify_joint_clipping.py) | candidate structural bounds; finite arithmetic proof-critical; independent review OPEN |
| tight total-demand threshold | if all demands >=h and `S=C_h(z_h)`, then `b+2t<=h(h+1)` | [hand lemma](../project/research/general_n/2026-09-12-joint-clipping-v1/TIGHT_THRESHOLD_LEMMA.md) | [foundations audit](../project/reviews/general-theory/2026-09-12-joint-followthrough-v1/FOUNDATIONS_AUDIT.md) | candidate universal bridge consequence; independent review OPEN |
| n=34 | `e(G)<=289`, equality exactly `K(17,17)` | [reviewer-v1](n34-reviewer-v1/README.md) | [solver-free verifier](../project/research/n34/2026-09-12-equality-v1/verify.py); [internal audit](../project/research/n34/2026-09-12-equality-v1/AUDIT.md) | Complete candidate: all 13,546 equality states excluded; external review OPEN |
| general-293-500 | `n >= 6 and Delta(G) >= (293/500)n imply e(G) < floor(n^2/4)` | [PDF](general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [PDF](general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) | retained candidate hand argument; superseded in threshold strength by 7/12; independent review OPEN |
| general-7-12 | `n >= 6 and Delta(G) >= (7/12)n imply e(G) < floor(n^2/4)` | [PDF](general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [PDF](general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) | complete candidate hand argument; internal exact audits green; independent review and novelty assessment OPEN |
| general-13-22 | `n >= 6 and Delta(G) >= (13/22)n imply e(G) < floor(n^2/4)` | [PDF](general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [PDF](general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) | retained candidate hand proof; independent mathematical review OPEN |

## Scope rule

This index covers the project's current **theorem-level candidate claims**: fixed-order bound-and-equality candidates at `n=25,27,28,29,30,31,32,33,34`; retained general maximum-degree candidates `13/22`, `293/500`, `7/12`; and the new step-back structural candidates above. The 7/12 profile-integral strengthening remains the strongest current broad maximum-degree threshold. The balanced-degree theorem is a different all-order reduction at the minimum possible dense maximum degree. The `a=14`, fifteen-label and sixteen-label results operate in fixed complement-minimum-degree bands.

The ongoing RX-Hall / monotone-potential programme is not an unrestricted theorem, although compact exact potential certificates are proof-critical in the N32/N33 packages and in the `a=14` boundary theorem.

The joint-clipping continuation adds fixed-a scalar results through a=23.
The [N34 reviewer-v1 package](n34-reviewer-v1/README.md) now gives the complete
candidate bound 289 and equality exactly K(17,17). Its new
[source-capped threshold lemma](../project/research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
and explicit heavy-degree transport extend the general bridge machinery.
The [bound-only package](n34-bound-reviewer-v1/README.md) and
[joint-clipping package](general-joint-clipping-reviewer-v1/README.md) preserve
the preceding upper-bound checkpoints and remain dependencies.

No item in this index is represented as externally accepted. Same-assistant independent implementations are not external independent verification.

## Fixed-order history note

The current project fixed-order candidates do not use Fan's 1987 density theorem as a logical dependency at `n=25,27,28,29,30,31,32,33,34`. Direct Fan-free replacements were constructed for `n=25..30`; N31..34 were assembled without invoking Fan's theorem in the first place. All earlier packages and workflows remain preserved as corroborating evidence and audit history.
