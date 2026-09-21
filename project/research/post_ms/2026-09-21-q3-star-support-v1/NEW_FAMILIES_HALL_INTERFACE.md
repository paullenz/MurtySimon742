# Actual star families versus the rigid Hall interface

21 September 2026. Independent graph-level diagnostic, not rigid-branch closure.

The new five-coordinate and six-coordinate constructions were passed through the pre-existing 19 September graph-level verifier, using every maximum-degree root and all three certificate policies. Parameters (r,q) were (1,0),(1,1),(2,2),(4,4),(8,8) for each family. X_3 was included as the mandatory negative control.

All 108 root-policy runs pass. However, all 105 runs from the new star fixtures have p=0: there are no tight rooted pairs at their maximum-degree roots. Only the three X_3 runs qualify for the nonnegative-lambda matched-pair package. These provide 18 Hall-cut checks and zero rigid cuts. The new graphs therefore expand raw actual-graph coverage but do not expand positive coverage of the rigid Hall branch or prove its source premises.

This distinction matters because their original Q3 construction root has four antipodal pairs, but is not a maximum-degree root and has lambda=7-a<0. Relabelling it as a qualifying rigid root would violate the package hypotheses.

The result steers the next work toward a structural explanation of the p=0 maximum-root obstruction, or genuinely new realized roots, rather than presenting the new examples as evidence for the conditional capacity theorem.

Reproduce with `python check_new_families_hall_interface.py` (networkx required). The wrapper imports the existing independent graph checker, reconstructs actual edge sets, checks D2C directly, then extracts rooted data and runs the verifier. Full parameters and counts are in `NEW_FAMILIES_HALL_INTERFACE_RESULTS.json`.
