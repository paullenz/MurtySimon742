# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around `M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 D2C graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control. The mixed `{4,5}` selected-excess ladder is closed. First-proof priority on Erdős #742 is not an optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_MINIMAL_RESERVOIR_E2_SHARED_CORE_PINCH_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `3e84858a2991c7f031400beaac7ec05f6baea118`

LAST VERIFIED RESULT: `The E=2,k>=3 exact support classification has been pushed through the unique deepest pair-cheap R2+R2 topology. The general E2 channel ledger is J<=d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+), B=s-c+q, K=k(c-d0), with exact pair correction Phi_{B,0}=max(D,-2B); for K>0, Phi=max(D,-2B) for D>=-2B-1 and Phi=max(ceil(D/2)-B,-(2B+K)) for D<=-2B-2. R3 has automatic all-positive X-edge Hamming excess. For R2+R2 the only zero-rho edges are defect-to-radius-one support edges. The unique Jmax topology for every k>=3 is h=1,c=2,d0=2: the two radius-two defects share the repeated-core coordinate and the common core witness meets both. Here B=3,K=0,A=g-2 and at t=1 the pair gate is p^2+M-k-2+max(D,-6)<=C0-sigma_P, with deep arm p^2+M-k-8<=C0-sigma_P and endpoint M_+=C0-sigma_P-p^2+k+8. Star separation already removes all 2k defect-core zero-rho edges, so throughout this shared-core arm at most two zero-rho X-edges remain and r>=a+y+2+eta_2([e(X)-2]_+). On D<=-6 with pair slack s_P<=1, all three bidirected channels must be active; hence both remaining private zero-rho edges are absent, every actual X-edge has positive Hamming excess, Delta<=floor((s_P-D)/2), and r>=a+y+2+eta_2([Emax-floor((s_P-D)/2)]_+). Thus M=M_+ and M=M_+-1 are literal support-saturation/near-saturation rows. Bounded replay reproduces the 5,404 t=1 pair/Hall states and 933 no-E1 states; 509 have k>=3. Only 65/509 retain even a safe relaxed route through this shared-core topology after the exact pair gate plus physical rooted-slot upper budget; 48 of those have an exact deep route and 49 an exact-or-one-unit deep route. This is diagnostic parameter-state evidence only, not graph counts or a union closure.`

UNPRESERVED WORK: `None. Exact E2 support classification is preserved under project/research/post_ms/2026-09-19-e2-exact-support-v1/. The shared-core exact/near pair pinch and bounded independent replay are preserved under project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/. No graph-realizability or global eventual claim is promoted.`

DEFERRED ADMIN: `README remains synchronized to the 19 September audit trust boundary and is intentionally lower-frequency. Refresh reviewer-facing status at the next daily adversarial checkpoint unless repository integrity requires earlier repair.`

NEXT ACTION: `Stay on m=g+1,t=1,k>=3 and remain inside the shared-core R2+R2 family before opening alternate topologies. First attack the exact/one-unit endpoint family (49 bounded diagnostic states) structurally: use the literal nonedge pattern—both defects anticomplete to H0, both private support edges absent, overlap-channel defect edge absent when active, all surviving X-edges positive-Hamming—together with the exact Hall-cut identity and physical q/E_U allocation. Retain M=M_+ or M_+-1 and pair-local sigma_P. Seek a compact contradiction or equality classification, not another total-score relaxation. If the endpoint survives, classify the 16 bounded shared-core routes requiring larger pair slack/nondeep D. Only then open other R2+R2 topologies or R3 near equality. Do not open k=2,k=1,m=g+2,loaded buffer,z=2,or the four-exception gate while this line remains live. Keep X_3 and the graph-level audit boundary explicit.`
<!-- CURRENT-STATUS:END -->

---

## 1. Mandatory audit gate

Before forward mathematics this run reread:

- `CURRENT_STATE.md`;
- root `README.md`;
- latest commits through `b5be3a06e7d197cdf9931883a714ca9d4e25c599`, then preserved the first E2 classification at `3e84858a2991c7f031400beaac7ec05f6baea118` before continuing the same coherent line;
- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`;
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`;
- `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit requirements remain binding:

- distinct physical beta-source identity is established from raw singleton criticality;
- selected `(source,coordinate)` uniqueness is a one-selected-representative statement, not raw witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression retains `X_3`, recorded 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall-cut decompositions and zero graph/formula mismatches;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so this branch remains a conditional hand implication;
- exact pair-local `S_P/Ccap_P` remains mandatory;
- the four-exception gate remains subordinate.

There is no departure from the audit's priority order.

---

## 2. Exact E2 support theorem retained

For `m=g+1,t=1,k>=3`, total Hamming excess `E=2` has only:

1. `R3`: one radius-three singleton matched-head defect;
2. `R2+R2`: two radius-two singleton matched-head defects.

For a support topology define `s,q,c,d0`, then

`B=s-c+q`, `K=k(c-d0)`.

The selected outside-witness wrong-head incidence count satisfies

`J<=d0(k+1)+2min(Delta,B)+min(K,[Delta-B]_+)`.

The exact Hall-minus-channel correction is

`Phi_{B,0}(D)=max(D,-2B)`,

and, for `K>0`,

`Phi=max(D,-2B)` for `D>=-2B-1`,

`Phi=max(ceil(D/2)-B,-(2B+K))` for `D<=-2B-2`.

Hence

`p(g+1)+k+M-d0(k+1)+Phi_{B,K}(D)<=C0-sigma_P`.

R3 has every actual X-edge positive-Hamming. In R2+R2 the only possible zero-Hamming X-edges are defect-to-radius-one head edges on defect support coordinates.

Primary note: `project/research/post_ms/2026-09-19-e2-exact-support-v1/EXACT_E2_SUPPORT_CHANNELS.md`.

---

## 3. Shared-core / double-active topology

For R2+R2,

`Jmax=8+2h+c(k-2)+d0`.

For every `k>=3` this is uniquely maximized by

`h=1,c=2,d0=2`.

The two radius-two defects share the repeated-core coordinate and the common core witness is adjacent to both.

Then

`B=3`, `K=0`, `A=g-2`, `Jmax=2k+8`.

At `t=1`,

`p^2+M-k-2+max(D,-6)<=T`, `T=C0-sigma_P`.

On `D<=-6`,

`p^2+M-k-8<=T`,

so

`M_+=T-p^2+k+8`.

---

## 4. Universal two-zero-edge theorem

Star separation from the two active core channels deletes all `2k` defect-core zero-Hamming edges.

The R2+R2 Hamming classification leaves only the two private defect-to-radius-one support edges as possible zero-Hamming edges.

Therefore

`j_+>=[e(X)-2]_+`,

and

`r>=a+y+2+eta_2([e(X)-2]_+)`.

This holds throughout the shared-core arm, with no pair-equality assumption.

---

## 5. Exact / one-unit pair endpoint theorem

On the deep arm define pair slack

`s_P=T-(p^2+M-k-8)`.

The excess above the pair minimum is

`[D+2Delta]_+ + (Jmax-J)<=s_P`.

If `s_P<=1`, no bidirected channel can be completely inactive because that would lose two incidences. Thus all three bidirected channels are active. One active direction already forces the corresponding head edge absent.

Consequently both private zero-Hamming edges are absent and every actual X-edge has positive Hamming excess.

Also

`Delta<=floor((s_P-D)/2)`.

With

`Emax=binom(g,2)+k(g-2)`,

this yields

`r>=a+y+2+eta_2([Emax-floor((s_P-D)/2)]_+)`.

At `M=M_+`, `s_P=0`; at `M=M_+-1`, `s_P=1`.

---

## 6. Rooted residual intersection

The exact rooted identity remains

`r=(p-lambda)(p+u)+q+E_U`.

The bounded replay retains the physical row ceilings

`q<=binom(u,2)-binom(k+1,2)-k-M`

and the corresponding `E_U` score/Hall ceiling. Thus the slot theorem is compared directly against an upper bound on the actual rooted residual rather than another global score relaxation.

---

## 7. Bounded diagnostic

Same abstract box as the predecessor:

- t=1 pair/Hall states: `5,404`;
- no support-capped E1 route: `933`;
- k>=3 among those: `509`.

No-E1 k-distribution:

`k=1:223, 2:201, 3:146, 4:104, 5:82, 6:60, 7:53, 8:47, 9:17`.

Safe shared-core route after exact pair gate + universal shared-core slot floor + physical rooted upper budget:

- total `65/509`;
- `k=3:23, 4:15, 5:17, 6:6, 7:4`;
- none for `k>=8` on this bounded box.

Deep exact pair route satisfying all-positive slot floor:

- total `48`;
- `k=3:23, 4:11, 5:11, 6:3`.

Deep exact-or-one-unit route:

- total `49`;
- `k=3:23, 4:11, 5:11, 6:4`.

These are abstract parameter states, not graph counts and not a global branch closure. The `444` k>=3 no-E1 states without a shared-core route may use R3 or another R2+R2 topology.

---

## 8. Preserved packages

Exact E2 support classification:

`project/research/post_ms/2026-09-19-e2-exact-support-v1/`

Shared-core pinch:

`project/research/post_ms/2026-09-19-e2-shared-core-pinch-v1/`

The companion checkers are arithmetic/topology diagnostics only.

---

## 9. Next work

Stay inside the exact/one-unit shared-core endpoint family first.

Use the literal missing-edge geometry, exact Hall decomposition, `M=M_+` or `M_+-1`, and the rooted `q/E_U` identity to seek a compact structural contradiction or equality classification. Do not replace these by a new total-score scalar inequality.

Only if that endpoint family survives should the 16 non-near shared-core routes be opened; after that, alternate R2+R2 support topologies and R3 near equality. Keep k=2/k=1 and all larger-reservoir/buffer/z/four-exception branches deferred.
