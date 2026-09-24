# Saturated (5,5,5) root-charge screen

24 September 2026. Status: exact finite necessary-condition classification for the fixed n=18, Delta=10 saturated `(5,5,5)` profile. This is not a new D2C exclusion; the separately audited staged SAT result remains the graph-level exclusion.

The saturated membership-step lemma leaves exactly five labelled membership-count vectors `(c_empty,c_0,c_1,c_01,c_2,c_02,c_12,c_012)`:

    (0,2,2,1,2,1,1,1)
    (1,1,1,2,2,1,1,1)
    (1,1,2,1,1,2,1,1)
    (1,2,1,1,1,1,2,1)
    (2,1,1,1,1,1,1,2).

The checker exhausts every one-use Boolean-step physical-source assignment compatible with the unique-common-neighbour nonedges. There is one valid forced skeleton for the first vector and eight for each of the other four.

It then applies the proved root-edge certificate dichotomy to the forced B-skeleton. A B-witness is allowed only when the endpoint types are disjoint and their forced B-neighbourhoods are disjoint. Reused B-witnesses pay the exact forced-neighbour union charge; otherwise a distinct inactive singleton A-witness pays `rho+1+r_t`. At most four singleton witnesses are available.

Result:

- the first vector forces exactly one singleton witness, at the top-type vertex, with visible charge three;
- each of the other four vectors routes every root edge through B-witnesses with zero forced-union deficit at this abstraction level.

Thus the new root-edge charge is genuine but does **not** independently reprove the `(5,5,5)` exclusion. The four zero-charge negative controls show exactly why: the empty/top layers can witness each other while singleton/pair layers provide disjoint forced neighbourhoods. Any theorem-facing strengthening must encode additional non-witness adjacencies, A-side common-neighbour restrictions, or full D2C constraints; merely adding the root-certificate disjunction to the forced Boolean-step skeleton is insufficient.

Reproduction:

    python classify_saturated_555_root_charge.py
