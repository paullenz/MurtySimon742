# Dependency correction: repeated outside code eliminates the X-reverse boundary arm

Date: 2026-09-21

Status: **same-session correction / dependency map**. This note records which earlier files are superseded or demoted by the strengthened raw boundary theorem.

## Corrected physical fact

For an exposed boundary edge `y q_i^{d_i}` with `y in Y_d`, an X-reverse witness w would require

`N(q_i^{d_i}) cap N(w)={y}`.

But both q_i and w see every vertex of `Y_d`: q_i because they all have coordinate bit d_i, and w because the rigid X--Y cut is complete. Hence

> **if `|Y_d|>=2`, X-reverse is impossible.**

The reverse channel survives only for singleton outside code classes.

## Superseded / demoted same-session artifacts

1. `RIGID_CUT_REVERSE_GAMMA_MULTIPLICITY.md`
   - corrected in place;
   - reverse-gamma multiplicity is now scoped to `y_d=1`;
   - its former repeated-code reverse-only branch is vacuous/superseded.

2. `RESIDUAL_ONE_ASYMPTOTIC_BOUNDARY_WEDGE.md`
   - marked superseded in place;
   - its reverse-capacity optimization is not live for `y>=2`.

3. `RESIDUAL_ONE_BOUNDARY_POPULATION_OBSTRUCTION.md`
   - corrected in place;
   - the old `y<=k` reverse-capacity alternative is replaced by the exact forward-only condition `c>=p-1`, sharpened to `c>=p+1` when the residual K class is nonempty.

4. `HALF_RAY_BOUNDARY_CERTIFICATE_SCORE_CLOSURE.md`
   - remains correct as a closure, but its score/gamma calculations are now merely backup;
   - the half-ray dies earlier by the forward population count.

5. `ONE_CODE_R1_K2_INTERMEDIATE_HALF_RAY.md` (20 September)
   - remains useful as a historical scalar-method diagnostic;
   - its conclusion that the parameter ray is an aggregate-method escape does **not** imply a graph-realizability escape and is superseded as a live candidate by the raw boundary theorem.

6. `ONE_CODE_NEAR_RIGID_SCALAR_ESCAPE_FAMILY.md` (20 September)
   - remains useful as a historical demonstration that the old scalar score package had room;
   - the family is **not graph-realizable** under the corrected boundary theorem: it has `p=3t,c=2t,r=t,y=t>=2,m=2t`, while forward-only routing requires `p<=c-r+2=t+2`, impossible for `t>=2`.

7. Half-ray H--U equality/superconstant files
   - not logically invalidated;
   - now strategically subordinate, because the ray itself is already unrealizable upstream.

## New live spine inside the rigid one-code interface

The correct order is now

`raw boundary trichotomy`
` -> repeated-code reverse exclusion`
` -> global matched-leaf collapse`
` -> full boundary exposure when m>=2`
` -> complementary witness-class exclusion from boundary U routing`
` -> exact forward reservoir e=c-r`
` -> p<=c-r+2 for y>=2`.

Only after this literal realizability filter should score, rooted-Q, pair-local capacity or H--U residual-slot machinery be applied.

## Strategic effect

Two prominent unbounded scalar escape families from 20 September are no longer live graph candidates:

- the corrected residual-one intermediate half-ray;
- the large-gap family `p=3t,c=2t,y=t,u=4t,x=5t,k=3t,m=2t`.

The remaining repeated one-code branch with `m>=2` must satisfy

> **`c>=p+r-2`.**

Thus the next work should intersect this near-maximal rooted-gap condition with the exact residual defect `delta`, rooted triangle count Q and pair-local Hall constraints, rather than continue optimizing the superseded scalar escape geometries.
