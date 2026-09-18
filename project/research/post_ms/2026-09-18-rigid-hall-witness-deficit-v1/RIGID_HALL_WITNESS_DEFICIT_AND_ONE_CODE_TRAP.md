# Rigid Hall witness deficit and the one-code trap

Date: 2026-09-18

Status: internal hand-theorem package for the eventual / sufficiently-large diameter-2-critical second-extremal programme around

`M(n)=floor((n-1)^2/4)+1`.

The published 2024 order-12, size-32 graph `X_3` is a mandatory negative control. Nothing below excludes it. No all-order or eventual second-extremal theorem is claimed.

## 1. Reassessment

The previous checkpoint showed that a near-equality Hall family becomes rigid: its A-cut is complete and every crossing A-edge takes its chosen criticality source on the outside of the family. The first witness-geometry theorem then showed that every outside source needs many singleton-head witnesses and that the U-witnesses lie in one complementary U-code class.

The next useful move is not another global scalar optimization. The singleton-head U-witnesses themselves create two local resources that had not yet been charged simultaneously:

1. A--U nonedges, hence loss of beta-source capacity;
2. U-slack, because reusing one singleton-head witness for several outside sources forces that witness to miss all of those sources.

The resulting bookkeeping is exact enough to turn the earlier code-count inequality into a residual/A-edge lower bound and, in the one-code outside case, a pair-local certificate-capacity bill.

## 2. Setup

Work in the live partial-Boolean branch. Put

- `B=N(v)`, `A=V\N[v]`;
- `p` tight antipode pairs in `B` and unmatched set `U`, `u=|U|`;
- `a=|A|=2p+u-lambda-1`;
- `T0=a-p=p+u-lambda-1`;
- `epsilon_z=b-d(z)`;
- `E_U=sum_{w in U}epsilon_w`, `L_A=sum_{z in A}epsilon_z`.

Let `X` be a nonempty proper union of complementary tight-code pairs, let

`x=|A_X|>=3`, `Y=A\A_X`, `y=|Y|=a-x`,

and assume the rigid Hall conclusion

`M_X=E_X=0`.

Thus the A-cut `X--Y` is complete and every crossing edge chooses its criticality source in `Y`.

Let `mu=mu_X` be the number of matched B-endpoints whose X-neighbourhood has size exactly one, and define

> `k=(x-mu)_+`.                                            `(K)`

The preserved singleton-head theorem gives `mu<=p`; for every `s in Y`, at least `k` of its `x` distinct witnesses lie in U, all in `U_bar(c(s))`, and every such U-witness has exactly one neighbour in X.

Let the distinct tight codes represented in Y be `d_1,...,d_h`, with multiplicities

`y_i=|Y_{d_i}|`, `sum_i y_i=y`.

For code `d_i`, let `W_i subset U_bar(d_i)` be the union of all U-witnesses used by sources in `Y_{d_i}`. Put `m_i=|W_i|`. For `w in W_i`, let `t_w` be the number of sources in `Y_{d_i}` whose crossing certificate uses w.

Different `W_i` are disjoint because they lie in distinct U-code classes.

## 3. The witness-incidence lemma

### Lemma 3.1 — incidence and singleton-head constraints

For every represented outside code `d_i`,

> `m_i>=k`,                                                `(I1)`
>
> `sum_{w in W_i} t_w >= y_i k`.                          `(I2)`

Every `w in W_i` satisfies

> `d_X(w)=1`,                                              `(I3)`

and is nonadjacent to each of the `t_w` outside sources that use it. Therefore

> `epsilon_w >= [x-T0+t_w-1]_+`.                          `(I4)`

Proof. A single outside source needs at least k distinct U-witnesses, giving `(I1)`; summing that requirement over the `y_i` sources gives `(I2)`. The rigid singleton-head property gives `(I3)`. Finally, w has at most one X-neighbour, at most `y-t_w` Y-neighbours, and at most `u-1` U-neighbours. Since a U-vertex has

`d_{A union U}(w)=p+u-1-epsilon_w`,

we get

`p+u-1-epsilon_w <= 1+(y-t_w)+(u-1)=y+u-t_w`.

As `p-y=x-T0`, this is `(I4)`. square

The point of `(I4)` is the reuse tradeoff: sharing a singleton-head witness among many outside sources saves U-population but costs one additional unit of U-slack for every additional source once the free threshold is exhausted.

## 4. Forced A--U nonedges and beta expulsion

Write

`Z_X=xu-e(X,U)`, `Z_Y=yu-e(Y,U)`, `Z=Z_X+Z_Y`.

### Theorem 4.1 — rigid witness-deficit floor

The rigid U-witness system forces

> `Z_X >= hk(x-1)`,                                       `(ZX)`
>
> `Z_Y >= yk`,                                            `(ZY)`
>
> `Z >= k[y+h(x-1)]`.                                    `(Z0)`

Proof. Every used U-witness has exactly one X-neighbour, hence contributes `x-1` distinct X--U nonedges. Each represented source code uses at least k distinct witnesses, and the witness code classes are disjoint, proving `(ZX)`. Every source-witness incidence is a Y--U nonedge, and `(I2)` summed over i gives at least yk such incidences, proving `(ZY)`. square

Since designated beta sources are U-neighbours, `ell_z<=d_U(z)` and hence

`B_beta<=e(A,U)=au-Z`.

Therefore:

### Corollary 4.2 — rigid beta ceiling

> `B_beta <= au-k[y+h(x-1)]`.                              `(RB)`

This is a new conservation law for a rigid cut: the very U-witnesses needed to certify the complete A-cut remove A--U adjacency slots that could otherwise carry beta traffic.

The source-tuple theorem can be kept local rather than global. For every preserved order r,

> `B_X <= min{x u-hk(x-1), x p-Phi_r(x)}`,                `(RBX)`
>
> `B_Y <= min{y(u-k), y p-Phi_r(y)}`.                     `(RBY)`

Thus

> `B_beta <= min{x u-hk(x-1),xp-Phi_r(x)}`
> `          +min{y(u-k),yp-Phi_r(y)}`.                   `(RBOX)`

This is the rigid Hall/source-tuple beta box. It should be used before collapsing to total slack.

## 5. Multiplicity-sensitive U-slack floor

Put

> `g=x-T0=p-y`.                                           `(G)`

### Theorem 5.1 — rigid U-slack floor

If `g>=1`, then

> `E_U >= k[y+h(g-1)]`
> `     = k[p-1+(h-1)(g-1)]`.                             `(EU+)`

If `g<=1`, then

> `E_U >= [yk-(1-g)u]_+`.                                 `(EU-)`

Proof for `g>=1`. By `(I4)`, every used witness has

`epsilon_w >= g+t_w-1`.

Hence for code d_i,

`sum_{w in W_i}epsilon_w >= (g-1)m_i+sum_w t_w`
`                         >= (g-1)k+y_i k`.

Sum over i. Since `x+y=a=p+T0`, the displayed alternative form follows.

Proof for `g<=1`. Put `c=1-g>=0`. Then `(I4)` gives

`epsilon_w >= [t_w-c]_+`.

If `u_i=|U_bar(d_i)|`, convex truncation gives

`sum_{w in W_i}epsilon_w >= [y_i k-c u_i]_+`.

Summing and using `sum_i u_i<=u` gives `(EU-)`. square

At the boundary `g=1`, both formulas give `E_U>=yk`.

### Interpretation

For `g>=1`, even the one-code outside model costs

> `E_U>=k(p-1)`.                                          `(BASE)`

Additional outside code diversity is not free: each extra represented code costs another

> `k(g-1)`

units of U-slack.

This is substantially stronger than choosing one outside source per code and counting only the baseline witness slack.

## 6. Rooted residual and forced A-edge consequence

The exact A--U nonedge identity is

> `Z=u(p-lambda)+2q+E_U`.                                 `(ZID)`

Define

> `Z_rig=k[y+h(x-1)]`,                                    `(ZR)`
>
> `D=Z_rig-u(p-lambda)`.                                  `(D)`

Let `E_rig` denote the right side of `(EU+)` or `(EU-)`, according to g. Then every rigid-cut survivor satisfies

> `E_U>=E_rig`,
>
> `2q+E_U>=D`.

The exact integer minimum of `q+E_U` under these constraints is

> `q+E_U >= E_rig + ceil((D-E_rig)_+/2)`.                 `(QE)`

The residual identity is

> `f=(p-lambda)(p+u)+q+E_U-delta`.                        `(RSF)`

For an above-M(n) graph, `delta<=D_M-1`, so:

### Theorem 6.1 — rigid-cut forced A-edge floor

> `f >= (p-lambda)(p+u)-D_M+1`
> `     +E_rig+ceil((D-E_rig)_+/2)`.                      `(RF)`

This is a direct bridge from rigid Hall witness geometry to the rooted-triangle/residual programme. It is local information converted into a compulsory increase in internal A-edge mass.

Also, with

`C0=2(D_M-1)+lambda(p+u)-p`,

an above-M(n) graph has `E_U<=C0`, and hence

> `q >= ceil((D-C0)_+/2)`,                                `(RQ)`
>
> `Q >= p(p+u-1)+ceil((D-C0)_+/2)`.                       `(RQT)`

Thus sufficiently severe rigid witness deficit directly raises the rooted triangle count.

## 7. The rigid feasibility envelope and automatic code collapse

Let `B_*` be any independently valid forced beta-load lower bound. Every rigid above-M(n) candidate must simultaneously satisfy

> `hk<=u`,                                                `(F1)`
>
> `E_rig<=C0`,                                            `(F2)`
>
> `B_*+k[y+h(x-1)]<=au`,                                  `(F3)`

as well as the sharper source-tuple beta box `(RBOX)`.

For `g>=1`, `(F2)` becomes

> `k[p-1+(h-1)(g-1)]<=C0`.                                `(F2+)`

Consequently:

1. if `k(p-1)>C0`, the rigid cut is impossible;
2. if `g>=2` and `k(p+g-2)>C0`, any surviving rigid cut has `h=1`;
3. independently, if
   `B_*+k[y+2(x-1)]>au`, any surviving rigid cut has `h=1`.

More generally, `(F2+)` and `(F3)` give explicit integer upper bounds on h. This is a second code-collapse mechanism, independent of the older population-only inequality `hk<=u`.

The important transition is that code collapse is now driven by actual residual resources: U-slack and beta capacity.

## 8. One-code outside trap

Assume now `h=1`. Then all vertices of Y have one tight Boolean code d. Because every direct A-edge joins complementary Boolean code classes, there are **no direct edges inside Y**. Let

`P={d,bar d}`

be the outside complementary pair. Every crossing edge is non-direct and sourced in Y, and every internal Y-edge is also non-direct and sourced in P. Hence, if `t_P` is the chosen non-direct traffic sourced in P,

> `t_P>=xy+e(Y)`.                                         `(T1)`

The pair-local certificate theorem gives

> `2t_P<=Ccap_P`.                                         `(T2)`

Because the rigid cut is complete,

> `2e(Y)=y(y-T0)-L_Y+Z_Y`.                                `(YDEG)`

Combining `(T1)--(YDEG)` and using `Z_Y>=yk` yields:

### Theorem 8.1 — one-code outside pair-capacity bill

> `Ccap_P+L_Y >= y(p+x+k)`.                               `(ONE)`

Proof. We have

`Ccap_P >= 2xy+2e(Y)`
`          =2xy+y(y-T0)-L_Y+Z_Y`
`          =y(p+x)-L_Y+Z_Y`.

Now use `Z_Y>=yk`. square

Thus the endpoint of the rigid-collapse process is not a free one-code model: the single outside pair must pay simultaneously for every crossing edge, every internal Y-edge, and the singleton-witness nonedges generated by the crossing certificates.

There is an additional aligned-code bill. Since `Y=A_d` has size y, the preserved aligned-code crowding theorem applies to code d. In particular, whenever `3y>=D0=5p+5u-3lambda-2`, monotonicity of the crowding polynomial above its positive threshold gives

> `S_P>=S_d>=y(3y-D0)`.                                   `(CROWD)`

Hence `y(3y-D0)>C0` rules out the one-code endpoint in an above-M(n) graph.

The natural next classification step is therefore compact: combine `(ONE)` with the explicit formula for `Ccap_P` and the local pair slack/crowding constraints, rather than returning to a global scalar channel bound.

## 9. Diagnostic audit and trust boundary

A deterministic/random abstract checker accompanies this note. It independently tests:

- the witness-incidence nonedge floors `(ZX)/(ZY)`;
- both branches of the U-slack theorem `(EU+)/(EU-)` on randomly generated witness-incidence systems;
- the beta ceiling `(RB)`;
- the integer minimization in `(QE)` by brute force;
- the finite rigid-feasibility filters `(F2)/(F3)` over a broad integer parameter box.

The checker is audit support only. The promoted statements above are the hand derivations in this note.

A development run gave:

- 12,841 random witness-incidence systems: zero failures;
- 100,000 independent integer minimization checks for `(QE)`: zero failures;
- 1,910,960 abstract rigid parameter/code-count instances for `3<=p<=18`, `1<=u<=18`: 39,902 newly rejected by the U-slack/beta-deficit filters after the older population condition `hk<=u` was imposed (28,102 by the U-slack ceiling and 11,800 by the beta-deficit ceiling; these two rejection sets were disjoint in this diagnostic box);
- failures: zero.

The parameter scan is deliberately an abstract diagnostic, not a count of realizable D2C graphs.

## 10. Mandatory negative control

For the published `X_3` graph, the canonical root has

`p=4, u=0, lambda=4, q=s=f=r=0, Q=12, delta=0`.

The rigid U-witness mechanism is inactive. In any rigid-cut instance to which the present notation could be applied, `u=0` together with the preserved inequality `x<=mu+u` forces `k=(x-mu)_+=0`. Hence every new witness-deficit, U-slack, beta-expulsion and residual penalty above vanishes.

So the order-12, size-32 graph remains a valid hostile control; this package does not promote the false all-order conjecture.

## 11. Frontier

The rigid branch is now reduced to two increasingly narrow possibilities.

1. Before code collapse, `(RBOX)`, `(EU+)`/`(EU-)` and `(RF)` charge code diversity directly to beta capacity, U-slack and forced A-edge mass.
2. Once the feasibility envelope forces `h=1`, the endpoint must satisfy the pair-local bill `(ONE)` together with aligned-code crowding and the existing explicit `Ccap_P` formula.

The next highest-value move is to insert the actual one-sided pair data into `Ccap_P` and determine whether `(ONE)` leaves any asymptotic room. If it does, the surviving equality geometry should be classified directly. If it does not, the rigid Hall branch is closed and attention returns to non-rigid low-density families via the Hall/beta localization theorem.