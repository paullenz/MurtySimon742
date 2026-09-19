# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E2_SHARED_CORE_WITNESS_SEPARATION_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `b544edde936319444b04fa0799db6dcd90fc2ba1`

LAST VERIFIED RESULT: `The exact E=2,k>=3 support classification and shared-core R2+R2 pair pinch have now been pushed to selected-witness geometry. General E2 support channels obey J<=d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+), B=s-c+q, K=k(c-d0), with the closed topology-retaining Phi pair correction. R3 has automatic all-positive X-edge Hamming excess; R2+R2 has zero-rho edges only on defect-to-radius-one support pairs. The unique deepest pair-cheap R2+R2 topology for all k>=3 is h=1,c=2,d0=2. At t=1 its deep pair bill is p^2+M-k-8<=C0-sigma_P and M_+=C0-sigma_P-p^2+k+8. Throughout this shared-core arm star separation removes all 2k defect-core zero-rho edges, so r>=a+y+2+eta_2([e(X)-2]_+). On D<=-6 with pair slack s_P<=1, all three bidirected channels are active, every X-edge is positive-Hamming, Delta<=floor((s_P-D)/2), and r>=a+y+2+eta_2([Emax-floor((s_P-D)/2)]_+). The new physical refinement is that Jmax-J<=1 forces each defect witness to meet a core head; the core singleton certificate then forces both defect witnesses nonadjacent to z_*, so M>=2. Each of the three active singleton-type channels also forces the corresponding two selected outside witnesses nonadjacent, giving three additional distinct U_o nonedges and q<=binom(u,2)-binom(k+1,2)-k-M-3. Bounded replay: 49 exact/one-unit shared-core endpoint states shrink to 39 after M>=2; exact equality shrinks 48->38. The additional q-3 alone closes no further bounded states, showing that the next useful step must exploit the locations/certificates of these witness nonedges rather than another scalar q subtraction. These are abstract parameter states, not graph counts.`

UNPRESERVED WORK: `None. Exact E2 support classification is under project/research/post_ms/2026-09-19-e2-exact-support-v1/. Shared-core pair pinch and its checker are under project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/. The selected-witness separation theorem and an exact JSON ledger of the 39 remaining bounded exact/near states are preserved in the same shared-core package. No graph-realizability or global eventual claim is promoted.`

DEFERRED ADMIN: `README remains synchronized to the 19 September audit trust boundary and is intentionally lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1,k>=3 and the exact/one-unit shared-core R2+R2 endpoint. Do not spend the next run on another scalar residual inequality: q-3 has already been tested and is too weak. Instead exploit the physical placement of the five newly explicit U-pair nonedges—z_* misses both defect witnesses and the three active support channels separate their selected witness pairs. Trace raw criticality for those witness-witness nonedges/adjacent head pairs and seek forced A/U holes, unmatched slack, or Hall-slot conflicts. Use the preserved 39-state JSON ledger as a diagnostic target, but derive graph lemmas first. Only if this endpoint survives should the 16 non-near shared-core routes be opened, then alternate R2+R2/R3. Keep k=2,k=1,m=g+2,loaded buffer,z=2,and the four-exception gate deferred. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

This run began by rereading `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily adversarial audit, `SOURCE_PREMISE_REPAIR.md`, and `RIGID_GRAPH_LEVEL_REGRESSION.md` before forward mathematics.

Binding trust boundary:

- distinct physical beta-source identity: raw-criticality proved;
- `(source,coordinate)` uniqueness: selected representative only;
- finite source-tuple theorem: not unconditional graph-level closure;
- actual-D2C regression: 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall decompositions, zero mismatches, `X_3` retained;
- no bounded actual D2C fixture realizes the full rigid complete-cut hypotheses, so the live branch remains conditional hand mathematics;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- four-exception gate remains subordinate.

No departure from the audit's priority order occurred.

---

## 2. E2 support classification retained

For `m=g+1,t=1,k>=3`, exact `E=2` has only:

1. R3: one radius-three singleton matched-head defect;
2. R2+R2: two radius-two singleton matched-head defects.

With support parameters `s,q,c,d0`, put `B=s-c+q`, `K=k(c-d0)`. Then

`J<=d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+)`.

The exact pair correction is

`Phi_{B,0}(D)=max(D,-2B)`;

for `K>0`,

`Phi=max(D,-2B)` if `D>=-2B-1`,

`Phi=max(ceil(D/2)-B,-(2B+K))` if `D<=-2B-2`.

Hence

`p(g+1)+k+M-d0(k+1)+Phi<=C0-sigma_P`.

R3: every actual X-edge positive-Hamming.

R2+R2: only defect-to-radius-one support edges can have zero Hamming excess.

---

## 3. Shared-core topology

For R2+R2,

`Jmax=8+2h+c(k-2)+d0`.

For all `k>=3`, the unique maximum is

`h=1,c=2,d0=2`.

Thus the two radius-two defects share the repeated-core coordinate and `z_*` is adjacent to both defect heads. Here

`B=3`, `K=0`, `A=g-2`, `Jmax=2k+8`.

At `t=1`,

`p^2+M-k-2+max(D,-6)<=T`, `T=C0-sigma_P`.

Deep arm `D<=-6`:

`p^2+M-k-8<=T`,

`M_+=T-p^2+k+8`.

---

## 4. Rooted-slot pinch

Star separation deletes all `2k` defect-core zero-Hamming edges. Only two private defect-to-radius-one support edges can remain zero-Hamming, so universally

`r>=a+y+2+eta_2([e(X)-2]_+)`.

On `D<=-6` with pair slack

`s_P=T-(p^2+M-k-8)<=1`,

we have

`[D+2Delta]_+ + (Jmax-J)<=s_P`.

No bidirected channel can be absent, so both private zero-Hamming edges are also absent. Every X-edge is positive-Hamming and

`Delta<=floor((s_P-D)/2)`.

With

`Emax=binom(g,2)+k(g-2)`,

`r>=a+y+2+eta_2([Emax-floor((s_P-D)/2)]_+)`.

`M=M_+` is exact pair equality; `M=M_+-1` is one-unit near equality.

---

## 5. New selected-witness separation

Let defect heads be `h_1,h_2`, defect witnesses `z_1,z_2`, and common core witness `z_*`.

Since `Jmax-J<=1` and `k>=3`, neither defect witness can miss all `k` reverse core incidences. Thus each `z_i` is adjacent to at least one core head `x_i`.

The core certificate is

`N(x_i) cap N(z_*)={b}`.

Therefore `z_i z_*` must be absent, or `z_i` would be a second common neighbour. Hence

`z_1 z_* notin E`, `z_2 z_* notin E`,

so

`M>=2`.

For any active singleton-type channel between heads `h_s,h_t`, with selected witnesses `z_s,z_t`, one direction `z_s~h_t` plus

`N(h_t) cap N(z_t)={b}`

forces `z_s z_t` absent.

All three bidirected channels are active when `s_P<=1`; therefore three additional distinct U_o witness-witness nonedges are forced. They are outside the generic independent-U_- / z_*--W_0 / M counts, so

`q<=binom(u,2)-binom(k+1,2)-k-M-3`.

---

## 6. Bounded diagnostic

Previous no-E1 t=1 states: `933`.

Current k>=3 frontier within them: `509`.

Safe shared-core route before exact/near restriction: `65`.

Exact-or-one-unit deep endpoint before witness separation: `49`; exact: `48`.

After the newly proved `M>=2` condition:

- exact-or-one-unit: `39`;
- exact: `38`.

Near by-k:

`k=3:15, 4:9, 5:11, 6:4`.

Exact by-k:

`k=3:15, 4:9, 5:11, 6:3`.

The extra `q-3` gives no further state closure on the bounded box. This negative diagnostic is preserved and redirects the next attack toward the locations of the forced nonedges rather than their scalar count.

Exact diagnostic state/row ledger:

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/WITNESS_SEPARATION_ENDPOINT_LEDGER.json`.

---

## 7. Preserved files

`project/research/post_ms/2026-09-19-e2-exact-support-v1/EXACT_E2_SUPPORT_CHANNELS.md`

`project/research/post_ms/2026-09-19-e2-exact-support-v1/check_e2_support_channels.py`

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/SHARED_CORE_R22_PAIR_PINCH.md`

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/check_shared_core_r22_pair_pinch.py`

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/SHARED_CORE_WITNESS_SEPARATION.md`

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/WITNESS_SEPARATION_ENDPOINT_LEDGER.json`

All checkers/ledgers are abstract arithmetic/topology diagnostics, not D2C graph enumeration.

---

## 8. Next work

Attack the physical witness-nonedge pattern at raw criticality level. The scalar rooted budget still has substantial room; the next gain must come from proving that these specifically located U-o nonedges force additional A/U holes, matched-foot restrictions, or unmatched slack.

Do not open broader branches until this endpoint has been exhausted.
