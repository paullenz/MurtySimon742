# Four-defect ray-extension diagnostic

17 September 2026. Research directed by Paul Lenz; exact exploration by ChatGPT/Geeps.

**Status: diagnostic only; not promoted as a theorem.**

After the general leaf-package reduction, lopsided-ray closure, and isolated-pair exclusion, the remaining four-defect frontier consists of no-pair attachment rays in which all attachment counts except the largest `z` belong to a fixed finite list.

Exact orientation-code calculations show a striking stability property which should guide the next hand proof.

## Observed ray extension law

Fix one of the remaining no-pair strips and a valid labelled exceptional four-vertex core. Once the largest attachment group has size at least the other attachment groups and at least three, every tested increment

`z -> z+1`

satisfies

> `tau(Omega(z+1)) = tau(Omega(z)) + 2`.

The exact leaf-package quantity has the same increment:

> `B_4(z+1)=B_4(z)+2`.

Therefore the observed exceptional-core increment

`C=tau(Omega)-B_4`

is constant along the unbounded `z`-ray.

The check covered every valid labelled exceptional core on all surviving strips:

- `g=2`: `(0,0,y,z)`, `1<=y<=6`;
- `g=3`: `(0,x,y,z)` for the seven surviving `(x,y)` pairs;
- `g=4`: `(w,x,y,z)` for the three surviving triples;

and three consecutive extension steps beginning at `z>=max(3,y)` in each case. No failure was observed.

## Why this is plausible structurally

Adding one new leaf to the already-large pendant group has two visible effects in the forced-code description:

1. the two complementary same-parent clique packages each gain one vertex, forcing the leaf-only cover `B_4` upward by exactly two;
2. every code involving the new leaf has the same parent/target form as the corresponding old large-group leaf codes, while the exceptional-source code classes are unchanged except for the ambient complement coordinate.

The data suggest that these latter additions are cover-neutral once the exceptional-core contribution is paid. A hand proof should formalize this by constructing mutually inverse cover transformations between `Omega(z)` and `Omega(z+1)` after removing the two new same-parent clique vertices.

## Consequence if proved

A ray-extension lemma would reduce the complete remaining four-defect problem to a finite exact base table: prove the core increment once at the smallest admissible `z` for each bounded strip, then extend to all `z` automatically.

Together with the diagnostic minimum increments already recorded,

- `g=2,y=1`: `C>=12`;
- `g=2,y>=2`: `C>=14`;
- surviving `g=3`: `C>=20`;
- surviving `g=4`: `C>=18`,

this would imply `tau(Omega)>2k` on every remaining nonlopsided four-defect ray. Combined with the already closed lopsided ray, it would complete the four-defect regime eventually.

## Trust boundary

This file records exact finite evidence and a proposed proof mechanism only. The extension law has not yet been proved universally and is not used as a theorem in `CURRENT_STATE.md`. The order-12/32 `X_3` negative control lies outside this regime.
