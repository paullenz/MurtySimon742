# Potential-certificate lemma behind the compact RX-Hall proofs

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact algebraic extraction from the candidate graph-to-RX-Hall framework. This removes LP vocabulary from the final contradiction mechanism. It is conditional on the established graph-to-incidence compatibility and resource inequalities; it is not by itself an unrestricted Murty–Simon theorem.

## 1. Graph-level data

Use the selected quasi-edge incidence notation from the RX-Hall programme. For labels `i` and sources `u`, let

- `s_i` be label demand, `x_i` selected label degree, and `R_i` residual column degree;
- `rho_u` be source residual degree, `q_u` selected source outdegree, and `p_u` supplement indegree;
- `b` be the size of the source/supplement side.

Set

```
d_i = R_i+s_i,              v_i = b-(R_i+x_i),
alpha_u = rho_u+q_u-1,       w_u = b-(q_u+p_u).
```

The graph-to-RX-Hall bridge supplies the following necessary relations:

```
sum_i R_i <= sum_u rho_u,                         (R)
sum_i x_i = sum_u q_u,                            (I)
sum_u q_u = sum_u p_u,                            (B)
```

and, for every threshold `j>=1`,

```
T_j := sum_{u:q_u>=j+1} q_u
       - sum_{u:rho_u+q_u>=j} p_u <= 0.            (T_j)
```

On every selected source-label incidence, BC compatibility gives

```
(d_i,v_i) <= (alpha_u,w_u)
```

coordinatewise. Therefore every coordinatewise nondecreasing function `F` obeys the incidence transport inequality

```
sum_i x_i F(d_i,v_i) <= sum_u q_u F(alpha_u,w_u). (F)
```

This includes nonnegative combinations of BC rectangle indicators and the diagonal slack indicators developed in `DIAGONAL_SLACK_THRESHOLD.md`.

## 2. Envelope certificate

Fix nonnegative numbers

```
lambda >= 0,  c >= 0,  tau_j >= 0,
```

an arbitrary real balance multiplier `mu`, and any coordinatewise nondecreasing potential `F`.

**12 September clarification:** the earlier statement unnecessarily restricted `mu>=0`. Its coefficient multiplies the exact balance `sum q=sum p`, so the proof below works for either sign. The existing envelope implementations represent this free multiplier as `mu+ - mu-`. Allowing it explicitly closes that wording mismatch; no inequality direction or certificate arithmetic changes.

For every demand value `s`, choose a real number `ell_s` such that every graph-admissible label state `(R,x)` with that demand satisfies

```
ell_s <= lambda R + c x + x F(R+s, b-R-x).        (L_s)
```

For every residual source degree `rho`, choose a real number `sigma_rho` such that every graph-admissible source state `(q,p)` satisfies

```
sigma_rho <= mu(q-p) - c q
             + sum_j tau_j [q 1(q>=j+1)
                            - p 1(rho+q>=j)]
             - q F(rho+q-1, b-q-p).               (S_rho)
```

Suppose finally that the demand and residual-degree profiles obey the strict scalar gap

```
sum_i ell_{s_i} + sum_u sigma_{rho_u}
   > lambda sum_u rho_u.                           (G)
```

Then no actual selected quasi-edge configuration realizing those profiles can exist.

## 3. Proof

Sum `(L_s)` over all labels and `(S_rho)` over all sources. The right side is

```
lambda sum_i R_i
+ c (sum_i x_i - sum_u q_u)
+ mu (sum_u q_u - sum_u p_u)
+ sum_j tau_j T_j
+ [sum_i x_i F(d_i,v_i) - sum_u q_u F(alpha_u,w_u)].
```

By `(I)` and `(B)`, the two balance terms vanish. Since every `tau_j>=0` and `T_j<=0`, the threshold-transport term is nonpositive. By `(F)`, the potential term is nonpositive. Finally `(R)` and `lambda>=0` give

```
sum_i ell_{s_i} + sum_u sigma_{rho_u}
   <= lambda sum_i R_i
   <= lambda sum_u rho_u,
```

contradicting `(G)`. QED.

The contradiction is therefore elementary summation, monotonicity and double counting. Linear programming is only one way to *discover* suitable coefficients and envelopes; it is not part of the mathematical implication once the inequalities are displayed and checked.

## 4. The current n=29, t=2 potential language

For `(a,b,t,dmax)=(12,16,2,10)`, the best exact support-minimized certificate uses three `d` layers and two diagonal slack thresholds. In generic form

```
F(d,v) = A_2(v) 1[d>=2]
       + A_3(v) 1[d>=3]
       + A_4(v) 1[d>=4]
       + gamma_2 1[d+v>=14]
       + gamma_0 1[d+v>=16],
```

where each `A_D` is a nondecreasing step function represented by nonnegative rectangle increments.

The diagonal terms have a particularly direct interpretation. Since

```
d_i+v_i = 16-(x_i-s_i),
alpha_u+w_u = 16-(p_u-rho_u+1),
```

they are precisely the cumulative slack inequalities

```
sum_i x_i 1[x_i-s_i<=2] <= sum_u q_u 1[p_u-rho_u+1<=2],
sum_i x_i 1[x_i-s_i=0]  <= sum_u q_u 1[p_u-rho_u+1<=0].
```

Thus the remaining problem is not to justify a mysterious computational cut. It is to understand why a short combination of three ordinary Hall-threshold layers and two slack-majorization levels forces the strict scalar gap `(G)` throughout the unresolved parameter band.

## 5. Research target

The next symbolic objective is to replace the profile-specific envelope choices `ell_s`, `sigma_rho`, `lambda`, `c`, `mu`, and `tau_j` by explicit formulae in the global parameters `(a,b,t,r)` or by a bounded case family whose breakpoint locations are parameter-derived.

A successful parameterisation would turn the finite common-potential certificate into a hand theorem. The correct falsification protocol is:

1. derive the coefficients from inequalities rather than fit them to n=29;
2. test the resulting rule on the known n=30 frontier;
3. use n=31 only as a falsification laboratory;
4. promote nothing beyond finite evidence until the graph-to-RX-Hall bridge and all scalar cases have been independently reviewed.
