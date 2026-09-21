# Single complementary-U repair hub: reciprocal criticality normal form

Date: 2026-09-21

Status: raw local classification inside the repeated rigid one-code interface. This note audits the most tempting next obstruction after the near-equality repair-reservoir theorem and shows that **local edge criticality does not by itself kill a single repair hub**.

## 1. Setup

Assume the generic repeated one-code near-equality face from `ONE_CODE_BOUNDARY_REPAIR_RESERVOIR.md`:

- `y>=2`, `m>=2`, `L=empty`;
- `e=u-k=p`;
- exactly one boundary vertex `w_i` of code `bar d xor e_i` for each coordinate i;
- every `w_i` is A-anticomplete;
- `K` is the complementary-U repair set, every `z in K` having code `bar d`;
- for every selected coordinate `i in S`, some `rho(i) in K` is adjacent to both the selected head `h_i` and `w_i`.

Now specialize to

> **`k=1`, `K={z}`.**                                   `(1.1)`

Then z is adjacent to `h_i` and `w_i` for every `i in S`.

## 2. The aligned nonedge has exactly one common neighbour

Fix `i in S`.

We already know

- `h_iw_i` is not an edge because w_i is X-anticomplete;
- `c(h_i)=d xor e_i` and `c(w_i)=bar d xor e_i=overline{c(h_i)}`, so there is no common matched endpoint;
- the root misses h_i;
- every boundary vertex `w_j` is X-anticomplete, so no `w_j` is a common neighbour;
- every w_i is A-anticomplete, so no A-vertex is a common neighbour;
- K contains only z.

Since z is adjacent to both h_i and w_i,

> **`N(h_i) cap N(w_i)={z}`.**                           `(2.1)`

Thus the diameter repair is not merely existential: it is a unique-common-neighbour relation.

## 3. Both forced repair edges are automatically critical

The two edges incident with the repair hub are

`z h_i` and `z w_i`.

Equation `(2.1)` supplies a valid criticality certificate for both:

- for edge `z h_i`, source `h_i` with witness `w_i` has singleton common neighbour `{z}`;
- for edge `z w_i`, source `w_i` with witness `h_i` has singleton common neighbour `{z}`.

Therefore each selected coordinate forms a reciprocal criticality gadget

`h_i -- z -- w_i`, with `h_iw_i` absent and z their unique common neighbour.

This is a genuine local D2C-compatible pattern, not an immediate contradiction.

## 4. Rooted B-edge slot is also consistent

The edge `z w_i` lies inside B. In the independent rooted-B selection language, `(2.1)` provides the selected slot

> **`(source,witness,head)=(w_i,h_i,z)`.**               `(4.1)`

Across different selected coordinates i, the physical sources w_i are distinct and the A-witnesses h_i have distinct one-flip codes. Hence the ordered selected slots `(w_i,h_i)` are automatically distinct.

Consequently neither

- rooted B-edge slot injectivity,
- the distinct physical-source premise, nor
- selected `(source,coordinate)` uniqueness

is violated merely because the same repair vertex z serves many selected coordinates.

This is an important negative result for the proof search: a naive attempt to bound one hub's reuse directly from local edge criticality or selected-slot injectivity cannot work.

## 5. Code localization of any rooted witness

The same conclusion can be read in reverse. For edge `z w_i`, the orientation with source z would require an A-vertex adjacent to w_i, but w_i is A-anticomplete, so that orientation is impossible. Any rooted A-witness must therefore use source w_i and head z.

To avoid an unwanted common matched endpoint with w_i, such a witness must have tight code exactly

`overline{c(w_i)}=d xor e_i`.

The selected head h_i is therefore in precisely the forced witness class and already realizes the slot.

## 6. Consequence for the next attack

The single-hub face survives the **local** raw-criticality replay in a particularly rigid normal form. Closing it requires genuinely global information that couples different coordinates: for example pair-local Hall/source load, residual defect, constraints on the simultaneous neighbourhood of z across all h_i/w_i, or an actual graph-level non-realizability argument.

The upstream source-tuple premises are not the missing ingredient at this exact step: the forced rooted slots already respect their physical-source semantics.

## 7. Scope

This note does not assert existence of the hub geometry in a D2C graph. It shows only that the immediate local criticality checks do not contradict it. The bounded actual-D2C regression still has no positive rigid complete Hall-cut fixture with `x>=3`, and X_3 remains the mandatory negative control.
