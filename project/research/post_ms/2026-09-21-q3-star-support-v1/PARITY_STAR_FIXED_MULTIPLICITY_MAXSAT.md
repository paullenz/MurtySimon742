# Exact fixed-multiplicity parity-star optimization

21 September 2026. Finite diagnostic only; external review open.

Fix one copy of every coordinate code and two copies of each of the four even star codes. For the seven parameter pairs

    (r,q)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),

an exact weighted MaxSAT encoding maximized all physical A-edges subject to diameter two and deletion-criticality of every fixed and optional edge. In every case the optimum is

    e(A)=rq+14.

Thus the parity-star interface is realizable throughout this tested rectangle, but it gives no increase over the complete `rq` parity term after its fixed 14-edge overhead. The equality is exact for the listed multisets, with full models and solver statistics in `PARITY_STAR_MAXSAT_GRID.json`; it is not promoted to an arbitrary-multiplicity theorem.

This materially changes the next proof target. The broad question “can parity-star incidence exist?” is closed positively. The useful target is the structural inequality `e(A)<=rq+14` for this eight-star slice, followed by identifying which raw criticality charges make every missing parity edge pay for any extra parity-star incidence. The existing general ledger gives only `e(A)<=rq+M+14-I`, so the missing step is precisely cancellation of `M-I` on this fixed support.

The independent verifier in `maxsat_fixed_codes.py` rebuilds each returned graph and checks diameter two and every edge deletion directly. The computation is diagnostic support for a proposed lemma, not a substitute for proof.
