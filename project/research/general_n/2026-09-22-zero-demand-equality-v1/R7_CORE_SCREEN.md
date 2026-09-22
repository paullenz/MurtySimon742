# Residual-mass-seven optimistic strict-surplus core screen

22 September 2026. Exact enumeration of a necessary relaxation; survivors are not graph realizations.

screen_r7_core.py repeats the declared r=6 core method at total residual mass seven. It enumerates all integer partitions and all simple positive-support core graphs, applies edge charge, the selected-source capacity inequality, the exact P/N core ledger, and optimistic minimum N-slack. The all-unit partition is excluded directly by the proved unit-column theorem.

Only three residual partitions retain optimistic strict-surplus cores:
- (3,1,1,1,1): 3 labelled survivors, one orbit;
- (2,2,1,1,1): 13 labelled survivors, four orbits;
- (2,1,1,1,1,1): 605 labelled survivors, ten orbits.

All other partitions have zero survivors. Thus any actual r=7 strict counterexample must map into one of 15 explicitly saved core orbits. Most representatives have t_upper=1; the exact JSON retains degrees, P/N sets, selected lower bounds and the occasional t_upper=2 case.

The relaxation is optimistic: it can suppress N-slack by hypothetical zero-residual attachments and does not impose source identities, supplements, deletion criticality, maximum-root realization or a full graph. No survivor is evidence of a D2C graph.

Exact output: R7_CORE_SCREEN.json. Next: impose exact residual source-state multisets on the 15 orbits, then the supplement forcing rule that closed r=6.
