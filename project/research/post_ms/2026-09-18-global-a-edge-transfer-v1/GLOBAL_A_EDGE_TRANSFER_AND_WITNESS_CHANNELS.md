# Global A-edge transfer and witness channels

Date: 2026-09-18

Status: internal structural theorem package for the eventual / sufficiently-large second-extremal D2C programme. No all-order theorem is claimed. The published order-12, size-32 graph remains a mandatory negative control.

## 1. Setup and preserved identities

Work in the near-full partial-Boolean normal form around a maximum-degree root `v`:

- `B=N(v)`, `A=V\N[v]`;
- `p` tight antipode pairs in `B`, with unmatched set `U`, `u=|U|`;
- `a=|A|=2p+u-lambda-1`;
- `q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`;
- `Q=e(G[B])=p(p+u-1)+q`;
- `delta=b(n-b)-m=r-f`;
- `E_U=u(p+u-1)-2q-s`;
- `L_A=a(p+u)-s-2f`.

The exact rooted-transfer identity is

`delta=E_U+Q-f-lambda(p+u)+p`.                         `(RQ3)`

Put

`D_M=b(n-b)-M(n)=ceil((4p+2u-c_lambda-2)/2)`,

where `c_lambda=ceil(lambda(lambda+2)/2)`. Then

`m>M(n) iff delta<=D_M-1`.                              `(RT)`

Every `z in A union U` has degree slack `epsilon_z=b-d(z)`. Its Boolean code is denoted `c(z)`. For a code `c`, write

- `A_c={x in A:c(x)=c}`, `n_c=|A_c|`;
- `V_c=(A union U)_c`, `N_c=|V_c|`;
- `L_c=sum_{x in A_c} epsilon_x`;
- `S_c=sum_{z in V_c} epsilon_z`.

Thus `sum_c L_c=L_A` and `sum_c S_c=E_U+L_A`.

The preserved matched-endpoint witness theorem says that each matched endpoint `w` has a forced source code `gamma(w)` and that the number of matched endpoints sharing one `gamma` is at most the largest switchable zero-signed subcore size `sigma_0`. Hence the total number of chosen matched-B certificates whose source lies in `A` is at most

`M_P<=sigma_0 a`.                                       `(MP)`

Also, for every switchable zero-signed subcore of order `sigma_0>=3`,

`L_A>=sigma_0(sigma_0-1)`.                              `(ZS)`

## 2. Rooted transfer forces internal A-edge mass

From `(RQ3)`,

`f=E_U+Q-lambda(p+u)+p-delta`.

Since `E_U>=0`, every above-`M(n)` candidate satisfies

`f>=Q-lambda(p+u)+p-D_M+1`.                             `(F1)`

Define

`F_min:=Q-lambda(p+u)+p-D_M+1`.

Using `Q=p(p+u-1)+q`, this is exactly

`F_min=(p-lambda)(p+u)+q-D_M+1`.                        `(F2)`

Therefore

`f>=F_min`.                                               `(FTR)`

This is the first direct use of rooted triangles to force the internal A-edge mass: if the residual defect is too small to meet the second-extremal threshold, the rooted triangle count must be paid for by A-edges unless unmatched slack already pays it.

### Mandatory negative-control check

For the published `X_3` graph,

`p=4`, `u=0`, `lambda=4`, `q=f=0`, `D_M=1`, `Q=12`.

Then `(F2)` gives `F_min=0`, exactly equal to `f`. Thus the theorem permits the order-12, size-32 exception and does not silently impose the false all-order conjecture.

## 3. Direct critical A-edges pay complementary-code slack

Call an edge `xy in E(G[A])` **direct** if `x` and `y` have no common neighbour in `G`. Let `D` be the number of direct A-edges.

### Lemma 3.1 — complement code

If `xy` is direct, then

`c(y)=bar(c(x))`.

**Proof.** Each A-vertex selects exactly one endpoint from every tight pair. If `x` and `y` selected the same endpoint in any tight fibre, that matched endpoint would be a common neighbour of `x,y`, contradicting directness. Hence they choose opposite endpoints in every tight fibre. `square`

### Lemma 3.2 — direct-edge slack payment

Assume `lambda>=0`. For every direct A-edge `xy`,

`epsilon_x+epsilon_y>=lambda+1`.                         `(DES)`

**Proof.** Since `xy` has no common neighbour, the sets

`N_{A union U}(x)\{y}` and `N_{A union U}(y)\{x}`

are disjoint subsets of `(A union U)\{x,y}`. Moreover

`d_{A union U}(z)=p+u-epsilon_z`

for every `z in A`. Therefore

`(p+u-epsilon_x-1)+(p+u-epsilon_y-1)<=a+u-2`.

Using `a=2p+u-lambda-1` and simplifying gives `(DES)`. `square`

### Corollary 3.3 — global direct-edge capacity

Direct edges occur only between complementary code classes, so

`D<=1/2 sum_c n_c n_bar(c)`.                             `(DC1)`

Also

`(lambda+1)D`
` <= sum_{xy direct}(epsilon_x+epsilon_y)`
` =  sum_x epsilon_x d_D(x)`
` <= sum_c n_bar(c) L_c`.

Hence

`D<=min{ 1/2 sum_c n_c n_bar(c),`
`        (1/(lambda+1)) sum_c n_bar(c)L_c }`.             `(DAE)`

This is an exact global payment theorem for the direct criticality channel.

## 4. Every non-direct A-edge enters one of the preserved witness channels

Let `xy in E(G[A])` be non-direct. Because `G` is diameter-2-critical, deleting `xy` destroys some distance-at-most-two relation. Since `x,y` still have a common neighbour, the damaged pair is not `x,y` itself. Consequently one may orient the critical edge so that, for one endpoint `z in {x,y}` and the other endpoint `h`, there is a vertex `w` with

`N(z) intersect N(w)={h}`.                               `(UCN)`

The witness `w` cannot be the root `v`. Thus it lies either

1. at a matched endpoint in the tight core, or
2. in `A union U`.

Choose one such certificate for every non-direct A-edge.

### 4.1 Matched-B channel

By the preserved `gamma(w)` source-code theorem and `(MP)`, the total number of chosen matched-B certificates is at most

`sigma_0 a`.                                             `(ABC-P)`

### 4.2 A/U channel

For the A/U witness channel, the preserved unique-common-neighbour code theorem forces complementary codes: if the A-source has code `c`, the witness has code `bar(c)`.

Let `C_c` be the number of chosen A/U certificates with source code `c`. A fixed ordered source-witness pair can certify at most one head, because `(UCN)` fixes its unique common neighbour. Therefore

`C_c<=n_c N_bar(c)`.                                     `(ABC1)`

The unique-common-neighbour hole identity also gives

`epsilon_z+epsilon_w>=lambda+1`.

Summing over all source-witness pairs of type `c`, while allowing arbitrary reuse subject only to pair uniqueness, gives

`(lambda+1)C_c<=N_bar(c)L_c+n_c S_bar(c)`.               `(ABC2)`

Hence

`C_c<=min{n_c N_bar(c),`
`          [N_bar(c)L_c+n_cS_bar(c)]/(lambda+1)}`.         `(ABC)`

No independence assumption between different centres is used here.

## 5. Complete global A-edge witness-channel theorem

Combining the direct, matched-B, and A/U channels gives the following finite theorem.

### Theorem 5.1 — global A-edge feasibility

In the near-full partial-Boolean branch with `lambda>=0`,

`f <= sigma_0 a`
`   + min{ 1/2 sum_c n_c n_bar(c),`
`          (1/(lambda+1)) sum_c n_bar(c)L_c }`
`   + sum_c min{ n_c N_bar(c),`
`                [N_bar(c)L_c+n_cS_bar(c)]/(lambda+1) }`. `(AFE)`

Every possible criticality channel for an internal A-edge is represented:

- direct / no-common-neighbour;
- external matched-B witness;
- external A/U witness.

The theorem is therefore not cylinder-specific.

### Coarse code-capacity form

Put

`mu_A=max_c n_c`, `mu_V=max_c N_c`, and `S=E_U+L_A`.

Since

`sum_c n_bar(c)L_c<=mu_A L_A`,

`sum_c N_bar(c)L_c<=mu_V L_A`,

`sum_c n_c S_bar(c)<=mu_A S`,

one gets

`f<=sigma_0 a`
`  +[mu_A E_U+(mu_V+2mu_A)L_A]/(lambda+1)`.              `(AFEc)`

In particular, since `mu_A<=mu_V`,

`f<=sigma_0 a+3mu_V(E_U+L_A)/(lambda+1)`.                `(AFE3)`

The constant `3` is intentionally crude; the exact code-resolved inequality `(AFE)` should be used whenever class data are available.

## 6. Rooted-transfer / macroscopic-code dichotomy

Combine the rooted lower bound `(FTR)` with `(AFE3)`:

`F_min<=sigma_0 a+3mu_V S/(lambda+1)`,                   `(RTC)`

where `S=E_U+L_A`.

Thus, whenever `F_min>sigma_0a`,

`mu_V >= (lambda+1)(F_min-sigma_0a)/(3S)`.               `(MC)`

This is a compact structural dichotomy:

> rooted-triangle transfer that forces a large internal A-edge mass must either be absorbed by a large switchable zero-signed core (and therefore by `L_A` through `(ZS)`), or by a macroscopic Boolean code class in `A union U`.

### Corollary 6.1 — sublinear root imbalance, linear unmatched set

Consider a sequence of above-`M(n)` candidates with

`u/p -> rho>0`, `u=O(p)`, `lambda=o(p)`, `lambda>=0`.

Then:

1. `F_min=(1+rho+o(1))p^2+q`, hence `F_min=Theta(p^2)`;
2. the above-threshold scorecard satisfies `S=o(p^2)`;
3. `(ZS)` therefore gives `sigma_0=o(p)`, so `sigma_0a=o(p^2)`;
4. from the exact scorecard cap, `S/(lambda+1)=O(p)` uniformly for `u=O(p)`.

Consequently `(RTC)` forces

`mu_V=Omega(p)`.                                         `(MACRO)`

Thus every surviving sequence in the sublinear-imbalance, linearly-unmatched regime has a Boolean code class containing a positive linear fraction of `A union U`.

This conclusion is substantially sharper than merely restricting `u/p`: it gives an explicit structural object that the next theorem can attack.

## 7. Independent audit

A graph-atlas regression through order seven was used only to audit the general D2C edge-criticality trichotomy underlying Section 4.

Among all graph-atlas graphs through order seven:

- 21 isomorphism classes are diameter-2-critical;
- 156 edges were checked;
- 127 edges were direct (their endpoints had no common neighbour);
- 29 non-direct edges admitted at least one oriented external unique-common-neighbour certificate;
- 47 total witness orientations were found;
- failures: 0.

This audit does not prove `(AFE)` and does not test the near-full Boolean coding itself. The promoted theorem rests on the hand channel decomposition and the already-preserved source-code / slack injections.

## 8. What this changes

The live `f=e(G[A])` problem is no longer unpriced. Rooted triangles force a lower bound on `f`, while D2C criticality gives a complete upper bound through three witness channels.

The resulting route is now:

`small residual defect`
` -> large rooted-transfer demand`
` -> forced A-edge mass f`
` -> direct / matched-B / A-U witness accounting`
` -> either L_A is large or a Boolean code class is macroscopic`.

The next high-value step is therefore not another q-only inequality. It is a **macroscopic-code-class exclusion/stability theorem**. A linear-sized code class must simultaneously accommodate its internal A-edge criticality, complementary witness demand, beta/source-tuple obligations, and the same-code clique payment. The dense case should pay scorecard directly; the sparse case should force complementary-code congestion.

## 9. Trust boundary

Promoted internally:

- `(FTR)` rooted-transfer A-edge floor;
- `(DAE)` direct-edge complementary-code/slack capacity;
- `(AFE)` complete global A-edge witness-channel theorem;
- `(RTC)/(MC)` rooted-transfer/macroscopic-code dichotomy;
- `(MACRO)` for `lambda=o(p)`, `u/p -> rho>0`, `lambda>=0`.

Not claimed:

- an all-order second-extremal theorem;
- a complete eventual theorem;
- an exclusion of the published order-12, size-32 graph;
- a theorem for negative `lambda` via the divisions by `lambda+1`;
- a classification of the macroscopic code class yet.
