# Dense diameter-2-critical research — live current state

> **Active target — 18 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly–Foucaud–Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty–Simon / Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `FULL_TIGHT_CLOSED_ROOTED_WITNESS_SLOT_HAMMING_FRONTIER`.

**WORK MODE:** `EVENTUAL_D2C_MATH`.

The full-tight Boolean branch remains internally closed for sufficiently large matched cores (`k>=19`). The mixed `{4,5}` selected-excess ladder is closed and is not a live branch. The active branch is the triangle-containing unmatched/errorful antipode regime.

The current structural spine is now

`rooted B-edge criticality -> exact unused witness-slot residual r -> saturation / hypercube stability -> A-edge Hamming energy -> forced non-direct A-edge demand -> pair-local matched/A-U capacity`.

The important change at this checkpoint is conceptual: the residual variable `r` is no longer only an algebraic remainder. It exactly counts the unused `B--A` nonedge slots after one criticality witness slot is assigned injectively to every rooted triangle edge in `G[B]`.

No global eventual second-extremal theorem is claimed.

## 1. Mandatory negative control

`M(n)=floor((n-1)^2/4)+1` is only the eventual comparison threshold.

The published Radosavljevic--Stanic--Zivkovic (2024) Figure-1 D2C graph has been reconstructed exactly and is isomorphic to the project's `X_3`:

- `n=12`, `m=32>M(12)=31`;
- diameter two and every edge critical;
- rooted data `p=4,b=8,a=3,u=0,lambda=4`;
- `q=s=f=r=0`, `Q=12`, `delta=0`, `E_U=0`, `L_A=12`, `D_M=1`.

Its rooted form is a universal root over `Q_3`, together with three A-vertices whose B-neighbourhoods are the three coordinate-zero faces. At the canonical root it is now recognized as an **exact witness-slot saturation model**: there are exactly 12 `B--A` nonedges, exactly 12 rooted B-edges, and every nonedge slot is used once.

Certification:

`project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## 2. Rooted residual / triangle spine

For a maximum-degree root `v`, write

`B=N(v)`, `A=V\N[v]`, `lambda=2b-n=b-a-1`.

There are `p` tight antipode pairs in `B` and an unmatched set `U`, `u=|U|`, so

> `b=2p+u`,
>
> `a=2p+u-lambda-1`.

Put

`q=e(G[U])`, `s=e_G(A,U)`, `f=e(G[A])`.

Then

> `Q=e(G[B])=p(p+u-1)+q`,
>
> `r=(p+u)(a-p)+p-s-q`,
>
> `delta=b(n-b)-m=r-f`.                                  `(DEF)`

With `epsilon_z=b-d(z)`, put

> `E_U=u(p+u-1)-2q-s`,
>
> `L_A=a(p+u)-s-2f`,
>
> `S=E_U+L_A`.

Let

`c_lambda=ceil(lambda(lambda+2)/2)`,

`D_M=ceil((4p+2u-c_lambda-2)/2)`.

Then

> `S=2delta+lambda(p+u)-p`,                               `(RS)`
>
> `D_M=b(n-b)-M(n)`,
>
> `m<=M(n) iff delta>=D_M`.                               `(RT)`

Rooted triangles remain an exact transfer variable:

> `r+Q=L_A+2f`,                                           `(RQ1)`
>
> `delta+Q=L_A+f`,                                        `(RQ2)`
>
> `delta=E_U+Q-f-lambda(p+u)+p`.                          `(RQ3)`

Rearranging gives the exact residual split

> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

Thus every above-`M(n)` candidate (`delta<=D_M-1`) satisfies

> `f>=F_0+q+E_U`,                                         `(RSF+)`

where

> `F_0=(p-lambda)(p+u)-D_M+1`.

Above threshold,

> `S<=C_0:=2(D_M-1)+lambda(p+u)-p`.                       `(C0)`

## 3. New rooted witness-slot theorem

Define the set of rooted witness slots

> `Omega={(x,z) in B x A : xz notin E(G)}`.              `(WS0)`

Since `sum_{z in A}d(z)=e(A,B)+2f`,

> `|Omega|=ab-e(A,B)=L_A+2f=Q+r`.                        `(WS1)`

Every edge `xy in E(G[B])` lies in the triangle `vxy`. Triangle-edge criticality therefore gives an orientation, say source `x`, head `y`, and a witness `z in A` with

> `N(x) cap N(z)={y}`.                                    `(WS2)`

The witness cannot lie in `B`, because `v` would be a second common neighbour. A fixed ordered pair `(x,z)` can certify only one head. Hence choosing one certificate per rooted B-edge gives an injection

> `E(G[B]) -> Omega`.                                     `(WS3)`

Let `W` be its image and `Upsilon=Omega\W`. Then

> `|Upsilon|=r`.                                          `(WS4)`

Consequently

> `delta=|Upsilon|-f`.                                    `(WS5)`

The second-extremal target is exactly

> `|Upsilon|>=f+D_M`.                                     `(WS6)`

Thus an above-`M(n)` survivor is precisely a graph in which rooted B-edge criticality leaves fewer than `f+D_M` unused B--A witness slots.

Core theorem package:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

## 4. Exact saturation and the hypercube mechanism

For `x in B`, define the rooted A-incidence code

> `phi(x)=(1_{xz in E})_{z in A} in {0,1}^A`.             `(HC0)`

If `r=0`, the slot injection is a bijection. Then:

1. `A` is independent, so `f=0` and `delta=0`;
2. every `B--A` nonedge slot has a unique common neighbour, lying in `B`;
3. every edge `xy in G[B]` is separated by exactly one A-coordinate,
   
   > `d_H(phi(x),phi(y))=1`;                              `(HC1)`
4. therefore `G[B]` is bipartite by the parity of `phi`;
5. for every `z in A`, if `S_z=N_B(z)` and `C_z=B\S_z`, every `x in C_z` has exactly one B-neighbour in `S_z`.

The proof that `A` is independent is itself informative. If an A-edge `yz` had different B-neighbourhoods, a saturated slot would already have an A common neighbour and could not be a rooted B-edge UCN slot. Hence `N_B(y)=N_B(z)`. But then criticality of `yz` has no possible B-witness, and an A-witness would share a B-neighbour with the source, again contradicting unique common neighbourhood.

The published `X_3` graph is exactly the `a=3` saturated model with `phi(B)={0,1}^3`, `G[B]=Q_3`, and A the three coordinate-face vertices. This gives the finite exception a direct structural role in the eventual programme rather than treating it as unrelated small-order noise.

## 5. Near-saturation collision identities

For `(x,z) in Omega`, put

> `c_B(x,z)=|N(x) cap N(z) cap B|`,
>
> `c_A(x,z)=|N(x) cap N(z) cap A|`.                       `(COL0)`

Used slots have `c_B=1` and `c_A=0`.

Define

> `H_B=sum_{xy in E(B)} |N_A(x) triangle N_A(y)|`,        `(HB0)`
>
> `H_A=sum_{yz in E(A)} |N_B(y) triangle N_B(z)|`.        `(HA0)`

Exact double counting gives

> `H_B=Q+sum_{(x,z) in Upsilon} c_B(x,z)`,                `(HB1)`
>
> `H_A=  sum_{(x,z) in Upsilon} c_A(x,z)`.                `(HA1)`

Since an A-vertex has at most `p+u` B-neighbours in the live partial-Boolean branch,

> `H_B-Q<=r(p+u)`.                                        `(HB2)`

Thus small `r` makes the rooted B-edge representation quantitatively close, in total edge-Hamming mass, to the saturated `d_H=1` hypercube model.

## 6. New A-edge Hamming-energy residual bound

An A-vertex satisfies

> `d_A(z)=p+u-epsilon_z-d_U(z)`.

Hence

> `d_A(z)<=K_A:=min(p+u,a-1)`.                            `(KA)`

Every unused slot contributes at most `K_A` to `(HA1)`, so

> `H_A<=rK_A`.                                             `(HA2)`

Let `c(z) in {0,1}^p` be the preserved tight-fibre Boolean code on A and define

> `J_A=sum_{yz in E(A)} d_H(c(y),c(z))`.                  `(HAM1)`

If an A-edge differs in `h` tight coordinates, its B-neighbourhoods differ in at least `2h` matched endpoints. Therefore

> `rK_A>=H_A>=2J_A`.                                      `(HAM2)`

Equivalently, for `K_A>0`,

> `r>=ceil(2J_A/K_A)`.                                   `(HAM3)`

This prices every A-edge according to how far it moves in the tight Boolean cube before any witness-channel split is used.

A direct A-edge has complementary tight codes and therefore Hamming distance `p`. If `D` denotes direct A-edge traffic,

> `rK_A>=2pD`,                                            `(DIR-R)`
>
> `D<=K_A r/(2p)=K_A(f+delta)/(2p)`.                     `(DIR-C)`

This is independent of the preserved direct-fan surplus/stability theorems.

## 7. Forced non-direct A-edge demand

Write the exact A-edge witness-channel decomposition

> `f=D+P_B+C`,                                             `(CH)`

where `P_B` is matched-B traffic and `C` is A/U UCN traffic.

Using `(DIR-C)` gives

> `P_B+C`
> ` >= [((2p-K_A)f-K_A delta)/(2p)]_+`.                  `(ND1)`

Now put

> `G=(p-lambda)(p+u)+q+E_U`,

so `(RSF)` is `f=G-delta`. The delta terms collapse:

> `P_B+C>=[(1-K_A/(2p))G-delta]_+`.                       `(ND2)`

Therefore every above-threshold survivor obeys

> `P_B+C`
> ` >= [(1-K_A/(2p))((p-lambda)(p+u)+q+E_U)`
> `      -(D_M-1)]_+`.                                    `(ND3)`

This is the first bridge that uses residual geometry itself to remove a definite portion of the direct channel before the matched/A-U capacity is optimized.

The preserved capacities include

> `P_B<=aR_A(L_A)`,                                       `(MB)`
>
> `(lambda+1)C<=R_code(S)S`,                              `(AU)`

and the stronger pair-resolved direct+A/U and fan packages remain available. A coarse global use of `(ND3)` with total `S` is still too weak; the gain should be retained into the pair allocation rather than collapsed immediately.

## 8. Preserved source/Hall and q/E machinery

For `x in A`, let `ell_x` be beta load and `k_x=p-ell_x`. The exact source-tuple hierarchy remains

> `sum_x binom(ell_x,r)/(p-ell_x+r)<=(1/r)binom(u,r)`     `(FDPr)`

for every `r>=3`, with integrated deficit profile

> `sum_{x in L}(p-ell_x)>=Phi_r(|L|)`.                    `(IST)`

Put `B_beta=sum_x ell_x`. The main beta floors are

> `B_beta >= [pu-R_hat a]_+`,                             `(STL)`
>
> `B_beta >= p(lambda+1-2p)_+`.                           `(RBF)`

Applying `(IST)` to all of `A` gives

> `B_beta<=ap-Phi_r(a)`.                                  `(ITB)`

The positive-support theorem gives the preserved `E_U` floor. The independent q coupling remains

> `q>=ceil([u(lambda-p)-E_U]_+/2)`,                       `(QL)`

and the beta-sensitive q upper bound with load-one compression remains

> `q<=au-B_beta+N_1`,                                     `(BQ)`

with

> `N_1<=floor((m_0a-B_beta)/(m_0-1))`,                    `(N1)`

for `m_0=min(p,u)>=2`.

These should feed actual `q,E_U,L_A` values into `(ND3)` rather than be globalized prematurely.

## 9. Preserved complete channel / local stability stack

For Boolean code `c`, write

`n_c=|A_c|`, `N_c=|(A union U)_c|`,

`w_c=N_c+n_c=2n_c+t_c`,

and let `S_c,L_c` be the corresponding total/A-slack.

Aligned-code self-pricing remains

> `S_c >= [(w_c/2)(3w_c/2-D_0)]_+`,                      `(AC1)`

where

> `D_0=5p+5u-3lambda-2`.

Define

> `R_code(s)=max(0,floor((D_0+sqrt(D_0^2+12s))/3))`.      `(RC)`

For a complementary pair `Pi`, direct and A/U traffic share the local capacity

> `2(lambda+1)(D_Pi+C_Pi)`
> ` <=R_code(S_Pi)(2L_Pi+S_Pi)`.                         `(CCP)`

The matched-B channel self-prices via

> `P_B<=aR_A(L_A)`,                                       `(MSP)`

with

> `R_A(L)=max(2,floor((1+sqrt(1+4L))/2))`.

The newer aligned matched-B cap and direct bounded-surplus fan theorem remain preserved, but the previous scalar collapse replacing pair slack by total `S` was diagnostically too weak. The live use of these results should therefore remain complementary-pair or source-local.

## 10. External eventual reduction: C5 is mandatory

Qiao Lin and Xiaolin Wang, *Discrete Applied Mathematics* 375 (2025), 332--337, DOI `10.1016/j.dam.2025.06.025`, prove that for sufficiently large `n`, every **C5-free** diameter-2-critical graph with at least

`floor((n-1)^2/4)+1`

edges is complete bipartite.

Therefore any sufficiently-large non-bipartite survivor at or above the live threshold must contain a `C5`. The live branch is already triangle-containing, so any eventual counterexample to the desired classification must contain **both a triangle and a C5**.

This is now a useful boundary condition for the near-saturation regime: the exact `r=0` model is hypercube-like/bipartite on `B`, while any eventual non-bipartite survivor must also realize a C5 somewhere in the full graph.

## 11. Audit

New package:

`project/research/post_ms/2026-09-18-rooted-witness-slot-saturation-v1/`.

The companion checker audits the rooted witness-slot identities on every graph-atlas D2C isomorphism class through order seven and every maximum-degree root, and separately reconstructs `X_3`:

- 21 D2C graph-atlas classes through order seven;
- 50 maximum-degree roots;
- 14 rooted B-edges checked for A-witness certificates;
- 91 B--A nonedge slots;
- 77 unused slots;
- 27 saturated (`r=0`) roots;
- zero failures of the exact collision identities or saturation consequences;
- `X_3`: `Q=12`, `|Omega|=12`, `r=0`, `H_B=12`, `H_A=0`.

These finite checks are audit support only. The promoted claims above are hand arguments.

## 12. Live frontier

The strongest next move should keep the new residual geometry local rather than return to a global scalar envelope.

Priority order:

1. combine the forced non-direct demand `(ND3)` with the **complementary-pair** A/U and matched-B capacities before summing pair slack;
2. exploit `(HB1)/(HB2)` and the Lin--Wang C5 requirement to understand how a C5 can coexist with a near-saturated hypercube-like rooted core;
3. use the preserved source/Hall beta-support stack to constrain `q,E_U` in the same local allocation.

The new key dichotomy is:

- if `r` is small, rooted B-edge criticality is close to exact hypercube saturation and A-edge tight-code Hamming energy is small;
- if A-edge Hamming/direct mass is large, `(HAM2)` converts it into unused slots and hence residual defect, forcing more of the required A-edge mass into the already self-priced non-direct witness channels.

Do not return to the closed mixed `{4,5}` selected-excess ladder, and do not optimize for first-proof priority on Erdős #742.
<!-- CURRENT-STATUS:END -->
