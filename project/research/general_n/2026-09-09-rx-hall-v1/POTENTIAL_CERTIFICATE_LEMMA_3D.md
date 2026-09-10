# Three-coordinate potential-certificate lemma for RX-Hall

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact algebraic extension of `POTENTIAL_CERTIFICATE_LEMMA.md` inside the candidate graph-to-RX-Hall framework. It uses the full three-coordinate incidence compatibility already proved in `MONOTONE_COUPLING_REDUCTION.md`. It is conditional on the surrounding graph-to-incidence/resource lemmas and is not by itself an unrestricted Murty-Simon theorem.

## 1. Three-coordinate compatibility

For a label state `(s,R,x)` put

```text
d = R+s,
v = b-(R+x).
```

For a source state `(rho,q,p)` put

```text
alpha = rho+q-1,
w = b-(q+p).
```

The retained source-label compatibility conditions on every selected incidence are

```text
s <= rho,
d <= alpha,
R+x >= q+p,
```

and hence

```text
(s,d,v) <= (rho,alpha,w)
```

coordinatewise. This is the same product order as `(s,d,-h) <= (rho,alpha,-beta)` in `MONOTONE_COUPLING_REDUCTION.md`, with `v=b-h` and `w=b-beta`.

Therefore every coordinatewise nondecreasing function

```text
Phi(s,d,v)
```

obeys the incidence transport inequality

```text
sum_i x_i Phi(s_i,d_i,v_i)
  <= sum_u q_u Phi(rho_u,alpha_u,w_u).             (P)
```

Indeed, apply monotonicity to each selected source-label incidence and sum. Every label `i` occurs in exactly `x_i` incidences and every source `u` in exactly `q_u` incidences. Equivalently, `(P)` follows from the monotone coupling of the stripped Hall core.

This single statement contains three useful generator families:

```text
BC rectangle:  1[d>=D and v>=V],
SH rectangle:  1[s>=S and v>=V],
diagonal slack: 1[d+v>=K].
```

Every nonnegative linear combination of these indicators is coordinatewise nondecreasing and is therefore a valid `Phi`.

## 2. Resource relations

The graph-to-RX-Hall bridge supplies

```text
sum_i R_i <= sum_u rho_u,                          (R)
sum_i x_i = sum_u q_u,                             (I)
sum_u q_u = sum_u p_u,                             (B)
```

and for every threshold `j>=1`,

```text
T_j := sum_{u:q_u>=j+1} q_u
       - sum_{u:rho_u+q_u>=j} p_u <= 0.            (T_j)
```

## 3. Envelope certificate

Fix nonnegative coefficients

```text
lambda >= 0,
c >= 0,
mu >= 0,
tau_j >= 0,
```

and any coordinatewise nondecreasing `Phi`.

For each demand value `s`, choose a real `ell_s` satisfying every graph-admissible label state `(R,x)` of that demand:

```text
ell_s <= lambda R + c x
         + x Phi(s, R+s, b-R-x).                   (L_s)
```

For each residual source degree `rho`, choose a real `sigma_rho` satisfying every graph-admissible source state `(q,p)`:

```text
sigma_rho <= mu(q-p) - c q
             + sum_j tau_j [q 1(q>=j+1)
                            - p 1(rho+q>=j)]
             - q Phi(rho, rho+q-1, b-q-p).         (S_rho)
```

If the profile also satisfies the strict gap

```text
sum_i ell_{s_i} + sum_u sigma_{rho_u}
  > lambda sum_u rho_u,                            (G)
```

then no actual selected quasi-edge configuration realizing that profile can exist.

## 4. Proof

Sum `(L_s)` over labels and `(S_rho)` over sources. The right side is

```text
lambda sum_i R_i
+ c (sum_i x_i - sum_u q_u)
+ mu (sum_u q_u - sum_u p_u)
+ sum_j tau_j T_j
+ [sum_i x_i Phi(s_i,d_i,v_i)
   - sum_u q_u Phi(rho_u,alpha_u,w_u)].
```

The `c` and `mu` terms vanish by `(I)` and `(B)`. The threshold term is nonpositive because `tau_j>=0` and `T_j<=0`. The potential term is nonpositive by `(P)`. Finally `(R)` and `lambda>=0` give

```text
sum_i ell_{s_i} + sum_u sigma_{rho_u}
 <= lambda sum_i R_i
 <= lambda sum_u rho_u,
```

contradicting `(G)`. QED.

## 5. Relation to the earlier two-coordinate lemma

`POTENTIAL_CERTIFICATE_LEMMA.md` is recovered by taking `Phi(s,d,v)=F(d,v)`, independent of `s`. The present version adds no new graph assumption: it merely retains the already available first coordinate `s<=rho` rather than projecting it away.

The n=30 `t=1` falsification laboratory shows why that retained coordinate can matter. The reduced BC/diagonal family misses one of the seven hard profiles numerically, while the single SH threshold

```text
39 * 1[s>=2]
```

is enough, together with the common BC/diagonal potential, to obtain an exact two-template contradiction across all seven profiles. See `N30_T1_TWO_TEMPLATE_POTENTIAL.md` and `n30_t1_two_rational_templates_exact.py`.

## 6. Trust boundary

The algebra above is exact. Its use at graph level remains conditional on the universal selected/residual construction, incidence compatibility, resource identities and threshold inequalities. The existing fixed-order n=29/n=30 candidate proofs do not depend on this post-hoc 3D potential compression.