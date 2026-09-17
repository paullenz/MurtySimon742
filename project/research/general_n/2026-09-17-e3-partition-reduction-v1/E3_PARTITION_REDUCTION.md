# E=3 partition reduction: two of the three excess shapes are impossible

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate bridge-level continuation; not promoted; external mathematical review remains open.** This note continues the mixed `{4,5}` near-Turán scope at `(a,b,t)=(20,23,2)` after the small-excess theorem `E>=3` and the full selected-incidence Hall theorem.

## 1. Step-back and correction of the first coefficient choice

At total selected excess

    E=sum_i e_i=3,

there are only three partitions:

    (3), (2,1), (1,1,1).

The first attempt was to reuse the preceding `10p+15q` source support inequality unchanged. That works for partition `(2,1)`, but **fails for `(1,1,1)`**: at

    rho=5, p=5, q=3, g=1,

one has

    10p+15q-q(p+q)=71 > 70=10rho+20.

That failed coefficient choice is preserved here because it identifies the right adjustment. Raising the incoming coefficient from 10 to 12 produces a cleaner support inequality with **no rho=4 bonus at all**, and it closes both split-excess partitions in one stroke.

The correct conclusion is:

> In the mixed `{4,5}`, `h>=5`, `(20,23,2)` scope, the excess partitions `(1,1,1)` and `(2,1)` are impossible. Hence any surviving `E=3` bridge must have a **unique label of excess three**.

## 2. Inherited notation

Let `k` be the number of demand-five labels. Then

    r=76+k,
    Q=83+k,
    sum_u p_u=sum_u q_u=Q.

For a source `u`, put

    g_u=max(0,p_u-rho_u+1).

Every selected incidence `ui` satisfies

    e_i>=g_u.

Selected labels at one source are distinct. Also

    p_u<=rho_u+2,
    q_u+rho_u<=20,
    p_u+q_u<=22,

and every active source has `rho_u>=4` because all demands are at least four.

## 3. A new 12/15 source support inequality

For either excess partition `(1,1,1)` or `(2,1)`, every source satisfies

> **Split-excess source inequality**
>
>     12p_u+15q_u-q_u(p_u+q_u)
>       <=12rho_u+24.                                  (1)

### Proof

If `q=0`, the incoming cap `p<=rho+2` gives (1) immediately.

Assume `q>0`.

### Case A: `g=0`

Then `p<=rho-1`. Also `q<=20-rho`.

If `q<=12`, the coefficient of `p` is nonnegative, so

    12p+15q-q(p+q)
      <=12rho-12 + q(16-rho-q).

For `rho>=4`, the final quadratic is at most 36, attained only at the boundary `rho=4,q=6`. Hence the whole expression is at most

    12rho-12+36=12rho+24.

If `q>=12`, the coefficient of `p` is nonpositive, so setting `p=0` only increases the expression. Then

    12p+15q-q(p+q) <= q(15-q) <=36 <12rho+24.

### Case B: partition `(1,1,1)` and `g>0`

Only three labels have positive excess and each has excess exactly one. Thus `g=1`, `p=rho`, and the simple selected-incidence condition gives `q<=3`. Therefore

    12p+15q-q(p+q)
      =12rho + q(15-rho-q)
      <=12rho+24,

because `rho>=4` and `q<=3`, with equality possible only at `rho=4,q=3`.

### Case C: partition `(2,1)` and `g>0`

For `g=1`, at most two distinct labels are eligible, so `p=rho`, `q<=2`; direct substitution gives at most `12rho+18`.

For `g=2`, only the excess-two label is eligible, so `p=rho+1`, `q<=1`; then

    12p+15q-q(p+q)
      <=11rho+25
      <=12rho+24.

No source with `g>=3` can be active. This proves (1).

## 4. Global source lower bound

Sum (1) over all `b=23` sources. Since `sum p=sum q=Q`,

    27Q - sum_u q_u(p_u+q_u)
      <=12r+24b.

Hence

>     sum_u q_u(p_u+q_u)
>       >=27Q-12r-24b
>       =777+15k.                                      (2)

Unlike the earlier `10/15` inequality, this bound needs no `c_4` count and no special `rho=4` correction.

## 5. Partition-specific label ceilings

The small-excess note established the zero-excess ceiling

    U_0(k)=624+13k+min(14k,76+k).                      (3)

For fixed `s_i,R_i`, excess changes the label contribution by at most

    24E + sum_i e_i^2.                                 (4)

At `E=3`:

- partition `(1,1,1)` has `sum e_i^2=3`, hence

      label side <= U_0(k)+75;                         (5)

- partition `(2,1)` has `sum e_i^2=5`, hence

      label side <= U_0(k)+77.                         (6)

It therefore suffices to compare the stronger source lower bound (2) with the larger of the two label ceilings, namely `U_0(k)+77`.

For `0<=k<=5`, `14k<=76+k`, so

    U_0(k)=624+27k,

and

    (777+15k)-(U_0(k)+77)
      =76-12k
      >=16.                                            (7)

For `6<=k<=20`, `76+k<14k`, so

    U_0(k)=700+14k,

and

    (777+15k)-(U_0(k)+77)
      =k
      >=6.                                             (8)

Thus the source side is strictly larger than even the worst partition-`(2,1)` label ceiling for every `k=0,...,20`.

## 6. Bounded theorem

> **E=3 split-partition exclusion.** In the canonical bridge at `(a,b,t)=(20,23,2)`, suppose all twenty demands lie in `{4,5}` and at least five residual sources have degree at least five. If total selected excess is `E=3`, then neither partition
>
>     (1,1,1) nor (2,1)
>
> can occur.
>
> Consequently every surviving `E=3` profile must have exactly one excess-positive label, of excess three:
>
>     (e_i)^+=(3).

The proof is bridge-level and is not a Murty-Simon theorem promotion.

## 7. Why partition (3) is genuinely different

The new inequality (1) does **not** survive for partition `(3)`. A unique excess-three label permits

    p=rho+2, q=1, g=3.

At `rho=4`, for example,

    12p+15q-q(p+q)
      =80
      >72=12rho+24.

At `rho=5`, with `p=7,q=1`, the value is `91`, while `12rho+24=84`, a surplus of 7. Thus the obstruction is real and localized.

Every such `g=3` source must use the **same unique excess-three label** `i_*`. Full selected-incidence eligibility additionally requires

    s_*<=rho_u,
    C_*>=p_u+q_u=rho_u+3,

and the exact selected column degree is

    x_*=s_*+3 in {7,8}.

So the remaining case is now a sharply defined **single-column row-packing / endpoint-tail problem**, not a general `E=3` search.

## 8. Next target

Close or realize partition `(3)` by coupling the number and residual degrees of the exceptional `g=3` sources to the unique label's exact selected capacity `x_*` and endpoint mass `C_*`. The first failed `10/15` attempt and the successful `12/15` correction show that further undirected scalar coefficient tuning is unlikely to be the main missing ingredient; the unique-column Hall information should now be used directly.
