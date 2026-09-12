# Review-ready proof index
Updated 12 September 2026. This index identifies the canonical reviewer-facing paper or source package for every current theorem-level candidate claim in the top-level project status. Historical failed or superseded development checkpoints remain preserved rather than silently rewritten.

The current fixed-order PDF packages are Fan-free reviewer-v2 at `n=25,27,28`, **reviewer-v4 at `n=29`**, and **reviewer-v3 at `n=30`**. Source-first reviewer-v1 packages cover `n=31,32,33,35`, with reviewer-v2 at `n=34`; complete candidate bound and equality classification now reach n=35. The 12 September step-back programme also has a source-first general-theory package collecting the new balanced-degree, `a=14`, fifteen-label and sixteen-label structural results.

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
| n=34 | `e(G)<=289`, equality exactly `K(17,17)` | [reviewer-v2](n34-reviewer-v2/README.md) | [v2 replay](../project/reviews/n34/2026-09-12-heavy-independent-v1/verify_v2.py); [normalization audit and hand replacement](../project/reviews/n34/2026-09-12-heavy-independent-v1/README.md) | Complete candidate: 6,709 hand/accounting and 6,837 envelope exclusions; external review OPEN |
| n=35 | `e(G)<=306`, equality exactly `K(17,18)` | [reviewer-v1](n35-reviewer-v1/README.md) | [exact replay](../project/research/n35/2026-09-12-candidate-v1/verify.py); [internal audit](../project/research/n35/2026-09-12-candidate-v1/AUDIT.md) | Complete candidate: all 485 new states excluded; 92,701 local integer checks; external review OPEN |
| Heavy-load / routing family | All-threshold inequalities with incoming-degree penalties; `s_i<=2, t>0, b-a<=5 => 9t+4(b-a)<=a` | [reviewer-v1](general-heavy-load-reviewer-v1/README.md) | [hand proof](../project/research/general_n/2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md); [internal audit](../project/research/general_n/2026-09-12-heavy-load-family-v1/AUDIT.md) | Candidate structural family; 595 alternative envelope exclusions and 45 rejected layer/profile instances; complete survivors and failed extensions preserved; external review OPEN |
| Joint heavy routing | General count-conditioned load inequality using destination indegrees and unordered-pair capacity | [reviewer-v1](general-joint-routing-reviewer-v1/README.md) | [hand lemma](../project/research/general_n/2026-09-12-joint-routing-pilot-v1/JOINT_ROUTING_LEMMA.md); [audit](../project/research/general_n/2026-09-12-joint-routing-pilot-v1/AUDIT.md) | Candidate structural lemma; 729 further exact exclusions from 6,307 eligible cases, 5,578 catalogue survivors; comparison correction and all failed attempts preserved; external review OPEN |
| Demand/tail projection and equality rigidity | Residual-budget tail bounds, demand-only joint routing, and a closed strictness criterion for the load inequality | [reviewer-v1](general-routing-tail-reviewer-v1/README.md) | [tail projection](../project/research/general_n/2026-09-12-routing-tail-projection-v1/TAIL_PROJECTION.md); [equality lemma](../project/research/general_n/2026-09-12-routing-tail-projection-v1/EQUALITY_BOUNDARY.md); [audit](../project/research/general_n/2026-09-12-routing-tail-projection-v1/AUDIT.md) | Candidate general lemmas; 114 further whole-profile exclusions, zero further exclusions among 5,578 previous state survivors; external review OPEN |
| Compatible destination routing | General selected-degree eligibility tails, mixed traffic cuts and count-conditioned potential envelope | [reviewer-v1](general-compatible-routing-reviewer-v1/README.md) | [hand example](../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/COMPACT_EXAMPLE.md); [audit](../project/research/general_n/2026-09-12-compatible-routing-pilot-v1/AUDIT.md) | Candidate general inequalities; 19/29 preselected pilot exclusions, 16 beyond selected-degree retention; mixed cuts add zero further states; full-pool continuation below; external review OPEN |
| Compatible routing: full catalogue and analytic reduction | Fixed eligible-routing potentials; exact q elimination and at most five p candidates per H for the recurring potential | [reviewer-v1](general-compatible-catalogue-reviewer-v1/README.md) | [hand reduction](../project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/FIXED_POTENTIAL.md); [audit and replay](../project/research/general_n/2026-09-12-compatible-routing-catalogue-v1/README.md) | Candidate general reduction; 990 catalogue exclusions plus four inherited pilot-only witnesses, 4,584 combined survivors; no per-state fitting; external review OPEN |
| general-293-500 | `n >= 6 and Delta(G) >= (293/500)n imply e(G) < floor(n^2/4)` | [PDF](general-293-500-reviewer-v1/General_293_500_Reviewer_Manuscript_v1.pdf) | [PDF](general-293-500-reviewer-v1/General_293_500_Verification_Companion_v1.pdf) | retained candidate hand argument; superseded in threshold strength by 7/12; independent review OPEN |
| general-7-12 | `n >= 6 and Delta(G) >= (7/12)n imply e(G) < floor(n^2/4)` | [PDF](general-7-12-reviewer-v1/General_7_12_Reviewer_Manuscript_v1.pdf) | [PDF](general-7-12-reviewer-v1/General_7_12_Verification_Companion_v1.pdf) | complete candidate hand argument; internal exact audits green; independent review and novelty assessment OPEN |
| general-13-22 | `n >= 6 and Delta(G) >= (13/22)n imply e(G) < floor(n^2/4)` | [PDF](general-13-22-reviewer-v1/General_13_22_Reviewer_Manuscript_v1.pdf) | [PDF](general-13-22-reviewer-v1/General_13_22_Verification_Companion_v1.pdf) | retained candidate hand proof; independent mathematical review OPEN |

## Scope rule

This index covers the project's current **theorem-level candidate claims**: fixed-order bound-and-equality candidates at `n=25,27,28,29,30,31,32,33,34,35`; retained general maximum-degree candidates `13/22`, `293/500`, `7/12`; and the new step-back structural candidates above. The 7/12 profile-integral strengthening remains the strongest current broad maximum-degree threshold. The balanced-degree theorem is a different all-order reduction at the minimum possible dense maximum degree. The `a=14`, fifteen-label and sixteen-label results operate in fixed complement-minimum-degree bands.

The ongoing RX-Hall / monotone-potential programme is not an unrestricted theorem, although compact exact potential certificates are proof-critical in the N32/N33 packages and in the `a=14` boundary theorem.

The joint-clipping continuation adds fixed-a scalar results through a=23.
The [N34 reviewer-v2 package](n34-reviewer-v2/README.md) now gives the complete
candidate bound 289 and equality exactly K(17,17). Its new
[source-capped threshold lemma](../project/research/general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
and the [general heavy-load/routing family](general-heavy-load-reviewer-v1/README.md)
extend the general bridge machinery. The original p<=4 hand theorem remains
preserved; the new family strengthens it and adds demand-only consequences.
Its measured alternative exclusions do not change the fixed-order ledgers.
The [N35 reviewer-v1 package](n35-reviewer-v1/README.md) now completes the
candidate bound 306 and equality K(17,18), with all 485 new states excluded.
The [bound-only package](n34-bound-reviewer-v1/README.md) and
[joint-clipping package](general-joint-clipping-reviewer-v1/README.md) preserve
the preceding upper-bound checkpoints and remain dependencies.

No item in this index is represented as externally accepted. Same-assistant independent implementations are not external independent verification.

The [joint-routing continuation](general-joint-routing-reviewer-v1/README.md)
adds destination congestion to the general load argument. Its 729 alternative
exclusions leave the canonical fixed-order ledgers unchanged. The corrected
comparison pool, full survivors and failed variants are preserved.

The [demand/tail continuation](general-routing-tail-reviewer-v1/README.md)
simplifies that mechanism and extracts a closed equality criterion. Its
114 whole-profile exclusions do not reduce the prior 5,578-state remainder.
The zero additional-state result and all counterexamples are preserved.

The [compatible-routing continuation](general-compatible-routing-reviewer-v1/README.md)
retains selected-degree destination eligibility. Its 29-state pilot gives
19 exact exclusions and ten survivors, with sixteen exclusions attributable
to eligibility beyond selected-degree retention. Mixed cuts add no further
whole-state exclusions. A compact hand example and the complete negative
record accompany that bounded pilot.

The [full-catalogue continuation](general-compatible-catalogue-reviewer-v1/README.md)
now tests all 5,578 preceding survivors with frozen weights. Its 990 exclusions
plus four retained pilot-only witnesses leave 4,584 combined survivors. The
recurring hand-example potential handles 707 cases and has an exact analytic
reduction of its local maxima. This gives new structural explanations within
the existing fixed-order candidates; their ledgers and the 7/12 threshold are
unchanged. All gaps, failed attempts, inherited witnesses and survivors are
preserved; external review remains OPEN.

## Fixed-order history note

The current project fixed-order candidates do not use Fan's 1987 density theorem as a logical dependency at `n=25,27,28,29,30,31,32,33,34,35`. Direct Fan-free replacements were constructed for `n=25..30`; N31..35 were assembled without invoking Fan's theorem in the first place. All earlier packages and workflows remain preserved as corroborating evidence and audit history.
