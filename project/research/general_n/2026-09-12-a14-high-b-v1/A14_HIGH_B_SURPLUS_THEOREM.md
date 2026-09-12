# Fourteen-label high-b surplus theorem

12 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate infinite-family structural theorem inside the canonical selected/residual bridge. Independent specialist review, novelty assessment and independent computational reproduction remain OPEN.**

## 1. Statement

Use the canonical bridge parameters

\[
a=n-1-\Delta=14,\qquad b=\Delta,
\qquad t=e(G)-b(a+1)=e(G)-15b.
\]

Assume `b>=17`.

Then the current candidate theory gives

\[
\boxed{t\le1\qquad(b\ge17),}
\tag{1.1}
\]

and more strongly

\[
\boxed{t\le0\qquad(b\ge20).}
\tag{1.2}
\]

Equivalently,

\[
e(G)\le15\Delta+1
\qquad\text{when }a=14,\ \Delta\ge17,
\]

and

\[
\boxed{e(G)\le15\Delta}
\qquad\text{when }a=14,\ \Delta\ge20.
\tag{1.3}
\]

Since `n=b+15`, (1.3) is an infinite family covering every

\[
n\ge35,\qquad \Delta=n-15.
\]

The theorem is a synthesis of the fourteen-label hand tail theorem, the fixed graph-level nine-term monotone potential, a few threshold-equality hand contradictions, and finitely many exact base cases at `b=17,...,21`.

## 2. Scalar reduction

The fourteen-label hand theorem proves

\[
Q(s)\le23.
\]

The canonical bridge gives, for positive surplus,

\[
Q(s)\ge b+2t.
\]

Hence universally in the `a=14` band,

\[
\boxed{b+2t\le23.}
\tag{2.1}
\]

This already leaves only a finite set of low-`b` positive-surplus boundary cases.

## 3. No surplus t>=2 for any b>=17

Suppose `t>=2`. By (2.1), only the following cases are possible:

```text
b=17: t=2 or 3,
b=18: t=2,
b=19: t=2.
```

All larger `b`, and `b=17,t>=4`, are scalar-impossible.

The remaining cases are closed as follows.

### 3.1 b=17

- `b=17,t=3`: the fourteen-label equality theorem leaves exactly
  `3^14`, `3,4^13`, `4^14`; all three are excluded by the hand core/threshold arguments preserved under
  `project/research/n32/2026-09-11-hand-route-v1/`.
- `b=17,t=2`: the exact N32 frontier has 71 demand profiles. The 70 positive-demand profiles expand to 154 residual-tail states and are all excluded by the nine-term potential; the sole zero-demand profile `0,3^13` is excluded by a hand threshold-equality contradiction. See
  `project/research/n32/2026-09-12-t2-frontier-v1/`.

### 3.2 b=18,t=2

This is the N33 equality frontier. There are 21 demand profiles and 29 residual-tail states. The shifted nine-term potential excludes 25 exactly; the remaining four are excluded by hand. See

`project/research/n33/2026-09-12-candidate-v1/`.

### 3.3 b=19,t=2

Now `b+2t=23`, so equality in the fourteen-label score theorem is forced. The only demand profiles are

\[
3^{14},\qquad 3\,4^{13},\qquad 4^{14}.
\]

Their monotone-minimal residual profiles are respectively

```text
1^9,2,3^9,
1^8,3,4^10,
1^8,4^11.
```

There is no residual-tail slack. The same graph-level nine-term potential used at `b=17,18`, with only the `v=b-h` coordinates shifted, exactifies all three states. The preservation checker in this directory verifies the three strict gaps in integer arithmetic.

Thus `t>=2` is impossible for every `b>=17`, proving (1.1).

## 4. No positive surplus for b>=20

By Section 3 it remains only to exclude `t=1`.

Equation (2.1) leaves only

```text
b=20,t=1,
b=21,t=1.
```

For `b>=22`, even `t=1` would give `b+2t>=24`, contradicting `Q<=23`.

### 4.1 b=21,t=1

Again `Q=23` is forced, so only the three score-equality profiles occur. The same shifted graph-level potential exactifies all three directly.

### 4.2 b=20,t=1: finite frontier

Here `Q>=22`. The fourteen-label score frontier consists of

```text
Q=22 : 18 demand profiles,
Q=23 :  3 demand profiles.
```

After monotone residual-tail closure and the one possible slack increment on the `Q=23` rows, this gives exactly

```text
29 (s,rho) states.
```

The same graph-level nine-term potential excludes 23/29 with exact integer acceptance. The six uncovered states are:

```text
A  s=(3,4,5^12),  rho=(1^8,3,4,5^10)
B  s=(3,5^13),    rho=(1^8,3,5^11)
C  s=(4^9,5^5),   rho=(1^8,2,4^6,5^5)
D  s=(4^2,5^12),  rho=(1^8,4^2,5^10)
E  s=(4,5^13),    rho=(1^8,4,5^11)
F  s=(5^14),      rho=(1^7,2,4,5^11).
```

All six are impossible by hand.

## 5. Hand closure of the six b=20 states

We use the standard threshold-capacity notation. For threshold `h`, let

```text
Z_h={u:rho_u>=h},
ell_u = actual selected incidences from u carrying demand >=h,
J={u in Z_h: ell_u>h}.
```

Heavy arcs from `J` have their supplements in `Z_h`. When

\[
W_h=C_h(z_h),
\]

equality holds throughout the threshold-capacity chain: the actual number of heavy incidences equals `W_h`, relevant non-`J` sources are saturated at `h`, and the pair-capacity equality determines `|J|` up to the two adjacent possibilities from the standard gap formula.

### A: (3,4,5^12)/(1^8,3,4,5^10)

At `h=4`,

```text
W_4=64,
z_4=11.
```

The unique `rho=4` source cannot carry a demand-five label and there is only one demand-four label, so it contributes at most one heavy incidence and cannot lie in `J`.

If `j=|J|<=10`, the other ten non-`J` sources contribute at most four each and the special source contributes at most one. Thus

\[
\sum_{Z_4}\ell_u
\le1+4(10-j)+11j-\frac{j(j+1)}2.
\]

The maximum is 62, below `W_4=64`. Contradiction.

### B: (3,5^13)/(1^8,3,5^11)

At `h=4`,

\[
W_4=65=C_4(11).
\]

Equality gives `j=6` or `7`, so at least

\[
65-(11-j)4\ge45
\]

heavy arcs have supplements inside `Z_4`. Hence

\[
\sum_{Z_4}p_u\ge45.
\]

Every high source has `rho=5`, and exact heavy-label degree gives `p_u<=4`; hence the upper bound is 44. Contradiction.

### C: (4^9,5^5)/(1^8,2,4^6,5^5)

At `h=3`,

\[
W_3=61=C_3(11).
\]

Equality gives `j=7` or `8`, so at least

\[
61-(11-j)3\ge49
\]

heavy arcs have supplements in `Z_3`.

All labels are heavy, so equality forces `x_i=s_i`; endpoint load and source forcing give

\[
p_u\le\rho_u-1.
\]

There are six `rho=4` and five `rho=5` sources in `Z_3`, so

\[
\sum_{Z_3}p_u\le6\cdot3+5\cdot4=38,
\]

contradicting the lower bound 49.

### D: (4^2,5^12)/(1^8,4^2,5^10)

At `h=5`,

\[
W_5=60=C_5(10).
\]

Thus every one of the ten `rho=5` sources is heavy-active and every demand-five label has actual selected degree five.

At `h=4`, the two `rho=4` sources can use only the two demand-four labels, so together they contribute at most four heavy incidences. Since `W_4=68`, at least 64 heavy arcs originate from the ten degree-five sources, all of which lie in the `h=4` set `J`. Therefore

\[
\sum_{Z_4}p_u\ge64.
\]

The ten degree-five sources satisfy `p_u<=4` from an exact demand-five incidence. The two degree-four sources satisfy the universal source bound

\[
p_u\le\rho_u+b-a-1=4+5=9.
\]

Hence

\[
\sum_{Z_4}p_u\le10\cdot4+2\cdot9=58,
\]

contradiction.

### E: (4,5^13)/(1^8,4,5^11)

At `h=2`,

\[
W_2=69=C_2(12).
\]

Equality gives `j=9` or `10`, hence at least

\[
69-(12-j)2\ge63
\]

heavy arcs have supplements in `Z_2`.

All labels are heavy and equality gives `x_i=s_i`; hence `p_u<=rho_u-1`. Therefore

\[
\sum_{Z_2}p_u\le3+11\cdot4=47,
\]

contradiction.

### F: 5^14/(1^7,2,4,5^11)

At `h=5`,

\[
W_5=70=C_5(11).
\]

All selected arcs are sourced in the eleven `rho=5` sources, every label has selected degree exactly five, and every core source satisfies `p_u<=4`. Let `J={u:\ell_u>5}`. Equality gives `|J|=5` or `6`.

If `|J|=6`, the five non-`J` sources have total selected outdegree at most 25. All arcs leaving the eleven-source core must originate there. But `sum p_core<=44`, while total selected indegree is 70, so at least 26 arcs must leave the core. Contradiction.

If `|J|=5`, equality in the threshold pair-capacity step forces all 40 unordered core pairs incident with `J` to be used by arcs sourced in `J`. In particular every one of the six non-`J` core vertices receives an arc from each of the five `J` sources, so `p_u>=5` for every non-`J` core vertex. This contradicts `p_u<=4`.

Thus all six states are impossible.

## 6. The common graph-level potential

The exact base cases use one fixed potential in the original `(d,h)` coordinates:

```text
F(d,h) = 4 1[d>=2]
       + 2 1[d>=2,h<=11]
       +   1[d>=2,h<=9]
       +   1[d>=2,h<=7]
       +   1[d>=2,h<=4]
       +   1[d>=2,h<=3]
       +   1[d>=3,h<=8]
       +   1[d>=3,h<=6]
       +   1[d>=3,h<=5].
```

This function is independent of `b`. In BC coordinates `v=b-h`, only the rectangle `V` thresholds shift with `b`.

Thus the N32, N33 and new `b=19,20,21` finite certificates are not unrelated fitted potentials: they are instances of one fixed graph-level monotone transport function.

## 7. What is genuinely general here

The theorem has two layers:

1. the hand scalar inequality `b+2t<=23`, valid for every `a=14` bridge image;
2. a finite boundary verification at `b=17,...,21`, using one common graph-level potential plus threshold-equality hand lemmas.

Once those five boundary values are settled, every larger `b` follows automatically from the scalar theorem. Therefore (1.2)-(1.3) are genuine infinite-family consequences, not extrapolation from finitely many tested orders.

## 8. Trust boundary

The result remains conditional on:

- the canonical selected/residual bridge;
- the fourteen-label threshold-tail hand theorem;
- the monotone potential-certificate lemma;
- the exact finite envelope semantics in the cited N32/N33 packages and the checker in this directory;
- the threshold-capacity equality arguments displayed above.

No floating-point infeasibility is accepted as a proof event.