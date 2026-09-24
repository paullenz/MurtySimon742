# Exact five-witness star slack closes the (5,5,5) tuple

24 September 2026. Status: internal exact finite theorem-facing computation with an independent labelled replay. It closes the fixed abstract `(5,5,5)` tuple at the assigned-witness interface; it does not close all n=18 profiles or the general theorem.

## Exact small-star calculation

For a star witness set T of size x, let `e` be the number of T-edges and let beta be the number of missing T--Z incidences needed by Z-certificate neighbourhoods to cover every T-edge. The exact slack is

    2(binom(x,2)-e)+beta.

The committed independent checker enumerates every labelled graph on T and solves the weighted certificate-neighbourhood set cover by direct dynamic programming. It does not reuse the prior SciPy MILP or Graph Atlas enumeration. Results are:

    x=3: minimum 4
    x=4: minimum 8
    x=5: minimum 14.

For x=5 this strengthens the generic `binom(5,2)+1=11` floor to 14. There are 1,024 labelled T-graphs, all covered exhaustively; 45 attain the minimum.

## Immediate (5,5,5) contradiction

At n=18, Delta=10, rho=2, suppose three demand-positive labels have `x_i=h_i=5`. For each label the exact x=5 star bound gives

    5 delta_i + sum_{t in T_i} delta_t
       >= 5(rho+1)+14 = 29.

Let `C=sum_i delta_i`. Summing over the three labels and using `r_t<=3` gives

    87 <= 5C + sum_t r_t delta_t
       <= 5C + 3(D-C)
       = 3D+2C.

For a strict n=18 counterexample, `D<=16`; and each centre has `delta_i<=h_i=5`, so `C<=15`. Therefore

    3D+2C <= 48+30=78 < 87,

a contradiction.

Thus **no exact-H assigned-witness obstruction with tuple `d=x=h=(5,5,5)` fits the strict-counterexample deficit budget**. This proof is independent of the common-C assumption, the membership-step classification and the full 18-vertex D2C SAT encoding. It also resolves the earlier tuple-transfer concern: the tuple itself is excluded, regardless of which right-incidence geometry realizes it abstractly.

Reproduction:

    python exact_star_slack_small.py 5

The calculation is internal verification rather than external mathematical acceptance. The general demand-15/16 obstruction remains open.
