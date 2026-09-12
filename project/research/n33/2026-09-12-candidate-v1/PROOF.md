# Murty–Simon at n=33: candidate proof route

12 September 2026. Research direction: Paul Lenz. Mathematical development, implementation and internal checking: ChatGPT/Geeps.

**Status: complete candidate fixed-order route. Independent mathematical review, novelty assessment and independent computational reproduction remain OPEN.** The unrestricted Murty–Simon conjecture is not claimed.

## 1. Candidate statement

Let `G` be a finite simple diameter-two edge-critical graph on 33 vertices. The candidate theorem is

\[
e(G)\le 272=\left\lfloor\frac{33^2}{4}\right\rfloor,
\]

with equality if and only if

\[
G\cong K_{16,17}.
\]

A bipartite diameter-two graph is complete bipartite. We therefore treat the dense non-bipartite case.

At `m=e(G)>=272`, average degree gives `Delta>=17`. The Dailly–Foucaud–Hansberg dominating-edge theorem gives at most `floor(33^2/4)-2=270` edges for the relevant non-bipartite dominating-edge case, so every non-bipartite graph in the target range has no dominating edge.

Put

```text
a = 32-Delta,
b = Delta,
t = m-b(33-b).
```

## 2. Delta=17: hand upper bound and equality

Assume `Delta=17`. Put

```text
epsilon_x = 17-d(x),
L = {x: epsilon_x>=2},
O = {x: epsilon_x=1},
h = |L|,
o = |O|,
T = 33*17-2m.
```

Because there is no dominating edge, every direct or two-step witness pair `xy` satisfies

\[
d(x)+d(y)\le32,
\]

so every witness has total deficit at least two. Hence

\[
2h+o\le T. \tag{2.1}
\]

Exactly as in the N29/N31 witness-deficit argument, count all edges incident with `L` directly. Every remaining critical edge is covered either by an `O-O` witness (capacity at most two) or by a missing `L-X` witness (capacity at most one). Therefore

\[
m\le {h\choose2}+h(33-h)+o(o-1). \tag{2.2}
\]

### 2.1 No graph above 272 edges

At `m>=273`, one has `T<=15`. Maximising (2.2) under `2h+o<=15` gives, for `h=0,...,7`,

```text
210, 188, 173, 165, 164, 170, 183, 203.
```

Every value is below 273. Thus `Delta=17` is impossible above the Turan number.

### 2.2 Equality forces K(17,16)

At `m=272`, `T=17`. The maxima of (2.2), for `h=0,...,8`, are

```text
272, 242, 219, 203, 194, 192, 197, 209, 228.
```

Equality therefore forces

\[
h=0,\qquad o=17.
\]

Every witness then lies inside `O`. Splitting direct `O`-edges from two-step `O`-nonedges gives

\[
272\le e(G[O])+2\left({17\choose2}-e(G[O])\right)=272-e(G[O]).
\]

Hence `O` is independent. Every vertex of `O` has degree 16, and there are exactly 16 vertices outside `O`, so each vertex of `O` is adjacent to every outside vertex. These `17*16=272` cross edges exhaust the graph. Therefore

\[
G\cong K_{17,16}.
\]

## 3. Delta>=19

### 3.1 Delta=19

Here `(a,b)=(13,19)` and the bipartite benchmark is

\[
19(33-19)=266.
\]

At `m>=272`, `t>=6`. The thirteen-label hand theorem gives

\[
Q\le21,
\]

while the canonical bridge gives

\[
Q\ge b+2t\ge19+12=31,
\]

impossible.

### 3.2 Delta>=20

For `20<=Delta<=31`, one has `a<=12`. The source-independent twelve-label theorem forbids positive surplus over `b(33-b)`. But throughout this range

\[
b(33-b)\le20\cdot13=260<272.
\]

Hence no graph in the target range occurs. If `Delta=32`, the universal-vertex D2C graph is a star.

Thus the only unresolved maximum degree at equality is `Delta=18`.

## 4. Delta=18 above equality

Here

```text
(a,b)=(14,18),
benchmark = 18*15 = 270,
t=m-270.
```

The fourteen-label theorem gives

\[
Q\le23,
\]

while the bridge gives

\[
Q\ge18+2t.
\]

Thus `m>=273` gives `t>=3` and `Q>=24`, impossible.

At equality `m=272`, one has `t=2`, so

\[
22\le Q\le23. \tag{4.1}
\]

The isolated-`C` lemma applies uniformly here. If `C=H[A]` had an isolated vertex, then

\[
b\le a-1-t=11,
\]

contradicting `b=18`. Hence `delta(C)>=1`; because `F` is the complement of `C` on 14 vertices,

\[
d_i\le12. \tag{4.2}
\]

This is the `dmax=12` cap used in the finite envelope below.

## 5. Exact equality frontier for (a,b,t)=(14,18,2)

The independent fourteen-label score checker enumerates all

\[
{27\choose14}=20,058,300
\]

nondecreasing demand multisets in `{0,...,13}`. Under (4.1) it finds exactly

```text
Q=22 : 18 profiles
Q=23 :  3 profiles
------------------
total: 21 profiles.
```

All 21 profiles have positive demand.

For each demand profile, take the threshold lower bounds

```text
z_h >= gamma_h(W_h)
```

and impose monotonicity of the residual tail counts. At `Q=22` there is no residual-tail slack; at `Q=23` there is at most one unit. Distributing every admissible slack increment among the 18 positive residual degrees produces exactly

```text
29 (s,rho) states:
18 from Q=22,
11 from Q=23.
```

No profile is lost to monotone-tail arithmetic at this stage.

## 6. A shifted nine-rectangle potential excludes 25/29 states exactly

Use the BC coordinates

```text
d = R+s,
v = b-(R+x)
```

on labels and

```text
alpha = rho+q-1,
w = b-(q+p)
```

on sources. Put

```text
B_{D,V}(d,v)=1[d>=D and v>=V].
```

The natural `b=18` lift of the N32 `t=2` potential retains the same original `h=R+x` cutoffs. It is

\[
\begin{aligned}
F={}&4B_{2,0}+2B_{2,7}+B_{2,9}+B_{2,11}\\
&+B_{2,14}+B_{2,15}+B_{3,10}+B_{3,12}+B_{3,13}.
\end{aligned}
\tag{6.1}
\]

Equivalently, in `(d,h)` coordinates,

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

Thus the *graph-level cutoffs are exactly the N32 cutoffs*; only the `v=b-h` coordinates shift by one.

The exact finite envelope checker holds these nine integer weights fixed and allows only the scalar envelope coefficients to vary profile-by-profile. Floating LP is proposal only. After rounding and one-sided `ell/sigma` repair, every accepted row is rechecked in integer arithmetic.

Result:

```text
N33 equality states tested      : 29
exact potential exclusions      : 25
states left for hand analysis   :  4
exactification failures         :  0
accepted denominator            : 10,000 for all 25
strict gap numerators           : -9,990 ... -9,937
```

The four uncovered states are precisely:

```text
A: s=(3,4,5^12), rho=(1^6,3,4,5^10)
B: s=(3,5^13),   rho=(1^6,3,5^11)
C: s=(4^2,5^12), rho=(1^6,4^2,5^10)
D: s=(4,5^13),   rho=(1^6,4,5^11).
```

They are all impossible by hand.

## 7. Hand closure of the four uncovered profiles

We use the threshold-capacity proof itself. For a threshold `h`, let `ell_u` be the number of actual selected incidences from source `u` whose label has demand at least `h`, and let

```text
Z_h={u:rho_u>=h}, z=|Z_h|,
J={u in Z_h: ell_u>h}, j=|J|.
```

Heavy arcs from `J` have their supplements in `Z_h`. Hence

\[
\sum_{u\in Z_h}\ell_u
\le (z-j)h+jz-\frac{j(j+1)}2. \tag{7.1}
\]

The standard threshold capacity is the maximum of the right-hand side.

### 7.1 Profile A: refined h=4 capacity

Here

```text
s=(3,4,5^12),
rho=(1^6,3,4,5^10).
```

At `h=4`,

```text
W_4=64,
z_4=11.
```

Among the eleven sources in `Z_4`, one has `rho=4` and the other ten have `rho=5`. By selected-incidence forcing `s_i<=rho_u`, the `rho=4` source cannot carry any demand-five label. There is only one demand-four label. Therefore that special source contributes at most one heavy incidence and can never lie in `J`.

For `j=|J|<=10`, the ten ordinary non-`J` sources contribute at most four heavy arcs each, the special source at most one, and heavy arcs from `J` use unordered pairs inside the eleven-source set. Thus

\[
\sum_{u\in Z_4}\ell_u
\le 1+4(10-j)+11j-\frac{j(j+1)}2.
\]

The right side has maximum 62 (at `j=6` or `7`). But `W_4=64` chosen heavy incidences are required. Contradiction.

### 7.2 Profile B: exact h=4 capacity

Here

```text
s=(3,5^13),
rho=(1^6,3,5^11).
```

At `h=4`,

```text
W_4=65,
z_4=11,
C_4(11)=65.
```

Therefore equality holds throughout the threshold-capacity chain. The equality-gap identity forces

```text
j=6 or 7.
```

Every source in `Z_4` is heavy-active, and every demand-five label has actual selected degree exactly five. Heavy arcs from `J` therefore send at least

\[
65-(11-j)4\ge45
\]

supplements back into `Z_4`, so

\[
\sum_{u\in Z_4}p_u\ge45. \tag{7.2}
\]

All eleven sources in `Z_4` have `rho=5`. For a heavy selected incidence `ui` we have, because positive demand and `x_i=s_i=5`,

\[
q_u+p_u\le R_i+x_i=d_i\le \rho_u+q_u-1=q_u+4.
\]

Hence `p_u<=4` for every source in `Z_4`, giving

\[
\sum_{u\in Z_4}p_u\le44,
\]

contradicting (7.2).

### 7.3 Profile C: tight h=5 plus h=4 supplement count

Here

```text
s=(4^2,5^12),
rho=(1^6,4^2,5^10).
```

At `h=5`,

```text
W_5=60,
z_5=10,
C_5(10)=60.
```

Thus equality holds throughout the `h=5` threshold proof. In particular every one of the ten `rho=5` sources carries at least five actual demand-five incidences, and every demand-five label has actual selected degree exactly five.

Now move to `h=4`. The two `rho=4` sources can carry only the two demand-four labels, hence each contributes at most two `h=4` heavy incidences. The ten `rho=5` sources already each contribute at least five, so all ten belong to the `h=4` set `J={ell_u>4}`.

Since

```text
W_4=68,
```

and the two `rho=4` sources together contribute at most four heavy incidences, at least 64 heavy arcs originate in `J`. Every one has its supplement in `Z_4`, so

\[
\sum_{u\in Z_4}p_u\ge64. \tag{7.3}
\]

For each of the ten `rho=5` sources, choose one of its demand-five selected incidences. As above, exact `x_i=5` gives `p_u<=4`, so these ten sources contribute at most 40 to the supplement indegree. Each of the two `rho=4` sources satisfies the universal source bound

\[
p_u\le \rho_u+b-a-1=4+3=7.
\]

Hence

\[
\sum_{u\in Z_4}p_u\le 10\cdot4+2\cdot7=54,
\]

contradicting (7.3).

### 7.4 Profile D: exact h=2 capacity

Here

```text
s=(4,5^13),
rho=(1^6,4,5^11).
```

At `h=2`,

```text
W_2=69,
z_2=12,
C_2(12)=69.
```

Hence equality holds throughout threshold capacity. The equality-gap identity gives `j=9` or `10`, and every label has actual selected degree exactly its demand. Heavy arcs from `J` therefore send at least

\[
69-(12-j)2\ge63
\]

supplements back into `Z_2`, so

\[
\sum_{u\in Z_2}p_u\ge63. \tag{7.4}
\]

For every active source in `Z_2`, use any selected incidence. Since every label is heavy and `x_i=s_i`, endpoint load and source forcing give

\[
q_u+p_u\le R_i+x_i=d_i\le \rho_u+q_u-1,
\]

hence

\[
p_u\le\rho_u-1.
\]

There is one `rho=4` source and eleven `rho=5` sources, so

\[
\sum_{u\in Z_2}p_u\le3+11\cdot4=47,
\]

contradicting (7.4).

Thus all four states are impossible.

## 8. Assembly

At `m>=272`, average degree gives `Delta>=17`.

- `Delta=17`: `m>=273` is excluded by the witness-deficit capacity table; at `m=272` equality forces `K_{17,16}`.
- `Delta=18`: `m>=273` is excluded by `Q<=23<Q_min`; at `m=272` the exact 29-state frontier is closed by 25 exact shifted-potential certificates plus the four hand contradictions above.
- `Delta=19`: the thirteen-label bound excludes the target range.
- `Delta>=20`: the twelve-label source-independent theorem puts the graph below 272; `Delta=32` is the star case.

Therefore the candidate conclusion is

\[
\boxed{e(G)\le272,\qquad e(G)=272\iff G\cong K_{16,17}.}
\]

## 9. Trust boundary

The only proof-critical computation in this N33 route is the finite envelope check for 25 of the 29 `(a,b,t)=(14,18,2)` states. Its global potential is the explicit nine-term function (6.1); only scalar envelope coefficients are computer-found, and every accepted row is checked in exact integer arithmetic.

The four difficult states are excluded by displayed hand arguments. The `Delta=17` branch is entirely hand. Higher-degree branches use the already preserved twelve-, thirteen- and fourteen-label candidate theorems.

As with N32, the principal external-review trust boundary remains the universal selected/residual bridge, threshold-capacity lemma (especially equality), endpoint load/source forcing and independent reproduction of the finite frontier. Same-assistant checking is not external validation.
