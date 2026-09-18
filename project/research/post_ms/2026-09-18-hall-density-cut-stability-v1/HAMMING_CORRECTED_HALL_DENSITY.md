# Hamming-corrected Hall density

Date: 2026-09-18

Status: hand structural strengthening of `HALL_DENSITY_STABILITY.md`, obtained by feeding the local rooted-slot Hamming inequality back into the Hall cut. No eventual second-extremal theorem is claimed.

## 1. Key observation

Let `X` be a nonempty proper family of complementary tight-code pairs. Put

> `x=a_X`, `y=a-x`,
>
> `M_X=xy-e(A_X,A\A_X)`.

Thus the actual A-cut has `xy-M_X` edges.

Every A-edge crossing this cut joins vertices whose tight Boolean codes belong to **different unordered complementary-pair classes**. Therefore the two endpoint codes are neither equal nor complementary; in particular their Hamming distance is at least one.

The local rooted-slot Hamming theorem says

> `sum_{z in A_X} sum_{w in N_A(z)} d_H(c(z),c(w)) <= R_X`. `(H1)`

Every internal direct edge of `A_X` is counted twice in `(H1)` and has Hamming distance exactly `p`, contributing `2pD_X`. Every crossing A-edge contributes at least one. Hence

> `R_X >= 2pD_X + (xy-M_X)`.                             `(H2)`

Recall

> `J_X=R_X/p-2D_X`.

Therefore:

### Theorem 1.1 — cross-Hamming floor on unused direct credit

> `J_X >= (xy-M_X)/p`.                                   `(HJ)`

The quantity previously treated as merely unused direct/Hamming credit is forced to be large whenever the pair-family A-cut is dense.

## 2. Strengthened low-density stability

For capacity Hall weight

> `W_P=Ccap_P+L_P-Z_P+R_P/p`,

we have exactly

> `W_X-x(x-T0)=2E_X+M_X+J_X+kappa_X`,                    `(CEH)`

with all terms nonnegative.

Assume every active pair in `X` has capacity density `<tau`, so `W_X<tau x`. Since

> `T0=a-p`,
>
> `T0+tau-x=y-p+tau`,

`(CEH)` gives

> `2E_X+M_X+J_X+kappa_X < x(y-p+tau)`.                   `(H3)`

Insert `(HJ)`:

### Theorem 2.1 — Hamming-corrected Hall stability

For every nonempty proper capacity-low-density family,

> `2E_X+kappa_X+(1-1/p)M_X`
> `< x[(y-p+tau)-y/p]`.                                  `(HC-STAB)`

This holds for `p>=2`; for `p=1` there is no nontrivial split into distinct complementary-pair families.

Define the corrected margin

> `Delta_{p,tau}(y)`
> ` := y-p+tau-y/p`
> ` = ((p-1)/p)y-(p-tau)`.                               `(DELTA)`

Then `(HC-STAB)` is simply

> `2E_X+kappa_X+(1-1/p)M_X < x Delta_{p,tau}(y)`.         `(HC)`

## 3. Strictly stronger Hall mass threshold

The left side of `(HC)` is nonnegative, so every nonempty proper low-density family must satisfy

> `Delta_{p,tau}(y)>0`.

Thus:

### Corollary 3.1 — Hamming-corrected density mass bound

> `y > p(p-tau)/(p-1)`,                                  `(YLOW)`

or equivalently

> `x < a - p(p-tau)/(p-1)`.                              `(XUP)`

The original Hall-density theorem gave only `y>p-tau`. The improvement comes entirely from the unavoidable Hamming cost of the actual A-cut.

For integer `tau` with `0<=tau<p`, `(YLOW)` often gains an entire A-vertex after rounding. More importantly, for real threshold optimization it creates a genuine open gap rather than merely a discrete correction.

## 4. Stronger rigidity window

The corrected margin also expands the near-equality rigidity range.

Since `E_X` is integral and appears with coefficient two, if

> `x Delta_{p,tau}(y) < 2`,                               `(E0)`

then

> `E_X=0`.                                                `(E0c)`

Since `M_X` is integral and appears with coefficient `1-1/p`, if

> `x Delta_{p,tau}(y) < 1-1/p`,                          `(M0)`

then

> `M_X=0`.                                                `(M0c)`

Therefore `(M0)` implies both `E_X=M_X=0` and activates the complete-cut/one-way-source geometry of `RIGID_HALL_WITNESS_GEOMETRY.md`.

This is strictly stronger than the previous sufficient condition

> `x(y-p+tau)<1`,

because the compulsory cross-Hamming term `xy/p` has first been removed from the available Hall slack.

## 5. Consequences in the rigid window

Under `(M0)`, with `x>=3`, all preserved rigid-cut conclusions apply:

> `x<=p+u`,                                               `(R1)`
>
> `h_Y(x-p)_+<=u`,                                       `(R2)`

where `h_Y` is the number of distinct tight codes in the outside A-layer.

If additionally `x>u`, at least `x-u` tight coordinates are singleton coordinates on `A_X`, and all but at most one occupied complementary pair in `X` are one-sided.

Thus the Hamming correction does not merely improve a numerical density bound: it substantially enlarges the parameter region in which Hall near-equality collapses to a highly specific Boolean-code geometry.

## 6. Strategic consequence

The live Hall attack now has three nested outcomes for a threshold family:

1. `(YLOW)` can rule out the proposed low-density mass immediately;
2. if the corrected margin is small, `(HC)` forces little export/missing-cut/capacity slack and eventually exact rigidity;
3. exact rigidity invokes the witness/code-collapse theorems.

This is preferable to optimizing the uncorrected Hall density because it reuses the already-proved local rooted-slot Hamming theorem and charges every cross-pair A-edge at the moment the Hall cut is formed.

The order-12 `X_3` hostile control remains untouched: its canonical root has independent A and no nontrivial A-cut demand of this type.