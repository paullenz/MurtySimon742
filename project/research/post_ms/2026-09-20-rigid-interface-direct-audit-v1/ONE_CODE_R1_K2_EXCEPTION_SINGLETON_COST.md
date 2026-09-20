# Residual-one k=2 exceptional-witness singleton cost

Date: 2026-09-20

Status: **same-session candidate structural continuation**, conditional on the rigid residual-one identities and the k=2 exception-budget note. No scan is used as proof.

The exception-budget theorem isolates K-free deficient U-vertices as the only escape vertices capable of repairing the heavy-reservoir edge-capacity obstruction. This note shows that an exceptional certificate is itself physically expensive: a U--U singleton has a degree-sum price, while the alternative orientation for a K-heavy--Y edge forces the exceptional witness to be X-anticomplete.

## 1. A general U--U singleton degree-sum lemma

For every `z in U`, the preserved exact identity is

> `d_{A union U}(z)=p+u-1-epsilon_z`.                    `(SC-UDEG)`

Take two nonadjacent U-vertices w,t with a literal singleton common neighbourhood

> `N(w) cap N(t)={e}`

where the singleton head `e` lies in `A union U`. Then, inside the universe `A union U`, their neighbourhood union contains at most

`|A|+u-2 = x+y+u-2`

vertices, while their intersection has size exactly one. Hence

`d_{A union U}(w)+d_{A union U}(t) <= x+y+u-1`.

Substitute `(SC-UDEG)` and `x=p+u-c`:

> **`epsilon_w+epsilon_t >= p+c-y-1`.**                  `(SC-UU)`

This is an exact physical price for any U--U singleton certificate. It does not depend on which code classes the two U-vertices occupy.

On the preserved low-k ray

`c=p=lambda=t`, `y=t-1`,

this specializes to

> **`epsilon_w+epsilon_t>=p`.**                          `(SC-RAY)`

Thus a low-slack K-heavy source cannot use a low-slack exceptional U-witness to certify a heavy-heavy edge.

## 2. Exceptional repair of a K-heavy internal edge pays `(SC-UU)`

In `ONE_CODE_R1_K2_EXCEPTION_BUDGET.md`, every exceptional U-witness t for an oriented K-heavy edge `w e` satisfies

`N(w) cap N(t)={e}`,

with w,t in U and e in U. Therefore every such source--witness incidence satisfies `(SC-UU)`.

Let `I` be the number of exceptional oriented-edge certificates between a K-heavy source set R (`|R|=r`) and a K-free exceptional witness set F (`|F|=f`). Summing `(SC-UU)` over the physical source--witness incidences gives

`(p+c-y-1) I`

` <= sum_{w in R} d_F(w) epsilon_w + sum_{t in F} d_R(t) epsilon_t`

` <= f E_R + r E_F`,

where `E_R=sum_R epsilon_w` and `E_F=sum_F epsilon_t`. Hence

> **`I <= (f E_R+r E_F)/(p+c-y-1)`.**                    `(SC-ICAP)`

On the low-k ray the denominator is p and `r,f<=p-1`, so in particular

> **`I <= E_R+E_F`.**                                    `(SC-RAY-I)`

Thus exceptional witness capacity cannot be restored faster than aggregate U-slack on that ray.

## 3. K-heavy--Y exceptional certificates have a second, X-hole orientation

Let w be K-heavy and `wy` an edge with `y in Y`. If `d_Y(w)>=2`, the heavy-reservoir argument rules out an H-witness; every certificate must use a K-free exceptional U-vertex t.

There are two possible singleton orientations.

### U--U orientation

If

`N(w) cap N(t)={y}`,

then w,t are nonadjacent U-vertices with singleton head y in A. The general lemma applies directly:

> `epsilon_w+epsilon_t>=p+c-y-1`.                         `(SC-YU)`

### Y--U orientation

If instead

`N(y) cap N(t)={w}`,

then t must be anticomplete to all of X. Indeed every X-vertex is adjacent to y because the X--Y cut is complete, so any X-neighbour of t would be an additional common neighbour of y and t.

Therefore

> **`N_X(t)=empty`.**                                     `(SC-X0)`

Such a witness contributes x located X--U nonedges. In the exact rigid identity

`2e_X=x g0-L_X+Z_X`,

those holes raise the X-side deficit/slack channel rather than disappearing into an undifferentiated exception count.

So every exceptional certificate needed to support `d_Y(w)>=2` pays in one of two currencies:

1. a U--U source/witness degree-sum of at least `p+c-y-1`, or
2. a witness vertex with the full X-hole block `N_X(t)=empty`.

## 4. Combined edge-capacity feedback

Retain the notation of the exception-budget note. Let A be the number of H--R holes and let I be the number of exceptional K-heavy internal-edge certificates actually used. The exact internal-edge count gives

> `E_R+3A+2I >= r^2-eta`,                                `(SC-EDGE)`

where `eta=sum_R d_Y(w)`; this is the pre-substitution form of the exception-budget inequality.

Substituting `(SC-ICAP)` prevents I from being treated as free capacity. On the low-k ray,

`I<=E_R+E_F`,

so any attempt to orient a quadratic number of K-heavy internal edges through K-free exceptions necessarily imports a quadratic U-slack bill unless the H-hole term A already carries that cost.

This is not yet a closed optimization because the Y-edge exceptions split between `(SC-YU)` and the X-anticomplete alternative `(SC-X0)`. But it removes the main loophole in the crude `rf` exception allowance: a single physical exception may be reusable across different sources, yet each source--witness singleton incidence still obeys the same degree-sum price, and the total reuse is controlled by `(SC-ICAP)`.

## 5. Strategic next move

The low-k ray is now reduced to a joint exception optimization with three genuinely physical currencies:

- H--K-heavy holes A, which feed Z_X/L_X;
- U-slack `E_R+E_F`, which bounds exceptional K-heavy edge capacity through `(SC-ICAP)`;
- X-anticomplete exceptional witnesses from `(SC-X0)`, each contributing a full block of x X--U holes.

The next step should keep the two Y-edge orientations separate and minimize this joint bill before applying the exact rooted identity and score ceiling. If that optimization is quadratic uniformly in the exception count, the current low-k asymptotic ray becomes finite-order.

Global caveat unchanged: bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`, so this remains conditional structural mathematics.