# Hall density and cut stability on complementary code pairs

Date: 2026-09-18

Status: hand-derived structural strengthening of the complementary-pair Hall-cut theorem. No eventual second-extremal theorem is claimed.

## 1. Setup

Let the unordered complementary tight-code pairs be denoted by `P`. For each pair retain the notation from `COMPLEMENT_PAIR_HALL_CUT.md`:

- `A_P`, with `a_P=|A_P|`;
- `L_P`, `Z_P`, `R_P`;
- direct internal A-edge count `D_P`;
- matched-B traffic `P_P` and A/U traffic `C_P`;
- `t_P:=P_P+C_P` for the actual chosen non-direct certificate traffic sourced in `A_P`;
- `T0:=a-p=p+u-lambda-1`.

For a family `X` of complementary pairs write the corresponding subscript `X` for sums and put `x:=a_X`.

The preserved pair capacity is

> `Ccap_P := R_code(S_P)[g_P+2S_P/(lambda+1)]+2h_P`,

so

> `2t_P <= Ccap_P`.                                      `(1.1)`

The Hall-cut theorem says

> `[x(x-T0)-L_X+Z_X-R_X/p]_+ <= sum_{P in X} Ccap_P`.    `(1.2)`

The point of this note is that the same structure admits an exact cut decomposition. This reveals a density/majorization form of the Hall system and a near-equality rigidity statement.

## 2. Exact A-cut degree identity

Let

> `c_X := e(A_X,A\A_X)`,
>
> `M_X := x(a-x)-c_X`.

Thus `M_X` is the number of missing A-edges across the cut.

Because

> `sum_{z in A_X} d_A(z)=xp-L_X+Z_X`,

and this degree sum is `2e(A_X)+c_X`, we have the exact identity

> `2e(A_X)=x(x-T0)-L_X+Z_X+M_X`.                         `(2.1)`

This is the exact version of the earlier subset crowding lower bound.

## 3. Actual certificate export and direct-credit slack

Choose one criticality certificate for every non-direct A-edge. Let `N_X` be the number of non-direct A-edges internal to `A_X`. Since `t_X` counts all chosen non-direct certificates whose selected source endpoint lies in `A_X`, define

> `E_X:=t_X-N_X >= 0`.                                   `(3.1)`

`E_X` has an exact meaning: it is the number of crossing A-edges whose chosen source lies in `A_X`.

Direct edges never cross a complementary-pair family cut. Define the unused local direct/Hamming credit

> `J_X:=R_X/p-2D_X >= 0`.                                `(3.2)`

Now define the **actual Hall weight**

> `w_P:=2t_P+L_P-Z_P+R_P/p`,                             `(3.3)`

and extend additively to families.

### Theorem 3.1 — exact Hall-cut decomposition

For every family `X`,

> `w_X-x(x-T0)=2E_X+M_X+J_X`.                            `(EH)`

#### Proof

From `(2.1)` and `e(A_X)=N_X+D_X`,

`2N_X=x(x-T0)-L_X+Z_X+M_X-2D_X`.

Since `t_X=N_X+E_X`, substitute in `(3.3)` and collect terms. `square`

Every term on the right of `(EH)` is concrete and nonnegative. Hence the Hall inequality is not merely a capacity consequence: before replacing actual traffic by an upper bound, its exact slack is the sum of source export, missing-cut mass and unused direct credit.

## 4. Capacity lift

Put

> `kappa_P:=Ccap_P-2t_P >= 0`,                            `(4.1)`

and define the **capacity Hall weight**

> `W_P:=Ccap_P+L_P-Z_P+R_P/p = w_P+kappa_P`.             `(4.2)`

Then for every family `X`,

> `W_X-x(x-T0)=2E_X+M_X+J_X+kappa_X`.                    `(CEH)`

In particular,

> `x(x-T0) <= W_X`.                                      `(HN)`

This is a positive-part-free normal form of `(1.2)`: if `x(x-T0)` is negative it is automatic, and otherwise it is exactly the Hall demand.

## 5. Density majorization

For `a_P>0` define

> `rho_P^cap := W_P/a_P`.                                `(5.1)`

For any real `tau`, let

> `X_<tau := {P : a_P>0 and rho_P^cap<tau}`,
>
> `A_tau := a_{X_<tau}`.

### Theorem 5.1 — low-density mass bound

If `A_tau>0`, then

> `A_tau < T0+tau`.                                      `(HD)`

#### Proof

`W_{X_<tau}<tau A_tau`, while `(HN)` gives `W_{X_<tau}>=A_tau(A_tau-T0)`. Divide by `A_tau`. `square`

For `0<=tau<=p`, since `a=T0+p`, more than `p-tau` A-vertices lie in pair classes with capacity density at least `tau`.

Equivalently, if the active pairs are sorted by nondecreasing `rho_P^cap` and a prefix has A-mass `A_j>T0`, then

> `rho_j^cap >= A_j-T0`.                                 `(5.2)`

This is the desired Hall cut-selection principle in threshold form: low-capacity pairs cannot collectively carry arbitrary A-mass.

## 6. Exact cut conservation and the dual Hall sandwich

For actual weights put

> `sigma_X:=w_X-x(x-T0)=2E_X+M_X+J_X`.                   `(6.1)`

Let `bar X` be the complementary family. Every A-edge crossing the cut is non-direct, and exactly one endpoint is its chosen source. Therefore

> `E_X+E_barX=c_X`,                                      `(6.2)`

while `M_barX=M_X` and `J_X+J_barX=J`, where

> `J:=R/p-2D`.

Consequently

> `sigma_X+sigma_barX=2x(a-x)+J`.                        `(CONS)`

For all pairs, `E=M=0`, so

> `w_all=ap+J`.                                          `(6.3)`

Applying the lower Hall inequality to `X` and to `bar X` gives the two-sided sandwich

> `x(x-T0) <= w_X <= x(a+p-x)+J`.                        `(SAND)`

Thus the A-mass of a family controls its possible actual certificate density from both sides.

## 7. Quantitative low-density stability

If every pair of a family `X` has `rho_P^cap<tau`, then, with `x=a_X`, `(CEH)` gives

> `2E_X+M_X+J_X+kappa_X < x(T0+tau-x)`.                  `(STAB)`

This is stronger than the mass bound `(HD)`: a low-density family close to its maximum allowable mass `T0+tau` must simultaneously have

1. very little selected-source export across its A-cut;
2. an almost complete A-cut (`M_X` small);
3. almost fully used direct/Hamming credit (`J_X` small);
4. almost saturated non-direct certificate capacity (`kappa_X` small).

### Corollary 7.1 — discrete near-equality rigidity

If

> `x(T0+tau-x)<1`,                                      `(7.1)`

then `E_X=M_X=0`.

Hence `A_X` is complete to `A\A_X`, and **every** crossing A-edge chooses its source endpoint outside `X`. Also

> `J_X+kappa_X<1`.                                       `(7.2)`

No integrality claim is made for `J_X` or `kappa_X` individually.

## 8. Forced complementary capacity

The stability statement has a useful directional consequence. Since

> `E_barX=c_X-E_X=x(a-x)-M_X-E_X`,

and every exported crossing edge counted by `E_barX` consumes actual non-direct traffic from `bar X`,

> `Ccap_barX >= 2t_barX >= 2E_barX`
>
> `             =2x(a-x)-2(M_X+E_X)`.                   `(8.1)`

For a capacity-low-density family as above, if

> `B:=x(T0+tau-x)`,

then `(STAB)` implies `M_X+E_X<B`, and therefore

> `Ccap_barX > 2x(a-x)-2B`.                              `(8.2)`

Under the discrete rigidity hypothesis `(7.1)`, this sharpens to

> `Ccap_barX >= 2x(a-x)`.                                `(8.3)`

Thus a nearly maximal low-capacity family does not merely become rigid internally: it forces a large amount of certificate capacity into its complement. This is a genuine capacity-polarization mechanism.

## 9. Cross-deficit localization

From `(4.2)`, `rho_P^cap<tau` is equivalent to

> `Z_P > Ccap_P+L_P+R_P/p-tau a_P`.                      `(9.1)`

Therefore `(HD)` gives:

### Theorem 9.1 — cross-deficit overload cannot occupy much A-mass

For every `0<=tau<=p`, the total A-mass of pairs satisfying `(9.1)` is less than `T0+tau`. Equivalently, **more than `p-tau` A-vertices** lie in pair classes satisfying

> `Z_P <= Ccap_P+L_P+R_P/p-tau a_P`.                    `(CROSS-LOC)`

This is the first direct threshold statement connecting the A--U nonincidence deficit `Z_P` to pair-local certificate capacity, A-slack and rooted-slot Hamming resource. It is the natural point at which the preserved beta/source-tuple machinery should enter: beta support controls how A--U nonincidences can be distributed, while `(CROSS-LOC)` says that most A-mass cannot hide in cross-deficit-overloaded low-capacity pairs.

## 10. Actual-density upper tail

For completeness define `rho_P^act=w_P/a_P`. The global average is exact:

> `sum_P a_P rho_P^act = ap+J`.                          `(10.1)`

If `Y_>tau={P:rho_P^act>tau}` has A-mass `y`, then the upper side of `(SAND)` yields

> `y^2-(a+p-tau)y-J < 0`.

Hence

> `y < [(a+p-tau)+sqrt((a+p-tau)^2+4J)]/2`.              `(TAIL)`

Together with `(HD)`, this gives a two-sided density-envelope picture; it is strongest when the unused direct credit `J` is small.

## 11. Interpretation and next move

The previous live frontier asked for a cut-selection/majorization theorem for `(HALL-P)`. `(HD)`, `(STAB)` and `(CROSS-LOC)` provide exactly such a theorem, but they do **not** yet close the eventual second-extremal branch.

The next high-value move is not another global scalar collapse. It is to combine `(CROSS-LOC)` with the preserved beta/source-support decomposition of A--U nonincidences. The target is to prove that the beta-forced A--U deficit cannot be concentrated entirely in the exceptional `<T0+tau` A-mass while the remaining `>p-tau` mass simultaneously pays the required local capacity/slack/Hamming bill. A second, complementary route is to classify the near-equality case of `(STAB)`: complete A-cut, one-way source orientation, and saturated local resources are substantially more rigid than the original Hall inequality reveals.

The published `X_3` control remains untouched. Its canonical root has `u=0`, `A` independent and zero non-direct A-edge demand, so the A--U cross-deficit/beta bridge is inactive.