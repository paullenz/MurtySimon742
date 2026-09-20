# Type-F support gap and maximal-m2 eventual closure

Date: 2026-09-20

Status: **internal candidate structural strengthening**. This note supersedes the final “all-F p=2 remains” sentence of `M2_P2_REMAINDER.md`; that earlier note remains preserved as the path by which the missing observation was exposed. The argument is upstream and uses only the first-strict funnel plus the independently audited raw meaning of tight codes.

## 1. A Type-F witness cannot have the same tight code as a_0

Recall the exact Type-F funnel. For a buffer neighbour `x` with outside witness `z`, Type F means

- `I_x={i}` for one coordinate `i in S_0`;
- `c(z)=bar c(x)`;
- `za_0` is a nonedge;
- the rooted matched-edge certificate is forward:

> `N(z) cap N(a_0)={q_i}`,                              `(F-FUNNEL)`

where `q_i` is the `bar d` endpoint of fibre i.

Because `I_x={i}`, the complementary outside code `c(z)=bar c(x)` differs from d **only** at i. In support notation,

> `S_z={i}`.                                             `(F-ZSUP)`

If `S_0={i}` as well, then

> `c(z)=c(a_0)`.

The 20 September raw same-code audit independently re-derived the basic code semantics: two coded vertices with the same code share the same selected matched endpoint in **every** one of the p tight fibres. Therefore, for `p>=2`, equal-code vertices have at least p distinct common matched neighbours.

This contradicts the singleton common-neighbour relation `(F-FUNNEL)`.

Hence:

> **Type F implies `|S_0|>=2` whenever `p>=2`.**         `(F-SUPPORT-GAP)`

No Hall inequality, score bound, source-tuple capacity theorem or finite scan is used.

## 2. Immediate correction to the maximal-m2 large-X narrative

The mandatory corrected m=2 bulk-block theorem says that for maximal `m=2`, `p>=3`, `x>=4`, the two X'-classes are complementary F/R and

> `|S_0|=1`, `I_F=S_0`, `I_R=I_0`.

But `(F-SUPPORT-GAP)` forbids the F class outright. Therefore the entire large-X branch is already empty:

> **maximal `m=2`, `p>=3`, `x>=4` is impossible.**       `(M2-X4-RAW-CLOSED)`

This is strictly upstream of the longer exact Hall/residual contradiction in `M2_FR_EXACT_HALL_CLOSURE.md`. That longer proof remains valid conditional mathematics and useful independent redundancy, but it is no longer the shortest logical route.

## 3. Complete p=2 closure

The first-strict setup itself excludes `p=1`, because X-codes must be neither `d` nor `bar d`.

Let `p=2`. Then the support `S_0` of `a_0` is a nonempty proper subset of a two-element coordinate set, so necessarily

> `|S_0|=1`.

By `(F-SUPPORT-GAP)`, **no Type-F buffer neighbour exists**.

Thus every head in `X'` is Type R. Its agreement block is the unique nonempty subset of `I_0`, so all X'-heads have the same tight code. The graph-fixed Type-R foot theorem then forces every selected outside witness for that code class to be the same physical vertex. Equivalently the raw eligibility component has matching number one.

Therefore maximal witness number two is impossible:

> **no maximal `m=2`, `p=2` first-strict graph exists.** `(M2-P2-CLOSED)`

This supersedes the provisional one-code all-F remainder isolated in `M2_P2_REMAINDER.md`.

## 4. Maximal-m2 eventual conclusion

Combine:

1. `p=1` impossible;
2. `p=2` impossible by `(M2-P2-CLOSED)`;
3. `p>=3,x>=4` impossible by `(M2-X4-RAW-CLOSED)`;
4. `p>=3,x=3` is absolutely bounded by `M2_X3_BOUNDED_TAIL.md`:
   `p<=8`, `omega<=8`, hence `n<=39`.

Therefore:

> **Conditional on the audited rigid first-strict and maximal-selection setup, every maximal `m=2` survivor has order `n<=39`.** `(MAX-M2-N39)`

In particular maximal `m=2` cannot support a sufficiently-large counterexample family.

This is an eventual-programme closure, not an all-order classification: the finite order-at-most-39 tail is not asserted empty.

## 5. Consequence for the next attack

The live unbounded first-strict frontier moves to

> `m>=3`.

The correct structural object remains the raw eligibility graph `H[X',U_o]` with

> `m=nu(H)`.

By Konig, a minimum vertex cover of size m controls all physical certificate incidence. The m=2 work suggests that the next compact theorem should be formulated in terms of cover geometry / code components rather than enumerating F/R selected representatives.

The support-gap lemma should be used immediately: every Type-F code consumes a coordinate in `S_0`, and now `|S_0|>=2`; distinct Type-F classes consume distinct support coordinates, while Type-R blocks live disjointly in `I_0`. Any future coordinate-capacity argument must retain that physical distinction.
