# Hostile regression of the raw boundary-code-edge trichotomy

Date: 2026-09-21

Status: independent finite diagnostic. This file is **not** part of the proof of the trichotomy and is not evidence that the rigid complete-Hall-cut interface is realizable.

## Purpose

The new raw theorem `RIGID_CUT_BOUNDARY_CODE_EDGE_TRICHOTOMY.md` was derived from triangle-edge criticality without choosing the A-edge certificate policy used by the older rigid regression. A separate implementation was therefore used to try to falsify the theorem directly on actual D2C graphs.

For every tested maximum-degree root it independently reconstructed

- the rooted partition;
- all tight antipode fibres;
- A/U tight codes;
- matched row-complement gamma codes;
- complete A-cuts;
- and **all** criticality certificates of every boundary edge `y q_i^{d_i}` exposed through the opposite side of a complete cut.

Every returned certificate was checked against the three asserted physical mechanisms rather than selecting a favourable certificate.

## Corpus

The hostile replay used

- the entire NetworkX graph atlas through order seven, filtered to actual D2C graphs;
- 25 independently seeded greedy D2C graphs at each order `8,9,10,11,12`;
- every maximum-degree root of those graphs.

This produced 269 rooted graph instances.

Two cut modes were checked.

### Complementary-pair-family cuts

These are the cuts relevant to the rigid Hall interface: X is a union of whole unordered complementary A-code pair classes.

In this modest replay, **no complete proper pair-family A-cut occurred at all**. Thus the rigid interface remains without a positive fixture in this sample and the new theorem is vacuous there.

### Arbitrary complete A-cuts

To ensure the local boundary theorem itself was not only being tested vacuously, the replay also examined every complete A-cut on roots with `|A|<=10`, without requiring X to be a pair-family union.

It found 12 complete cuts. Most have no exposed boundary coordinate. One order-8, size-13 D2C fixture/root produced

- two complete cuts;
- two exposed boundary B--A edges;
- two actual certificates in total;
- both certificates of the **U-forward** type.

For both positive certificates the independent checker recovered exactly

`c(w)=bar d xor e_i`

and X-anticompleteness of the unmatched witness, as required by the theorem.

Across all tested roots/cuts there were zero violations of

- witness-location classification;
- one-match U code localization;
- matched-forward universal-coordinate requirement;
- matched-forward degree-one row condition;
- reverse-X witness location;
- reverse gamma-code localization.

## Interpretation

The positive arbitrary-cut fixture exercises the U-forward arm of the theorem on an actual D2C graph, while the continued absence of complete complementary-pair cuts reinforces the correct trust boundary:

- the **local trichotomy** now has a small positive graph-level exercise;
- the **rigid pair-family interface** still has zero positive actual-D2C fixtures with `x>=3` and remains the dominant reachability risk.

No statistical or asymptotic conclusion is drawn from the corpus size.
