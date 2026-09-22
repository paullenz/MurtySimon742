# Equality-source obstruction and remaining leaf cores

22 September 2026. Internal follow-on to CORE_REGRESSION.md, not a full equality theorem.

## Diamond survivor fails legal supplements

The heavy-degree-three diamond has exactly one necessary source multiset under the saved finite kernel:
u=(1,2,1,1), w=(2,1,1,2), z=(2,1,2,1).
All three sources miss all four residual-support labels C. Any other B-source must be adjacent to every C-label, since the multiset exhausts both selected and residual crosspairs there (residual-free nonzero selected patterns are impossible in this connected diamond, as explained in the kernel report).

For any of u,w,z and any selected C-label, a B-supplement cannot be one of the other two active sources, which miss the whole of C. All remaining B-vertices are adjacent to every C-label. Thus every selected label at a fixed source has exactly the same set of possible B-common neighbors. Since the source is selected at at least two labels, uniqueness would force both labels to use the same supplement. The selected-triple injection forbids this. The finite-kernel survivor therefore cannot realize a legal assignment.

This combines an exhaustive finite necessary-pattern computation with a direct supplement contradiction; external review of the reduction remains open. The heavy-degree-two diamond already has zero pattern survivors.

## Remaining leaf shapes are not solved by scalar source patterns

leaf_source_kernel.py extends the same necessary-pattern calculation to the two remaining r=5 equality core shapes. It permits repeated source states and exact residual column sums, and requires the selected-neighbor injection at every selected label. Residual-free nonzero selected patterns are excluded because selected labels would be neighborhood-closed: neither the unit triangle nor a heavy star containing a zero-residual leaf can be wholly selected.

Results:
- Triangle with one heavy-center link and one zero-residual leaf: 71 candidate single-source patterns; six surviving multisets.
- Triangle disjoint from the two-leaf heavy star: 195 candidate patterns; 332 surviving multisets.

Patterns involving a positive residual at a zero-residual column never enter a surviving multiset; candidate pattern counts include these unused possibilities. These counts are not graph counts. B-edges, legal supplements and actual criticality are not checked by this kernel. Only the first five survivors per shape are printed; counts enumerate all.

A promising proof route for the disjoint triangle is to localize the unit-column cycle argument to that F-component: its selected sources lie among its three residual sources, and b>=a+1 guarantees a common B-neighbor outside those sources when t=0. The component's three edges then require all three residual witnesses. The cycle contradiction should apply locally, but this localization is a next-action candidate, NOT yet promoted to a new theorem in this checkpoint.

Next exact work: independently audit the localized triangle proof and the finite-kernel supplement exclusions below, then test actual D2C realizability. Do not equate pattern survival with graph existence.

## Final in-slot supplement check of the six one-link survivors

The script now asserts on ALL six one-link populations that every active source misses triangle label 1 and that some source is selected at label 1 and at another modeled label. All unlisted B-sources are adjacent to every modeled label (residual-free selected states were excluded). A legal supplement at label 1 must therefore be an unlisted source. That same B-neighbor is also common with the other selected label at this source, forcing the same supplement twice or violating uniqueness. Thus none of the six source populations admits legal supplements.

This is a finite-kernel-plus-direct-contradiction result, not an independent all-graph search. The disjoint-triangle component localization remains an unpromoted proof obligation. The public S<=7 bound / S<=4 equality statement is unchanged. The saved output now prints up to SIX survivors, so the preceding reference to five is superseded.

