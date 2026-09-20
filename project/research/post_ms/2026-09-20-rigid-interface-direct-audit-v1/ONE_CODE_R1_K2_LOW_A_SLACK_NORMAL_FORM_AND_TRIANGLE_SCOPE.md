# Residual-one k=2: low-A-slack normal form and triangle-scope blocker

Date: 2026-09-20

Status: **same-session conditional synthesis plus hostile scope check**, under the rigid one-code residual-one branch, `k=2`, `J2=empty`, on the exact low-k ray. No graph-realizability claim is made.

This note follows `ONE_CODE_R1_K2_Y_INDEPENDENCE_AND_HH_CERTIFICATE_SPLIT.md`. Its purpose is twofold:

1. record the sharply compressed geometry forced by small A-side slack once `e(Y)=0` is known;
2. preserve a tempting but invalid extension of the F0--Y reverse-certificate argument, so that future work does not silently reuse a triangle-only lemma on arbitrary Y--U edges.

## 1. Exact Y-side slack after Y-independence

The new Y-independence theorem gives

`e(Y)=0`.

Therefore the exact Y-side identity is

> **`L_Y=Z_{Y,U}-(p-1)`.**                                `(LAS-Y)`

In particular any quadratic Y--U hole block is paid directly in A-side slack.

## 2. Two populations which necessarily create Y--U holes

Let `E=U\W_s`, `|E|=p-1`.

Define

- `P={t in E:d_H(t)>0}`;
- `B0={w in U_bar(d):d_H(w)=0}`.

The global H/Y polarization gives, for every `t in P`,

`d_Y(t)<=1`,

so t misses at least `p-2` vertices of Y.

Every B0 vertex is Y-anticomplete. The two selected witnesses `W_s` are also Y-anticomplete.

Consequently

> `Z_{Y,U} >= |P|(p-2)+|B0 cap E|(p-1)+2(p-1)`.          `(LAS-ZY)`

Hence, asymptotically,

> **`|P|/p <= L_A/p^2+o(1)`** and
>
> **`|B0|/p <= L_A/p^2+o(1)`.**                           `(LAS-POP)`

Thus low A-side slack simultaneously suppresses the H-positive escape population and the only U-code class with linear U--U source capacity.

## 3. Quantitative low-slack normal form

Write

`ell=L_A/p^2` along an unbounded sequence.

From `(LAS-POP)`:

- all but at most `(ell+o(1))p` outside escapes are H-free;
- `|B0|<=(ell+o(1))p`.

The oriented U-source capacity theorem gives

`e(U)<= (p-1)|B0|+2u`,

and therefore

> **`e(U)/p^2 <= ell+o(1)`,**
>
> **`M_U/p^2 >= 1/2-ell-o(1)`.**                         `(LAS-U)`

Because almost every escape is H-free, the H--U hole block satisfies

> **`Z_{H,U}/p^2 >= 1-ell-o(1)`.**                        `(LAS-HHOLE)`

Using

`L_H=Z_{H,U}+|H|-2e(H)`

and `L_H<=L_A`, we obtain

> **`e(H)/p^2 >= (1-2ell)/2-o(1)`.**                     `(LAS-HDENSE)`

Similarly `(LAS-Y)` and `L_Y<=L_A` give

> **`e(Y,U)/p^2 >= 1-ell-o(1)`.**                        `(LAS-YDENSE)`

So whenever ell is small, the branch is forced toward the explicit product-like geometry

- H internally dense;
- Y independent;
- H--U sparse;
- Y--U dense;
- U internally sparse;
- the linear-capacity `bar d` source class B0 small.

At `ell=o(1)` this becomes the extreme hostile normal form

> **H almost complete, Y independent, H--U almost empty, Y--U almost complete, U sparse.** `(LAS-NF)`

This is a much narrower target than the predecessor generic H-dense/Y-dense compensator split.

## 4. The tempting next shortcut is invalid without a triangle

After proving Y-independence it is tempting to argue:

> if an H-free U-vertex t has two Y-neighbours, then every edge ty must use the reverse singleton orientation and hence consume a `B0` witness.

That statement is **not valid without an additional triangle hypothesis**.

The corrected raw two-orientation lemma used earlier is automatic only when the deleted edge lies in a triangle, because then deleting the edge does not itself separate its endpoints beyond distance two. For a triangle-free edge `ty`, the edge can be critical simply because the pair `(t,y)` itself jumps from distance one to distance at least three after deletion. No external singleton certificate need exist.

For an H-positive t, every ty edge is safely triangular through an H-neighbour, which is exactly why the global H/Y polarization theorem is valid. For an H-free t, however, triangle membership is not automatic:

- Y is now independent;
- t may be X-anticomplete;
- its U-neighbours may all be nonadjacent to y.

Therefore the predecessor F0 reverse-certificate capacity **must not be extended wholesale to the H-free Y-dense population**.

## 5. What a triangle-free Y--U edge does force

The triangle-free alternative is not free. If `t in U` and `y in Y` are adjacent and `ty` lies in no triangle, then

1. y is adjacent to every X-vertex, so t must be X-anticomplete;
2. `N_U(t) cap N_U(y)=empty`.

On the exact ray, let `d_U(t)` denote t's U-degree. Since t is X-anticomplete,

`z_A(t)>=x=p+1`,

and the exact U identity gives

`epsilon_t=z_A(t)-d_U(t)>=p+1-d_U(t)`.

Also `N_U(y)` contains t but is disjoint from `N_U(t)`, so

`d_U(y)<=p+1-d_U(t)`.

Because `e(Y)=0`, the Y-degree identity gives

`epsilon_y=p-d_U(y)>=d_U(t)-1`.

Hence every triangle-free Y--U edge satisfies the exact endpoint-slack inequality

> **`epsilon_t+epsilon_y>=p`.**                            `(LAS-TF)`

Thus the loophole left by triangle scope has a direct physical price. It does not yet by itself close the branch, because many triangle-free edges may share the same high-slack endpoints. It is nevertheless the correct object to retain in the next optimization.

## 6. Dense-H certification remains controlled

Independently of the Y--U triangle issue, the H--H theorem from the companion note is unaffected:

- every H--H edge is either private-foot certified or U-certified;
- at most `u=p+1` H--H edges can be U-certified in total.

Therefore `(LAS-HDENSE)` implies that a low-slack survivor has a quadratic family of **private-foot-certified H--H edges**.

This is the safe next local target. It avoids the triangle-scope trap entirely.

## 7. Next move

The preferred continuation is now a two-pronged but tightly coupled attack on `(LAS-NF)`:

1. use the private-foot certificates of the dense H graph to constrain the private-coordinate support of the Y-dense, H-free U population;
2. partition Y--U edges into triangular and triangle-free edges, using valid reverse-certificate capacity only on the triangular part and `(LAS-TF)` on the triangle-free part.

Any future coefficient optimization must retain that partition explicitly. Treating every H-free Y--U edge as reverse-certified is invalid.

The upstream caveat remains unchanged: all statements are conditional downstream of the unresolved rigid complete Hall-cut reachability interface.