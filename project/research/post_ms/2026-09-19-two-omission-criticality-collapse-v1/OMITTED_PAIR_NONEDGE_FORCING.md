# Forced omitted nonedges and the corrected rooted-triangle baseline

Date: 2026-09-19

Status: internal hand structural theorem inside the already-purified rigid one-code `z=1`, `h=0`, full-support branch. No eventual second-extremal theorem is claimed. The published order-12 graph `X_3` remains a mandatory hostile control and is untouched because its canonical root has `u=0`.

## 1. Audit reconciliation

Before this continuation, the live `CURRENT_STATE.md`, root `README.md`, latest commits, the 19 September daily red-team audit/handoff, the independent source-tuple reproof, the source-premise repair, and the independent graph-level Hall/pair-capacity regression were reread.

There is no departure from the audit priority order. The two named source-tuple premises remain repaired at the exact raw/selected interface used by the finite theorem, the actual-D2C regression still records no graph/formula mismatch and retains `X_3`, and the present argument stays inside the audit-authorized one-code rigid branch. The graph regression still has no positive actual-graph fixture realizing a rigid complete Hall cut with `x>=3`; accordingly the results below are hand deductions conditional on the rigid-branch hypotheses, not graph-exercised empirical facts.

This note also performs a hostile correction to the immediately preceding two-omission handoff: the variable called `Q_rest=Q-e(U_-,U_o)` contains a large forced tight-fibre baseline and must not be interpreted as a small correction term. In particular the earlier hypothetical condition `Q_rest=0` is not feasible in the present `p>=1`, `u>=k+1` branch.

## 2. Setup

Use the notation of `FULL_SUPPORT_SOURCE_VISIBILITY_PURIFICATION.md` and `TWO_OMISSION_TRIANGLE_SLACK_LEDGER.md`.

Thus:

- `X,Y` partition the A-layer across a rigid complete Hall cut;
- `X--Y` is complete;
- every source in `Y` has tight Boolean code `d`;
- `A_d=Y` and `A_{bar d}=emptyset`;
- `U_-=U_{bar d}` and `U_o=U\U_-`;
- `g=g_P`, `k=x-g>0`, `|U_-|=k+1`;
- `h=0`, so every source uses all `g` relevant matched gamma-`d` feet and exactly `k` vertices of `U_-` as its crossing witnesses;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- the full-support omission design has exactly two omitted vertices `o_1,o_2 in U_-`, sharing the same X-head `x_*`, and every source in `Y_i` omits `o_i`.

Let `nu` count omitted source--`U_-` pairs which are graph nonedges. There is exactly one omitted pair per source, so a priori `0<=nu<=y`.

The previous ledger treated `nu` as a free correction variable. The main result here is that raw edge-criticality plus the already-established Boolean/gamma geometry forces the opposite extreme:

> `nu=y`.

Equivalently, **every omitted source--witness pair is a graph nonedge**.

## 3. A small Boolean lemma

Let the tight antipode pairs be `P_j={q_j^0,q_j^1}`, `j=1,...,p`. Tightness means every vertex of `A union U` is adjacent to exactly one endpoint of every `P_j`, so it has a Boolean code in `{0,1}^p`.

### Lemma 3.1 — no common matched neighbour iff complementary code

For `r,s in A union U`, the following are equivalent:

1. `r` and `s` have no common neighbour in the matched layer `P=union_j P_j`;
2. their tight codes are complementary: `c(r)=bar c(s)`.

### Proof

At fibre `j`, the two vertices share a matched neighbour exactly when they choose the same endpoint of `P_j`, i.e. exactly when their code bits agree at coordinate `j`. They have no common matched neighbour in any fibre iff their bits differ in every coordinate, which is precisely complementarity. `square`

The present one-code branch has `Y` nonempty and `A_{bar d}=emptyset`, so necessarily `p>=1`; for `p=0` the unique empty code equals its own complement and the pair-purity conclusion would be impossible.

## 4. Suppose one omitted pair were an edge

Fix `s in Y_i` and suppose, for contradiction, that

> `s o_i in E(G)`.                                           `(4.1)`

Because `o_i` and the other omission vertex have the common X-head `x_*`, and `X--Y` is complete,

> `s-x_*-o_i-s`

is an ordinary triangle. It is not a rooted-neighbourhood triangle; both `s` and `x_*` lie in A.

The generic triangle-edge criticality lemma gives one of two singleton-common-neighbour orientations after deleting `s o_i`.

We now eliminate both orientations without a class-size hypothesis.

## 5. Structural unit I — the old Orientation A is impossible for every source

Orientation A supplies a vertex `z` with

- `s z in E`,
- `o_i z notin E`,
- `N(o_i) intersect N(z)={s}`.                              `(5.1)`

As in the preceding trichotomy note, `z` cannot lie in B, because the root would then be a second common neighbour of `o_i` and z; and `z` cannot be the root. Hence `z in A`. Since `Y` is independent while `s z` is an edge, `z in X`.

But `(5.1)` says in particular that `o_i` and z have no common matched-B neighbour: their unique common neighbour is the A-vertex s. Lemma 3.1 therefore gives

`c(z)=bar c(o_i)=d`,

because `o_i in U_-=U_{bar d}`. Pair purity says every A-vertex of code d lies in Y, contradicting `z in X`.

### Theorem 5.1

For an omitted pair which is an edge, Orientation A is impossible **for every source**, including a source in a singleton omission class.

This strictly sharpens the predecessor argument, which needed `|Y_i|>=2`.

## 6. Structural unit II — the ROOT alternative is impossible

The remaining orientation supplies z with

- `o_i z in E`,
- `s z notin E`,
- `N(s) intersect N(z)={o_i}`.                              `(6.1)`

The predecessor trichotomy locates z in one of three places: the root, `U_o`, or the matched layer.

If `z=v`, then `(6.1)` says

`N_B(s)={o_i}`.

This is impossible from the foundational tight-pair geometry, without any scalar degree estimate. Since `p>=1` and `s in A`, the vertex s has exactly one matched-B neighbour in each of the p tight fibres. These matched neighbours are distinct from the unmatched vertex `o_i`. Under the temporary assumption `(4.1)`, s therefore has at least `p+1` B-neighbours.

### Theorem 6.1 — tight-code source B-degree floor

In this branch every source `s in Y` has at least p matched B-neighbours, and if its omitted pair `s o_i` is an edge then

> `d_B(s)>=p+1>=2`.

Consequently the ROOT certificate `N_B(s)={o_i}` is impossible.

This closes the explicit B-degree-one question left by the previous handoff at definition level, rather than by importing a later scalar bound.

## 7. Structural unit III — the OUT alternative is impossible

Suppose `z in U_o`. Equation `(6.1)` again says s and z have no common matched-B neighbour, because their unique common neighbour `o_i` is unmatched. By Lemma 3.1,

`c(z)=bar c(s)=bar d`.

But every unmatched vertex of code `bar d` belongs by definition to

`U_-=U_{bar d}`.

This contradicts `z in U_o=U\U_-`.

### Theorem 7.1

No outside-unmatched vertex can certify an omitted edge in the surviving orientation. The earlier OUT correction through `H_Y` is therefore not merely expensive in the minimal h=0 full-support model: it is structurally unavailable.

## 8. Structural unit IV — generalized matched-foot localization kills MATCHED

It remains to exclude a matched B-vertex z satisfying `(6.1)`.

The preserved matched-foot localization lemma was stated for a singleton head in A, but its proof uses only the matched fibres. The same proof gives the following exact variant.

### Lemma 8.1 — matched foot with a nonmatched singleton head

Let `s in A`, let `w=q_j^e` be a matched B endpoint, and suppose

- `s w` is a nonedge;
- `N(s) intersect N(w)={h}`;
- the singleton head h is not in the matched layer.

Then

> `c(s)=gamma(w)`.

### Proof

In fibre j, s is nonadjacent to w and therefore chooses the mate of w. In every other tight fibre, if s chose the matched endpoint adjacent to w, that endpoint would be a second common neighbour of s and w, distinct from the nonmatched singleton head h. Hence s chooses the opposite endpoint in every other fibre. This is exactly the definition of `gamma(w)`. `square`

Apply the lemma to `(6.1)`, where the singleton head is the unmatched vertex `o_i`. Since `c(s)=d`, any matched certificate z must satisfy

> `gamma(z)=d`.                                             `(8.1)`

There are exactly g such matched endpoints, one in each gamma fibre counted by `g=g_P`.

Now use the h=0 crossing classification. Every source `s in Y` has x crossing heads in X, exactly k of which use U-witnesses and exactly g of which use matched witnesses. Every matched crossing witness for s must have gamma code d. There are only g gamma-d matched endpoints, so s uses **all** of them. For each such z the graph-fixed pair `(s,z)` already satisfies

> `N(s) intersect N(z)={x_z}`

for its crossing head `x_z in X`.

It cannot simultaneously satisfy `(6.1)`, whose singleton is the distinct unmatched vertex `o_i`.

If `g=0`, equation `(8.1)` already leaves no compatible matched endpoint.

### Theorem 8.2

The MATCHED alternative is impossible for an omitted edge in the minimal full-support h=0 branch.

This is stronger than the predecessor observation that a MATCHED witness would merely add an edge to the rooted-triangle correction.

## 9. Structural unit V — every omitted pair is forced to be a nonedge

We can now close the contradiction.

An omitted pair `s o(s)` which were an edge lies in the triangle `s-x_*-o(s)`. D2C criticality of that edge requires Orientation A or Orientation B. Theorem 5.1 excludes A. In B, the complete physical location trichotomy leaves ROOT, OUT or MATCHED, excluded respectively by Theorems 6.1, 7.1 and 8.2.

Therefore no omitted pair can be an edge.

### Theorem 9.1 — forced omitted-nonedge theorem

In the purified rigid one-code `z=1`, `h=0`, full-support two-omission model,

> **every source is nonadjacent to its unique omitted U_- vertex.**

Equivalently,

> `nu=y`.                                                  `(9.1)`

No injectivity between different edge-criticality witnesses is used. The conclusion is per omitted pair.

This reverses the previous near-equality heuristic: `nu` is not driven toward zero by the scorecard because zero is not realizable. Raw criticality fixes it at its maximum possible value y.

## 10. Structural unit VI — exact ledger collapse after `nu=y`

Substitute `(9.1)` into the exact two-omission ledger. Writing `H=H_X+H_Y`, we obtain

> `Z=Z0+H`,                                                 `(10.1)`
>
> `L_Y=y(p-g+1)+H_Y`,                                      `(10.2)`
>
> `E_-=B+M`,                                                `(10.3)`
>
> `2q+E_U=D0+H`.                                           `(10.4)`

Thus the apparent `-y` savings in both the A--U nonedge count and the U_- slack disappear exactly.

The score floor becomes

> `S>=B+M+max{phi(g), y(p-g+1)+H_Y}`.                     `(10.5)`

The exact pair-local crossing bill is unchanged:

> `2xy<=Ccap_P=R_code(S_P)[g+2S_P/L]`.                    `(10.6)`

The older `(ONE-P)` inequality is correspondingly even less informative here; `(CROWD)` remains an independent aligned lower bound on `S_P`.

The refined residual floor becomes, with `E0=B+M` and `D=D0+H`,

> `q+E_U >= B+M+ceil([D0+H-B-M]_+/2)`.                   `(10.7)`

This is the correct h=0 full-support starting point for the next intersection with exact pair capacity and crowding.

## 11. Structural unit VII — hostile correction: `Q_rest` contains a forced baseline

The previous ledger defined

`Q_rest=Q-e(U_-,U_o)`.

That quantity is exact, but its interpretation as a small residual correction is misleading in a tight-fibre branch.

Let P be the 2p matched vertices. Tightness gives two exact edge counts.

### Lemma 11.1 — forced matched baseline

> `e(G[P])=p(p-1)`,
>
> `e(P,U)=pu`.                                             `(11.1)`

### Proof

For two distinct tight pairs, every endpoint of either pair is adjacent to exactly one endpoint of the other. Hence the `2 x 2` bipartite graph between the two fibres is a perfect matching, contributing two edges. Summing over all unordered fibre pairs gives `2 binom(p,2)=p(p-1)`.

Every unmatched vertex lies outside each tight pair and therefore chooses exactly one endpoint of each of the p fibres, giving p matched neighbours and total `pu` matched--unmatched edges. `square`

Consequently

> `Q=e(G[B])=p(p-1)+pu+e(G[U])`.                          `(11.2)`

Full-support source visibility already gives `e(G[U_-])=0`, so

`e(G[U])=e(U_-,U_o)+e(G[U_o])`.

Therefore

> `Q_rest=p(p-1)+pu+e(G[U_o])`.                           `(11.3)`

In the present branch `p>=1` and `u>=k+1>=2`, so `Q_rest>0` automatically. The predecessor hypothetical equality condition `Q_rest=0` is therefore infeasible and must not be used as a meaningful zero-correction state.

A better genuinely residual triangle variable is

> `Q_o:=e(G[U_o])>=0`.                                    `(11.4)`

Then `(11.2)` reads

> `Q=p(p-1)+pu+e(U_-,U_o)+Q_o`.                           `(11.5)`

Combining with `E_-=B+M` and

`M=(k+1)u_o-e(U_-,U_o)`

gives a second exact cancellation:

### Theorem 11.2 — corrected triangle--slack invariant

> `Q+E_-`
> ` =p(p-1)+pu+B+(k+1)u_o+Q_o`.                           `(11.6)`

The entire `U_- -- U_o` edge choice cancels. The only remaining triangle correction beyond the forced tight-fibre baseline is the genuinely internal outside-unmatched term `Q_o=e(G[U_o])`.

This supersedes the earlier use of `Q_rest` as though it were a small correction variable.

## 12. What survives, what is corrected

The predecessor exact identities themselves remain algebraically valid. What changes is the realizable geometry.

Survives:

- source-visibility purification;
- the two-omission classification;
- the exact formulas before specializing nu;
- exact pair capacity `Ccap_P`;
- `(CROWD)`;
- the `U_- -- U_o` triangle/slack cancellation.

Strengthened:

- Orientation A is impossible without `|Y_i|>=2`;
- ROOT is impossible from tight-fibre transversality;
- OUT is impossible by complementary-code localization;
- MATCHED is impossible by generalized gamma localization plus saturated matched crossing use;
- hence `nu=y` exactly.

Corrected interpretation:

- `Q_rest` contains the forced baseline `p(p-1)+pu`; it is not a zero-able local correction in this branch;
- the old putative state `nu=H_Y=Q_rest=0` is not a realizable equality geometry;
- the correct local triangle correction after removing the baseline is `Q_o=e(G[U_o])`.

## 13. Negative control and trust boundary

`X_3` remains untouched. At its canonical root `u=0`, so the present unmatched-U full-support branch is inactive. Nothing here would exclude the order-12, size-32 hostile control.

The proof does not use the finite source-tuple capacity theorem. It uses the already-preserved tight-pair Boolean representation, pair purity, full-support source visibility, exact h=0 crossing classification, matched-foot gamma localization, and raw D2C edge-criticality. The independent graph-level regression has checked the upstream code/gamma/pair quantities on actual D2C graphs but still lacks a realized rigid `x>=3` fixture; that conditional scope remains explicit.

## 14. Next move

Stay in `z=1`.

1. Replace the old free-`nu` full-support normal form everywhere by the forced specialization `nu=y` and replace `Q_rest` by its forced baseline plus `Q_o`.
2. Intersect the strengthened score floor `(10.5)`, residual floor `(10.7)`, exact pair bill `(10.6)` and `(CROWD)` while retaining `g,S_P,H_X,H_Y,M,Q_o` long enough to avoid another lossy scalar collapse.
3. Test whether the forced +y surcharge closes the h=0 full-support branch asymptotically or leaves a sharply parameterized equality strip.
4. Then compare that surviving strip, if any, with the unloaded common-buffer one-omission model. Do not move to z=2 until both minimal z=1 geometries are exhausted.
