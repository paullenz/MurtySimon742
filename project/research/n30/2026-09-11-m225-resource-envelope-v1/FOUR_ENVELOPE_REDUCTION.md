# Four explicit envelope certificates for the N30 equality endpoint

11 September 2026. Research direction: Paul Lenz. Mathematical development, implementation and internal checking: ChatGPT/Geeps.

**Status: candidate analytic/certificate reduction; exact arithmetic REPRODUCED. Independent mathematical review remains OPEN. No governed theorem-ledger promotion is made.**

The four certificates below exclude **all 211 ledger-tight demand/residual rows** at `n=30,Delta=16,m=225`, conditional on the saved complete 100-profile demand frontier and the universal graph-to-model bridge. The earlier ledger argument excludes the other 61 of the historical 272 rows. Thus the final endpoint LP/Farkas models can be replaced in this supplementary route by four explicit functions and small integer envelope tables.

This is **not a fully hand-derived N30 proof**: completeness of the 100 `Q>=18` demand profiles remains a finite input, and the envelope values are supplied as explicit finite certificates. The frozen reviewer-v2 proof remains preserved with its original evidence.

## 1. Exact setup and the additional individual label cap

Use the selected/residual construction with

```text
a=13, b=16, t=m-224=1.
```

For labels, use demand `s_i`, F-degree `d_i`, residual degree `R_i` and selected degree `x_i`. At a source use residual degree `rho_u`, selected outdegree `q_u` and supplement indegree `p_u`. Write

```text
S=sum_i s_i, r=sum_u rho_u=sum_i R_i.
```

The [threshold-slack reduction](../2026-09-11-threshold-tail-v1/N30_M225_THRESHOLD_SLACK_REDUCTION.md) leaves 211 rows with

```text
S=r+2.
```

Since `s_i=max(0,d_i-R_i)` and `sum_i(d_i-R_i)=r+2`, this equality forces

```text
d_i=R_i+s_i
```

at **every** label, including labels with zero demand. Also `x_i>=s_i`.

The bridge gives `s_i<=rho_u` on every selected incidence at `i`. Each source can be selected at a fixed label at most once because the selected cross-edges form a subset of the edges of a simple graph. Therefore define

```text
H_s = #{u:rho_u>=s},
Q_rho = min(13-rho, #{i:s_i<=rho}).
```

Every individual label of demand `s` and source of residual degree `rho` obeys

```text
Label domain:
  0<=R<=12-s,
  s<=x<=min(16-R,H_s).

Source domain:
  0<=q<=Q_rho,
  0<=p<=rho+2.                                    (1)
```

The label bound `R<=12-s` uses only `d_F<=12`, since F has thirteen vertices. The stronger isolated-C bound `d_F<=11` used in older models is **not** a premise here.

The supplement bound in (1) follows from the corrected degree identity

```text
deg_H(u)=(rho_u+q_u)+(15-q_u-p_u)=rho_u+15-p_u>=13.
```

It is `p<=rho+2`, not the previously rejected `rho+1` tightening. Since `q<=13-rho`, the rectangular source domain already ensures `q+p<=15`.

## 2. The monotone-incidence inequality

For a label state define

```text
d=R+s, v=16-R-x.
```

For a source state define

```text
alpha=rho+q-1, w=16-q-p.
```

On every selected source-label incidence the bridge gives

```text
s<=rho,
d<=alpha,
v<=w.                                             (2)
```

Consequently any coordinatewise nondecreasing function `Phi(s,d,v)` obeys

```text
sum_i x_i Phi(s_i,R_i+s_i,16-R_i-x_i)
  <= sum_u q_u Phi(rho_u,rho_u+q_u-1,16-q_u-p_u).  (3)
```

Apply monotonicity separately to each selected edge and then sum. Every label occurs exactly `x_i` times and every source exactly `q_u` times. This direct count is the [existing three-coordinate potential lemma](../../general_n/2026-09-09-rx-hall-v1/POTENTIAL_CERTIFICATE_LEMMA_3D.md), not an assumption about constructing a graph from a relaxation.

The useful new simple term is `s*v`. Both factors in (2) are nonnegative, so

```text
s*v <= rho*w
```

on each selected incidence. It retains how demand interacts with the remaining cross-capacity, which the previous aggregate excess estimate discarded.

## 3. Resource identities and supplement tails

The exact identities are

```text
sum_i R_i=r,
sum_i x_i=sum_u q_u,
sum_u q_u=sum_u p_u.                               (4)
```

For each `j>=1`, let

```text
T_j = sum_{u:q_u>=j+1} q_u
      - sum_{w:rho_w+q_w>=j} p_w.
```

Every selected arc from a source with `q_u>=j+1` has a supplement satisfying `rho_w+q_w>=q_u-1>=j`. Therefore

```text
T_j<=0.                                            (5)
```

The selected orientations count each arc once; the supplement's total incoming degree is `p_w`.

## 4. Exact scalar envelopes

Choose nonnegative integer coefficients `lambda,c,mu,tau_j`, and a nondecreasing potential `Phi`. Define the two finite envelopes over the entire domains in (1):

```text
ell_s = min [lambda*R + c*x
             + x*Phi(s,R+s,16-R-x)],

sigma_rho = min [mu*(q-p)-c*q
                  + sum_j tau_j*(q*1[q>=j+1]-p*1[rho+q>=j])
                  - q*Phi(rho,rho+q-1,16-q-p)].      (6)
```

Let `n_s` be the demand multiplicities and `n_rho` the residual-degree multiplicities. A necessary condition for an actual graph is

```text
gap := sum_s n_s*ell_s + sum_rho n_rho*sigma_rho
       - lambda*r <= 0.                            (7)
```

**Proof.** The minima in (6) are lower bounds for the values at the actual vertex states. Sum those bounds over all labels and sources. The `c` and `mu` terms cancel by (4). The `tau` terms are nonpositive by (5); the potential difference is nonpositive by (3). The only remaining contribution is `lambda*sum_i R_i=lambda*r`. This proves (7). Thus any strictly positive value is an exact contradiction. No optimizer, transport matrix or numerical infeasibility decision is a premise. QED.

## 5. Four explicit potentials

Use the monotone generators

```text
V(s,d,v)=s*v,
E_k(s,d,v)=1[d+v>=16-k],
J(s,d,v)=1[s>=2],
R_{D,V0}(s,d,v)=1[d>=D and v>=V0].
```

All variables lie in a nonnegative domain. Each generator is coordinatewise nondecreasing, and each coefficient below is nonnegative. At a label, `E_k=1[x-s<=k]`; at a source, `E_k=1[p<=rho+k-1]`.

### Certificate B1

```text
lambda=150, c=88, mu=150,
tau_2=11, tau_3=107, tau_5=5,

Phi = 4V + 51E_0 + 40E_1 + 40E_2 + 150J
      + 91R_{1,13} + 142R_{1,14}
      + 36R_{2,10} + 37R_{2,11} + 61R_{2,12}
      + 21R_{4,7} + 21R_{4,8} + 32R_{4,9} + R_{4,10}.
```

This single certificate excludes 195 of the 211 tight rows.

### Certificate B2

```text
lambda=15, c=8, mu=17,
tau_2=3, tau_3=4,

Phi = 3E_0 + 6E_1 + 3E_2 + 14J + 11R_{1,14}
      + 3R_{2,7} + 2R_{2,8} + 5R_{2,9}
      + 5R_{2,10} + 5R_{2,11} + 7R_{2,12} + 8R_{2,13}.
```

It excludes 79 rows in total, including 13 not excluded by B1.

### Certificate B3

```text
lambda=18, c=4, mu=24,
tau_2=2, tau_3=4,

Phi = V + 4E_0 + 8E_1 + 3E_2 + 7J
      + 2R_{1,12} + 11R_{1,13} + 14R_{1,14}
      + 3R_{3,11} + R_{3,12} + R_{4,9} + 3R_{4,10}.
```

It excludes 24 rows in total, including the next two rows missed by B1 and B2.

### Certificate C1

```text
lambda=25, c=28, mu=0,
tau_2=22, tau_4=6,
Phi=V=s*v.
```

It excludes ten rows in total, including the sole row missed by B1, B2 and B3. All unlisted `tau_j` are zero.

Together the four certificates cover

```text
195 + 13 + 2 + 1 = 211
```

distinct rows. This includes the four zero-demand rows and all 207 positive-demand rows. Four is a convenient explicit cover; **minimality is not claimed**. This count concerns a different profile domain and different potentials from the earlier fixed-potential two-template result on seven hard N30 rows.

## 6. The final exceptional row, written out

The row missed by the first three certificates is

```text
s=(2,5^12),
rho=(1^4,2,4,5^10),
S=62, r=60.
```

For C1, the exact minima in (6) are

```text
ell_2=112, ell_5=415,
sigma_1=0, sigma_2=-138, sigma_4=-232, sigma_5=-322.
```

Consequently

```text
gap = 112 + 12*415 -138 -232 -10*322 -25*60
    = 2 > 0.
```

This contradicts (7). The [complete appendix](EXACT_APPENDIX.md) gives the same type of explicit arithmetic for every one of the 211 rows; the minimum assigned gap is one.

## 7. Why the envelope tables can be checked without optimization

For each fixed label value `x`, the expression in (6) is linear in `R` between the rectangle breakpoints. It therefore suffices to check the endpoints

```text
R=0, R=min(12-s,16-x),
R=D-s-1, D-s,
R=16-V0-x, 17-V0-x
```

for the active rectangles, retaining only values inside the allowed interval. These include the integer states immediately before and after each rectangle indicator changes. The diagonal indicators depend only on `x-s`; the `s*v` term is linear in R for fixed x.

For each fixed source value `q`, the source expression is linear in `p` between indicator changes. It suffices to check

```text
p=0, rho+2;
p=rho+k-1, rho+k for each active E_k;
p=16-q-V0, 17-q-V0 for each active rectangle whose
  source degree rho+q-1 is at least D.
```

Again retain only admissible p values. These formulas account for both sides of every discrete jump, including the endpoints `p=rho+2` and `R=12-s`. There is no hidden minimization over fractional vertex states.

The [standalone checker](verify_joint_certificates.py) computes every envelope twice: by direct traversal of the full integer box and by these independently structured endpoint formulas. The two evaluations agree exactly. It also checks monotonicity on the full finite coordinate box, tests every certificate on every row before choosing assignments, and stops with failure if the resulting cover is incomplete.

The saved [exact audit](EXACT_AUDIT.json) records:

- 211/211 tight rows covered by four templates;
- 12,772 direct local-state evaluations;
- 8,069 endpoint-formula evaluations;
- 37,128 product-order comparisons;
- minimum assigned gap 1;
- no solver, floating point or discovery-module import in acceptance.

The [acceptance-boundary audit](ACCEPTANCE_BOUNDARY_AUDIT.json) confirms that removing C1 or introducing a negative monotone weight is rejected. It also exhibits an allowed source-box boundary at `p=rho+2` which strictly changes a minimum; the invalid historical `rho+1` tightening would omit it.

## 8. Resulting dependency chain and remaining work

The supplementary equality-endpoint route is now

```text
universal bridge and threshold-tail bound
 -> complete 100-profile Q>=18 input
 -> exact at-most-three-slack reconstruction of 272 rows
 -> 61 positive-slack rows contradicted by ledger equality
 -> all 211 tight rows contradicted by these four certificates.
```

Conditional on acceptance of that chain, the older residual-row scan, final grouped LP/Farkas systems, special four-zero-demand Hall certificates, 200-row residual-budget Hall elimination and separate seven-hard-row 3-D treatment are unnecessary to this endpoint's *new supplementary* derivation. They remain preserved as independent internal corroboration and as the evidence underlying the frozen current reviewer package.

The remaining main task toward a hand-derived N30/Delta16 equality branch is the complete **100-profile demand classification**. The present checker validates the listed profiles and reconstructs their rows; it does not prove that no other demand profile exists. The graph-to-model lemmas and this new use of individual label capacity still need independent mathematical review. Finite exact envelopes, internal replay and publication are not external acceptance or an unrestricted Murty-Simon proof.
