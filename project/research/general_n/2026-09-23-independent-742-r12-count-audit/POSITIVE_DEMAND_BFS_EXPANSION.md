# BFS-validated high-load expansion, orders 17--22

23 September 2026. Status: **FINITE_INTERNAL_DIAGNOSTIC**.

Every one of 600 fresh greedy-deletion graphs was independently checked by BFS to have diameter two and to lose diameter at most two after every edge deletion. Balanced complete bipartite controls of both parities at orders 4--20 and X_3 (n=12,m=32) passed the same checker.

Across 848 maximum-degree roots and 41,353 legal selections, the run found 4,837 positive-demand and 112 high-load selections, but no positive-surplus selection and no selection satisfying the discrete exact plateau hypotheses. The strongest recorded demand example has n=22, a=12, b=9, S=5 and H0=4; it is still far from the plateau, with t=-49, selected mass Q=8 versus a^2/4=36, and a failed all-endpoint selected-degree floor.

Together with the smaller-order witness, this makes high-load/common-selected-source/high-codegree configurations genuine and fairly repeatable in actual D2C graphs. Therefore the next theorem cannot forbid that local configuration. It must exploit the asymptotic positive density forced by (PC4), positive surplus/near-extremality, or the simultaneous endpoint hypotheses. Zero positive-surplus observations are diagnostic only, never a nonrealizability theorem.

Selection spaces at most 256 were exhaustive; larger spaces used 48 deterministic samples and are labelled in the JSON.
