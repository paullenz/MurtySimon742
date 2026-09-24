# Common-C exclusion and the exact scope of the (5,5,5) transfer

> **Later resolution, linked 24 September:** [STAR5_EXACT_SLACK_AND_555_CLOSURE.md](STAR5_EXACT_SLACK_AND_555_CLOSURE.md) excludes the complete (5,5,5) tuple without common-C assumptions. The scope warning below remains correct for the older transfer proof; the old index 20,851 identity discrepancy remains historical metadata, not repaired evidence.


24 September 2026. Status: internal graph-interface proof plus a trust-boundary correction. It does not close every abstract realization of the tuple `d=x=h=(5,5,5)`.

## Direct exclusion of the recorded common-witness geometry

The first strengthened n=18 survivor recorded three labels with the same five right endpoints `T`. Since `x_i=h_i=5`, saturation gives

    T_i = B minus C_i,

so common `T_i=T` forces a common five-set `C_i=C=B\T`.

This geometry is already impossible at the exact-H assigned-edge interface, without invoking the later full D2C SAT model. Fix `t in T` and two labels `i,j`. Their assigned incidences require distinct physical edges `u_i t` and `u_j t`, because every physical edge is assigned to at most one label. Both sources lie in the common set `C`. Hence both `u_i` and `u_j` are neighbours of each of `i,j` and of `t`. The pair `(i,t)` therefore has at least two common neighbours, contradicting that its assigned certificate source is unique.

Equivalently, the newer private-source antichain lemma says that labels sharing an assigned endpoint must have incomparable `C`-sets; equality `C_i=C_j` is forbidden.

Thus the **specific recorded survivor with five copies of the common right type `{0,1,2}` is excluded directly** by exact physical-edge one-use and unique-common-neighbour geometry. The staged 18-vertex SAT exclusion is a stronger independent negative control but is not needed for that fixed common-C case.

## Tuple-only transfer is not established by this argument

The bare tuple

    d=(5,5,5),  x=(5,5,5),  h=(5,5,5)

does not by itself force common `T_i` or common `C_i`. The exact saturated-membership classification in `SATURATED_555_ROOT_CHARGE_SCREEN.md` has five alternative membership-count vectors satisfying the Boolean-step/one-use necessary conditions. Therefore a reference to the tuple alone cannot silently import the common-C block geometry.

This narrows the valid interpretation of `STABLE_20851_REALIZABILITY_TRANSFER.md`: its graph-level transfer is sound only if the stable-index survivor includes, or a separate equality lemma forces, the same common-right-type geometry. The presently fetched `N18_STABLE_20851.json` in fact reports `abstract_survivor_count: 0` and a different closest tuple, while the transfer prose says that the index has a unique `(5,5,5)` survivor. That durable-source discrepancy is recorded here rather than resolved by guessing or rewriting history.

## Exact next question

Determine from the canonical stable-index generator/output whether deficit-budget equality forces five common right types. If it does, cite and prove that equality step and use the one-paragraph private-source contradiction above. If it does not, the tuple-only transfer must remain unverified and the five alternative saturated membership geometries require their own graph-realizability test.
