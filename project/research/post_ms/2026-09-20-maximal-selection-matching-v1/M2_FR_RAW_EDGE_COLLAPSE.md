# Maximal m=2 F/R geometry: raw edge collapse and full outside-reservoir pricing

Date: 2026-09-20

Status: **internal candidate structural continuation**, conditional on the audited first-strict unique-hole setup, maximal raw eligibility matching number `m=2`, `p>=3`, `x>=4`, and the corrected complementary F/R normal form `(M2-FR-NORMAL-CORRECTED)` from `M2_BULK_BLOCK_SCOPE_CORRECTION.md`. This note was derived after rereading `CURRENT_STATE.md`, root `README.md`, the 20 September daily red-team audit, the raw same-code audit, and the latest m=2 commits. It does not change the zero-positive-fixture caveat.

## 1. Normal form and fixed certificate pairs

Write `S_0={s}`. Let `C_R` be the radius-one code differing from `d` only at `s`, and `C_F=bar C_R`. In the `omega=|U_o|>2` branch:

- `a_0` and the `x-2` R-heads `R_X` have code `C_R`;
- the unique F-head `f` and the unique R-witness `z_R` have code `C_F`;
- `Z_F=U_o\{z_R}` has size `omega-1` and every vertex of `Z_F` has code `C_R`;
- `z_R` certifies every buffer edge `br`, `r in R_X`, hence `N(r) cap N(z_R)={b}`;
- every `z in Z_F` certifies `bf`, hence `N(f) cap N(z)={b}`;
- `z_R a_0 in E`, while `z_R` misses `R_X` and `Y`;
- every `z in Z_F` misses `f,a_0,Y`.

The equal-code raw-criticality theorem and ordered `(source,witness)` injection have already been independently re-derived in `SAME_CODE_RAW_CRITICALITY_AUDIT.md`.

## 2. Unit I — F-star witnesses miss every R-head

### Theorem 2.1

> `E(Z_F,R_X)=emptyset`.                                  `(ZF-R0)`

### Proof

Suppose `zr` is an edge with `z in Z_F`, `r in R_X`. The endpoints have the same code `C_R`, so the raw same-code theorem forces a complementary-code witness.

If the source is `z in U`, the witness must lie in `A_{C_F}`. The only such A-vertex is `f`, but the fixed eligibility certificate gives `N(z) cap N(f)={b}`, not `{r}`.

If the source is `r in A`, a complementary witness can only be `f` or `z_R`. The A-vertex `f` shares all nonempty `Y` with `r`, so it cannot have singleton common neighbourhood `{z}`. The U-vertex `z_R` has the fixed common-neighbour set `N(r) cap N(z_R)={b}`, not `{z}`.

Both orientations fail. `square`

This uses physical fixed common-neighbour sets, not selected-incidence multiplicity.

## 3. Unit II — the entire outside reservoir is independent

### Theorem 3.1

> `E(z_R,Z_F)=emptyset`.                                  `(ZR-ZF0)`

### Proof

Assume `z_R z in E` with `z in Z_F`. The edge lies in the root triangle because both endpoints are in U. In either raw orientation a U-source must use an A-witness.

If the source is `z` (code `C_R`), any witness agreeing with `C_R` in a tight coordinate creates an extra matched common neighbour, so the witness must have code `C_F`. The only A-vertex of code `C_F` is `f`, but `N(z) cap N(f)={b}`.

If the source is `z_R` (code `C_F`), the witness must have code `C_R`. The candidate `a_0` is adjacent to the source and therefore cannot be the witness. Every R-head is nonadjacent to `z_R`, but by `(ZF-R0)` is also nonadjacent to the head `z`. Vertices of `Y` are anticomplete to `U_o` and in any event do not have the required complementary code.

Thus neither orientation has a singleton witness. `square`

Together with the previously proved `G[Z_F]` edgeless,

> `G[U_o]` is edgeless.                                   `(UO-INDEP)`

This strengthens `(ZF-INDEP)` from the previous note.

## 4. Unit III — the R-witness also misses the F-head

### Theorem 4.1

> `z_R f notin E`, hence `N_A(z_R)={a_0}`.               `(ZR-A1)`

### Proof

If `z_R f` were an edge, its endpoints would have the same code `C_F`.

With source `z_R in U`, the witness must lie in `A_{C_R}`. The vertex `a_0` is adjacent to `z_R`, so it cannot witness. Every `r in R_X` is nonadjacent to `z_R`, but its fixed common-neighbour set with `z_R` is `{b}`, not `{f}`.

With source `f in A`, a complementary-code witness lies among `a_0,R_X,Z_F`. Every `z in Z_F` has fixed common-neighbour set `N(f) cap N(z)={b}`. Any nonadjacent witness in `a_0` or `R_X` shares the nonempty set `Y` with `f`, so its common neighbourhood with `f` cannot be the singleton `{z_R}`; moreover R-heads miss `z_R`.

Contradiction. Since the known A-adjacencies of `z_R` are `a_0` versus nonadjacency to `R_X,Y`, the displayed neighbourhood identity follows. `square`

## 5. Unit IV — every F-star witness is A-anticomplete

The previous normal form already gives nonadjacency from `Z_F` to `f,a_0,Y`; Theorem 2.1 supplies nonadjacency to `R_X`. Therefore

> `N_A(z)=emptyset` for every `z in Z_F`.                 `(ZF-A0)`

Combining `(ZF-A0)` with `(UO-INDEP)`, every `z in Z_F` has at least

`a+(omega-1)`

physical nonneighbours in `A union U`. Using `epsilon_z=H_z+p-a`,

> `epsilon_z >= p+omega-1`.                              `(ZF-SCORE+)`

The R-witness has at least `y+(x-2)+1+(omega-1)=a+omega-2` nonneighbours in `A union U` (Y, all R-heads, f, and Z_F), hence

> `epsilon_{z_R} >= p+omega-2`.                          `(ZR-SCORE)`

Consequently the entire outside reservoir satisfies the clean physical bill

> `E_{U_o} >= (omega-1)(p+omega-1)+(p+omega-2)`
>
> `          = omega^2+(p-1)omega-1`.                   `(UO-SCORE)`

This strictly dominates the earlier F-star-only bill.

## 6. Unit V — strengthened rooted-triangle loss

The independent sets `U_-=W_0 dotcup {b}` and `U_o` give disjoint forced missing U-U pairs. Retaining the previously proved `k-1` core-separation holes gives

> `q <= binom(u,2)-binom(k+1,2)-binom(omega,2)-(k-1)`.  `(Q-UO)`

Thus the whole physical outside reservoir, not merely `Z_F`, is priced quadratically in rooted triangle capacity.

## 7. Unit VI — all internal X-edges disappear

### Theorem 7.1

> `G[X]` is edgeless.                                     `(X0-M2-FR)`

### Proof: first `f--R_X`

Suppose `fr` is an edge with `r in R_X`. Its endpoint codes `C_F,C_R` are complementary.

Orient source `r`, head `f`. A matched witness chosen by `f` fails as follows: off `s` it is a `bar d` endpoint and shares the buffer `b` with `r`; at `s` it is the `d` endpoint and shares every vertex of nonempty `Y` with `r`. A-witnesses either are adjacent to the source or share Y / the tight code with it. On the U-side, `z_R` misses `f`, every `Z_F` vertex misses both `f` and `r`, while `b` is adjacent to the source; any common-core candidate shares the tight endpoint at `s` with `r`. Thus this orientation fails.

Orient source `f`, head `r`. A matched witness chosen by `r` shares Y with `f` off `s`, and shares `b` with `f` at `s`. A-witnesses again share Y. The R-witness `z_R` has the same code as `f`, hence shares all tight matched neighbours with it; every F-star witness misses `r`; and common-core / buffer candidates are eliminated by adjacency or shared tight endpoints. Thus this orientation also fails. Hence `fR_X` is empty.

### Proof: then `R_X` is independent

The previous note showed that every same-code R-R edge must use `f` as its complementary-code raw witness (the R-witness `z_R` cannot do so because it misses every R-head). But `f` has just been proved anticomplete to `R_X`, so no R-R edge can be certified. Hence `G[R_X]` is empty.

### Proof: finally `a_0f`

Assume `a_0f` is an edge. For source `a_0`, head `f`, a matched witness selected by `f` has an extra common neighbour: off `s`, `z_R` is common to `a_0` and that matched endpoint; at `s`, Y supplies an extra common neighbour. The buffer candidate shares the `s`-fibre endpoint with `a_0`; F-star witnesses miss `f`; R-heads are nonadjacent to `a_0`; and common-core candidates share fixed tight neighbours.

For source `f`, head `a_0`, matched witnesses have Y or `b` as an extra common neighbour. The candidate `z_R` is adjacent to `a_0` and nonadjacent to `f`, but `f` and `z_R` have the same code and therefore share all `p` tight matched neighbours, so their common neighbourhood is not singleton. F-star witnesses miss `a_0`; R-heads miss `a_0`; buffer/core candidates again have fixed extra tight common neighbours.

Thus neither orientation works, and `a_0f` is absent.

Type R already gives `a_0R_X` empty. Hence all possible X-X edge types are absent. `square`

## 8. Unit VII — pair-local score gate after physical reservoir pricing

Let `Sigma_P(omega)` be the exact pair-local threshold already used in `check_m2_fr_reservoir.py`: it includes the exact common-core floor, the first-strict buffer slack, the physical Y-price

`L_Y=y(p-g+1+omega)`,

`(CROWD)`, and exact `Ccap_P` without substituting total score for pair-local score.

Since `(UO-SCORE)` lies outside the pair `{d,bar d}` for `p>=3`, every `omega>2` survivor must satisfy

> `Sigma_P(omega)+omega^2+(p-1)omega-1 <= C0`.           `(M2-UO-SCORE-GATE)`

The new q ceiling `(Q-UO)` and the exact `G[X]=empty` conclusion should be fed into the rooted residual identity next; no finite scan is a substitute for that hand step.

A same-session broad-box diagnostic (same ranges and coarse baseline as the existing m2 checker) gives, for `omega>2` only:

- physical-reservoir base rows: `182396`;
- exact pair survivors: `171981`;
- survivors after `(M2-UO-SCORE-GATE)`: `103860`;
- survivors after additionally applying the conservative rooted-q residual gate with `(Q-UO)`: `73663`.

These are abstract necessary-condition rows, **not graphs**. The accompanying checker should be independently replayed before the counts are used in any confidence statement.

## 9. Next structural attack

The highest-value follow-on is now the exact rooted/Hall use of `(X0-M2-FR)`. The previous diagnostic only used the stronger physical reservoir and q bills; it did not exploit all consequences of `e(X)=0`. Reinsert `e(X)=0` into the exact Hall-density / residual ledger before opening `omega=2`, `x=3`, `p<=2`, loaded-buffer, `z=2`, or the four-exception gate.

The audit boundary remains unchanged: the rigid complete-cut interface still lacks a positive actual-D2C fixture, and every same-hour closure in this note remains provisional pending independent adversarial review.