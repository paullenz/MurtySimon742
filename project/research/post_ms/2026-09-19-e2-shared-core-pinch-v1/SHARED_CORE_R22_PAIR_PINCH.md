# Shared-core R2+R2 pair pinch and rooted-slot feedback

Date: 2026-09-19

Status: continuation of `EXACT_E2_SUPPORT_CHANNELS.md` under the same rigid one-code complete-cut / minimal outside-reservoir hypotheses and the same 19 September audit boundary. This is internal conditional mathematics, not D2C graph-realizability evidence.

## 1. Audit and priority reconciliation

The immediately preceding checkpoint classified the exact `E=2,k>=3` support topologies and identified a unique deepest pair-cheap `R2+R2` family:

- `t=1`, hence `g=p-1`;
- two radius-two singleton matched-head defects;
- their supports meet in exactly one coordinate (`h=1`);
- that shared coordinate is the repeated-core support (`c=2`);
- the common core witness is adjacent to both defects (`d0=2`).

The 19 September red-team audit requires exact pair-local `S_P/Ccap_P`, the graph-level negative control `X_3`, and rooted residual feedback rather than further global scalarization. This note follows that prescription exactly. No weakened or invalidated line is resumed.

`X_3` remains outside the present hypotheses because its canonical rooted control has `u=0`; nothing below excludes it.

## 2. Geometry and pair minimum

Let the two defect supports be

`{r,i}` and `{r,j}`,

where `r` is the repeated-core coordinate and `i!=j` are the private coordinates.

The common core witness `z_*` is adjacent to both defect heads. Star separation therefore deletes all `2k` defect--core head edges. These are zero-Hamming-excess edges because each defect differs from the core radius-one code in exactly one private coordinate.

For this topology the exact E2 channel parameters are

`s=4`, `q=h=1`, `c=2`, `d0=2`,

hence

`B=s-c+q=3`, `K=k(c-d0)=0`.

The three remaining bidirected singleton-type channels are:

1. defect 1 against the radius-one class on private coordinate `i` (if present);
2. defect 2 against the radius-one class on private coordinate `j` (if present);
3. the defect--defect overlap channel through `r`.

The active repeated-core channels contribute `2(k+1)` incidences before these three channels are used. Thus

`Jmax=2(k+1)+6=2k+8`.

Writing `D=D(A,M)` and `Delta=Emax-e(X)`, the exact pair correction is

`max(D,-6)`.

At `t=1`, `p(g+1)=p^2`, so the pair-local necessary condition is

> **`p^2+M-k-2+max(D,-6) <= T`,**                      `(SC-PAIR)`
>
> where `T=C0-sigma_P`.

On the deep arm `D<=-6`, this is

> **`p^2+M-k-8 <= T`.**                                  `(SC-DEEP)`

Therefore the literal right endpoint is

> **`M_+ = T-p^2+k+8`.**                                 `(SC-MPLUS)`

`M=M_+` is exact pair minimum; `M=M_+-1` has one unit of pair slack.

## 3. Unit I — universal two-zero-edge theorem

The previous E2 Hamming classification says that the only possible zero-Hamming-excess X-edges in an `R2+R2` geometry are defect-to-radius-one head edges on a defect support coordinate.

In the present shared-core / double-active topology, the `2k` defect--core candidates are already absent by star separation. The only zero-Hamming candidates not automatically deleted are therefore the two private defect--singleton edges on `i` and `j`.

Hence, without any pair-saturation assumption:

> **SHARED-CORE TWO-ZERO-EDGE LEMMA.** At most two actual X-edges have Hamming excess zero.

Let `j_+` be the number of positive-Hamming X-edges. Then

> `j_+ >= [e(X)-2]_+`.                                   `(SC-JPLUS)`

If `eta_2(j)` denotes the least `q>=0` with `binom(q+2,2)>=j`, the rooted local-slot theorem yields

> **`r >= a+y+2+eta_2([e(X)-2]_+)`.**                   `(SC-UNIV-SLOT)`

This is a topology-specific strengthening that applies throughout the shared-core arm, not merely at equality.

## 4. Unit II — exact and one-unit pair slack delete both remaining zero edges

On the deep arm define pair slack

`s_P := T-(p^2+M-k-8)`.

For an actual graph in this topology, the excess above the pair minimum is

`xi=[D+2Delta]_+ + (Jmax-J)`.

Thus `xi<=s_P`.

Assume `s_P<=1`.

If any one of the three bidirected channels were completely unused, it would lose two incidences from `Jmax`, contradicting `Jmax-J<=1`. Therefore every bidirected channel has at least one direction active.

The inherited singleton criticality/star-separation argument says that one active direction already forces the corresponding head-head edge absent. In particular both private defect--radius-one head edges are absent. Those were the only remaining zero-Hamming candidates.

Therefore:

> **NEAR-EQUALITY POSITIVE-EDGE THEOREM.** On `D<=-6` with `s_P<=1`, every actual edge of `G[X]` has positive Hamming excess.

The Hall summand simultaneously satisfies

`[D+2Delta]_+<=s_P`,

so

> **`Delta <= floor((s_P-D)/2)`.**                       `(SC-DELTA)`

Let

`Emax=binom(g,2)+k(g-2)`

because `A=g-2`. Then

`e(X)>=Emax-floor((s_P-D)/2)`.

Combining with the positive-edge theorem gives the explicit rooted-slot bill

> **`r >= a+y+2`**
> **`     +eta_2([Emax-floor((s_P-D)/2)]_+)`.**          `(SC-PINCH-SLOT)`

This holds both at exact pair minimum (`s_P=0`) and one unit above it (`s_P=1`).

## 5. Unit III — endpoint interpretation

By `(SC-MPLUS)`, still assuming the row lies on `D<=-6`:

- `M=M_+` gives `s_P=0` and
  `Delta<=floor(-D/2)`;
- `M=M_+-1` gives `s_P=1` and
  `Delta<=floor((1-D)/2)`.

Thus the pair endpoint and its immediate predecessor are not merely arithmetic rows. They are literal support-saturation / near-saturation geometries in which all X-edges have positive Hamming excess.

This is the E2 analogue of the repaired E1 pair-endpoint mechanism, but here the two radius-two defects provide an extra base rooted-slot unit.

## 6. Unit IV — exact rooted residual intersection

The rooted identity remains

`r=(p-lambda)(p+u)+q+E_U`.

For every physical row the preserved minimal-reservoir ledger gives

`q <= binom(u,2)-binom(k+1,2)-k-M`,

and the row score/Hall allocation gives a corresponding `E_U` upper budget. Therefore `(SC-UNIV-SLOT)` and `(SC-PINCH-SLOT)` can be compared against an actual upper bound on `r`, rather than another total-score relaxation.

The companion diagnostic does exactly that. It does not substitute a new global inequality for the pair-local variables; it retains `(A,M,D)`, the exact `sigma_P`, and the physical `q/E_U` row ceiling.

## 7. Unit V — bounded diagnostic: the shared-core family is already narrow

The companion checker replays the same abstract box used by the predecessor and first reproduces the known difficult slice exactly:

- `t=1` pair/Hall survivor states: `5,404`;
- states with no support-capped E1 route: `933`;
- their k-distribution remains
  `1:223, 2:201, 3:146, 4:104, 5:82, 6:60, 7:53, 8:47, 9:17`.

Hence `509` of the no-E1 states lie in the present `k>=3` E2 frontier.

Applying only the **safe shared-core necessary conditions** `(SC-PAIR)` and `(SC-UNIV-SLOT)` leaves a shared-core route in just **65 of those 509** states. The by-k counts are:

- `k=3: 23`;
- `k=4: 15`;
- `k=5: 17`;
- `k=6: 6`;
- `k=7: 4`;
- `k>=8: 0` on this box.

This does **not** close the other `444` states globally: they may use R3 or a different R2+R2 topology. It says only that the uniquely pair-cheapest shared-core escape is already highly restricted once its physical rooted-slot cost is charged.

Among the 65 shared-core states, **48** have an exact deep-pair-equality route satisfying the stronger all-positive-edge slot bill, and **49** have an exact-or-one-unit deep route. The exact/near by-k distribution is

- `k=3: 23`;
- `k=4: 11`;
- `k=5: 11`;
- `k=6: 4`;
- `k>=7: 0`.

So only 16 shared-core states on the bounded box require a genuinely non-near-equality row.

These are abstract parameter states, not D2C graphs and not realizability counts.

## 8. Unit VI — consequence for the next move

The unique pair-cheapest E2 topology is no longer a broad equality escape. Its deepest endpoint has a direct physical interpretation and, on the bounded diagnostic, almost all surviving routes are already concentrated at exact/one-unit pair slack.

The next mathematical target should therefore be **the 49 exact/near shared-core states as a structural family**, not another whole-parameter scan. The most promising additional resource is the forced absence pattern itself:

- both defects miss all `k` core heads;
- both private support edges are absent;
- the defect-defect edge is absent whenever the overlap channel is active;
- all surviving X-edges are positive-Hamming;
- the exact/near endpoint fixes `M` to `M_+` or `M_+-1` and bounds `Delta` explicitly.

The next run should feed this literal X-nonedge pattern back into the exact Hall-cut decomposition and the `q/E_U` residual allocation, looking for a compact contradiction or a finite equality classification. Only if that family survives should the non-near shared-core arm or alternate R2+R2/R3 topologies be opened.

## 9. Trust label

The theorem statements are conditional on the rigid complete-cut/minimal-reservoir hypotheses. The bounded replay is an arithmetic diagnostic only. The actual-D2C graph regression still has no positive fixture realizing the full rigid complete-cut hypotheses, and `X_3` remains a mandatory negative control outside this branch.
