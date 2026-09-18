# Global max-degree slack criterion for the second-extremal threshold

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status: exact algebraic identity and equivalent reformulation.** No D2C hypothesis is needed for the identity itself. This note is recorded because the live near-full programme naturally produces vertex-slack inequalities, while the extremal target has usually been written in the residual form `delta=r-e(F)`.

Let `G` be any graph on `n` vertices, let `v` be a maximum-degree vertex, and put

`b=d(v)=Delta(G)`,

`lambda=2b-n`.

For every vertex `z`, define its maximum-degree slack

`epsilon_z=b-d(z)>=0`,

and let

`T=sum_{z in V(G)} epsilon_z`.

Since `sum_z d(z)=2m`,

> `T=nb-2m`.                                            (1.1)

At the root `v`, the canonical residual defect is

`delta=b(n-b)-m`.

Using `n=2b-lambda`, (1.1) gives

> **GLOBAL SLACK--DEFECT IDENTITY**
>
> `2 delta = T-b lambda`.                               (1.2)

Thus the residual defect is exactly total maximum-degree slack after subtracting the deterministic imbalance term `b lambda`.

---

## 1. Exact slack reformulation of m <= M(n)

Recall

`M(n)=floor((n-1)^2/4)+1`.

For fixed `n,b`,

`m<=M(n)`

is equivalent by (1.1) to

`T>=nb-2M(n)`.

A parity calculation with `lambda=2b-n` simplifies the right side to

> `nb-2M(n) = floor(n(lambda+2)/2)-2`.                  (1.3)

Therefore:

> **SECOND-EXTREMAL SLACK CRITERION.**
>
> `m<=M(n)` if and only if
>
> `T >= floor(n(lambda+2)/2)-2`.                        (1.4)

Since changing `m` by one changes `T` by two, an above-threshold graph satisfies the strict two-unit gap

> `m>M(n)  ==>  T <= floor(n(lambda+2)/2)-4`.           (1.5)

This is exactly equivalent to the edge-count formulation, not a relaxation.

---

## 2. Near-full tight-matching form

In the near-full notation with `p` tight antipode pairs and unmatched set `U`, `|U|=u`, write

`E_U=sum_{y in U} epsilon_y`,

`L_A=sum_{x in A} epsilon_x`.

Every tight pair contributes total slack `lambda+1`, while the root itself has slack zero. Hence

> `T=p(lambda+1)+E_U+L_A`.                              (2.1)

Substituting `b=2p+u` into (1.2) gives the particularly useful exact form

> **NEAR-FULL SLACK--DEFECT IDENTITY**
>
> `2 delta = E_U+L_A+p-lambda(p+u)`.                    (2.2)

This can also be recovered directly from the preserved near-full formulas

`delta=(p+u)(a-p)+p-s-q-f`,

`E_U=u(p+u-1)-2q-s`,

`L_A=a(p+u)-s-2f`.

Equation (2.2) eliminates `s,q,f` completely.

---

## 3. Why this changes the live target

The current near-full machinery already produces lower bounds on `E_U` from errorful antipodes and branching. Equation (2.2) shows exactly what remains missing: a sufficiently strong lower bound on **combined unmatched plus A-side slack**.

For example:

### lambda = -1

Here `n` is odd and `b=(n-1)/2=2p+u`. The threshold criterion becomes

`T=E_U+L_A >= b-2 = 2p+u-2`.

Therefore an above-`M(n)` candidate must satisfy

> `E_U+L_A <= 2p+u-4`.                                  (3.1)

The branching theorem alone only supplies `E_U>=ceil(u/5)`, so the missing payment must predominantly come from `L_A`. This quantifies why an ABE-only route cannot close the branch.

### lambda = 0

Now `n` is even, and the tight pairs themselves contribute `p` units of slack. The threshold criterion is

`p+E_U+L_A >= n-2 = 4p+2u-2`,

or

> `E_U+L_A >= 3p+2u-2`.                                 (3.2)

An above-threshold candidate is again two units below this.

Thus the selected/Hall programme should ultimately be judged by whether it forces **A-side slack `L_A`**, not merely extra A-code support.

---

## 4. Interaction with the new unmatched-row inequalities

The companion notes establish

`E_U <= 2 bar q + W_alpha`,

from selected/Hall alpha spill, and

- `E_U>=ceil(u/5)` when `lambda=-1`;
- the sharper branching floor for `lambda>=0`.

The global criterion shows how these local inequalities must be completed. A successful compact near-full theorem needs one of two things:

1. convert row/capacity structure directly into a lower bound on `L_A`; or
2. use the row collapse to force enough structure in `F=G[A]` and the A--U incidences that (2.2) reaches the threshold in (1.4).

This is a more precise target than attempting to make the antipode-error matching theorem carry the whole defect by itself.

The order-12/32 `X_3` control remains untouched: it lies in `u=0`, and (1.4) is an identity that correctly records its one-edge excess over `M(12)`.
