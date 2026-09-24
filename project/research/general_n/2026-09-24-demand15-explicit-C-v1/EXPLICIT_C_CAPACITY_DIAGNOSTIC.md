# Explicit C-overlap/private-source capacity diagnostic

24 September 2026. Status: internal necessary-condition test only; not a graph-realizability theorem.

## Joint set-count model

For the demand-15/16 witness model, introduce an integer variable `c_K` for every nonempty label membership type `K`: `c_K` is the number of physical vertices of `B=N(v)` which belong to exactly the neighbourhood sets `C_i` with `i in K` among the active labels. Then

- `sum_{K: i in K} c_K = h_i` for every label `i`;
- `sum_K c_K <= Delta`;
- for a right-incidence label set `J` and `i in J`, the number of source vertices private to `i` relative to `J` is
  `P_i(J)=sum_{K: i in K, K cap (J\{i}) empty} c_K`.

The proved private-source capacity lemma therefore gives the valid joint constraint

    sum_z n_{J,z} <= (Delta-2) P_i(J)     for every i in J.

This links the witness-pattern multiplicities to one globally consistent family of actual `C_i` overlaps instead of allowing each pattern to consume an unrelated abstract source budget. It is stronger than the preceding source-union floor/right-vertex budget model, but is still only a necessary condition because it does not encode all graph adjacencies or exact degree-weighted source capacities.

## First exact test: five audited n=18, Delta=10, rho=2 survivors

A direct integer MILP reconstruction of the preceding v3 model plus the `c_K` variables and the coarse private-source capacities was solved on the five audited leading profiles. All five remain feasible and their minimum deficits are unchanged:

- `d=x=(8,7)`, `h=(8,7)`: minimum deficit 17;
- `d=(8,7), x=(8,8)`, `h=(8,9)`: minimum deficit 16;
- `d=x=(8,6,1)`, `h=(8,6,1)`: minimum deficit 17;
- `d=x=(8,5,2)`, `h=(8,5,2)`: minimum deficit 18;
- `d=x=(5,5,5)`, `h=(5,5,5)`: minimum deficit 16.

Representative feasible `C_i` membership decompositions returned by the model were:

- `(8,7)`: `c_{0}=3, c_{1}=2, c_{01}=5`;
- `(8,8)` on demands `(8,7)`: `c_{0}=1, c_{1}=2, c_{01}=7`;
- `(8,6,1)`: `c_{0}=3, c_{1}=2, c_{01}=4, c_{02}=1`;
- `(8,5,2)`: `c_{0}=4, c_{1}=1, c_{2}=1, c_{01}=3, c_{012}=1`;
- `(5,5,5)`: `c_{0}=3, c_{1}=1, c_{2}=1, c_{01}=1, c_{02}=1, c_{12}=3`.

## Consequence

The coarse explicit-overlap/private-source-capacity formulation is **not** the missing realizability obstruction: even after forcing a single globally consistent set system for the `C_i`, the leading dense abstract profiles survive at the same objective values. This is a useful negative result. The next bounded strengthening should therefore use the *exact degree-weighted* capacity `sum_{u in P_i(J)}(d(u)-2)` or directly encode source-to-endpoint incidence/degree consistency, rather than adding more scalar profile inequalities.

Balanced complete-bipartite equality controls and the `X_3` negative control are not altered by this diagnostic. General theorem and equality characterization remain open.
