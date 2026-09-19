# Zero-buffer core/outside separation and lambda-7 singleton frontier

Date: 2026-09-19

Status: internal hand-theorem continuation inside the rigid one-code `z=1` unloaded common-buffer zero-buffer branch. This note strengthens the previous outside-independence package. It does not claim an eventual theorem.

## 1. Audit-compatible pivot

The preceding package proved `U_o` independent and reduced lambda=6 to four scalar states. The natural next raw-criticality object is an edge between the common core `W_0` and `U_o`. This stays entirely within the latest audit's authorized one-code route and does not use the finite source-tuple theorem as graph-level closure.

Retain:

- complete rigid cut `X--Y`, Y one code d;
- `g=p`, `x=p+k`, `k>0`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`;
- b complete to X and U_o and anticomplete to Y;
- Y anticomplete to all U;
- every core w has exactly one X-neighbour, its core head;
- `supp_A(X)={0,e_1,...,e_p}`, multiplicities k,1,...,1;
- `supp_U(U_o)` is the complementary support;
- `p>=4`, `rho:=u-k=u_o+1>=p+2`;
- `U_o` independent.

## 2. Unit I — W_0 and U_o are anticomplete

### Theorem 2.1

> `e(W_0,U_o)=0`.                                         `(WU0)`

### Proof

Suppose `wz` is an edge with `w in W_0`, `z in U_o`.

Both endpoints lie in `U subset B` and share the root, so the edge lies in a triangle. A singleton witness for the critical edge cannot lie in B: the relevant U-source and a B-witness would share the root, producing an extra common neighbour. The root itself is also impossible because every U-vertex has p matched neighbours. Hence the witness lies in A.

Since Y is anticomplete to U, any witness adjacent to w or z must lie in X.

There are two orientations.

**Orientation A.** The witness a is adjacent to w, nonadjacent to z, and

`N(z) cap N(a)={w}`.

But w has exactly one X-neighbour, its core head h(w), so `a=h(w)`. The buffer b is adjacent to z and to every vertex of X. Thus b is a second common neighbour of z and a, contradiction.

**Orientation B.** The witness a is adjacent to z, nonadjacent to w, and

`N(w) cap N(a)={z}`.

The singleton common neighbourhood contains no matched B-vertex. Therefore w and a cannot agree in any tight coordinate; their Boolean codes must be complementary. Since `c(w)=bar d`, this forces `c(a)=d`. But the outside pair `{d,bar d}` is disjoint from X, so no X-vertex has code d. Contradiction.

Both orientations fail. Hence `wz` is not an edge. square

This is raw physical D2C criticality and uses no selected-witness injectivity.

## 3. Unit II — exact U graph and exact U-side slack

Put `u_o=rho-1`.

The unmatched layer now has the exact structure:

- `U_-` independent;
- `U_o` independent;
- `W_0--U_o` anticomplete;
- b complete to U_o.

Therefore

> `q=e(G[U])=u_o=rho-1`.                                  `(Q0)`

The common-core hole count is exact:

> `H=e_bar(W_0,U_o)=k u_o`.                               `(H0)`

For `z in U_o`, every W_0 vertex is a nonneighbour. If

`h_X(z)=x-d_X(z)`,

then the previous outside degree identity simplifies to

> `epsilon_z=rho-2+h_X(z)`.                               `(UOE)`

Let

> `J=e_bar(X,U_o)`.

Summing gives

> `E_o=u_o(rho-2)+J`.                                     `(EO0)`

The core slack is

> `E_core=k(p+u-2)`,                                      `(EC0)`

and hence the total unmatched slack is exactly

> `E_U=k(p+u-2)+u_o(rho-2)+J`.                            `(EU0)`

Also

> `q+E_U=k(p+u-2)+u_o^2+J`.                              `(QEU0)`

Since the buffer-X certificates cover every X-row by a nonedge and the b-U_o certificates cover every U_o-column,

> `J>=max(x,u_o)`.                                        `(J0)`

## 4. Unit III — exact X-side slack retained

The exact X-side identity remains

> `L_X=x(lambda+1-rho)+k(x-1)+J-2e_X`,                   `(LX0)`

where `e_X=e(G[X])`.

Let

> `R=rho-p-2`.

The duplicate-complement support theorem from the preceding package gives

> `e_X<=kR`.                                               `(XCAP)`

Thus

> `L_X>= [x(lambda+1-rho)+k(x-1)+max(x,u_o)-2kR]_+`.      `(LXF)`

Together with

> `L_Y=rho(p+rho-lambda-1)`,                              `(LY0)`

we now have a completely explicit physical score floor in `(p,rho,k,lambda)`.

## 5. Unit IV — lambda=6 closes without new case geometry

The preceding package had already hand-reduced lambda=6, using only the weaker `H>=k` floor, to four scalar states:

> `(p,rho,k)=(4,6,1),(4,6,2),(4,7,1),(4,7,2)`.           `(OLD-L6)`

The old U-side bound used `H=k`; exact `(H0)` instead has `H=k u_o`, and the exact E_U formula contains two copies of H before simplification. Relative to that previous floor, the score increases by

> `2k(u_o-1)>0`.

For the four states in `(OLD-L6)` the previous lower-score margins `S_floor-C0` were respectively

> `-6,-2,0,-2`.

The exact core/outside separation adds respectively

> `8,16,10,20`.

All four become strictly positive. Therefore:

> **No zero-buffer above-M candidate exists at lambda=6.** `(L6)`

Combined with the preceding packages, the zero-buffer branch is now closed for every `lambda<=6`.

## 6. Unit V — a safe strong score floor for lambda>=7

Write

> `rho=p+s`, `s>=2`.

Put

> `M=max(x,u_o)`.

Using `(EU0)`, `(LXF)` and `(LY0)`, define

> `S_strong`
>
> `=rho(p+rho-lambda-1)`
> ` +k(p+u-2)+u_o(rho-2)+M`
> ` +[x(lambda+1-rho)+k(x-1)+M-2k(s-2)]_+`.              `(SSF)`

Every zero-buffer survivor must satisfy

> `S_strong<=C0`,                                         `(SSG)`

where

`C0=(lambda+3)p+(lambda+2)u-2 floor((lambda+1)^2/4)-4`.

This is a hand structural inequality. A finite script only audits its algebra/classification.

## 7. Unit VI — lambda=7 reduces to one scalar state

There are two cases:

- A: `x>=u_o`, equivalently `k>=s-1`;
- B: `x<u_o`, equivalently `k<=s-2`.

Before the final `[L_X]_+` term, `S_strong-C0` is

A:
> `D_A=k^2+2kp+ks-10k`
> `    +3p^2+5ps-29p+2s^2-20s+38`,                      `(D7A)`

B:
> `D_B=k^2+2kp+ks-11k`
> `    +3p^2+5ps-29p+2s^2-19s+37`.                      `(D7B)`

The raw X-slack terms are

A:
> `X_A=k^2-3ks+12k-p^2-ps+9p`,                           `(X7A)`

B:
> `X_B=k^2-3ks+11k-p^2-ps+9p+s-1`.                       `(X7B)`

A candidate needs `D_A+[X_A]_+<=0` or `D_B+[X_B]_+<=0`.

The reduction is short.

1. For fixed s,k, both D_A and D_B increase with p on `p>=4`: the p-step is already positive at the lower boundary.
2. In case A, D_A increases with k, so for fixed p,s its minimum is at `k=s-1`; that minimum increases with s from s=2.
3. In case B, D_B increases with k, so its minimum is k=1; it increases with s from the first allowed value s=3.
4. Hence for `p>=6`, D itself is already positive in both cases.
5. At `p=5`, the only case-A points with `D_A<=0` are `(s,k)=(2,1),(2,2)`; adding X_A gives totals 6 and 20. Case B is already positive.
6. At `p=4`, the only points with `D+[X]_+<=0` reduce to one:

> `s=2`, `k=1`.

Therefore:

> every lambda=7 zero-buffer survivor has
>
> `(p,rho,k)=(4,6,1)`.                                    `(L7-ONE)`

This is a hand integer classification, not a scan theorem.

## 8. Exact geometry of the lambda=7 singleton

For

> `(lambda,p,rho,k)=(7,4,6,1)`,

one has

- `u=7`, `u_o=5`;
- `x=5`, `y=2`;
- `R=0`, hence `e_X=0` exactly;
- `q=5` exactly;
- `H=5` exactly;
- `L_Y=12`;
- `E_U=29+J`;
- `L_X=14+J`;
- hence

  > `S=55+2J`.

The above-M score ceiling is

> `C0=67`.

Since `J>=5`, only

> `J in {5,6}`                                             `(J56)`

can survive.

The exact residual identity gives

> `delta=J-9`,

so these are the two structural possibilities

> `(J,delta)=(5,-4),(6,-3)`.                              `(L7-2)`

At `J=5`, the X--U_o nonedge graph is exactly the code-complement matching. At `J=6`, it is that matching plus exactly one additional physical X--U_o hole.

Thus lambda=7 is no longer an asymptotic or multi-parameter region: it is a five-by-five local incidence problem with at most one extra hole.

## 9. Next criticality attack

The next load-bearing edges are the many remaining X--U_o edges. For an edge `h_i z_j` with i != j:

- the edge lies in a triangle through b;
- an external B-witness in the orientation `N(z_j) cap N(t)={h_i}` is impossible because z_j and any B-witness share the root;
- an A-witness in the reverse orientation is heavily constrained because X is independent while every two X-vertices have the two Y-vertices as common neighbours.

The remaining possible matched-B orientation should be classified exactly. With only J=5 or 6, a single forced additional X--U_o hole closes the lambda=7 branch.

Do not move to lambda=8 until this local five-by-five geometry has been exhausted.

## 10. Trust boundary

The new theorem `(WU0)` is raw criticality. The exact q/E_U identities are degree bookkeeping. `(XCAP)` is physical ordered-pair capacity after subtracting the already-consumed buffer certificate pair. The lambda=6 and lambda=7 reductions are finite symbolic consequences of these hand statements.

No source-tuple theorem or four-exception gate is used. `X_3` remains untouched because `u=0`.
