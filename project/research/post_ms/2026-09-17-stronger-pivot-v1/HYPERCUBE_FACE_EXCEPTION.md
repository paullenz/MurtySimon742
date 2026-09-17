# Independent hypercube-face reconstruction of the 12-vertex exception mechanism

17 September 2026. Research directed by Paul Lenz; independent reconstruction, derivation and checks by ChatGPT/Geeps.

**Status:** internally proved construction and deterministic finite checks. **Novelty open.** The `k=3` graph matches every published coarse invariant of the 12-vertex/32-edge counterexample, but direct isomorphism to the published Figure 1 has not been certified from an authoritative adjacency list. Do not cite this file as an identification of Figure 1.

## 1. Construction

For an integer `k>=3`, let

`B={0,1}^k`

be the binary k-cube. Add a root `r` and vertices

`A={a_1,...,a_k}`.

Define `X_k` by the following edges:

1. two vertices of `B` are adjacent iff their binary strings differ in exactly one coordinate (`G[B]=Q_k`);
2. `r` is adjacent to every vertex of `B`;
3. `a_i` is adjacent to `x in B` iff `x_i=0`;
4. there are no edges among A and no edges from `r` to A.

Thus

`|V(X_k)|=2^k+k+1`.

The cube contributes `k 2^(k-1)` edges, the root contributes `2^k`, and the coordinate-face vertices contribute another `k 2^(k-1)`. Hence

> `e(X_k)=(k+1)2^k`.                                  (1)

## 2. `X_k` has diameter 2

- Any two cube vertices have distance at most 2 through `r`.
- `r` and `a_i` have a length-2 path through any cube vertex with i-th coordinate 0.
- `a_i` and `a_j` (`i!=j`) have a common cube neighbour with both coordinates zero.
- If `x_i=0`, then `a_i x` is an edge. If `x_i=1`, flip the i-th coordinate to obtain `y`; then `a_i-y-x` has length 2.

The graph is not complete (`r` is not adjacent to any `a_i`), so its diameter is exactly 2.

## 3. Every edge is critical

It suffices to give, for each edge, a pair whose unique path of length at most 2 uses that edge.

### 3.1 Cube edge

Let `xy` be a cube edge differing in coordinate i, with

`x_i=0`, `y_i=1`.

The pair `(a_i,y)` is nonadjacent. Any cube common neighbour of `a_i` and `y` must both have i-th coordinate 0 and be a cube neighbour of y. The only such vertex is x. The root is not adjacent to `a_i`, and no A-vertex is adjacent to `a_i`. Therefore

`N(a_i) intersect N(y)={x}`.

Deleting `xy` destroys the unique length-2 path `a_i-x-y`.

### 3.2 Face edge

For the edge `a_i x` with `x_i=0`, let y be obtained from x by flipping coordinate i to 1. Exactly the same calculation gives

`N(a_i) intersect N(y)={x}`.

Deleting `a_i x` again destroys their unique length-2 path.

### 3.3 Root edge

For a root edge `rx`, let `bar(x)` be the bitwise antipode of x. Since `k>=3`, x and `bar(x)` are neither adjacent nor at cube-distance 2. No `a_i` is adjacent to both because their i-th bits are complementary. Both are adjacent to r. Hence

`N(x) intersect N(bar(x))={r}`.

Deleting `rx` destroys their unique length-2 path through r.

Every edge lies in one of these three classes, so:

> **For every `k>=3`, `X_k` is diameter-2-critical.**

No enumeration enters this proof.

## 4. The k=3 member

For k=3,

`n=8+3+1=12`,
`m=4*8=32`.

Its degree sequence is

`8,7,6,6,6,5,5,5,4,4,4,4`.

The root has unique maximum degree 8. The zero vector `000` is adjacent to all three A-vertices, so the edge `r-000` is dominating. A direct check finds it is the unique dominating edge. The graph is primitive/twin-free: all open neighbourhoods are distinct.

Since

`M(12)=floor(11^2/4)+1=31`,

this graph is itself a counterexample to the 2019 all-order second-extremal conjecture, independently of the published drawing.

An independently found arbitrary labelling has graph6

`KnbI^UpaKgi\``.

The deterministic coordinate labelling in the checker has a different graph6 string because graph6 is label-dependent; the two were checked isomorphic during discovery.

Radosavljević's 2023 enumeration claims the complete D2C list through order 13 and reports one Conjecture-3 counterexample, while the peer-reviewed 2024 paper exhibits a 12/32 counterexample with a dominating edge. Conditional on that enumeration, the present k=3 graph must be isomorphic to the published exception. We nevertheless keep the stronger identity claim open until an authoritative adjacency representation of Figure 1 is compared directly.

## 5. Canonical selected/residual profile

Take the root r. Then

`B=N_G(r)=Q_k`,
`A={a_1,...,a_k}`,
`b=2^k`,
`a=k`.

Because A is independent in G,

`F=G[A]` is empty.

Equation (1) gives

`m=b(n-b)=2^k(k+1)`,

so

`t=0`, `delta=-t=0`.

The exact ledger `e(F)=r+t` therefore gives

> `r=0`.                                                (2)

Thus **every residual degree rho_x is zero**.

The selected count is the rooted triangle count

`Q=e(G[B])=e(Q_k)=k 2^(k-1)`.                          (3)

There are exactly the same number of H-cross edges: `a_i x` is an H-edge exactly when `x_i=1`, giving `k 2^(k-1)` such pairs. By (2) every one is selected.

The selected representatives have an explicit unique form. For each cube edge in coordinate i, write its endpoints x,y with

`x_i=0`, `y_i=1`.

In the complement H,

> `y a_i -> x`.                                        (4)

Indeed `y a_i` is an H-edge and its endpoints dominate every H-vertex except x. The deterministic checker also searches all possible source/label orientations and finds (4) to be the unique canonical quasi-edge for every cube edge at k=3.

Consequently, for a cube vertex y,

`q_y=HammingWeight(y)`,
`p_y=k-HammingWeight(y)`,
`rho_y=0`.                                             (5)

Every label `a_i` has selected multiplicity

`x_i=2^(k-1)`,

but

`d_i=R_i=s_i=0`                                       (6)

because F and the residual system are empty.

Equations (2)–(6) expose the failure mode of a demand-only proof: the selected system is large and highly structured, yet every canonical demand is zero.

## 6. Why the obstruction is finite at second-extremal density

The k=3 member has

`32>M(12)=31`.

For k>=4, put `N=2^k`. Then

`n-1=N+k`,
`m=(k+1)N`.

Compare the unfloored second-extremal quadratic:

`(N+k)^2 - 4(k+1)N`
` = N^2-(2k+4)N+k^2`
` = N(N-2k-4)+k^2`.                                  (7)

For k>=4, `2^k>2k+4`, so (7) is positive. Therefore

`m < (n-1)^2/4 < floor((n-1)^2/4)+1 = M(n)`

(with the integer/floor conclusion immediate from the large positive gap).

Thus the natural infinite continuation of the 12-vertex mechanism remains D2C but drops below the second-extremal threshold from k=4 onward. This supplies one concrete explanation of how the finite exception can fail to scale.

## 7. Interpretation for the project

The key boundary is not merely `t=0`; it is the extreme profile

`t=0, F=empty, r=0`.

In that profile every H-cross edge is selected, every B-source is residual-zero, and the demand h-index is identically zero. The hypercube construction realizes the selected representatives as coordinate-labelled oriented cube edges.

This suggests a new structural subproblem:

> Classify or bound canonical systems with `t=0`, `F=empty`, `r=0` by translating the quasi-edge system into an orientation/edge-labelling of `G[B]`.

If high-density realizations of this boundary can be shown finite or quantitatively sparse, the 12-vertex obstruction can be isolated without contaminating the eventual argument.

## 8. Novelty boundary

A quick targeted search did not locate this exact `Q_k` + coordinate-face construction under a standard name. That is **not** a novelty determination. It may be a known D2C construction or an implicit reformulation of an existing family. No originality claim should be made until a dedicated literature comparison is completed.
