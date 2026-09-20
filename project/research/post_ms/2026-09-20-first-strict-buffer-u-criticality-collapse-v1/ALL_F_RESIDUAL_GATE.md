# All-F one-witness residual gate after exact z isolation

Date: 2026-09-20

Status: internal conditional synthesis for the sole surviving `m=1` polarization. It uses physical edge/score bounds as a proof interface; bounded scans are not part of the theorem.

## 1. Exact structural inputs

From `ONE_WITNESS_ALL_F_REDUCTION.md`:

`epsilon_z=p+u-2`,

`q<=Q_F:=binom(u,2)-binom(k+1,2)-(u-2)`.

The exact all-F local rooted-slot bill from the audited polarization theorem is

> `r>=R_F^low:=x+y h_F`,
>
> `h_F=p-1-floor((p-2)/x)`.                             `(F-RLOW)`

The Y-source score floor for one selected outside witness is

`L_Y=y(p-g+2)`.

The safe a0 floor inherited from `F-EPS` with `F=x-1` is

`epsilon_{a_0}>=A_F:=[p-y-x+2]_+`.

The exact common-core identity plus `z--W_0=empty` gives the pair/core physical floor `E_core>=k(p+k)`. Let `Sigma_F` denote the least pair-local score satisfying that floor together with buffer score `p-g+1`, the Y floor, `(CROWD)` and exact `Ccap_P`.

Every survivor must in particular satisfy

> `Sigma_F+(p+u-2)+A_F<=C0`.                            `(F-PAIR)`

## 2. Rooted residual upper bound

The total score identity gives the safe U-score ceiling

> `E_U<=C0-max{phi(g),L_Y+A_F}`.                        `(F-EU)`

Using the rooted identity

`r=(p-lambda)(p+u)+q+E_U`,

every all-F one-witness survivor must satisfy the explicit no-search inequality

> `R_F^low <= R_F^up`,                                  `(F-RES)`
>
> `R_F^up=(p-lambda)(p+u)+Q_F`
> `       +C0-max{phi(g),L_Y+A_F}`.

For `y>=2`, the head-saturation theorem additionally restricts `g` to 0 or 1, so `phi(g)=0` and the max term reduces to `L_Y+A_F`.

This is the correct rooted residual interface for the surviving one-witness branch. It replaces the obsolete all-R d/J optimization as the live `m=1` gate.

## 3. Immediate lambda floor in the y>=2 branch

Put

`T=u-k-2>=0`.

Since `x=k+g` and `a=x+y=2p+u-lambda-1`, exactly

> `lambda=2p+T-g-y+1`.                                 `(F-LAM)`

For `y>=2`, `g<=1` and the principal slice has `y<=p-1`. Therefore

> `lambda>=p+1`.

More precisely:

- g=0 gives `lambda>=p+2`;
- g=1 gives `lambda>=p+1`.

Equality requires the smallest outside reservoir `T=0` and `y=p-1`.

Thus the surviving y>=2 all-F arm already lives in a large-lambda corner rather than near lambda=0.

## 4. Exact two-step scaling law

Fix the shape parameters `(p,g,k,y)` and increase T by 2. Then u and lambda both increase by 2 while x,a,k,y and the lower rooted bill stay fixed.

The q term satisfies

`Q_F(u+2)-Q_F(u)=2u-1`.

The score cap satisfies the exact parity-preserving identity

`C0(lambda+2,u+2)-C0(lambda,u)=2p+2u+4`,

because

`floor((lambda+3)^2/4)-floor((lambda+1)^2/4)=lambda+2`.

Finally

`[(p-lambda-2)(p+u+2)]-[(p-lambda)(p+u)]`
`=-2(lambda+u+2)`.

The max term in `(F-EU)` is shape-fixed. Therefore

> `R_F^up(T+2)-R_F^up(T)=2(a-p)+1`.                    `(F-SLOPE)`

This is exact, not asymptotic.

Consequences along each parity class of T:

1. if `a<=p-1`, the available rooted residual upper bound decreases by at least one every two T-steps, so every fixed shape is eventually excluded;
2. if `a>=p`, this residual gate alone becomes weaker with T and cannot close an unbounded T-family; any eventual proof must obtain an additional physical bill on precisely those shapes.

The same slope appeared in the now-historical all-R grid gate. Its reappearance here shows that `2(a-p)+1` is a genuine scaling boundary of the present rooted residual relaxation rather than an artifact of the all-R certificate grid.

## 5. Next structural target

For y>=2 only `g=0,1` remain, with z having exactly one U-neighbour. The unresolved asymptotic obstruction is therefore very narrow: head-saturated all-F shapes with `a>=p`. The next useful theorem should create a new physical U-hole/A-U-hole or A-score bill that scales on those shapes, rather than further optimizing the already exact residual algebra. The y=1 matched-foot slice remains separate.