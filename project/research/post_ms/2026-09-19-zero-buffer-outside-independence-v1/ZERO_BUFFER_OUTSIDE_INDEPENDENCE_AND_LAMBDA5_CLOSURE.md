# Zero-buffer outside independence, exact ledgers, and lambda<=5 closure

Date: 2026-09-19

Status: stronger continuation of `ZERO_BUFFER_CODE_SIMPLEX_AND_SMALL_LAMBDA_CLOSURE.md`. This is a conditional hand theorem inside the same rigid one-code `z=1` zero-buffer common-buffer branch. It supersedes the previous lambda=3 six-tuple handoff by proving that none of those tuples is graph-realizable.

## 1. Reconciliation and reason for the next move

The preceding checkpoint reduced the zero-buffer branch sharply by raw `b--U_o` criticality and exact code support. It left a very dense lambda=3 residual and proposed attacking actual U-edges. That is exactly the audit-compatible next step: no weakened premise is reused, no source-tuple closure is assumed, and the attack stays at raw graph criticality.

Retain all notation and hypotheses of the code-simplex note:

- `X--Y` complete, `x=p+k`, `k>0`;
- `g=p`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, and `U_-` is independent;
- zero buffer slack, so b is complete to X and U_o;
- Y is anticomplete to U;
- `rho=u-k=u_o+1`;
- `supp_A(X)={0,e_1,...,e_p}` with multiplicities `k,1,...,1`;
- `supp_U(U_o)` is the complementary support;
- `p>=4`, `rho>=p+2`;
- every x in X has a selected buffer-edge witness in its complementary U_o code class;
- `H:=e_bar(W_0,U_o)>=k`;
- `J:=e_bar(X,U_o)>=max(x,u_o)`.

The mandatory `X_3` negative control remains outside the branch because `u=0`.

## 2. Unit I — U_o is independent

### Theorem 2.1

> `e(G[U_o])=0`.                                          `(UO0)`

### Proof

Suppose `zz'` is an edge with `z,z' in U_o`.

The edge lies in a triangle through the root, so D2C criticality supplies a singleton-common-neighbour orientation. A B-side witness is impossible: any B-witness shares the root with the relevant U-source, so the root is an extra common neighbour. Thus the external witness lies in A.

Y is anticomplete to U, so any A-witness adjacent to z or z' lies in X. But b is complete to X and to U_o. In either orientation, the singleton common neighbourhood involving the nonadjacent endpoint and the X-witness therefore contains b in addition to the claimed head endpoint. This is impossible.

Hence no U_o edge exists. square

This is a raw physical graph theorem. It does not use source-tuple capacity, Hall counting, or selected-witness injectivity.

## 3. Unit II — exact q and U-slack ledgers

Let

- `H=e_bar(W_0,U_o)`;
- `J=e_bar(X,U_o)`.

Because U_- and U_o are both independent, b is complete to U_o, and the only remaining U-edges are W_0--U_o edges,

> `q=e(G[U])`
>
> ` =u_o+(k u_o-H)`
>
> ` =(k+1)u_o-H`.                                         `(Q-EX)`

The core slack identity is

> `E_core=k(p+k-1)+H`.                                    `(EC-EX)`

For `z in U_o`, write

- `h_X(z)=x-d_X(z)`;
- `h_W(z)=k-d_{W_0}(z)`.

Since z has no Y-neighbours, no U_o-neighbours, and is adjacent to b,

`d_{A union U}(z)=x-h_X(z)+k-h_W(z)+1`.

Thus

> `epsilon_z`
>
> ` =rho-k-2+h_X(z)+h_W(z)`.                              `(UO-EPS)`

Summing over U_o gives

> `E_o=u_o(rho-k-2)+J+H`.                                 `(EO-EX)`

Therefore the total U-side slack is exactly

> `E_U`
>
> ` =k(p+k-1)+u_o(rho-k-2)+J+2H`.                         `(EU-EX)`

Adding `(Q-EX)` gives the especially clean cancellation

> `q+E_U`
>
> ` =k(p+k-1)+u_o^2+J+H`.                                 `(QEU-EX)`

Using only `H>=k` and `J>=max(x,u_o)`,

> `E_U`
>
> ` >=k(p+k-1)+u_o(rho-k-2)+max(x,u_o)+2k`,               `(EU-F)`
>
> and
>
> `q+E_U`
>
> ` >=k(p+k)+u_o^2+max(x,u_o)`.                           `(QEU-F)`

The previous lambda=3 dense-U residue is already incompatible with `(UO0)`; the old six tuples are now superseded.

## 4. Unit III — exact X-slack identity

Let `e_X=e(G[X])`.

The X--U holes are exactly

- `k(x-1)` across X--W_0;
- zero across X--b;
- J across X--U_o.

Hence

`e(X,U)=xu-k(x-1)-J`.

Summing the A-side degree identity over X gives

> `L_X`
>
> ` =x(lambda+1-rho)+k(x-1)+J-2e_X`.                     `(LX-EX)`

This is exact.

## 5. Unit IV — residual internal-X edge capacity from duplicate complement support

Put

> `R:=u_o-(p+1)=rho-p-2>=0`.

This is the number of U_o vertices beyond the compulsory one-per-complementary-simplex-code support.

For `p>=4`, no two codes in `{0,e_1,...,e_p}` are complementary. Thus an internal X-edge cannot be a direct complementary-code edge.

At `g=p`, every matched gamma code belongs to `{d,bar d}`, while X avoids both. Hence an internal X-edge cannot use a matched-B witness.

Therefore every internal X-edge must be certified in an A/U channel. If the chosen source has code c, its witness must have code `bar c`, and all such witnesses lie in U_o.

For an X-source x of code c and a U_o witness z of code `bar c`, the physical pair `(x,z)` certifies at most one singleton head. One such pair per X-source is already consumed by the buffer-X certificate, with common neighbourhood `{b}`. If the complementary U_o code class has population t, a fixed source therefore has at most `t-1` residual pairs available for internal X-edges.

The X code-class sizes are k for the core code and 1 for each unit-vector code. Distributing the R duplicate U_o vertices to maximize residual pair supply puts all duplicates in the core-complement class. Consequently:

### Theorem 5.1 — duplicate-support X-edge capacity

> `e_X<=kR=k(rho-p-2)`.                                   `(XCAP)`

Combining with `(LX-EX)` gives the safe local X-slack floor

> `L_X`
>
> ` >= [x(lambda+1-rho)+k(x-1)+max(x,u_o)-2kR]_+`.        `(LX-F)`

This is physical pair capacity, not the global finite source-tuple theorem.

## 6. Unit V — lambda=3 closes immediately

Write

> `rho=p+s`, `s>=2`.

Use the score floor

> `S>=L_Y+E_U`                                             `(S0)`

with exact `L_Y=rho(p+rho-lambda-1)` and `(EU-F)`.

There are two cases according to

- A: `x>=u_o`, equivalently `k>=s-1`;
- B: `x<u_o`, equivalently `k<=s-2`.

For lambda=3, after subtracting the above-threshold ceiling C0, the two lower-bound differences are

A:
> `D_A=k^2-ks-2k+3p^2+5ps-17p+2s^2-12s+14`;

B:
> `D_B=k^2-ks-3k+3p^2+5ps-17p+2s^2-11s+13`.

For `p>=4,s>=2`, both are minimized at `p=4`. At `p=4`, even the smallest integer values in the relevant A/B domains are positive. Hence

> `S>C0`

throughout lambda=3.

Thus the lambda=3 zero-buffer branch is closed directly by outside independence; the previous six residual tuples are not realizable.

## 7. Unit VI — lambda=4 closes

For lambda=4, the corresponding differences `S0-C0` are

A:
> `D_A=k^2-k(s+3)+3p^2+5ps-20p+2s^2-14s+18`;

B:
> `D_B=k^2-k(s+4)+3p^2+5ps-20p+2s^2-13s+17`.

Again both increase with p on `p>=4,s>=2`, so p=4 is the only possible minimum.

At p=4:

A:
> `D_A=k^2-k(s+3)+2s^2+6s-14`;

B:
> `D_B=k^2-k(s+4)+2s^2+7s-15`.

For `s>=3` both case minima are positive. For `s=2`, only case A exists and

> `D_A=(k-2)(k-3)`.

Thus the only scalar states not already rejected by `S0` are

> `(p,s,k)=(4,2,2),(4,2,3)`,

and in both `S0=C0`.

But `s=2` is the minimal-support layer `R=0`, so `e_X=0`. Formula `(LX-EX)` with `J>=x` gives

> `L_X>=k(x-1)>0`.

Therefore the actual score is strictly larger than `S0=C0`. Both states are impossible.

Hence the zero-buffer branch has no lambda=4 candidate.

## 8. Unit VII — lambda=5 reduces to one equality state

For lambda=5, the `S0-C0` differences are

A:
> `D_A=k^2-k(s+4)+3p^2+5ps-23p+2s^2-16s+24`;

B:
> `D_B=k^2-k(s+5)+3p^2+5ps-23p+2s^2-15s+23`.

Again p=4 is extremal.

At p=4:

A:
> `D_A=k^2-k(s+4)+2s^2+4s-20`;

B:
> `D_B=k^2-k(s+5)+2s^2+5s-21`.

For `s>=4` these are positive in their allowed integer domains. For `s=3`, only A-values `k=2,3,4,5` survive S0; for `s=2`, A-values `k=1,...,6` survive S0.

Now use `(LX-F)`.

### s=3

Here `R=1`, and for the surviving case-A values

> `L_X>=k^2+k`.

Adding this to `D_A` makes every k=2,...,5 state strictly positive. So all `s=3` states are impossible.

### s=2

Here `R=0`, `e_X=0`, and

> `L_X>=(k+2)^2`.

Adding this to `D_A` rejects k=2,...,6 and leaves exactly one equality state:

> `(lambda,p,rho,k)=(5,4,6,1)`.                           `(L5-EQ)`

In this state equality is forced throughout:

- `u=7`, `u_o=5`;
- `x=5`, `y=4`;
- `H=1`;
- `J=5`;
- X and U_o are both independent;
- the five X--U_o nonedges are exactly the code-complement matching
  `h_0z_0,h_1z_1,...,h_4z_4`;
- w, the unique core vertex in W_0, is adjacent to z_1,...,z_4 and nonadjacent to z_0;
- w has unique X-neighbour h_0.

## 9. Unit VIII — raw criticality kills the lambda=5 equality state

Fix `i in {1,2,3,4}`. Equality gives the U-edge

> `w z_i in E`.

This edge shares the root, so a D2C singleton witness must lie in A. Since Y is anticomplete to U, it must lie in X.

One orientation would require an X-vertex adjacent to w and nonadjacent to z_i. The only X-neighbour of w is h_0, but `J=5` makes h_0 adjacent to every z_i with i>=1. So this orientation is impossible.

In the opposite orientation, a witness must be adjacent to z_i and nonadjacent to w. The possible X-witnesses are matched heads h_j with `j!=i`.

But w is adjacent to all four `z_1,...,z_4`, while h_j is adjacent to all U_o vertices except z_j. Therefore

> `N(w) cap N(h_j)`

contains the three distinct vertices

> `{z_l: 1<=l<=4, l!=j}`.

It cannot be the singleton `{z_i}`.

Both orientations fail. Thus the edge `wz_i` is not critical, contradicting diameter-2-criticality.

Therefore `(L5-EQ)` is impossible.

## 10. Consequence

Combining the preceding zero-buffer results:

> **ZERO-BUFFER SMALL-LAMBDA CLOSURE**
>
> There is no above-`M(n)` candidate in the rigid one-code unloaded common-buffer zero-buffer branch for
>
> `lambda<=5`.                                             `(L05)`

The lambda=0 case is inherited from the earlier score theorem; lambda=1,2 from the code-simplex gate; lambda=3,4,5 are strengthened/closed here by outside independence, exact local ledgers, duplicate-support X-edge capacity, and raw criticality.

This remains conditional on the rigid one-code complete-cut hypotheses. It is not an eventual theorem.

## 11. Next scalar frontier: lambda=6

Applying the exact hand floors `(EU-F)` and `(LX-F)` at lambda=6 reduces the scalar zero-buffer frontier to four states.

Again write `rho=p+s`. The p-dependent score differences are increasing on `p>=4,s>=2`, so p=4.

At p=4, case A (`k>=s-1`) and case B (`k<=s-2`) have

A:
> `D_A=k^2-ks-5k+2s^2+2s-26`;

B:
> `D_B=k^2-ks-6k+2s^2+3s-27`.

The X-slack floors before truncation are

A:
> `X_A=k^2-3ks+11k-4s+16`;

B:
> `X_B=k^2-3ks+10k-3s+15`.

A candidate requires

> `D_A+[X_A]_+<=0`

or

> `D_B+[X_B]_+<=0`.

For `s>=4` the integer minima are positive. At `s=2,3`, exactly four scalar states remain:

> `(p,rho,k)=(4,6,1),(4,6,2),(4,7,1),(4,7,2)`.           `(L6-4)`

This classification is also checked independently by the arithmetic diagnostic, but the displayed case formulas are the hand reduction.

The next run should attack these four lambda=6 geometries directly, starting with the two minimal-support rho=6 cases where `e_X=0` and the W_0--U_o edge set is tightly constrained. The raw edge-criticality template from Unit VIII is likely reusable; the rho=7 cases have only one duplicate complementary-code witness and `e_X<=k`.

## 12. Trust boundary and negative control

No source-tuple theorem is used in this note.

The load-bearing new claims are:

1. raw D2C criticality makes U_o independent;
2. exact degree bookkeeping yields `(Q-EX)`, `(EU-EX)`, `(LX-EX)`;
3. each extra complementary-code witness creates at most n_c new source-witness pairs, giving `(XCAP)`;
4. finite lambda=3,4,5 scalar reductions are explicit integer consequences of those formulas;
5. the final lambda=5 equality is rejected by a direct edge-criticality contradiction.

The arithmetic checker is audit support only.

`X_3` remains allowed because its canonical root has `u=0`; none of the zero-buffer unmatched-layer hypotheses apply.
