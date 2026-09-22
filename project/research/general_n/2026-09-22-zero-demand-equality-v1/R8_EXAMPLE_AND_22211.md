# Residual-mass-eight example probe and exact (2,2,2,1,1) closure

22 September 2026. Internal bounded computation. The example probe is not exhaustive outside the one partition explicitly closed.

## Example probe

probe_r8_examples.py applies an exact memoized source-state feasibility decision to every edge set retained under first_examples in R8_CORE_CENSUS.json: 27 labelled cores across the five surviving partitions. It uses exact residual column sums and selected-demand lower bounds, permits repeated physical-source states, and enforces the selected-neighbour injection.

Results:
- (3,2,1,1,1): 0/2 source-feasible;
- (3,1,1,1,1,1): 0/8;
- (2,2,2,1,1): 1/1;
- (2,2,1,1,1,1): 0/8;
- (2,1,1,1,1,1,1): 0/8.

Outside (2,2,2,1,1), these are only the first saved examples and prove nothing about unsampled labelled cores or degree signatures.

## Exact closure of (2,2,2,1,1)

The core census has exactly one labelled survivor for this partition: K5 minus the edge between the two unit-residual labels. Its degrees are (4,4,4,3,3), every label is in P, and every selected lower bound is two.

check_r8_22211_kernel.py exhausts its physical source states. Among 52 allowed active source patterns, exactly one unordered multiset realizes residual sums (2,2,2,1,1) and all selected demands:

(1,1,1,2,2),
(1,2,2,1,1),
(2,1,2,1,1),
(2,2,1,1,1).

The supplement forcing rule eliminates this unique population: at least one selected incidence has no active or universal B-source edge forcing exactly that incidence. There are no nontrivial residual-free states because P is the whole core.

Therefore the entire residual partition (2,2,2,1,1) cannot support r=8 strict surplus. Four partitions remain in the r=8 optimistic census. No S-bound or equality scope is extended by this unit.

The core census script now has an explicit --output mode; its mathematical enumeration is unchanged.
