# Complementary-pair fan packing

Date: 2026-09-18

Status: follow-on structural theorem to `WHOLE_CODE_FAN_CAPACITY_AND_COMPACT_SCORECARD.md`.

No global eventual theorem is claimed.

## 1. Motivation

The whole-code fan theorem identifies the next possible escape very sharply: a large A/U fan can survive the global scorecard only if a substantial amount of slack is concentrated in the one complementary Boolean-code pair containing its source and witnesses.

This note makes that statement quantitative and shows that large fans supported on many different complementary pairs cannot all coexist cheaply.

## 2. Pair notation

Let

`P={c,bar(c)}`

be an unordered complementary code pair. Put

`S_P=S_c+S_bar(c)`,

`M_P=max(N_c,N_bar(c))`,

and

`L=lambda+1>0`.

For a fan with source code `c` and witness code `bar(c)`, the exact same-code edge budget is

`E_P=floor((N_cS_bar(c)+N_bar(c)S_c)/L)`.

Since both code-class populations are at most `M_P`,

> `E_P <= M_P S_P/L`.                                    `(PE)`

The whole-code source-local fan theorem gives

> `2d^2-(T+1)d <= S_bar(c)+2E_P`,                        `(PFC2)`

where

`T=p+u-lambda-1`.

## 3. One large fan forces pair-slack concentration

Since `S_bar(c)<=S_P`, `(PE)/(PFC2)` imply

`d(2d-T-1)`
` <= (1+2M_P/L)S_P`.

Therefore:

### Theorem 3.1 — complementary-pair slack floor

If

`d>(T+1)/2`,

then the complementary pair supporting the fan satisfies

> `S_P >= L d(2d-T-1)/(L+2M_P)`.                         `(PSF)`

Equivalently, in integer form,

> `S_P >= ceil(L d(2d-T-1)/(L+2M_P))`.                   `(PSFi)`

Thus a genuinely large A/U fan has only two ways to remain cheap:

1. its supporting complementary pair contains a very large Boolean code class (`M_P` large); or
2. the pair itself captures a substantial amount of the total slack `S`.

This is the desired bridge from fan rigidity to code-distribution rigidity.

## 4. Explicit pair-local fan cap

Rearranging `(PSF)`, every fan supported on pair `P` obeys

> `2d^2-(T+1)d`
> ` <= (1+2M_P/L)S_P`.                                   `(PFC3)`

Hence

> `d`
> ` <= floor((T+1`
> `   +sqrt((T+1)^2+8(1+2M_P/L)S_P))/4)`                `(PCR)`

whenever the positive-root expression is used as a real upper bound and then floored.

The exact integer test `(PFC3)` should be preferred in code; `(PCR)` is the compact reviewer-facing form.

## 5. Distinct-pair packing theorem

Choose at most one A/U fan from each of a family of distinct unordered complementary pairs `P_j`. Let its order be `d_j` and pair maximum population be `M_j`.

Assume each chosen fan lies above the free threshold

`d_j>(T+1)/2`.

The pair slacks are disjoint and

`sum_j S_{P_j}<=S`.

Applying `(PSF)` pair by pair gives:

### Theorem 5.1 — complementary-pair fan packing

> `sum_j`
> ` [ L d_j(2d_j-T-1)/(L+2M_j) ]`
> ` <= S`.                                                `(PFP)`

In particular, if every chosen pair has `M_j<=M` and every chosen fan has order at least `D>(T+1)/2`, then their number `h` satisfies

> `h`
> ` <= S(L+2M)/(L D(2D-T-1))`.                           `(PH)`

Use the floor of the right side for an integer count.

Thus the rooted A-edge traffic cannot evade local fan pricing merely by dispersing over many Boolean code pairs.

## 6. Structural trichotomy

Fix thresholds `D>(T+1)/2`, `M`, and `Sigma`.

If a rooted-transfer argument produces a fan of order at least `D`, then at least one of the following occurs:

1. **large code class:** its pair has `M_P>M`;
2. **pair slack concentration:** its pair has

   `S_P >= ceil(LD(2D-T-1)/(L+2M))`;

3. the supposed fan does not exist.

If rooted traffic produces such fans in more than

`floor(S(L+2M)/(L D(2D-T-1)))`

distinct low-population pairs, the candidate is impossible.

This is the useful formulation for the next Hall/source-tuple step: Hall machinery can attack large code classes, while the global scorecard can attack repeated pair-slack concentration.

## 7. Relation to the residual target

Above `M(n)`, rooted triangles force the A-edge floor

`f>=F_min=(p-lambda)(p+u)+q-D_M+1`.

After matched-B traffic, the preserved fan gate forces either a direct fan or an A/U fan. The new whole-code theorem turns the A/U alternative into `(PSF)/(PFP)`.

So the active structural chain is now

`delta<D_M`
` -> rooted triangle transfer`
` -> large A-edge mass`
` -> direct fan OR A/U fan`
` -> false-twin sparsity OR complementary-pair slack/code concentration`.

This is substantially closer to a compact stability theorem than the previous independent A/U witness-reservoir split.

## 8. Scope and negative control

The order-12, size-32 `X_3` graph remains untouched: at its canonical root `u=0` and `F_min=0`, so no positive rooted fan is forced.

The theorem is conditional on the live partial-Boolean near-full setup and the already proved A/U fan geometry. It does not assert the false all-order 2019 conjecture or a complete eventual result.
