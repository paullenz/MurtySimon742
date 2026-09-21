# Corrected residual-one half-ray: raw boundary-certificate score closure

Date: 2026-09-21

Status: conditional structural theorem for the corrected rigid one-code half-ray. The core closure uses the post-audit raw boundary-code-edge trichotomy, universal opposite-endpoint independence, the corrected half-ray parameter ledger, the preserved gamma-collision theorem, and the corrected H/Y slack floors. A stronger finite threshold uses only the already audited predecessor residual-slot floor `Delta>=h`; the disputed equality-face strengthening is not needed.

This note is deliberately upstream of the superseded H--U private-foot route.

## 1. Corrected half-ray

Work with

`p=2t, c=y=t, lambda=2t-1, u=t+1, x=2t+1, k=2, m=p-1=2t-1`,

for integer `t>=4`, with residual coordinate j.

The one-code outside block is

`Y=A_d`, `|Y|=t`.

The X-side consists of

- `H={h_i : i!=j}`, with one vertex of code `d xor e_i` for each private coordinate i;
- two K-heads of the common residual code `d xor e_j`.

Hence every occupied X-code class has size at most two, and the unique size-two class is the K-code `d xor e_j`.

The exact score ceiling is

> **`E_U+L_A <= C0=4t^2+7t-3`.**                         `(1.1)`

## 2. Every tight coordinate is boundary-exposed and none is universal

For every tight coordinate i,

> `i in I(d,X)`.

Indeed, at the residual coordinate j every H-code agrees with d. At a private coordinate i choose any distinct private head `h_l`; its code agrees with d at i.

On the other hand

> **`C(d,X)=empty`.**                                     `(2.1)`

At a private coordinate i, the head h_i disagrees with d. At the residual coordinate j, both K-heads disagree with d.

Therefore the matched-forward arm of the raw boundary trichotomy is unavailable on **every** coordinate.

## 3. Reverse capacity per coordinate is at most two

For coordinate i, a reverse boundary certificate must use an X-witness of the forced code

`gamma_i=gamma(q_i^{d_i})`.

Let

`r_i=|X_{gamma_i}|`.

Since every X-code class has size at most two,

> `r_i<=2`.                                               `(3.1)`

For fixed source `q_i^{d_i}`, one physical witness cannot certify two distinct Y-heads, because its common-neighbour set with the source is fixed. Hence at most r_i of the y=t boundary edges at coordinate i can use the reverse arm.

Thus at least

> `f_i>=t-r_i`                                            `(3.2)`

outside sources use U-forward certificates. Since `t>=4` and `r_i<=2`, `f_i>0` on every coordinate.

## 4. Exact U-slack bill at one coordinate

Every U-forward witness at coordinate i has code

`bar d xor e_i`

and is X-anticomplete. If one such witness w serves `t_w` outside sources, the exact U-degree identity gives

`epsilon_w >= p-y+t_w = t+t_w`.

Let W_i be the actual witness set at coordinate i. Then

`sum_{w in W_i} epsilon_w`
` >= t|W_i|+f_i`
` >= t+(t-r_i)`
` =2t-r_i`.                                               `(4.1)`

The one-match witness codes `bar d xor e_i` are distinct over i, so the W_i are pairwise disjoint. Summing over all p=2t coordinates gives the raw boundary floor

> **`E_U >= 4t^2-sum_i r_i`.**                           `(4.2)`

The coarse bound `r_i<=2` already gives

> **`E_U>=4t^2-4t`.**                                    `(4.3)`

Together with the corrected H/Y floor `L_A>=t^2`, this alone yields

`E_U+L_A>=5t^2-4t`,

which contradicts `(1.1)` for every `t>=11`.

Thus the half-ray is already eventually closed without any residual-slot equality analysis.

## 5. Gamma refinement: closure for t>=10 from the raw boundary package

Let

`g=|{i: gamma_i=d xor e_j}|`,

the number of coordinates whose forced reverse code is the unique size-two K-code.

Every other occupied forced gamma class has size at most one, so

> `sum_i r_i <= p+g=2t+g`.                               `(5.1)`

Therefore

> `E_U>=4t^2-2t-g`.                                      `(5.2)`

The preserved gamma-collision theorem says that a common gamma class on g tight coordinates, for `g>=3`, forces

`L_A>=g(g-1)`.

Independently, corrected H/Y accounting gives `L_A>=t^2`. Hence

> `L_A>=max{t^2,g(g-1)}`.                                `(5.3)`

Combining `(5.2)` and `(5.3)`,

`E_U+L_A >= 4t^2-2t-g+max{t^2,g(g-1)}`.                 `(5.4)`

This expression has an exact minimum over `0<=g<=2t`:

- for `g<=t`, the maximum is t^2 and the minimum occurs at g=t, giving `5t^2-3t`;
- for `g>=t+1`, the gamma term is active and the expression is increasing in g, so its minimum is at g=t+1, giving `5t^2-2t-1`, which is larger for t>=2.

Therefore

> **`E_U+L_A >= 5t^2-3t`.**                              `(5.5)`

Against `(1.1)`, the gap is

`(5t^2-3t)-(4t^2+7t-3)=t^2-10t+3`.

This is positive for every integer

> **`t>=10`.**                                            `(5.6)`

### Core closure theorem

> **No actual D2C realization of the corrected rigid one-code half-ray can exist for `t>=10`.**

This conclusion uses raw boundary criticality plus already corrected score/gamma machinery; it does not use the disputed equality-face strengthening from the 20 September late session.

## 6. Audited residual-slot floor sharpens the finite threshold to t>=8

The midnight audit retained the predecessor residual-slot theorem

`Delta>=h=2t-1`

as independently secure. Since `L_H=3t-1+Delta`, this gives

`L_H>=5t-2`.

Together with the corrected Y floor

`L_Y>=t^2-3t+1`,

we obtain

> `L_A>=t^2+2t-1`.                                       `(6.1)`

Replace t^2 by this stronger independent floor in `(5.3)`. The exact minimum becomes

> **`E_U+L_A >= 5t^2-t-2`.**                             `(6.2)`

Indeed the baseline branch remains active through `g=t+1`, where it gives `5t^2-t-2`; at `g=t+2` the gamma branch gives `5t^2`, and it then increases.

Comparing `(6.2)` with `(1.1)` gives the gap

`t^2-8t+1`,

which is positive for every integer

> **`t>=8`.**                                             `(6.3)`

Thus the audited residual-slot floor improves the finite closure threshold from 10 to 8, without using `Delta>=h+1` or the candidate global superconstant theorem.

Only the finite diagnostic values `t=4,5,6,7` remain outside this particular half-ray score contradiction.

## 7. Why this changes the live strategy

The intermediate half-ray was previously treated as an unbounded method escape because aggregate pair-local and rooted-Q gates had quadratic margin. Raw boundary criticality changes that conclusion: the B--A boundary itself forces almost all `Y q_i^{d_i}` edges into expensive, coordinate-distinct U-forward witness classes. The cost is quadratic and lands directly in E_U, the score currency that could not be hidden by the earlier aggregate optimizations.

Therefore the half-ray no longer deserves further asymptotic H--U carrier optimization. For the eventual theorem programme, it is closed within the conditional rigid interface. The high-value frontier moves back upstream to realizability of general rigid cuts and to showing that any sufficiently-large survivor must enter a boundary profile with similarly expensive U-forward or gamma-collision structure.

## 8. Scope and caveat

This is still conditional on reaching the rigid complete-Hall-cut / one-code interface. Bounded actual-D2C regression contains zero positive rigid complete pair-family cuts with `x>=3`; X_3 remains the mandatory negative control. The result is therefore not an unconditional eventual second-extremal theorem.
