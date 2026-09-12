# Hostile internal audit — 12 September general-theory extraction

12 September 2026. Same-assistant hostile audit. **Not independent external mathematical review.**

## Verdict

**NO BLOCKING FLAW FOUND in the newly extracted balanced-degree theorem, the a=14 high-b surplus theorem, or the fifteen-/sixteen-label tail theorems.**

The work does, however, expose a clear methodological boundary: the original layerwise safe-interval clipping test becomes too crude from `a=17` onward and genuine `6->5` clipping failures appear by `a=23`. Any claim of a uniform all-a tail theorem would therefore be premature.

## 1. Balanced-degree theorem

Source:

`project/research/general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md`

### Coverage

At the Turan edge level, average degree forces `Delta>=ceil(n/2)`. The theorem treats the minimum possible value `Delta=ceil(n/2)`.

- Even `n=2k`: handshaking gives `e<=k^2`; equality is `k`-regular. In the non-bipartite dense case the dominating-edge theorem removes dominating edges, while every critical-edge witness would have degree sum at most `2k-1`, contradicting regular sum `2k`. Hence equality is the bipartite graph `K(k,k)`.
- Odd `n=2k+1`: the deficit/witness capacity argument is symbolic and replaces the separate N29/N31/N33 tables.

### Witness-capacity hardening

The initial theorem text compressed the step

```text
e <= C(h,2)+h(n-h)+o(o-1)
```

too aggressively. `WITNESS_CAPACITY_HARDENING.md` makes the injection explicit:

1. actual edges incident with `L` contribute `E_L`;
2. a two-step witness meeting `L` and covering an edge outside `L` is a missing `L-X` pair and covers at most one outside edge;
3. `E_L + M_LX <= C(h,2)+h(n-h)` because actual and missing cross-pairs partition the `L-X` pairs;
4. a witness disjoint from `L` must be an `O-O` pair and has capacity at most two.

No hidden extra `L-X` capacity remains.

### Endpoint algebra

For odd `n=2k+1`, with deficit budget `T`, the relaxed capacity is

```text
F_T(h)=T^2-T+(7/2)h^2+(2k+5/2-4T)h,
```

a convex quadratic. Thus only the two endpoint values matter. The displayed parity formulas at `T=k+1` and `T=k-1` were independently rederived; `check_balanced_degree.py` checks them exactly for `3<=k<10000` but is not a proof premise.

**Audit conclusion:** the all-order reduction

```text
any counterexample must have Delta >= ceil(n/2)+1
```

is internally justified, conditional on the established witness lemmas and the published dominating-edge theorem.

## 2. Fourteen-label high-b family

Source:

`project/research/general_n/2026-09-12-a14-high-b-v1/A14_HIGH_B_SURPLUS_THEOREM.md`

The universal scalar input is the hand theorem

```text
Q<=23,
Q>=b+2t.
```

Thus `b+2t<=23`.

### t>=2

The only non-scalar scopes are

```text
(b,t)=(17,2),(17,3),(18,2),(19,2).
```

The first three are already frozen in the N32/N33 packages. The new `(19,2)` scope has only the three `Q=23` equality profiles, and all three exactify under the same graph-level nine-term potential.

Hence `t<=1` for every `b>=17`.

### t=1 for b>=20

Only `b=20,21` survive the scalar inequality.

- `b=21`: all three equality states exactify directly.
- `b=20`: 29 residual-tail states; 23 exactify under the same potential and six are hand-closed.

The six hand contradictions were recomputed. Their decisive inequalities are respectively:

```text
A: refined h=4 capacity 62 < W4=64;
B: p(Z4)>=45 but p(Z4)<=44;
C: p(Z3)>=49 but p(Z3)<=38;
D: p(Z4)>=64 but p(Z4)<=58;
E: p(Z2)>=63 but p(Z2)<=47;
F: h=5 equality gives j=5 or6; j=6 needs >=26 external arcs but permits <=25, while j=5 saturates every J--nonJ core pair and forces p>=5 against p<=4.
```

For `b>=22`, `t=1` is scalar-impossible. Therefore `t<=0` for all `b>=20`.

The new checker `check_a14_high_b.py` reuses the already-preserved N33 envelope implementation but shifts only `v=b-h`; it does not fit a new global potential. New exact scope counts are:

```text
b=19,t=2 : 3/3 exact;
b=20,t=1 : 23 exact + 6 hand;
b=21,t=1 : 3/3 exact.
```

**Audit conclusion:** the infinite family `a=14,b>=20 => e<=15b` is a genuine consequence of a universal scalar theorem plus finitely many exact boundary cases, not extrapolation from N32/N33.

## 3. Fifteen-label theorem

Source:

`project/research/general_n/2026-09-12-fifteen-label-tail-v1/FIFTEEN_LABEL_TAIL.md`

Claim:

```text
D<=11,
Q<=26,
equality exactly 3^2 4^13 and 4^15.
```

### Clipping

Levels `h>=10` are nonpositive by the same exact quadratic used previously. The safe-interval clipping table for

```text
9->8->7->6->5->4
```

was independently recomputed; every lower-level guaranteed gain is at least the disappearing loss.

### Terminal domain

After clipping, the state is determined by

```text
0<=N4<=N3<=N2<=15,
```

only 816 triples. Exact substitution gives maximum `D=11` only at

```text
(N2,N3,N4)=(15,15,13),(15,15,15).
```

The displayed `5->4` preimage lists contain no `D=11` row, completing equality classification.

`check_fifteen_label_tail.py` checks the proof-critical finite arithmetic with standard-library integer operations. The separate C++ scan over all 77,558,760 nondecreasing demand multisets reproduces `Qmax=26` and exactly the two equality profiles; it is corroborative only.

**Audit conclusion:** no blocking flaw found. The theorem genuinely extends the source-independent tail sequence to `a=15`.

## 4. Sixteen-label theorem

Source:

`project/research/general_n/2026-09-12-sixteen-label-tail-v1/SIXTEEN_LABEL_TAIL.md`

Claim:

```text
D<=13,
Q<=29,
equality exactly 4^16 and 5^16.
```

Levels `h>=11` are nonpositive. The safe clipping chain

```text
10->9->8->7->6->5
```

has no loss: the only tight row is `(M,k)=(6,11)`, where disappearing loss and guaranteed lower gain are both one.

The terminal max-five domain has 4,845 quadruples and exact maximum `D=13` only at

```text
(16,16,16,0),
(16,16,16,16).
```

The sixteen `6->5` preimages of `5^16` all have `D<=10`, so no higher-demand equality vector survives.

The first committed version of `check_sixteen_label_tail.py` contained a **packaging-only parse bug** (a stray `global A`). It was caught before any result was promoted and corrected in commit `ad2a7183487bb2951f873a3b3fdc6df4e785789d`. The theorem text and arithmetic were unaffected. The corrected checker also reproduces the first false alarm in the unmodified `a=17` safe-interval method.

**Audit conclusion:** no blocking mathematical flaw found; the parse bug is preserved in commit history and explicitly documented here.

## 5. What does not generalise automatically

The simple layerwise safe-interval method is not an all-a theorem.

At `a=17`, the row `(M,k)=(6,11)` has safe bound

```text
loss=1,
guaranteed independent lower-level gain=0.
```

A joint compatibility scan over all 462 actual lower-demand multisets shows this is only a false alarm: actual clipping increases `D` by 2 to 4.

However the same issue proliferates as `a` grows. Joint scans show genuine `6->5` clipping failures by `a=23`, for example

```text
s=6^23:
D(before)=31,
D(after to 5^23)=30.
```

Therefore a uniform theorem obtained merely by repeating the existing safe clipping architecture would be invalid. From `a=23` onward the terminal cap itself must adapt, or a stronger joint smoothing argument is needed.

This is the main research lesson of the step-back phase.

## 6. Highest-value external review targets

1. the order-independent witness-capacity injection in `WITNESS_CAPACITY_HARDENING.md`;
2. the use and exact scope of the published dominating-edge theorem in the balanced-degree result;
3. the common potential-certificate semantics across the `a=14` boundary scopes;
4. the finite but proof-critical clipping/terminal tables at `a=15,16`;
5. the canonical selected/residual bridge underlying every graph transfer.

## 7. Bottom line

The step-back programme has produced genuine compression:

- three odd fixed-order witness tables become one all-order theorem;
- N32/N33 potential geometry becomes an infinite `a=14` high-b theorem;
- the source-independent tail sequence extends symbolically to `a=15,16`;
- the first true limitation of the current clipping architecture has been located rather than hidden.

Independent specialist review remains essential before any of these candidate structural theorems are treated as established.