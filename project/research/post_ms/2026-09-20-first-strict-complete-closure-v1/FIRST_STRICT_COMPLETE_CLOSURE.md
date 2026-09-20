# Complete closure of the first-strict unloaded buffer layer

Date: 2026-09-20

Status: **same-session internal structural strengthening**, conditional on the audited rigid one-code/common-buffer setup. This note is deliberately upstream of pair-capacity and finite diagnostics. It combines the new Type-F elimination with a raw matched-edge obstruction for the remaining all-R geometry.

## 1. Audit reconciliation

The 20 September daily adversarial audit remains binding. In particular:

- P1/P2 use the repaired physical/selected semantics;
- `X_3` remains the mandatory negative control;
- the actual-D2C regression still has zero positive rigid complete Hall cuts with `x>=3`;
- the raw same-code theorem and ordered `(source,witness)` injectivity have been independently re-derived in `SAME_CODE_RAW_CRITICALITY_AUDIT.md`;
- exact pair-local `Ccap_P/(ONE-P)/(CROWD)` remain mandatory whenever that machinery is used;
- finite scans are diagnostics only.

The immediate predecessor `TYPE_F_ELIMINATION_AND_DEPENDENCY_AUDIT.md` proves that Type F is impossible in the first-strict unloaded branch and gives the all-R class/witness bijection. The present note checks the remaining all-R possibility directly before any downstream optimization.

## 2. Inherited first-strict all-R normal form

Assume

`d_Y(b)=0`, `epsilon_b=p-g+1`.

The first-strict theorem gives a unique buffer--X hole `ba_0`, with `b` complete to `U_o` and to `X'=X\{a_0}`. After Type-F elimination, every `x in X'` is Type R.

For each X'-code class `C`, put

`I_C={i:C_i=d_i}`.

Then:

- `empty != I_C subseteq I_0`, where `I_0={i:c(a_0)_i=d_i}`;
- `S_0=[p]\I_0` is nonempty;
- distinct represented blocks `I_C` are pairwise disjoint;
- `a_0` is nonadjacent to every vertex of `X'`;
- each code class has one graph-fixed complementary outside witness;
- every physical outside vertex is one of these class witnesses;
- hence `omega=|U_o|=h=m`, where `h` is the number of represented X'-codes and `m` is the maximal representative number.

The maximal `m=1` all-R branch is already closed by the preserved raw-criticality argument. Thus a surviving first-strict graph would have `h=m>=2`.

## 3. Key matched-edge obstruction at an `S_0` coordinate

Let `C` be any represented Type-R code and let `x` be any head in that class. Choose

`j in S_0`.

Since `I_C subseteq I_0`, we have `j notin I_C`, so `C_j!=d_j`. Let `q_j` be the `bar d` endpoint of tight fibre `j`. Then

`xq_j in E`, `bq_j in E`, `bx in E`,

so `xq_j` lies in the triangle `x-b-q_j` and must have a raw singleton criticality certificate.

Assume first that

`d_H(C,d)>=2`.

The radius-at-least-two matched-edge exhaustion already isolated in `MAXIMAL_SELECTION_MATCHING_AND_M1_CLOSURE.md` Section 10 and corrected in `M2_BULK_BLOCK_SCOPE_CORRECTION.md` applies here. We record why the only possible extra rescue created by having several code classes is unavailable.

### Orientation `q_j -> x`

- Every `y in Y` is nonadjacent to `q_j` and adjacent to all of `X`. Because every Type-R block lies in `I_0`, **every** vertex of `X'` differs from `d` at `j` and is adjacent to `q_j`. Since `|X'|=x-1>=2`, a Y-witness has at least two X' common neighbours with `q_j`, not the singleton `{x}`.
- Vertices of `X'` and `a_0` cannot isolate `x`; at coordinate `j in S_0`, they are adjacent to `q_j`, while the remaining A-side alternatives carry the fixed complete-cut/Y common-neighbour obstruction.
- Any outside vertex of `U_o` is adjacent to `b` in the first-strict layer, and `bq_j in E`; hence it has the extra common neighbour `b` with source `q_j`.
- The remaining rooted-B/matched locations are excluded by the same fixed root/buffer/common-neighbour checks as in the preserved matched-edge exhaustion.

Thus this orientation cannot certify the edge.

### Orientation `x -> q_j`

- A-side witnesses fail by the complete `X--Y` cut / fixed shared-Y obstruction used in the preserved exhaustion.
- The buffer is adjacent to the source and cannot be a witness. A common-core `bar d` vertex which is nonadjacent to `x` shares with `x` every `bar d` fibre endpoint at which `C` differs from `d`; because `d_H(C,d)>=2`, there is another such endpoint besides `q_j`, so the common neighbourhood cannot be the singleton `{q_j}`.
- A physical outside witness belonging to another code class `D` can be adjacent to `q_j` only if its complementary code selects `q_j`, equivalently only if `D_j=d_j`, i.e. only if `j in I_D`.

But every represented class is Type R and therefore `I_D subseteq I_0`, while `j in S_0=[p]\I_0`. So **no outside class can provide the only remaining rescue**.

Both orientations fail. Therefore no represented Type-R code can satisfy `d_H(C,d)>=2`.

Hence every represented Type-R code must have

> `d_H(C,d)=1`.                                         `(R-RADIUS1)`

## 4. Radius one collapses all R classes to one code

For a Type-R class, `I_C subseteq I_0`, so its difference set from `d` contains all of `S_0`.

If `d_H(C,d)=1`, then necessarily

> `|S_0|=1`,
> `I_C=I_0`.

Thus every represented Type-R class has the **same** agreement block `I_0` and therefore the same tight code.

Consequently

> `h=1`.

By the all-R class/witness bijection,

> `m=omega=h=1`.

But maximal `m=1` all-R has already been closed by raw criticality. Contradiction.

Therefore:

> **FIRST-STRICT COMPLETE CLOSURE.** There is no graph in the unloaded first-strict layer
>
> `d_Y(b)=0`, `epsilon_b=p-g+1`.                         `(S1-EMPTY)`

No finite scan, pair-capacity bound or asymptotic estimate is used.

## 5. Stronger buffer floor

The exact unloaded-buffer defect identity is

`epsilon_b=(p-g)+h_X+h_o`,

where `h_X` is the number of buffer--X holes and `h_o` the number of buffer--`U_o` holes.

The old equality layer `h_X+h_o=0` was already closed by the rooted matched-edge self-pricing theorem. The present theorem closes `h_X+h_o=1` as well. Hence every surviving unloaded common-buffer configuration must satisfy

> `h_X+h_o>=2`,
>
> **`epsilon_b>=p-g+2`.**                               `(BUFFER+2)`

This is the new live frontier.

## 6. Immediate second-strict consequence

At equality in `(BUFFER+2)`, i.e. `epsilon_b=p-g+2`, the exact identity leaves only

1. `(h_X,h_o)=(2,0)`;
2. `(h_X,h_o)=(1,1)`;
3. `(h_X,h_o)=(0,2)`.

The last subtype is impossible by the same physical counting used for the first-strict outside-hole subtype. If `h_X=0`, the outside-certificate self-pricing theorem forbids outside Orientation-A certificates for every buffer--X edge. Matched Orientation A remains unavailable. Reverse certificates can use only the two physical `U_o` non-neighbours of `b`; each fixed pair `(b,z)` can singleton-certify at most one X-head. Since `b` is complete to all `x>=3` vertices of X, two such witnesses cannot certify all buffer--X edges.

Therefore the exact second-strict layer, if nonempty, has

> `(h_X,h_o) in {(2,0),(1,1)}`.                          `(S2-SPLIT)`

This is the next structural attack: two X-holes with no outside hole, or one X-hole plus one outside hole. The first-strict F/R machinery should not be reused without re-derivation because the rooted matched-edge certificates now have two possible X-hole feet in the `(2,0)` case and a competing reverse channel in the `(1,1)` case.

## 7. Dependency cleanup

Once `(S1-EMPTY)` is independently audited, all same-day maximal-m1/m2/F-R calculations are historical conditional mathematics below an empty first-strict parent. They remain useful as an audit trail but are no longer the reason the first-strict branch closes.

The live unloaded common-buffer programme should move to `(BUFFER+2)` / `(S2-SPLIT)`, while retaining the global zero-positive-rigid-cut interface risk from the daily audit.