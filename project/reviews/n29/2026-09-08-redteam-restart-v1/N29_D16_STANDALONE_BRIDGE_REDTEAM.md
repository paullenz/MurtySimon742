# Hostile audit of the standalone n=29, Delta=16 graph-to-model bridge

8 September 2026. Audit performed by ChatGPT/Geeps at Paul Lenz's request.

**Object audited:** `N29_D16_STANDALONE_BRIDGE.md`.

**Status:** same-assistant hostile review, not independent peer review. The purpose is to find the first invalid universal implication, not to accumulate agreement with earlier code. The frozen n=29 candidate proof remains unchanged.

## Verdict

**No blocking defect found.**

The audit rederived each graph implication from the diameter-two edge-critical definition and checked the finite-model embedding dimensionally. The most important outcome is not another computation: the proof-critical bridge is now short enough that its remaining trust boundary can be named precisely.

A clean GitHub Actions replay of the new bridge regressions completed successfully:

- workflow: `N29 Delta16 standalone bridge red team`;
- run: `34286148314`;
- head: `3678c1c68daacbd73b6ba010a3dddd3bde452f5a`;
- conclusion: **success**.

The workflow runs exact scalar identities plus exhaustive labelled-graph regression through `n=6`.

## 1. Complement / adjacent-total-domination equivalence

### Attack

Could deleting a critical G-edge create a complement obstruction not represented by an adjacent total-dominating pair? Could the new pair avoid both endpoints of the inserted H-edge?

### Result

No. For an H-edge `xy`, adjacent total domination is exactly the statement that the corresponding G-nonedge has no common G-neighbour. Adding one H-edge changes only the two endpoint neighbourhoods and creates only that new adjacency, so any genuinely new adjacent total-dominating pair must use an inserted-edge endpoint unless it is the inserted pair itself.

For a missing B-pair `uw`, the inserted pair `{u,w}` cannot dominate `v`, because both B-vertices miss `v`. Therefore the new pair uses exactly one B endpoint and an old neighbour. To cover `v`, that old neighbour lies in `A`. Before insertion the only possible uncovered vertex is the opposite B endpoint. The quasi-edge `ui->w` follows.

**Verdict:** pass.

## 2. Selected-edge injection

### Attack

Could two missing B-pairs choose the same cross-edge? Could the same unordered B-pair be represented twice with opposite orientations?

### Result

A selected cross-edge `ui` determines its B-source `u`. Its open-neighbourhood union has a unique exception `w`, so it also determines the supplement. Hence it recovers the missing unordered pair `{u,w}`. The construction chooses one cross-edge per missing pair, so no pair receives two chosen orientations.

This one-orientation rule is later essential to endpoint-load disjointness and threshold capacity.

**Verdict:** pass.

## 3. Edge ledger and label demand

### Attack

Could the selected-edge count or H[B] count be double-counted? Is `S>=r+2t` using `x_i=s_i` implicitly?

### Result

Selected cross-edges plus actual H[B] edges partition the unordered B-pairs. This gives the exact complement ledger

`e(F)=r+t`.

Minimum H-degree at a label gives `x_i>=d_i-R_i`, but the proof never replaces actual `x_i` by demand `s_i`. Instead

`S=sum max(0,d_i-R_i) >= sum(d_i-R_i)=r+2t`.

The distinction between actual selected degree and minimum demand is preserved throughout.

**Verdict:** pass.

## 4. The delicate residual-forcing step

### Attack

The source-demand inequality `d_i<=rho_u+R_i` is load-bearing. The obvious danger is that an edge forced at column `i` might itself be selected rather than residual, destroying the injection into `R_i`.

### Reconstruction

For selected `ui->w` and an F-neighbour `j` of `i`, `uj` is forced into H. If `uj` is selected with supplement `w_j`, then `iw_j` is forced because `ui->w` must dominate `w_j` and `u` misses `w_j`.

Why is `iw_j` residual? Two A/B nonadjacencies are simultaneously available:

- `ij` is missing because `ij in F`;
- `jw_j` is missing because `w_j` is the unique exception of `uj->w_j`.

Thus the cross-edge `iw_j` misses the A-vertex `j` from both endpoints. If it were one of our selected B-pair cross-edges, its chosen quasi-edge would have a unique exception in `B`, impossible because `j in A` is also uncovered. Hence it is residual.

Distinct supplements at source `u` make the injection into residual column edges distinct.

The symmetric argument forcing `wj` residual establishes `d_i<=rho_u+rho_w`.

**Verdict:** pass. This is one of the first points an external reviewer should attack.

## 5. Source/supplement capacities and endpoint load

### Attack

Could `p_u` count something other than missing B-degree? Could incoming sources collide with outgoing supplements in the endpoint-load count?

### Result

Each missing B-pair incident with `u` has exactly one chosen orientation. It contributes to exactly one of `q_u` or `p_u`, so `q_u+p_u` is the missing H[B]-degree of `u`. Therefore

`deg_H(u)=rho_u+b-1-p_u`,

and minimum H-degree gives `p_u<=rho_u+b-a-1` directly.

For a selected `ui->w`, the B-neighbours counted at `i` are:

- `u`;
- supplements of the other `q_u-1` selected labels at `u`;
- sources of the `p_u` incoming orientations.

An incoming source cannot equal an outgoing supplement, because that would orient the same missing B-pair both ways. An incoming source cannot equal `w`, because `{u,w}` is already oriented out of `u`. All counted vertices are therefore distinct, proving `R_i+x_i>=q_u+p_u`.

**Verdict:** pass.

## 6. Residual activity

### Attack

Assume `rho_u=0`. The previous short proof could fail if:

1. an F-edge between `U=N_A(u)` and `T=A\U` survives;
2. the two residual edges produced by an F-edge in `U` collide across edges;
3. an F-edge in `T` creates a quasi-edge with auxiliary `v` or in `A`;
4. the U-family and T-family residual edges overlap.

### Reconstruction

1. If `i in U` and `j in T`, selected `ui->w_i` must dominate `j`; `u` misses `j`, hence `ij in H`. So there is no F-edge U--T.
2. An F-edge `{i,j}` in `U` produces residual edges `iw_j` and `jw_i`. Supplements at source `u` are distinct. A residual edge `iw_j` identifies `j` from its B-endpoint and identifies `i` from its A-endpoint, so different F-edges cannot collide.
3. For an F-edge `{i,j}` in `T`, the inserted pair itself misses `u`. A new pair using `i` has an old auxiliary `z` which must neighbour `u`. `z=v` cannot work because `v` already neighbours the supposed exception in `A`. If `z in A`, then `z in U`; absence of F-edges U--T makes `z` adjacent to the supposed exception, contradiction. Thus `z in B`, producing a residual cross-edge whose unique exception is in `A`.
4. U-family edges have A-endpoint in `U`; T-family edges have A-endpoint in `T`.

Therefore

`r>=2e(F[U])+e(F[T])>=e(F)=r+t`,

contradicting `t>0`.

**Verdict:** pass. No positive-surplus actual graph occurs through `n=6`, so the small-graph regression cannot exercise this branch; its assurance here remains the hand proof.

## 7. Charging

### Attack

Check denominator boundaries, source multiplicity, and the direction of the monotone charge comparison.

### Result

A chosen incidence is selected, hence its source has `q_u>=1`, so `rho_u<=a-1`; the denominator `a-rho_u` is positive. At source `u`, at most `q_u<=a-rho_u` chosen incidences can occur, giving source charge at most `rho_u-1`.

For a label of demand `s`, source demand gives every chosen source `rho_u>=s`; `(x-1)/(a-x)` is increasing on the integer range used, so each chosen incidence receives at least `(s-1)/(a-s)`. The inequality direction is therefore correct.

Exact arithmetic independently checks

`s-s(s-1)/(a-s)=s(a+1-2s)/(a-s)`

for every n=29 demand value.

**Verdict:** pass.

## 8. Isolated-C exclusion / dmax=10

### Attack

The earlier n=29 proof had omitted this bridge. Recheck the possibility that a missing pair inside `X=A\{x}` uses `v` as its newly total-dominating auxiliary, and recheck disjointness of the extra `b` residual edges.

### Result

If `x` is isolated in `C`, an F-edge `ij` in `X` cannot create new total domination through edge `iv`: `v` already neighbours `j`, so inserting `ij` changes nothing needed for pair `{i,v}` at the supposed exception. An auxiliary in `A` cannot dominate `x`, because `x` has no C-neighbours. Hence the auxiliary lies in `B` and yields a residual cross-edge with A-exception.

For every B-source used in this first family, the forced edge to `x` is residual because both endpoints miss the A-exception. For an unused B-source, residual activity supplies a residual edge. These `b` edges are source-distinct and are disjoint from the first family.

The resulting inequality

`b<=a-1-t`

fails strongly at `(a,b,t)=(12,16,2)` and `(12,16,3)`. Hence `delta(C)>=1` and `d_i<=10`.

**Verdict:** pass.

## 9. Threshold capacity

### Attack

This inequality fails abstractly if either of two premises is dropped:

1. allow both selected orientations of one unordered B-pair;
2. allow a heavy source with load `>h` to use supplements outside `Z_h`.

Thus both premises must be supplied by the graph bridge, not assumed in the extremal algebra.

### Result

Premise 1 is Lemma 3.2.

For premise 2, a supplement of a source with more than `h` selected heavy labels sees at least `h` other heavy labels. If the supplement had residual degree below `h`, source demand would prevent any of those heavy-label edges from being selected at that supplement; all would be residual, contradiction. Hence the supplement lies in `Z_h`.

The exact extremal gap is

`(z_h-h-j)(z_h-h-j-1)/2>=0`

for every integer `j`. The new exact sanity script checks the identity over a much larger scalar range than n=29 requires.

**Verdict:** pass.

## 10. Demand-stage source-capacity dual

### Attack

Could the dual prune a profile because it models source counts too strongly? Could `A_{k,j}` underestimate actual contribution?

### Result

For residual degree `j`, an actual source has at most `a-j` selected slots and can select only labels with demand `<=j`. Thus

`A_{k,j}=min(a-j, eligible labels in the chosen top-k prefix)`

is an upper bound on actual source contribution. The inequalities `D_k<=sum n_j A_{k,j}` are therefore necessary, not sufficient assumptions.

The dual certificate combines only these necessary inequalities, `sum n_j=b`, and `sum(j-1)n_j<=rmax-b`. Its final strict inequality is checked exactly. Any rejection is consequently a literal linear-combination contradiction for every possible source-count vector.

**Verdict:** pass.

## 11. Residual-row scanner

### Attack

The danger is cap refinement becoming self-fulfilling: replacing unknown `q_w` by an upper cap and then shrinking all caps could accidentally pass from an upper bound to a lower bound.

### Result

Assume current `c_w>=q_w` for every source. A source of actual degree `q` has `q` distinct supplements satisfying `rho_w+q_w>=q-1`, hence those same vertices satisfy the weaker condition `rho_w+c_w>=q-1`. Therefore actual `q` is no larger than the scanner's newly computed maximum supported value. Simultaneous update preserves valid upper bounds. Induction preserves them through every iteration.

The top-prefix Hall check is itself necessary for the actual selected incidence system. It does not claim sufficiency.

**Verdict:** pass.

## 12. Corrected-v2 dimensional audit

### Attack

This is where the real v1 bug occurred. Reconstruct every variable from empirical graph counts and track whether it is per label, per source, per ordered source pair, or per source-label pair.

### Result

A graph maps to:

- `Y`: fraction within one equal-demand label group;
- `T`: fraction of that whole label group with a given `(d,R)` option and `x>=h`;
- `W`: fraction within one equal-rho source group;
- `P`: density among ordered distinct source/target pairs;
- `Z`: density among source-label pairs.

The source-side Z identity is

`sum_g n_g Z=qW`.

The label-side identity is

`sum_k n_k Z=sum_h T_h`.

There is **no `n_g` factor on the right**. Corrected v2 has this form; historical v1 did not.

For a fixed label option, the nested selected-slot capacity is exactly

`E[x 1{x>=h}]=(h-1)T_h+sum_{j=h}^U T_j`.

The source/supplement `P` flow is deliberately weaker than the graph in the same-rho-group case: the graph gives density at most `1/2`, while v2 allows `<=1`. This enlarges the feasible relaxation and is therefore safe.

No normalization reversal or hidden equality stronger than empirical graph averaging was found.

**Verdict:** pass.

## 13. Exact Farkas semantics

### Attack

Verify the certificate sign convention directly against the model code, rather than relying on the prose description.

### Result

`Model.le(row,b)` means `row*x<=b`; primal variables have lower bound zero. The verifier permits only nonnegative multipliers on inequality rows and signed integer multipliers on equalities. It reconstructs the summed coefficient vector and requires every coefficient nonnegative and the exact summed RHS negative.

For any feasible `x>=0`, the summed left side would then be nonnegative while also being `<=` a negative RHS: contradiction.

The certificate generator may use floating point to propose a ray, but `verify_certificate` rechecks integer multipliers, signs, coefficients and RHS exactly.

**Verdict:** pass.

## 14. Exhaustive small-graph negative search

`bridge_smallgraph_attack.py` independently enumerates every labelled simple graph through six vertices, retains all diameter-two edge-critical graphs, and checks the pointwise selected/residual bridge for every minimum-complement-degree choice of `v`.

Exact labelled counts reproduced:

- n=3: 3;
- n=4: 7;
- n=5: 27;
- n=6: 571.

Total diameter-two edge-critical graphs checked: **608**.

Minimum-degree complement views checked: **920**.

Violations found: **0**.

Positive-surplus views (`t>0`): **0**.

Thus this regression is useful against basic quasi-edge, ledger, source-demand, source/supplement, endpoint-load and threshold transcription errors, but it is not evidence for the positive-surplus residual-activity branch beyond the hand proof.

## 15. Remaining trust boundary

After this audit, the principal n=29 Delta=16 mathematical risk is concentrated in a small set of universal hand claims:

1. the quasi-edge construction for a missing B-pair;
2. the forced-residual edge argument behind source demand;
3. residual activity at `t>0`;
4. high-load supplement confinement in threshold capacity;
5. the empirical embedding into corrected v2.

The arithmetic after those claims is now highly redundant and exact. An external reviewer should spend time on the five items above before rerunning millions of rows.

**Final internal verdict:** standalone bridge survives hostile same-assistant review; n=29 remains a **candidate**, with independent mathematical review still OPEN.
