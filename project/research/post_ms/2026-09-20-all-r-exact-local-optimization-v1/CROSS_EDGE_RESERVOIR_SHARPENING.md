# Cross-edge reservoir sharpening inside the all-R equality pinch

Date: 2026-09-20

Status: **internal conditional follow-up** to `ALL_R_EXACT_LOCAL_OPTIMIZATION.md`. The rigid complete-cut realizability caveat and the 20 September daily audit remain binding.

## 1. Why the crude cross-capacity gate is not the end of the calculation

For `y>=2`, the preceding note proves that at least

`R=gy`

edges of the complete `X--Y` cut must be certified by outside witnesses among the d vertices of `U_o\{z}` which are nonadjacent to z. The k core vertices can account for at most `ky` cut edges; the buffer, z, and the J purified z-neighbours cannot supply the remaining certificates.

Let `s` be the number of **actually used outside cross-edge witnesses**. These witnesses are disjoint from the m internal-X witnesses: an internal-X witness has code `bar C` and is anticomplete to Y, whereas a `bar C` cross witness must have one Y-head; a `bar d` cross witness has the wrong code for an internal-X certificate.

Thus

> `m+s<=d`.                                             `(MS-d)`

Every outside cross witness has code `bar C` or `bar d`, neither of which can be adjacent to `a_0` by the already-proved `A0-CODE` localization. Therefore

> `d_U(a_0)<=1+d-m-s`,                                  `(A0-DMS-DEG)`
>
> `epsilon_{a_0}>=p+u-y-d+m+s-1`.                      `(A0-DMS)`

This strengthens the z/a0 conservation law to

> `epsilon_z+epsilon_{a_0}>=2p+k+u-y+m+s-2`.           `(ZA0-MS-CONS)`

## 2. Selected cross certificates are physical A--U holes

Choose one raw criticality certificate for each of the at least R outside-certified cut edges. Ordered `(source,witness)` injectivity makes the resulting source-witness pairs distinct. Since source lies in A and witness in U, these are R distinct physical A--U nonedges.

The outside cross witnesses lie in columns disjoint from the core, buffer, z, J purified neighbours, and the m internal-X witness columns. Hence the total missing A--U incidence ledger strengthens to

> `Z >= Z_0+NJ+e+m(y+1)+R`.                             `(Z-CROSS)`

No orientation choice is hidden in this bound: every selected raw certificate contributes its nonadjacent source-witness pair.

## 3. Slack-weighted cross capacity

For a used `bar C` cross witness w, fixed-head localization gives `N_Y(w)={y_w}`. If it certifies `r_w` distinct X-sources, then w is nonadjacent to those r_w sources. Maximizing every other adjacency gives

> `epsilon_w >= [r_w-(x-p+1)]_+`.                       `(C-CROSS-PAY)`

For a used `bar d` cross witness, fixed-head localization gives `N_X(w)={x_w}`. If it certifies `r_w` distinct Y-sources, then

> `epsilon_w >= r_w+(p-y-1) >= r_w`,                    `(D-CROSS-PAY)`

because the all-R setup has `p-y>=1`.

Put

> `F=[x-p+1]_+`.

For either witness type, the amount of certificate load that can be carried without forcing positive slack is at most F, and a single witness carries at most `M=max{x,y}` selected cut edges. Therefore, for s used outside cross witnesses carrying total selected load at least R,

> `s M >= R`,                                           `(S-CAP)`
>
> `E_cross >= [R-sF]_+`.                                `(CROSS-PAY)`

The second inequality is deliberately a type-relaxed lower bound; it remains valid if some witnesses are `bar d`, whose cost is higher.

Consequently

> `s>=ceil(R/M)`,                                       `(S-LOW)`

and the total U-slack floor used in local optimization becomes

> `E_U >= E_0(d)+P_int(e,m)+[R-sF]_+`,                 `(EU-CROSS)`

where `P_int(e,m)=[e-m(x-p-2)]_+` is the exact internal-X witness price from the predecessor note.

## 4. Hall and pair gates with the cross population retained

For fixed `(d,m,s,e)`, retain simultaneously:

- `m+s<=d`;
- `m<=e<=m(x-2)` when `m>0`, and `e=0` when `m=0`;
- exact pair-local `Sigma_P^+(1)` with `(A0-DMS)`;
- `E_U` bounded below by `(EU-CROSS)`;
- the exact Hall inequality using `ZX-M`;
- the J-independent-set q ceiling;
- the physical total-Z lower bound `(Z-CROSS)`;
- the rooted residual requirement.

The Hall lower bound becomes

> `e >= B_d+m+P_int(e,m)+[R-sF]_+`.                    `(H-CROSS)`

The cross witness population therefore cannot be treated as a free capacity reservoir: using more physical witnesses reduces `(CROSS-PAY)` but raises `epsilon_{a_0}` through `(A0-DMS)`.

## 5. Diagnostic replay

The same bounded abstract box used by the daily-audited all-R diagnostic was replayed with the strengthened `(d,m,s,e)` system.

Baseline predecessor equality-pinch rows:

> **173,347**.

Rows surviving the first exact `(d,m,e)` package plus the crude cross-capacity gate:

> **78,582**.

Rows surviving the slack-weighted cross-witness population, `(A0-DMS)`, `(EU-CROSS)`, `(Z-CROSS)` and `(H-CROSS)`:

> **71,996**.

Thus this sharpening rejects a further **6,586** abstract rows beyond the immediately preceding checkpoint.

Among first-feasible representatives, the remaining set is still overwhelmingly `e(X)=0`: 67,096 rows with `y>=2` and 4,515 with `y=1` choose `e=0`, while only 385 choose `e>0`. This is optimizer diagnostic information only, not a uniqueness statement and not graph evidence.

## 6. Next structural target

The diagnostic now says very clearly where hand work should go: the surviving geometry is predominantly the complete bipartite A-layer with `e(X)=e(Y)=0`. The next theorem should therefore refine the two witness-star types themselves rather than add another generic score inequality.

For `y>=2`, every outside cut witness has a graph-fixed single head on one side. The next attack should determine whether raw criticality of the witness-head edge forces additional located U--U holes or forces reuse of a graph-fixed complementary witness, and then charge those physical incidences to `Q`, `E_U`, and the residual defect ledger.

The `y=1` slice should be kept separate because the special matched endpoint can in principle certify `X -> Y` cut edges and the cross-reservoir lower bound is not valid there.
