# Saturated one-code reservoir: forced slack and residual feedback

Date: 2026-09-19

Status: follow-on hand theorem to `ONE_CODE_BIDIRECTIONAL_RESERVOIR.md`.

## 1. Why revisit the equality case immediately

The bidirectional-reservoir theorem shows that the natural equality parameter is

`z=u_{\bar d}-k`.

A deliberately generous diagnostic of the new cylinder gate found that, among the bounded states which still survive that relaxed gate, the minimizing relaxed geometry overwhelmingly chooses `z=0`. That makes the saturated case load-bearing rather than decorative. The equality classification already gives a complete witness transversal; the remaining degree consequences can be extracted exactly.

The notation is unchanged:

- `Y=A_d`, `|Y|=y`;
- `U_-=U_{\bar d}`, `u_-=k>0`;
- `U_+=U_d`, `u_+=|U_+|`;
- `g=g_P`, `k=x-g` (hence `g<x` in the nontrivial saturated branch);
- the cut `X--Y` is complete;
- `Y`, `U_+`, and `U_-` are independent in the senses proved in the saturation theorem, and there are no `Y--U_+` edges;
- every pair in `Y x U_-` is a used source/witness nonedge;
- each vertex of `U_-` has exactly one neighbour in `X`;
- the `g+k=x` matched/unmatched crossing witnesses form a bijection with the heads in `X`.

## 2. New unit: every saturated unmatched witness pays `k-1` extra slack

### Theorem 2.1 — saturated unmatched slack

For every `w in U_-`,

> `epsilon_w >= p+k-2`.                                   `(SAT-EW)`

Consequently

> `E_- >= k(p+k-2)`.                                      `(SAT-E)`

### Proof

For an unmatched vertex,

`d_{A union U}(w)=p+u-1-epsilon_w`.

In the saturated model, `w` has exactly one neighbour in `A`, namely its assigned head in `X`; it has no neighbours in `Y`; and `U_-` is independent. Thus among the coded layer `A union U`, the vertex `w` has at most

`1+(u-k)`

neighbours: one in `X` and every vertex of `U\U_-` in the most generous case. Therefore

`p+u-1-epsilon_w <= 1+u-k`,

which rearranges to `(SAT-EW)`. Summing over the `k` vertices of `U_-` proves `(SAT-E)`. `square`

The previous generic one-code floor in the `p-y>=1` branch was `E_- >= k(p-1)`. Saturation therefore forces the additional exact payment

> `k(k-1)`                                                 `(SAT-BONUS)`

before any other U-slack is counted.

## 3. New unit: the outside sources also acquire a direct degree bill

### Theorem 3.1 — saturated source slack

Every `s in Y` satisfies

> `epsilon_s >= p-g+u_+`.                                 `(SAT-LY-PT)`

Hence

> `L_Y >= y(p-g+u_+) >= y(p-g)`.                         `(SAT-LY)`

### Proof

An A-vertex has

`d_{A union U}(s)=p+u-epsilon_s`.

In the saturated model, `s` is adjacent to every vertex of `X`, giving `x` neighbours. It has no neighbour in `Y\{s}` because `Y` is independent; no neighbour in `U_-` because every `Y x U_-` pair is a certificate nonedge; and no neighbour in `U_+` because `e(Y,U_+)=0`.

Thus even if `s` is adjacent to every remaining unmatched vertex, its coded-layer degree is at most

`x+(u-k-u_+)`.

Therefore

`p+u-epsilon_s <= x+u-k-u_+`,

so

`epsilon_s >= p-x+k+u_+ = p-g+u_+`.

Sum over `Y`. `square`

This payment is qualitatively different from same-code crowding: it comes directly from the complete cut plus the exhausted complement reservoir.

## 4. Saturated scorecard theorem

Retain the gamma-collision floor

`L_A>=phi(g)`,

where `phi(g)=g(g-1)` for `g>=3` and `0` for `g<=2`.

Since `L_Y` is part of `L_A` while `E_-` is part of `E_U`, Theorems 2.1 and 3.1 give:

### Theorem 4.1 — saturated scorecard floor

> `S=L_A+E_U`
> ` >= max(phi(g), y(p-g+u_+)) + k(p+k-2)`.               `(SAT-SCORE+)`

In particular, discarding `u_+>=0`,

> `S >= max(phi(g), y(p-g)) + k(p+k-2)`.                 `(SAT-SCORE)`

For an above-`M(n)` candidate, `S<=C0`, so every saturated one-code survivor must satisfy

> `max(phi(g), y(p-g)) + (x-g)(p+x-g-2) <= C0`,          `(SAT-GATE)`

for some integer `0<=g<x` with `x-g<=u`.

This is an explicit one-variable equality-branch gate. It is stronger than the previous shared gamma/U floor by the `k(k-1)` unmatched-witness penalty and, independently, by the direct source-degree bill `y(p-g)`.

## 5. Residual defect feedback strengthens automatically

The exact one-code nonedge floor remains

`Z>=k(a-1)`.

Put

`D_sat=k(a-1)-u(p-lambda)`.

The new U-slack floor

`E_sat=k(p+k-2)`

can be inserted directly into the exact integer residual minimization:

> `q+E_U >= E_sat+ceil([D_sat-E_sat]_+/2)`.               `(SAT-QE)`

Hence

> `f >= (p-lambda)(p+u)`
> `     +E_sat+ceil([D_sat-E_sat]_+/2)-delta`.            `(SAT-F)`

For an above-threshold candidate, one may replace `delta` by `D_M-1` exactly as in the preserved rigid residual theorem.

This is a genuine strengthening of the forced A-edge mass in the saturated equality geometry. No extra lower bound for `Q` is asserted without separately controlling how the new payment splits between `q` and `E_U`.

## 6. Diagnostic effect

Over the same coarse bounded box `3<=p<=18`, `1<=u<=18` used by the one-code diagnostics:

- `106,368` old population-feasible states are present;
- `89,400` have at least one `k>0` gamma choice surviving the older shared gamma/U score floor in the saturated subcase;
- after imposing `(SAT-SCORE)`, only `66,402` retain a saturated `k>0` gamma choice;
- therefore `22,998` previously saturation-compatible states are eliminated by the exact saturated degree geometry.

These figures are diagnostics of the hand inequality, not graph counts. Their value is strategic: the branch to which the relaxed reservoir gate most often retreats (`u_-=k`) is not a soft equality escape. Once equality is used fully, it acquires a substantial additional scorecard and residual cost.

## 7. Next local target

The next coherent step is **not** another global scalar scan. It is the first near-saturated layer

`u_-=k+1`.

There the bidirectional reservoir allows only

`e_++e_-<=y`,

so the two same-code cylinders have at most one block of `y` edge room. The useful question is whether the saturated transversal can be perturbed by a single extra complementary unmatched vertex without either:

1. forcing enough same-code edge mass to consume that whole block; or
2. reproducing most of the saturated degree-slack penalty.

That `z=1` classification is now the highest-value continuation of the rigid one-code line.
