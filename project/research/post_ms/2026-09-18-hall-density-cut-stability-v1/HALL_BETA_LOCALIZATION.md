# Hall-density / beta-source localization bridge

Date: 2026-09-18

Status: hand structural composition of the new Hall-density theorem with the preserved integrated source-tuple beta theorem. No eventual second-extremal conclusion is claimed.

## 1. Local beta load

For `z in A`, let `ell_z` be its beta load. Its designated beta sources are pairwise-distinct U-neighbours, so

> `ell_z <= d_U(z)`.                                      `(B0)`

For a complementary-pair family `X`, put

> `B_X:=sum_{z in A_X} ell_z`,
>
> `x:=a_X`,
>
> `s_X:=e(A_X,U)=xu-Z_X`.                                `(B1)`

Then immediately

> `B_X <= s_X = xu-Z_X`.                                  `(B2)`

This is elementary, but it is the missing local bridge between pair cross-deficit `Z_X` and the beta/source hierarchy.

## 2. Low Hall density expels beta load

Recall the capacity Hall weight

> `W_P=Ccap_P+L_P-Z_P+R_P/p`,                             `(B3)`

and suppose every active pair in a nonempty family `X` has

> `W_P/a_P < tau`.                                        `(B4)`

Then `W_X<tau x`, so

> `Z_X>Ccap_X+L_X+R_X/p-tau x`.                           `(B5)`

Combining `(B2)` and `(B5)` yields:

### Theorem 2.1 — beta evacuation from a low-capacity family

> `B_X`
> `< x(u+tau)-Ccap_X-L_X-R_X/p`.                          `(BE)`

Thus low Hall-density is not merely a statement about certificate capacity. It forces the same family to carry little beta load, because its low density can only be achieved by a large A--U nonincidence deficit `Z_X`.

Equivalently, if `B_beta` is total beta traffic and `bar X` is the complementary family,

> `B_barX`
> `> B_beta-x(u+tau)+Ccap_X+L_X+R_X/p`.                   `(BE-C)`

So beta traffic is **expelled into the high-density complement**.

## 3. Integrated source-tuple obstruction on the complement

The preserved integrated source-tuple theorem applies to every subset `L subseteq A`: for every fixed `r>=3`,

> `sum_{z in L}(p-ell_z)>=Phi_r(|L|)`.                    `(IST)`

For `L=A_barX`, of size `a-x`, this gives

> `B_barX <= (a-x)p-Phi_r(a-x)`.                          `(BUP)`

Combining `(BE-C)` and `(BUP)` gives:

### Theorem 3.1 — Hall/beta localization inequality

Every nonempty capacity-low-density family `X` of A-mass `x` satisfies, for every fixed `r>=3`,

> `B_beta`
> `< x(u+tau)+(a-x)p-Phi_r(a-x)`
> `  -Ccap_X-L_X-R_X/p`.                                  `(HBL)`

In particular, dropping only nonnegative terms gives the parameter/mass-only necessary condition

> `B_beta`
> `< F_{r,tau}(x):=`
> `  x(u+tau)+(a-x)p-Phi_r(a-x)`.                         `(HBL0)`

This is the first direct composition of the complementary-pair Hall density with the exact source-tuple hierarchy.

## 4. Excluding candidate low-density masses

Let `B_*` be any valid forced lower bound on total beta traffic. If for some integer `x>0`

> `B_* >= F_{r,tau}(x)`,                                  `(EX)`

then **no** capacity-low-density family of A-mass `x` can exist.

Hence for the threshold family

> `X_<tau={P:a_P>0, W_P/a_P<tau}`,                        `(TH)`

whose mass already obeys `a_{X_<tau}<T0+tau`, the possible integer masses are further restricted to those `x` satisfying `(HBL0)` for every available source-tuple order `r`.

If `(EX)` holds for every integer

> `1 <= x < T0+tau`,                                      `(EXALL)`

then `X_<tau` must be empty: every active complementary pair has Hall-capacity density at least `tau`.

This is a clean route from global forced beta traffic to a **pointwise lower density statement on every occupied code pair**.

## 5. Support version

The same result can be stated through source support. From `(BE-C)` define

> `B_out := [B_beta-x(u+tau)+Ccap_X+L_X+R_X/p]_+`.         `(Bout)`

The complement must carry strictly more than the untruncated quantity in brackets and therefore at least the corresponding integer beta load. The preserved support inverse gives

> `N_{+,barX} >= N_sup(B_out)`                             `(SUP)`

(up to the obvious integer handling if the strict lower bound is nonintegral).

Since `N_{+,barX}<=a-x`, feasibility requires the source-support capacity of `a-x` vertices to accommodate `B_out`; `(HBL)` is the direct integrated form of that statement.

## 6. Strategic consequence

The previous live frontier asked whether beta/source support could prevent the A--U deficit `Z_P` from being anti-correlated with the large/high-capacity pair classes. The answer is now partially explicit:

- a low-capacity family requires large `Z_X`;
- large `Z_X` directly suppresses its local beta load through `B_X<=xu-Z_X`;
- therefore forced beta traffic is pushed into the complementary high-density family;
- the integrated source-tuple theorem limits how much beta traffic that complement can carry as a function of its A-mass.

What remains is quantitative optimization/classification, not discovery of the bridge. The next useful calculation is to evaluate `(HBL0)` with the project's existing forced beta lower bound `B_*` across the still-live finite/asymptotic parameter region and determine whether it eliminates whole ranges of threshold masses `x`; any surviving near-equality range should then be attacked with the complete-cut/one-way-source rigidity from `HALL_DENSITY_STABILITY.md`.

The published 12-vertex `X_3` control is untouched: `u=0` and the beta mechanism is inactive at its canonical root.