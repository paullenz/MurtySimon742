# One-code first near-saturation layer: `u_{bar d}=k+1`

Date: 2026-09-19

Status: conditional hand-theorem package inside the rigid one-code branch. This continues `ONE_CODE_BIDIRECTIONAL_RESERVOIR.md` and `SATURATED_RESERVOIR_REFINEMENT.md`.

## 1. Setup

Use the same notation. The rigid cut `X--Y` is complete, `Y=A_d`, `A_{bar d}=empty`, `|X|=x`, `|Y|=y`, `g=g_P`, and

`k=(x-g)_+>0`.

Write

`W=U_{bar d}`

and assume the first near-saturated layer

> `|W|=u_-=k+1`.                                          `(Z1)`

Every source `s in Y` uses at least `k` distinct vertices of `W` as crossing witnesses. Since `|W|=k+1`, a source either uses exactly `k` such witnesses and misses one member of `W`, or uses all `k+1`.

Let

`H=e_++e_-`,

where `e_+=e(G[Y union U_d])=e(Y)+e(Y,U_d)` and `e_-=e(G[W])`.

The bidirectional reservoir theorem gives

> `H<=y`.                                                  `(1.1)`

The point below is that the crossing-incidence matrix has only two possible support types, and both admit substantially sharper structure than `(1.1)` alone records.

---

## 2. First unit: support dichotomy

Let `W_cross` be the union of all `W`-vertices actually used as crossing witnesses by sources in `Y`.

### Lemma 2.1 — exact support dichotomy

> `|W_cross|` is either `k` or `k+1`.                     `(SUP)`

If `|W_cross|=k`, then every source uses the same `k`-set `W_0=W_cross`, once each, and the unique vertex

`b in W\W_0`

is unused by every crossing certificate.

If `|W_cross|=k+1`, every vertex of `W` is used by at least one source.

### Proof

One source already uses at least `k` distinct members of the `(k+1)`-set `W`, so the union has size at least `k`; there are no other sizes available. If the union has size exactly `k`, each source needs at least `k` distinct witnesses and therefore uses the entire same `k`-set. `square`

Call the first case the **common-buffer branch** and the second the **full-support branch**.

---

## 3. Second unit: common-buffer geometry

Assume `W_cross=W_0`, `|W_0|=k`, with buffer `b` unused by every crossing certificate.

Every physical pair in `Y x W_0` is already consumed by a crossing certificate. Cross-family physical-pair exclusivity therefore forces every auxiliary certificate counted by `H` to use a pair in

`Y x {b}`.

### Theorem 3.1 — buffer localization

In the common-buffer branch:

1. `W_0` is independent;
2. every edge of `G[W]` is incident with `b`;
3. every such `W`-edge is certified with source `b` and a witness in `Y`;
4. the selected auxiliary objects counted by `H` inject into `Y`, one per source/witness vertex;
5. consequently `H<=y` is realized as a genuine one-buffer capacity, not merely a global count.

### Proof

A same-code edge inside `W_0` must be certified by a source in `W_0` and a witness in `Y` (the U-source localization theorem). That would use a physical `Y x W_0` pair already occupied by a crossing certificate, contradicting physical-pair exclusivity. Thus `W_0` is independent.

Any `W`-edge is therefore `bw` with `w in W_0`. If it were certified with source `w`, its Y-witness pair would again lie in the exhausted `Y x W_0` block. Hence its source must be `b`. Every other auxiliary family already localizes to a `Y x W` physical pair; because all `Y x W_0` pairs are occupied, it too must use `Y x {b}`. Injectivity leaves at most one auxiliary object per `Y` vertex. `square`

This gives a literal saturated core plus one certificate buffer.

---

## 4. Third unit: the saturated core keeps the full unmatched-slack bill

### Theorem 4.1 — common-buffer core slack

For every `w in W_0`,

> `epsilon_w>=p+k-2`.                                     `(CORE-EW)`

Hence

> `E_- >= k(p+k-2)`.                                      `(CORE-E)`

### Proof

Every `w in W_0` is used by all sources in `Y`, so it has exactly one neighbour in `X` and no neighbour in `Y`. The core `W_0` is independent. The most generous remaining coded-layer neighbourhood consists of the buffer `b` plus all unmatched vertices outside `W`; there are

`1+[u-(k+1)]=u-k`

such possible U-neighbours. Thus

`d_{A union U}(w)<=1+(u-k)`.

Since an unmatched vertex satisfies

`d_{A union U}(w)=p+u-1-epsilon_w`,

we obtain `epsilon_w>=p+k-2`. Sum over the `k` core vertices. `square`

Thus adding one unused complementary unmatched vertex does **not** release any of the `k(k-1)` extra U-slack forced by the saturated witness core.

### Corollary 4.2 — common-buffer score floor

The gamma-collision term lies in `L_A` and the core bill lies in `E_U`, so

> `S>=phi(g)+k(p+k-2)`.                                   `(CORE-S)`

This is a safe scorecard floor even before using the extra buffer geometry.

---

## 5. Fourth unit: every buffer use increases the rooted nonedge defect

Let `H=e_++e_-` as above. Each auxiliary object in the common-buffer branch uses a distinct pair `{s,b}` with `s in Y`; that physical pair is a nonedge. The `k` core witnesses already contribute the generic one-code nonedge floor.

### Theorem 5.1 — common-buffer defect surcharge

> `Z >= k(a-1)+H`.                                        `(CORE-Z)`

### Proof

Each of the `k` core vertices has exactly one neighbour in `X`, contributing `x-1` X--U nonedges, for `k(x-1)` total. Every source/core incidence is a Y--U nonedge, giving `yk`. Finally each of the `H` auxiliary buffer pairs is a distinct additional Y--U nonedge. Hence

`Z>=k(x-1)+yk+H=k(a-1)+H`. `square`

Therefore, with

`D_core=k(a-1)+H-u(p-lambda)`,

and `E_core=k(p+k-2)`, the exact residual minimization gives

> `q+E_U >= E_core+ceil([D_core-E_core]_+/2)`.             `(CORE-QE)`

This feeds the number of actual buffer uses directly into forced A-edge mass via

`f=(p-lambda)(p+u)+q+E_U-delta`.

---

## 6. Fifth unit: full-support crossing holes

Assume now `W_cross=W`, so all `k+1` complementary unmatched vertices are used by crossing certificates.

For `s in Y`, let it be **full** if it uses all `k+1` vertices of `W`; otherwise it uses exactly `k` and has one crossing hole. Let

`rho`

be the number of crossing holes. Equivalently, `rho` is the number of sources using exactly `k` witnesses, so

> `0<=rho<=y`.                                             `(6.1)`

The number of crossing source/witness incidences is

> `I=yk+(y-rho)`.                                         `(6.2)`

Every auxiliary selected certificate must use a crossing hole, because every non-hole `Y x W` pair is already consumed by a crossing certificate. Therefore

> `H<=rho`.                                                `(6.3)`

For each `w in W`, write `t_w` for the number of crossing sources using it, `a_w` for the number of auxiliary physical pairs using it, and `d_W(w)` for its degree in `G[W]`. Since every `w` is a crossing witness, it has exactly one neighbour in `X`. Its Y-nonneighbours include the disjoint sets of its `t_w` crossing sources and its `a_w` auxiliary partners. Thus

`d_{A union U}(w)`
` <=1+(y-t_w-a_w)+d_W(w)+[u-(k+1)]`.

Using `d_{A union U}(w)=p+u-1-epsilon_w` gives

> `epsilon_w>=p-y+k-1+t_w+a_w-d_W(w)`.                   `(6.4)`

Summing over all `k+1` members of `W`, with

`sum t_w=I`, `sum a_w=H`, `sum d_W(w)=2e_-`,

proves:

### Theorem 6.1 — full-support slack/crowding identity

> `E_- >= (k+1)(p+k-1)-rho+H-2e_-`.                      `(FULL-E)`

Since `H=e_++e_-`, equivalently

> `E_- >= (k+1)(p+k-1)-rho+e_+-e_-`.                    `(FULL-E2)`

Using `e_-<=H<=rho<=y` gives the safe pure floor

> `E_- >= [(k+1)(p+k-1)-2y]_+`.                          `(FULL-E0)`

This is the first exact price for distributing the crossing witness load over all `k+1` complementary unmatched vertices.

---

## 7. Sixth unit: full support also raises the A--U defect

All `k+1` crossing witnesses have exactly one neighbour in `X`, so

`Z_X>=(k+1)(x-1)`.

The crossing incidences give `I=yk+y-rho` Y--U nonedges, while each of the `H` auxiliary hole uses is an additional distinct Y--U nonedge. Therefore:

### Theorem 7.1 — full-support defect floor

> `Z >= k(a-1)+(a-1)-rho+H`.                             `(FULL-Z)`

In particular,

> `Z >= k(a-1)+(x-1)`.                                   `(FULL-Z0)`

### Proof

Add

`(k+1)(x-1)+(yk+y-rho)+H`

and use `a=x+y`. The relaxed form follows from `rho<=y` and `H>=0`. `square`

Thus using the extra unmatched vertex is not free even if its slack can be softened by same-code edges: full support contributes at least an additional `x-1` units of A--U defect beyond the generic `k(a-1)` one-code floor.

Let

`E_full=[(k+1)(p+k-1)-2y]_+`,

`D_full=k(a-1)+(x-1)-u(p-lambda)`.

Then the exact residual bridge gives

> `q+E_U >= E_full+ceil([D_full-E_full]_+/2)`.            `(FULL-QE)`

Again this translates directly into forced A-edge mass `f`.

---

## 8. Seventh unit: a compact `z=1` score gate

The two support branches now have independent U-slack floors. Retain the disjoint gamma-collision floor `L_A>=phi(g)`.

Every `z=1` survivor must satisfy **at least one** of:

### Common-buffer gate

> `phi(g)+k(p+k-2) <= C0`.                                `(Z1-CORE)`

### Full-support gate

> `phi(g)+[(k+1)(p+k-1)-2y]_+ <= C0`.                    `(Z1-FULL)`

with `k=x-g>0` and `k+1<=u`.

These gates deliberately omit `(ONE-P)`, `(CHAN-P)`, the exact reservoir cylinder `(CYL)`, and the stronger `rho,H,e_+,e_-` forms. Failure of both therefore robustly excludes the first near-saturated layer; survival is only a signal for where the exact geometry must next be used.

A bounded diagnostic over `3<=p<=18`, `1<=u<=18` records:

- `106,368` old one-code population-feasible states in the common comparison box;
- `86,820` states have at least one `k>0`, `k+1<=u` gamma choice surviving the older shared gamma/U floor;
- `76,463` retain a common-buffer choice under `(Z1-CORE)`;
- `77,310` retain a full-support choice under `(Z1-FULL)`;
- only `78,167` retain either `z=1` support type.

So the exact first-near-saturation geometry eliminates `8,653` of the states that previously admitted a `z=1` gamma choice under the older shared floor. These are arithmetic diagnostics of the hand inequalities, not counts of realizable D2C graphs.

---

## 9. Trust boundary and next move

The support dichotomy and common-buffer/full-support inequalities are hand deductions from the already-regressed one-code certificate interface. The bounded actual-graph corpus still has no positive rigid-cut fixture with `x>=3`; this entire branch remains conditional structural mathematics.

The next local move should use the **unrelaxed** variables in whichever `z=1` support type survives:

1. common-buffer: combine `(CORE-Z)` with the fact that every auxiliary object is routed through a single buffer and classify whether the buffer can simultaneously support internal-Y traffic, `Y--U_d` edges and the star `G[W]` without forcing additional buffer slack;
2. full-support: retain `rho,H,e_+,e_-` in `(FULL-E)` and `(FULL-Z)` rather than replacing them by `y`; the same hole budget controls both slack relief and residual defect, which should permit an exact two-variable elimination;
3. only after `z=1` is exhausted move to `z=2` or back to the non-rigid Hall branch.

`X_3` remains outside this branch (`u=0` at the canonical root), so the mandatory order-12 hostile control is unaffected.
