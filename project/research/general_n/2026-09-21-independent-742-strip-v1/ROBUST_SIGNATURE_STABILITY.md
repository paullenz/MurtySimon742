# Robust selected-signature stability

21 September 2026.

**Status:** candidate quantitative corollary of selected-signature union
rigidity, at the inherited canonical-bridge trust level.

## Theorem

Let `J` be a set of at least `lambda*a` labels.  Assume constants
`d,x,c,q,X>0` such that

1. every `j in J` has `d_F(j)>=d*a`;
2. every F-neighbour `i` of a label in `J` has `x_i>=x*a`;
3. every `j in J` has `C_j<=c*a`;
4. every selected row has `q_u<=q*a`; and
5. the total selected mass is `Q=sum_u q_u<=X*a^2`.

If `d*x*a>=c/2`, then the selected-row-pair weighted average F-codegree obeys

\[
\boxed{
\frac{\sum_u\sum_{\{i,k\}\subseteq S_u}c_F(i,k)}
     {\sum_u\binom{q_u}{2}}
\ge
\frac{\lambda d^2x^2}{cqX}a
-\frac{\lambda dx}{qX},
}
\tag{RS}
\]

whenever the denominator is positive.

## Proof

For `j in J`, put `M_j=sum_{i in N_F(j)}x_i`.  The assumptions give

\[
M_j\ge dx a^2,
\qquad
C_j\le ca.
\]

The function `M -> M^2/C-M` is increasing for `M>=C/2`.  The signature-union
second-moment theorem therefore gives

\[
\sum_u\binom{\lambda_{j,u}}2
\ge\frac12\left(\frac{d^2x^2}{c}a^3-dxa^2\right).
\]

Sum this over at least `lambda*a` labels and use the exact double-count in
`SIGNATURE_UNION_RIGIDITY.md`.  This lower-bounds the numerator of (RS) by

\[
\frac\lambda2\left(\frac{d^2x^2}{c}a^4-dxa^3\right).
\]

Meanwhile

\[
\sum_u\binom{q_u}{2}
\le\frac12\sum_uq_u^2
\le\frac12(qa)Q
\le\frac{qX}{2}a^3.
\]

Division proves (RS).

## Plateau band

For the rational `x=1/4` plateau, the exact certificates give

```text
d >= 27/64,
x = X = 1/4,
c <= 6771/16000,
q <= 19/50
```

in the symmetric row realization.  With `lambda=1`, (RS) becomes

\[
\operatorname{avg}c_F(i,k)
\ge
\frac{759375}{2744512}a-\frac{675}{608}
>0.2766a-1.111.
\]

The point is stability rather than the last decimal: any realization that
keeps the demand, endpoint, and selected-row profiles in these broad bands is
forced into linear common-neighbour clustering.  If an attempted survivor
escapes by concentrating selected load so that `q` is much larger, that
concentration is itself a precise alternative for the next raw-criticality
attack.

### Removing the concentration escape under a uniform endpoint cap

There is a useful automatic row bound.  If `q_u>0`, source `u` has an actual
selected incidence `ui`, and endpoint eligibility gives

\[
q_u\le p_u+q_u\le C_i.
\]

Therefore, if every selected label in the band has `C_i<=c*a`, one may take
`q=c` in (RS) without any symmetry assumption.  For the same rational plateau
constants this gives the unconditional band estimate

\[
\boxed{
\operatorname{avg}c_F(i,k)
\ge
\frac{1265625}{5094049}a-\frac{2250}{2257}
>0.2484a-0.997.
}
\tag{RS-plateau}

Thus endpoint concentration does not destroy linear codegree rigidity; it only
weakens the coefficient from the symmetric `0.2766` value to `0.2484`.

Without a uniform endpoint cap, near-profile-integral extremizers satisfy a
clean dichotomy:

1. bounded selected rows force dense F-codegree clustering through (RS); or
2. selected mass concentrates on fewer physical sources, which can be attacked
   by source/supplement pair capacity and raw criticality.

With the endpoint cap, (RS-plateau) removes that second escape.

Balanced complete bipartite equality has zero positive-demand plateau and is
not affected.
