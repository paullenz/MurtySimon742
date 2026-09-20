# Residual-one k=2 U-density source-capacity normal form

Date: 2026-09-20

Status: **same-session conditional structural consequence** of raw U--U complement localization plus the global H/Y polarization, at `J2=empty`. No finite scan is used.

The preceding hole/slack note showed that the remaining low-k problem is no longer the existence of a quadratic defect, but whether the U-layer can stay dense enough to keep `M_U` small while paying the compulsory A-hole block. This note localizes where that U-density can come from.

## 1. Oriented U--U capacity by complementary A-code

For every U--U edge choose one valid raw criticality orientation. If s is the chosen source, its witness lies in A and has code `bar(c(s))`. Ordered `(source,witness)` injection gives

> `out(s) <= |A_{bar(c(s))}|`.                           `(UD-CAP)`

At residual dimension one with `J2=empty`, the complete A-code repertoire is

- `A_d=Y`, size y;
- `A_C=K`, `C=d xor e_j`, size 2;
- `A_{d xor e_i}={h_i}`, size 1 for each `i in I`.

Every other A-code class is empty.

Thus, apart from sources of code `bar d`, every U-vertex has oriented U--U capacity at most two. A `bar d` source has the only potentially linear witness class, namely Y.

If `n_{bar d}=|U_{bar d}|`, then the crude exact consequence is

> `e(U) <= y n_{bar d}+2(u-n_{bar d})`.                 `(UD-CRUDE)`

On the exact q=1 ray this already implies

`M_U/p^2 >= [1/2-n_{bar d}/p-o(1)]_+`.

Hence a U-dense survivor requires at least about half of U to have code `bar d`.

## 2. H-positive `bar d` vertices cannot source U--U edges

The global H/Y polarization gives a stronger source restriction.

Let `s in U_{bar d}` have an H-neighbour h. Any U--U edge oriented from s must use a witness in `A_d=Y`, by `(UD-CAP)`.

But every Y-vertex is adjacent to every H-vertex. Therefore h is a common neighbour of s and the Y-witness, distinct from the U-head of the certificate. The required singleton common-neighbour relation is impossible.

Hence

> **if `s in U_{bar d}` and `d_H(s)>0`, then `out(s)=0`.** `(UD-HBLOCK)`

Only H-anticomplete `bar d` vertices can provide the linear U--U source capacity.

## 3. Refined global edge bound

Write

`B_0={s in U_{bar d}:d_H(s)=0}`,

`B_+={s in U_{bar d}:d_H(s)>0}`.

Let `b0=|B_0|`, `b+=|B_+|`.

Choose one valid orientation of every U--U edge. By `(UD-HBLOCK)`, vertices of B_+ contribute zero source capacity; vertices of B_0 contribute at most y each; every remaining U-vertex contributes at most two. Therefore

> **`e(U) <= y b0+2(u-b0-b+)`.**                        `(UD-REF)`

In particular, on the exact low-k ray `u=p+1`, `y=p-1`,

> `M_U/p^2 >= [1/2-b0/p-o(1)]_+`.                       `(UD-MISS)`

Thus a sequence with `M_U=o(p^2)` must satisfy

> **`|B_0| >= (1/2-o(1))p`.**                            `(UD-DENSE)`

The price of U-density is therefore a very concrete physical normal form: at least half the rooted U-layer must consist of vertices of the single code `bar d` which are completely H-anticomplete.

## 4. Interaction with the global hole theorem

Every `B_0` vertex already pays all `|H|=p-1` H--U holes. Every `B_+` vertex, by global polarization, has at most one Y-neighbour and therefore pays at least `y-1=p-2` Y--U holes.

So the new statement is not another copy of the global A-hole bill. Its content is directional:

- if the graph uses the U-layer to avoid missing U--U pairs, the sources responsible for those edges must concentrate in one code and one side of the H/Y polarization;
- if it does not create that large H-free `bar d` class, then `(UD-MISS)` gives an additional quadratic `M_U` bill, which carries coefficient two in the rooted ledger.

This is the correct next normal form for the dense-U branch.

## 5. Next raw-criticality target

A vertex in `B_0` has code `bar d`, hence full private-coordinate support and is adjacent to the residual hub. It is also H-anticomplete.

That combination is highly rigid. The next attack should classify its private-spoke orientations and Y-neighbourhood while retaining whether it is K-free, one-K, or K-heavy. In particular, K-free H-anticomplete `bar d` vertices cannot use an H-witness in the reverse private-spoke orientation, pushing all private spokes forward and therefore forcing Y-antichain behaviour. If that extends to a positive fraction of `B_0`, the U-dense normal form acquires a second A-hole block.

Global trust boundary unchanged: the rigid complete Hall-cut interface is still conditional and has no positive bounded actual-D2C fixture with `x>=3`.