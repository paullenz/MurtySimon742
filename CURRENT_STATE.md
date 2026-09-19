# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_T1_EXCEPTIONAL_GAMMA_FOOT_COLLAPSE_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `924f98f78cee240df3b5b87ab9a07eaa9f53f07c`

LAST VERIFIED RESULT: `Raw triangle-edge criticality of every selected outside-witness wrong-head edge gives a secondary matched foot q with gamma(q)=target code and with q lying in a support coordinate of the source head. Therefore wrong-head traffic can use only tight fibres whose gamma pair is not P={d,bar d}. At t=p-g_P=1 there is one exceptional coordinate e and every wrong-head edge in the entire minimal reservoir has source support containing e and the same graph-fixed target code c_e=gamma(q_e^d). This immediately kills the predecessor's shared-core R2+R2 d0=2 endpoint: the core witness has one-coordinate support and cannot meet two distinct defect codes. A complete E2 support case split shows the sharp t=1 traffic hierarchy: shared-core R2+R2 has J<=2k, uniquely at e=the repeated-core coordinate and target=the repeated core code, hence d0=0; one-core R2+R2 and core-containing R3 have J<=k; the remaining topologies have J<=2 or 1. Independently, raw criticality of every X-edge also forces a matched foot in the unique exceptional gamma fibre, so the exceptional gamma pair is a vertex cover of G[X]. In shared-core R2+R2 no two represented X-codes are complementary; a fixed exceptional-code vertex can use only one singleton head with its unique matched foot. Hence e(X)<=k, A>=g-1 and Delta>=binom(g,2)+kA-k. The corrected exact pair-local necessary condition is p^2+M-k+[D+2(binom(g,2)+kA-k)]_+<=C0-sigma_P, A in {g-1,g}. The old 39 exact/near d0=2 endpoint rows are not survivors; their topology is impossible.`

UNPRESERVED WORK: `None at this checkpoint. The new theorem and independent support/arithmetic checker are preserved under project/research/post_ms/2026-09-19-exceptional-gamma-foot-v1/. The old 39-row ledger remains preserved only as a superseded historical diagnostic.`

DEFERRED ADMIN: `README remains synchronized to the 19 September audit trust boundary and is intentionally lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1,k>=3,E=2. Do not return to the impossible d0=2 five-U-nonedge endpoint. Attack the corrected shared-core R2+R2 d0=0 exceptional-fibre geometry: e is the repeated-core coordinate, c_e is the core code, all wrong-head traffic is defect-witness-to-core, H_M is forced sparse and e(X)<=k. Intersect the new pair-local gate with the exact rooted residual/slot ledger and classify equality in e(X)<=k before opening the J<=k R2+R2/R3 alternatives. Keep k=2,k=1,m=g+2,loaded buffer,z=2,and the four-exception gate deferred. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

This run began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, and the independent actual-D2C graph regression before forward mathematics.

Binding trust boundary:

- distinct physical beta-source identity: raw-criticality proved;
- `(source,coordinate)` uniqueness: selected representative only;
- finite source-tuple theorem: not unconditional graph-level closure;
- actual-D2C regression: 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall decompositions, zero mismatches, `X_3` retained;
- no bounded actual D2C fixture realizes the full rigid complete-cut hypotheses, so the live branch remains conditional hand mathematics;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- four-exception gate remains subordinate.

There is no departure from the audit priority order. The predecessor explicitly asked for raw criticality on the physical selected-witness pattern; the present matched-foot collapse is exactly that repair path.

---

## 2. Superseded predecessor endpoint

The predecessor's exact/one-unit shared-core R2+R2 endpoint used

`h=1,c=2,d0=2`,

with the common core witness adjacent to both distinct defect heads, and produced 39 bounded parameter states after `M>=2`.

That topology is now impossible.

For an active wrong-head edge `z_s h_t`, triangle-edge criticality leaves only a matched witness `q`; generalized matched-foot localization gives

`gamma(q)=c(h_t)`,

and `q!~b` forces q to be the d-selected endpoint in a support coordinate of the source head.

The core witness has a one-coordinate support. One matched endpoint has one fixed gamma code, so it cannot support adjacency to two distinct defect codes. Thus `d0<=1`.

Do not reuse the old `p^2+M-k-8` endpoint as a live equality model.

---

## 3. Exceptional-fibre localization

Let `P={d,bar d}`. By definition `g=g_P` is the number of tight fibres whose two gamma codes form P.

Every wrong-head edge requires a matched foot with gamma equal to an X-code, while X contains neither d nor bar d. Hence wrong-head traffic can use only the `t=p-g` exceptional gamma fibres.

At `t=1`, with exceptional coordinate e,

- every emitting source code support contains e;
- every wrong head has the one fixed code `c_e=gamma(q_e^d)`.

Thus all selected-witness wrong-head traffic globally targets one code class.

---

## 4. Correct E2 traffic hierarchy at t=1

For `k>=3`:

### R2+R2

`(h,c)=(1,2): J<=2k`;

`(1,1)` or `(0,1): J<=k`;

`(1,0): J<=2`;

`(0,0): J<=1`.

The unique `2k` maximum is the shared-core topology with the exceptional coordinate equal to the repeated-core coordinate and the exceptional d-endpoint gamma equal to the core code. Therefore the pair-cheapest shared-core orientation has

`d0=0`, not `d0=2`.

### R3

core coordinate present: `J<=k`;

core coordinate absent: `J<=1`.

The shared-core R2+R2 family therefore remains the first E2 target, but with completely corrected physical orientation.

---

## 5. Exceptional gamma pair controls all X-edges

Any edge `xy` of G[X] lies in triangles through b and Y. The same location classification as in the zero-buffer X-edge theorem leaves only a matched critical foot q. Generalized matched-foot localization gives one endpoint code equal to `gamma(q)`.

At t=1, q lies in the unique exceptional gamma fibre. Hence every X-edge has an endpoint whose code belongs to the exceptional gamma pair `P_e`.

In shared-core R2+R2 no two represented X-codes are complementary. Therefore `P_e` meets X in at most one code class. For a represented exceptional code c, there is one matched endpoint q_c with gamma c; a fixed pair `(x,q_c)` can have only one singleton common-neighbour head. Hence every exceptional-code X-vertex has X-degree at most one.

The largest X-code class is H0 of size k, so

`e(X)<=k`.

Also the core witness can have at most one wrong H_M neighbour, so

`A>=g-1`.

With

`Emax(A)=binom(g,2)+kA`,

we have

`Delta>=binom(g,2)+kA-k`.

---

## 6. Corrected pair-local gate

The preserved minimal-reservoir decomposition gives

`sum epsilon_selected >= p(g+1)+k+M-J`,

`L_X >= [D+2Delta]_+`.

At t=1, `g=p-1`, so `p(g+1)=p^2`. Using `J<=2k` and the new density floor gives

`p^2+M-k+[D+2(binom(g,2)+kA-k)]_+ <= C0-sigma_P`,

with `A in {g-1,g}`.

This keeps the exact pair-local sigma/Ccap budget and is the live gate to feed into the rooted residual ledger.

---

## 7. Preserved package

`project/research/post_ms/2026-09-19-exceptional-gamma-foot-v1/EXCEPTIONAL_GAMMA_FOOT_COLLAPSE.md`

`project/research/post_ms/2026-09-19-exceptional-gamma-foot-v1/check_exceptional_gamma_foot.py`

The checker exhausts only the small E2 support/exceptional-coordinate system and audits the displayed topology hierarchy. It is not D2C graph enumeration and is not part of the raw criticality proof.

The predecessor files and 39-state endpoint ledger remain in

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/`

for audit history, but the `d0=2` endpoint is superseded.

---

## 8. Next work

Remain on the corrected `t=1,E=2,k>=3` shared-core family. The next structural question is equality/stability in `e(X)<=k`: identify the allowed matching-like X geometry, feed its exact missing-edge count through the Hall and rooted slot ledgers, and use raw criticality of the remaining X-edges before opening any broader support topology.
