# Rigid Hall cuts — private-coordinate normal form for matched singleton witnesses

Date: 2026-09-20

Status: **same-session structural lemma** conditional on the exact rigid Hall event `M_X=E_X=0`, `x=|A_X|>=3`. This refines the singleton-gamma resource theorem and is intended as a bridge back to the rooted Hamming-slot ledger.

## 1. Setup

Fix a represented outside source code d in Y. Let

`M_d`

be the set of tight matched endpoints w satisfying

- `gamma(w)=d`;
- `|N(w) cap A_X|=1`.

Put `mu_d=|M_d|`. For `w in M_d`, write `h(w)` for its unique A_X-neighbour.

Because the two endpoints of one tight fibre partition A_X and x>=3, at most one endpoint of a fibre lies in the union of all `M_d`. Hence distinct elements of `M_d` lie in distinct fibres.

## 2. Each matched singleton is a private Boolean coordinate

Let w in M_d lie in fibre i, and let `bar w` be the opposite endpoint of that fibre. Since `gamma(w)=d`, a d-coded source is nonadjacent to w and adjacent to `bar w` in fibre i. The singleton condition says

`N(w) cap A_X={h(w)}`.

Therefore:

- `h(w)` chooses w in coordinate i and so differs from d at i;
- every other vertex of A_X chooses `bar w` and so agrees with d at i.

Thus fibre i is a **private coordinate** for the head h(w) relative to source code d:

> `c(h(w))_i != d_i`,
> `c(x')_i=d_i` for every `x' in A_X\{h(w)}`.             `(PC-1)`

The head map `h:M_d -> A_X` is injective. If two distinct singleton matched endpoints had the same head, that is allowed physically, but they would represent two distinct private coordinates for that head; what is impossible is one endpoint having two heads. For witness accounting, a fixed source uses at most one matched endpoint per crossing head, so any chosen matched-witness subset gives an injective coordinate-to-head assignment after redundant same-head endpoints are discarded.

## 3. Chosen matched witnesses give a private-coordinate system

Fix one d-coded source s. Its x crossing edges require x distinct witnesses. Suppose m of them are matched endpoints. Their heads are necessarily distinct because each crossing edge has a different head. Therefore those m witnesses occupy m distinct fibres and give m distinct heads, each with its own private coordinate relative to d.

Consequently, if `H_s subseteq A_X` is the set of heads whose selected witness for s is matched, then

> `|H_s|=m<=mu_d`,

and there is an injection

> `i_s:H_s -> [p]`

such that for every head h in H_s,

> h is the unique A_X vertex whose code differs from d in coordinate `i_s(h)`. `(PC-2)`

This is stronger information than the scalar bound `m<=mu_d`.

## 4. Hamming separation forced by private coordinates

If two distinct heads h1,h2 both lie in H_s, then at coordinate `i_s(h1)` the first differs from d and the second agrees with d; at coordinate `i_s(h2)` the reverse holds. Hence

> **`d_H(c(h1),c(h2))>=2`.**                              `(PC-HD2)`

More generally, if a set H of heads is covered by distinct matched singleton witnesses for one source code d, then every h in H has a coordinate private against all of `A_X\{h}`. In particular the restricted code family `{c(h):h in H}` contains an explicit identity submatrix after complementing columns according to d.

If all x heads are matched-covered for a d-coded source (equivalently that source uses no U-witness), then

> **p>=x and the A_X code matrix contains an x by x identity minor relative to d.** `(PC-ID)`

The familiar population obstruction `x<=p+u` is therefore the scalar shadow of a stronger dichotomy:

- unmatched U-witnesses pay physical population/nonedge/slack;
- matched witnesses pay **private Boolean coordinates**.

## 5. Link to the rooted Hamming-slot ledger

The private-coordinate normal form suggests a route not present in the existing rigid witness-deficit theorem. For any internal A_X edge hh', the local rooted Hamming budget charges its code distance to unused rooted slots. When both endpoints are in one matched-covered head set, `(PC-HD2)` supplies at least two units of Hamming distance before any other coordinates are considered.

Thus a dense internal A_X graph among matched-covered heads forces extra rooted-slot mass, while replacing matched coverage by U coverage triggers the gamma-budget nonedge/slack bills. This is a genuine **matched-coordinate versus U-defect tradeoff**.

A next theorem should quantify this at the level of a chosen source code d:

- let `m_d^*` be the maximum number of heads simultaneously covered by singleton matched witnesses of gamma d;
- the covered head set has a private-coordinate system and min Hamming distance at least two;
- the remaining `x-m_d^*` heads require complementary U witnesses;
- combine the resulting internal-X Hamming cost with `Z_X`, `Z_Y`, and `E_U` before total-score aggregation.

This may be the right structural mechanism for explaining why the bounded actual-D2C regression sees no positive rigid complete Hall-cut fixture, rather than attempting another unconstrained random construction search.