# Saturated-fan row capacity dichotomy

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand theorem; not externally reviewed. This note combines the equality structure of `SATURATED_BOOLEAN_FAN_PRIVATE_HOLES.md` with the exact row identities and per-source Hall capacity from `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md`.

## 1. Common row of one antipode fan

Let `z in U` be an unmatched antipode centre and let `Y` be a set of `d` U-antipode partners. Every member of `Y` has the same partial Boolean code

`c=bar c(z)`.

Hence every member of `Y` has the same row graph `K=K_c` on the `p` tight coordinates: the selected endpoint `q_i` in each tight pair is determined by `c`, and `K` records adjacency among those selected endpoints.

Put

`L=bar K`,

and for each coordinate `i` write

`A_i=N_L(i)`.

The preserved row identity says

`alpha(q_i) Delta bar c = A_i`,

`beta_i(c) Delta bar c = {i}`.                                (1.1)

Since `bar c=c(z)`, the alpha code at coordinate `i` is

> `alpha(q_i)=c(z) Delta A_i`.                                  (1.2)

In particular

> `alpha(q_i)=c(z) iff A_i=emptyset iff i is universal in K`.   (1.3)

Thus the private-hole code forced by saturation is an alpha code **exactly** on the universal coordinates of the common partner row. This is the precise version of the Hall interface left open in the predecessor note.

## 2. Neighbourhood classes are alpha-code classes

For each subset `C subseteq [p]`, define

`m(C)=|{i:A_i=C}|`.

Equal `A_i` are equal open neighbourhoods in `L`, hence form a true-twin clique in `K`. Let

`D=max_C m(C)`.                                                  (2.1)

The codes `alpha(q_i)` are equal exactly when the corresponding `A_i` are equal. Therefore `D` is simultaneously

1. the largest repeated alpha code among the `p` selected matched sources of this row;
2. the largest equal-open-neighbourhood class of `L`;
3. the size of a true-twin clique in `K`.

By the preserved projective-twin theorem for the matched 2-lift,

> `mu_alpha >= D`,                                               (2.2)

so some switching state of the matched core contains a true-twin clique of size at least `D`.

## 3. Exact fanwise alpha-capacity inequality

Let `n_s` be the number of A-vertices with Boolean code `s`, with

`sum_s n_s=a`.

For each coordinate `i`, the fan supplies exactly `d` physical P-U obligations at the matched source `q_i`, one for each `y in Y`.

The per-source Hall capacity says that at most

`n_{alpha(q_i)}`

of these `d` obligations can be oriented to the alpha endpoint. Therefore the number `B_i` forced to the beta endpoint satisfies

> `B_i >= (d-n_{alpha(q_i)})_+`.                                 (3.1)

Summing by neighbourhood/alpha classes gives

`B_beta(Y) >= sum_C m(C)(d-n_{c(z) Delta C})_+`.                 (3.2)

Dropping the positive-part only weakens the lower bound:

`B_beta(Y)`

` >= dp-sum_C m(C)n_{c(z) Delta C}`

` >= dp-D sum_C n_{c(z) Delta C}`

` >= dp-Da`.

Hence:

> **FAN ALPHA-SPILL THEOREM.**
>
> `B_beta(Y) >= max(0, dp-Da)`.                                  (FAS)

This is stronger than applying the global alpha-spill inequality blindly, because it uses the fact that all `d` partners present the same row and identifies the exact repetition parameter `D` controlling alpha reuse.

## 4. Distinct beta-code support

Define a coordinate to be **alpha-sufficient for the fan** if

`n_{alpha(q_i)}>=d`.

Otherwise (3.1) forces at least one beta-oriented obligation at coordinate `i`. Its beta code is

`beta_i(c)=c(z) Delta {i}`.

These `p` beta codes are pairwise distinct as `i` varies.

Let `J` be the set of alpha-insufficient coordinates. The alpha-sufficient coordinates lie in neighbourhood classes of size at most `D`. Every distinct alpha code that is sufficient consumes at least `d` A-vertices, so there can be at most

`floor(a/d)`

distinct sufficient alpha-code classes. Consequently

`p-|J| <= D floor(a/d)`,

and therefore

> **FAN BETA-SUPPORT THEOREM.**
>
> `|J| >= max(0, p-D floor(a/d))`.                               (FBS)

For every `i in J`, A contains at least one vertex of the distinct beta code

`c(z) Delta {i}`

which is adjacent to a member of `Y`. Because every `y in Y` is antipodal to `z`, every such beta witness is necessarily nonadjacent to `z`.

Thus a small true-twin/alpha repetition parameter `D` forces a large Hamming-radius-one beta support around the hub code.

## 5. Saturated-fan dichotomy

Now suppose the fan saturates Boolean antipode capacity,

`d=2η+1`.

The private-hole theorem independently forces at least `d` distinct external vertices of code `c(z)`, private one-per-source in `Y`. If `U` cannot host them all, equation (4.2) of the predecessor note forces corresponding A-multiplicity in the central code `c(z)`.

The present theorem shows exactly what that central multiplicity can and cannot buy:

- it supplies alpha capacity only for the `m(emptyset)` universal coordinates of `K`;
- all other coordinates use alpha codes `c(z) Delta C` with nonempty `C`;
- unless many coordinates collapse into large equal-neighbourhood classes (large `D`), a substantial set of coordinates is forced onto distinct beta codes.

Quantitatively, if one wants **no beta spill at all** from the `d` identical partner rows, (FBS) requires

> `D floor(a/d) >= p`,                                           (5.1)

so

> `D >= ceil(p/floor(a/d))`.                                    (5.2)

Thus high fan capacity without beta spill forces a large true-twin class in the matched core.

Conversely, if

`D < p/floor(a/d)`,

then beta spill is unavoidable on at least

`p-D floor(a/d)`

distinct coordinates and hence on that many distinct radius-one Boolean codes.

This is the desired **row-incidence dichotomy**:

> a saturated low-error U-antipode fan forces either
>
> 1. a large true-twin/alpha class in the matched 2-lift, or
> 2. a large, explicitly located set of beta witness codes adjacent to the fan and nonadjacent to its hub.

## 6. Relation to the first extremal fan

At `lambda=-1`, the cheapest saturated zero-slack fan has

`eta=1`, `d=3`.

Then

`B_beta(Y)>=max(0,3p-Da)`

and

`|J|>=max(0,p-D floor(a/3))`.

For `a=2p+u`, no-beta saturation already requires approximately `D>=3/2` when `u=o(p)`, i.e. at least a repeated alpha/neighbourhood class. This alone is not a contradiction; the important point is that the obstruction has now been reduced from an arbitrary row to either a repeated true-twin class or an explicit beta sphere.

For larger saturated fans (`d=2eta+1` growing), (5.2) forces `D` on the order of `d/2` when `a` remains near `2p`. Thus the matched core must develop a proportionally large switching true-twin class unless many beta coordinates appear.

## 7. Trust boundary and next move

The inequalities above are direct consequences of previously proved per-source capacity and the exact row translation identities; no finite enumeration is used.

They do **not** yet close the unmatched branch. In particular, beta spill corresponds to actual A-U edges and therefore does not by itself increase the global slack; it must next be priced through criticality of those A-U edges or through the disjoint-neighbourhood geometry of the hub/partner antipodes.

The next structural target should therefore be the beta side of this dichotomy: price many distinct beta-code neighbours of a saturated fan against A-side slack or additional antipode error. The alternative large-`D` branch can be attacked through the matched-core switching-defect/true-twin machinery already developed for the full-tight case.