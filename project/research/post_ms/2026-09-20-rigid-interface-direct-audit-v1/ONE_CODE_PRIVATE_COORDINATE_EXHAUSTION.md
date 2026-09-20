# One-code rigid cut — private-coordinate exhaustion theorem

Date: 2026-09-20

Status: **same-session structural theorem**, conditional on the rigid one-code near-equality interface and the already-preserved private-coordinate normal form. Independent hostile replay is still required before promotion. The zero-positive actual-D2C rigid-fixture caveat remains binding.

This note keeps the selected matched coordinates rather than replacing them immediately by the scalar inequality `m<=p`. The resulting conclusion is stronger: if the selected matched witnesses exhaust all p coordinates, there is no Boolean code left for an unmatched X-head.

## 1. Setup

Fix a d-coded source `s in Y=A_d`. Let

- `x=|A_X|>=3`;
- `k` be the number of selected crossing witnesses for s that lie in U;
- `m=x-k` be the number of selected matched singleton witnesses;
- `I subseteq [p]` be the private-coordinate set supplied by `RIGID_PRIVATE_COORDINATE_NORMAL_FORM.md`, so `|I|=m`;
- `R=[p]\I`, and put `r=|R|=p-m`.

The selected matched heads are distinct. For every selected matched head `h_i`, coordinate `i in I` is private relative to d:

`c(h_i)_i != d_i`,

while **every other vertex of `A_X` agrees with d at coordinate i**.

Let K be the set of the k U-certified heads, i.e. the heads not in the selected matched-covered set.

## 2. Coordinate exhaustion

### Theorem 2.1

For every `h in K`,

> `supp(c(h) xor d) subseteq R`.                          `(CE-1)`

Moreover the support is nonempty.

### Proof

For every `i in I`, private-coordinate normal form says that the selected head `h_i` is the unique A_X vertex differing from d at i. Since `h in K` is a different head, `c(h)_i=d_i`. This proves `(CE-1)`.

The support cannot be empty because then `c(h)=d`, but in the one-code endpoint `A_d=Y` and `K subseteq A_X`, so `A_X cap A_d=emptyset`. `square`

Thus all U-certified heads occupy nonempty subsets of the same residual coordinate set R. In particular:

> the number of distinct codes among K is at most `2^r-1`; `(CE-2)`
>
> every K-code lies at Hamming distance between 1 and r from d. `(CE-3)`

If `K` is nonempty, necessarily

> **`r>=1`.**                                             `(CE-4)`

## 3. Link to the rooted gap and escape count

Use the minimum-source parameterization from the large-gap note:

`c=lambda+1-g0`,

`d_U:=u-k`,

`m=x-k=p-c+d_U`.

Therefore

> **`r=p-m=c-d_U`.**                                     `(CE-5)`

This identifies the residual Boolean dimension exactly with the part of the rooted gap **not** spent on escaping U vertices.

Consequently, if `k>0`, `(CE-4)` gives

> **`d_U<=c-1`,**                                        `(CE-6)`
>
> **`k>=u-c+1`.**                                        `(CE-7)`

This sharpens the predecessor `d_U<=c`, `k>=u-c` by one whenever a genuine U-certified head exists.

Equivalently:

> **if `d_U=c`, then necessarily `k=0`.**                 `(CE-8)`

In that case `m=x=p`, and the size identity `x=p+u-c` gives `u=c`.

## 4. The first residual dimensions

The theorem gives literal normal forms when r is small.

### r=0

There is no nonempty Boolean support available. Hence K is empty:

> `r=0 => k=0`.                                          `(CE-R0)`

### r=1

Let `R={j}`. Every U-certified head has a nonempty support contained in `{j}`, so every one has the **same** code

> `C=d xor e_j`.                                          `(CE-R1)`

Thus the entire U-certified head set is one radius-one A_X code class.

### general r

The k U-certified heads are distributed among at most `2^r-1` nonempty residual supports. Hence some A_X code class contains at least

> **`ceil(k/(2^r-1))` heads.**                            `(CE-PH)`

For fixed small r this creates a forced large same-code A_X class, which can be fed into the preserved same-code edge/crowding machinery rather than treated as arbitrary X geometry.

## 5. Immediate correction to the small-gap picture

### c=0

Here `d_U<=c=0`. If `u>0`, then `k=u>0` and `(CE-5)` gives `r=0`, contradicting `(CE-R0)`. Therefore

> **`c=0 => u=0`, hence `x=p`.**                          `(CE-C0)`

The predecessor score-only zero-gap theorem allowed the tiny arithmetic tuples with `u=1,2`; the full private-coordinate geometry removes them. Only the `u=0` tail remains. This is a strengthening, not an invalidation of the earlier score bound.

### c=1

If `k>0`, then `(CE-6)` forces `d_U=0`, so

> `k=u`, `m=p-1`, `r=1`,                                 `(CE-C1a)`

and every U-certified head has the single common radius-one code from `(CE-R1)`.

The alternative `k=0` is possible only when `u=1`, in which case `m=p` and `x=p`. Thus the predecessor c=1 Branch A (`k=u-1,m=p`) collapses to its literal `u=1,k=0` endpoint; for every `u>=2` only the no-escape branch `k=u,m=p-1` survives.

## 6. Impact on the post-physical scalar escape direction

Any proposed scaling direction with

`d_U=c`, `k>0`, `m=p`

is impossible by `(CE-8)`. In particular the natural minimizer direction

`c=2t, p=2t, u=3t, y=1, k=t, d_U=2t, m=2t`

cannot represent the private-coordinate geometry: the p selected matched witnesses would use every coordinate, forcing each of the remaining k heads to have code d, forbidden in `A_X`.

The nearest admissible boundary is `d_U=c-1`, i.e. `r=1`; there the unmatched heads are not arbitrary but collapse to one common radius-one code. That is the correct structural frontier, treated separately in `ONE_CODE_POST_EXHAUSTION_ESCAPE_FAMILY.md`.

## 7. Trust boundary and next move

The proof uses only:

1. the rigid one-code purity `A_d=Y`;
2. the selected private-coordinate normal form for one fixed source;
3. the exact minimum-source identities `m=p-c+d_U` and `k=u-d_U`.

No finite scan or score relaxation enters the theorem.

The next high-value attack is the `r=1` normal form: a large single A_X code class at Hamming distance one from the source code, together with a large independent selected `U_bar(d)` witness set. This is substantially more rigid than the scalar `d_U=c-1` boundary suggests.