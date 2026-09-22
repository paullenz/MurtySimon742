# Local cycle hostile replay

22 September 2026. PASS at bounded internal-computation scope; not external verification or exhaustive graph enumeration.

The unchanged deterministic fixture suite contains 1,396 graph fixtures, 2,783 maximum-root cases and 68,741 legal selected assignments. It rechecked 39,846 edge deletions by independent BFS. Of the roots, 2,727 exhaust all legal selections under the configured limit and 56 are sampled.

New assertions passed:
- 704 assignments with 1<=r<=5 all have f<=r-1; 578 have nonempty F.
- all 68,741 assignments satisfy the S<=5 edge/equality conclusion; all 863 equality instances are zero-demand balanced complete bipartite controls.
- no unit-residual cycle component occurred in these actual maximum-root fixtures. The local-cycle lemma's exact nontrivial premise is therefore not directly exercised and retains a genuine non-vacuity caveat.
- the suite's observed demand reaches only S=5, so the separate S<=7 edge-bound statement is not tested at S=6 or S=7.

Exact output: LOCAL_CYCLE_RESULTS.json. Reproduce with check_local_cycle.py next to the inherited raw-profile wrappers and fixture files. Source SHA256: 170b2301c2a24165aee1878e3140886cefac983b70970d6c6b2069713d98a7e4. Fixture ledger SHA256: 74b2166c218867b5ccb6090846e813ac7cb4900f6c402817fd744bf9150e2b5b.

The computation confirms consistency and equality controls; it does not substitute for the proof of the local cycle lemma or prove graph realizability of abstract residual cores.
