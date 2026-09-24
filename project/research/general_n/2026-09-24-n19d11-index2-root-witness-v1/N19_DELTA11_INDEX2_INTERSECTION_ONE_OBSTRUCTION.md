# n=19, Delta=11: stable index 2, source-intersection one

Status: **internal graph-level exclusion, conditional on the audited graph-to-profile/source bridge, one-use rule, root-edge criticality characterization, and exact-star inequalities.** This is not external mathematical acceptance.

We treat stable index 2 of the leading two-label family:

- `x=(9,7)`, `h=(9,8)`;
- normalize `C0={1,2}`, `C1={1,3,4}`;
- `T0={3,...,11}` and all nine endpoints are assigned to `L0`;
- `T1={2,5,...,11}` has eight endpoints and exactly seven are assigned to `L1`.

Let `p=def(L0)`, `q=def(L1)`, and

    U = def(2) + sum_{t=3}^{11} def(t).

The audited exact-star inequalities imply

    U >= 73 - 9p,
    U >= 58 - 7q,

and the fixed B-degrees of the two labels give `3<=p<=9` and `2<=q<=8`.
A strict counterexample at `n=19, Delta=11` would have total degree deficit

    D = 19*11 - 2e <= 209 - 2*91 = 27.

## A reusable two-singleton deficit bound

Suppose two distinct inactive A-vertices `r,s` have singleton B-neighbourhoods. Their combined B-degree is 2. Among A-edges, their mutual edge contributes at most two incidences, their edges to the other three inactive A-vertices contribute at most six incidences, and their incidences to `L0,L1` contribute at most

    min(2,9-p) + min(2,8-q).

Therefore

    def(r)+def(s) >= 12 - min(2,9-p) - min(2,8-q).      (TW)

Combining (TW) with the two star inequalities gives

    p + q + U + def(r)+def(s) >= 29.                   (1)

A short exact case check is transparent. If `p<=6`, the first star inequality and the crude `(TW)>=8` give at least `81-8p+q >=35`. If `q<=6`, the second gives at least `66+p-6q >=33`. The remaining six pairs `(p,q)` in `{7,8,9} x {7,8}` give lower bounds respectively

    (7,7):33, (7,8):35, (8,7):34,
    (8,8):29, (9,7):36, (9,8):31.

Thus any branch forcing two singleton-B A-vertices contradicts `D<=27`.

## Case 1: the omitted T1 endpoint is not 2

Then endpoint 2 is assigned to `L1`. One-use forces its source to be 1: using source 3 or 4 would reuse physical edge `23` or `24`, already available as the source edge for the `L0` assignment at endpoint 3 or 4. Exact uniqueness therefore gives

    12 present; 23,24 absent; 13,14 present.

For every assigned `t in {5,...,11}`, one-use forbids `1t`, so `2t` is present. At the unique omitted endpoint `w`, the `L0` assignment still forces exactly one of `1w,2w`.

Now criticality of root edge `01` cannot use the endpoint pair (1 already has B-neighbours), and no B-side witness is possible: every non-neighbour among the assigned `t` shares B-neighbour 2 with 1, while if `w` is a non-neighbour of 1 then `2w` is present and again 2 is common. Hence an A-vertex with `N_B={1}` is forced.

Similarly root edge `02` forces an A-vertex with `N_B={2}`. The only forced B non-neighbours 3 and 4 share B-neighbour 1 with 2, and if the omitted `w` is a non-neighbour of 2 then `1w` is present and again 1 is common. The two singleton witnesses are distinct, so (1) gives `D>=29`, contradiction.

## Case 2: endpoint 2 is the omitted T1 endpoint

All seven endpoints `5,...,11` are assigned to `L1`. Put

    a=e(1,2),  b=e(1,3),  c=e(1,4).

For each `t=5,...,11`, one-use forces `1t` absent and `2t` present, and the `L1` assignment uses exactly one of sources 3 and 4. The `L0` assignments at 3 and 4 give

    e(2,3)=1-b,   e(2,4)=1-c.

### 2A. Root edge 02 has a singleton-A witness

Let `s` have `N_B(s)={2}`. If root edge `01` also has a singleton-A witness, (1) closes the branch. Suppose it does not.

Then at least two of `a,b,c` are zero. If at least two were one, every possible B-side witness for `01` is defeated: endpoint 2 shares `L0` with 1; endpoints 3 and 4 share `L1` with 1; and every `t=5,...,11` shares either B-neighbour 2 with 1 (when `a=1`) or its source 3/4 with 1 (when `a=0` and `b=c=1`).

The one-one-zero pattern `(a,b,c)=(1,0,0)` is itself impossible without a singleton witness for `01`: 3 and 4 share `L1` with 1 and every `t` shares B-neighbour 2 with 1.

If `(a,b,c)=(0,1,0)`, criticality of root edge `04` forces an A-vertex with singleton B-neighbourhood `{4}`. Indeed 4 has B-neighbour 2; a nonadjacent B-vertex 1 or 3 shares `L1` with 4, while any nonadjacent `t` is one whose L1 source is 3 and then both 4 and t share B-neighbour 2. Thus no endpoint or B-side witness exists for `04`. The pattern `(0,0,1)` symmetrically forces a singleton `{3}`.

If `(a,b,c)=(0,0,0)`, the same argument forces singleton witnesses for root edges `03` and `04`, because both 3 and 4 are adjacent to 2 and any nonadjacent `t` shares B-neighbour 2 with the relevant endpoint.

Hence every legitimate subcase in 2A has at least two singleton-B A-vertices, contradicting (1).

### 2B. Root edge 02 has no singleton-A witness

The endpoint pair cannot witness `02`, because 2 is adjacent to every `t=5,...,11`. A B-side witness can only be 3 or 4: vertex 1 shares `L0` with 2, while the `t` are adjacent to 2. Up to swapping 3 and 4, a witness at 3 requires

    a=0, b=1, and every t=5,...,11 uses source 4.

These are necessary conditions because any `12` edge or any `3t` edge would give 2 and 3 an additional common neighbour.

Under this extreme pattern, criticality of root edge `04` forces an A-vertex `r` with `N_B(r)={4}`. Every possible B-side non-neighbour of 4 shares either `L1` (vertices 1 and 3) or a `t`/B-neighbour with 4, while 4 itself has the forced `t`-neighbours.

If root edge `01` also has a singleton-A witness, (1) closes the branch. Otherwise `c=0`; if `c=1`, every `t` shares B-neighbour 4 with 1 and the remaining B candidates are defeated by `L0` or `L1`. Thus the only hard pattern is

    a=0, b=1, c=0,

with all seven `t` using source 4.

If edge `34` is present, root edge `03` forces another singleton-A witness: its non-neighbour 2 shares B-neighbour 4 with 3, every `t` shares 4 with 3, and vertex 1 is adjacent to 3. Again (1) closes the branch.

It remains only the subcase `34` absent. Here the forced singleton `r` at 4 is enough together with the forced sparsity:

- vertex 1 has degree at most 8, hence `def(1)>=3`;
- vertex 3 has degree at most 7, hence `def(3)>=4`, so `U>=4`;
- since `r` has only B-neighbour 4,

      def(r) >= 6 - min(1,9-p) - min(1,8-q).

Consequently

    D >= p+q+U+3+def(r) >= 28.                         (2)

For completeness, if `p<=6`, (2) and the first star inequality give at least `80-8p+q >=34`; if `q<=6`, the second gives at least `65+p-6q >=32`. For the remaining six pairs `(p,q)` in `{7,8,9} x {7,8}`, using `U>=max(4,73-9p,58-7q)` gives lower bounds

    (7,7):31, (7,8):33, (8,7):31,
    (8,8):28, (9,7):33, (9,8):31.

Thus the final subcase also contradicts `D<=27`.

## Conclusion

Stable index 2 with source-set intersection one is excluded at graph level. Combined with the earlier exact exclusion of its disjoint source-set case, stable index 2 is eliminated. Together with the separately proved index-1 intersection-one obstruction and the previously verified disjoint/index-3 exclusions, the first three leading two-label abstract survivors are now graph-level excluded at the stated internal/conditional trust level.

This does **not** close the full `n=19, Delta=11` row and does not prove the general theorem. The next useful step is to inspect the next abstract survivor(s) for whether the same root-edge singleton-witness mechanism generalizes, rather than extending scalar shards blindly.
