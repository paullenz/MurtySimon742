# Exceptional Fz k=1 scaling — physical nonnegative-buffer correction and finite-order collapse

Date: 2026-09-20

Status: **same-session corrective audit** of `EXCEPTIONAL_FZ_K1_SCALING.md` and the companion finite diagnostic. This note identifies a genuine omitted physical feasibility condition in the claimed unbounded scalar family. The old “genuinely unbounded k=1 family” conclusion is **withdrawn**.

## 1. The omitted condition

The exact second-strict mixed-hole layer has

> `epsilon_b=p-g+2`.                                      `(K1-BUF)`

Slack is defined by

`epsilon_v=d(root)-d(v)`

with the root chosen at maximum degree. Therefore every vertex slack is nonnegative, in particular

> **`epsilon_b>=0`.**                                     `(K1-NONNEG)`

The current `check_y1_physical_bills.py` computes `eps_b=p-g+2` but does not reject rows with `eps_b<0`; it adds the negative number to the score floor instead. Those rows are physically impossible and must not be counted even as abstract necessary-condition survivors.

## 2. Consequence in the purported k=1 scaling family

The old scaling note puts

`k=1`, hence `g=x-1`,

and

`omega=x-p+t`, `t>=0`.

Then `(K1-BUF)` becomes

> `epsilon_b=p-x+3`.

Nonnegativity gives the immediate physical bound

> **`x<=p+3`.**                                           `(K1-XP)`

Thus the old statement

> “for every fixed admissible `(p,t)`, sufficiently large x survives”

is false: for fixed p, x cannot exceed p+3 before any score/rooted optimization is applied.

## 3. The rooted margin then bounds p

The old note's exact rooted margin remains algebraically valid:

> `2B=eps-p^2-t^2+4t+4x-11`,                             `(K1-B)`

where `eps in {0,1}` is the parity remainder.

Using `x<=p+3`, `eps<=1`, and

`-t^2+4t<=4`

for all real t, a survivor with `B>=0` must satisfy

`0<=2B`
` <=1-p^2+4+4(p+3)-11`
` =-p^2+4p+6`.

Hence

`p^2-4p-6<=0`,

so for integer `p>=2`,

> **`p<=5`.**                                             `(K1-P5)`

Combining with `(K1-XP)` gives

> **`x<=8`.**                                             `(K1-X8)`

Therefore the exceptional-Fz k=1 arm is not asymptotic at all.

## 4. t, omega and order are bounded as well

Rewrite `(K1-B)` as

`2B=eps-p^2-(t-2)^2+4x-7`.

Thus `B>=0` implies

> `(t-2)^2<=eps-p^2+4x-7`.

Using `eps<=1`, `p>=2`, `x<=8`,

`(t-2)^2<=22`.

For integer `t>=0`,

> **`t<=6`.**                                             `(K1-T6)`

Then

`omega=x-p+t<=8-2+6=12`.                                 `(K1-W12)`

In the mixed y=1 branch,

`u=k+1+omega=omega+2`,

`a=x+1`,

and the rooted partition order is

`n=1+a+(2p+u)=x+2p+omega+4`.

Therefore

> **`n<=8+10+12+4=34`.**                                 `(K1-N34)`

So the entire k=1 exceptional-Fz arm is a finite-order tail:

> **no k=1 exceptional-Fz survivor can have `n>=35`.**   `(K1-N35-CLOSED)`

This conclusion uses only the already-preserved exact margin `(K1-B)` plus the omitted physical fact `epsilon_b>=0`. No bounded parameter scan is used as proof.

## 5. Impact on prior diagnostics and strategy

The following earlier statements are superseded:

1. `EXCEPTIONAL_FZ_K1_SCALING.md` — its algebraic formulas `(K1-A)/(K1-B)` remain useful, but the interpretation as a genuine unbounded physical family is invalid because `(K1-NONNEG)` was omitted.
2. `check_y1_physical_bills.py` survivor counts — the checker must reject `eps_b<0` before reporting physically admissible necessary-condition rows. Existing counts remain historical diagnostics but are too weak because they include impossible negative-buffer-slack rows.
3. The strategic instruction “do not return to scalar work because k=1 is analytically unbounded” is withdrawn. The k=1 tail is already finite-order.

This is exactly the kind of physical-feasibility omission that the daily adversarial programme is intended to expose. The correction does not by itself close all large-head mixed y=1 geometry: other k values must be checked for genuine unbounded families.

## 6. Next move

1. repair the y=1 diagnostic by imposing `eps_b>=0`;
2. re-evaluate which R/Fx/Fz parameter families remain unbounded after that physical gate;
3. analytically characterize any remaining scaling family before invoking pair-local `Ccap_P/(ONE-P)/(CROWD)`;
4. preserve the zero-positive-rigid-cut interface caveat throughout.
