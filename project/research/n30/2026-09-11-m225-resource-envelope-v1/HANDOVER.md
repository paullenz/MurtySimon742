# Four-envelope endpoint continuation: provenance and handover

11 September 2026. Paul requested further continuation after confirming that N29 reviewer-v4 is the candidate hand proof. Work resumed from a clean local checkout and verified remote main at `34763cb17ce554a27e57643cfb8e74882e66fc86` in `paullenz/MurtySimon742`.

The visible prior-turn checkpoint and its saved handover supplied the complete starting state; no new personal-context search or sub-agent delegation was needed. Existing standing orders on preservation, candidate status, current reviewer links and completed non-forced GitHub publication continue to apply.

## Starting problem

The earlier scalar-excess checkpoint excluded 57 of 207 positive ledger-tight N30/m225 rows, leaving 150 positive rows to simplify. Four zero-demand tight rows had separate exact Hall/Farkas certificates. All 211 tight rows were already excluded by the existing more complex candidate proof; they were not unresolved cases of that proof.

The objective here was to replace the older endpoint machinery with a smaller transparent certificate family. The 100-profile demand classification was explicitly retained as an input.

## Discovery sequence and retained unsuccessful work

1. `mine_resource_envelope.py` tested a simple aggregate residual-plus-excess bound on the 150 rows. On a selected incidence, `R+e>=q+p-rho` and `e>=max(0,p-rho+1)`. The test combined clipped costs from those inequalities with supplement Hall tails. It produced **zero new positive exact reconstructed gaps**. The best proposed float bound was approximately `-0.1743119`; that numerical optimum is not claimed as a proof that the architecture can never work. Full records are in `SIMPLE_RESOURCE_DISCOVERY.json`.

2. `mine_joint_potential.py` retained actual `(R,x)` label states, the exact residual-column budget and the product-order source/label constraints. It used the conservative `d_F<=12` box and the pointwise label cap `x<=#{rho>=s}`. A nine-generator dictionary produced positive exact reconstructed gaps on **121/150** rows. The useful generators in those positive results reduced to `s*v` and the three thresholds `E_0,E_1,E_2`. The other proposed generator types remained unused. Records: `JOINT_SMALL_DMAX12_DISCOVERY.json`.

3. Adding monotone `(d,v)` rectangles and the already-established first-coordinate threshold produced exact reconstructed positives on all remaining **29/29** rows. Records: `JOINT_RECTANGLES_DMAX12_DISCOVERY.json`. This was proposal generation, not final acceptance.

4. `compress_joint_cover.py` evaluated every proposed integer-scaled formula on every row before selecting a deterministic greedy cover. This gave four formulas for the 121-row group and three for the 29-row group. `simplify_joint_templates.py` then found small integer coefficients. Two MILP calls stopped at their configured time limit with incumbents; those incumbents were accepted only after independent exact envelope evaluation. No optimizer optimality or minimal-template claim is made.

5. A fresh standard-library checker applied those seven formulas to the **entire 211-row tight frontier**, rather than only the original 150-row target. It covered 210 rows, including all four zero-demand rows. The original certificate and audit are retained as `JOINT_CERTIFICATES_SEVEN_INITIAL.json`, `EXACT_AUDIT_SEVEN_INITIAL.json` and `EXACT_APPENDIX_SEVEN_INITIAL.md`. That audit was explicitly PARTIAL, not complete endpoint evidence. A later acceptance guard makes incomplete coverage return a nonzero exit code by default.

6. Exact cross-coverage showed that the three rectangle formulas B1/B2/B3 alone cover the same 210 rows, assigned as `195+13+2`. The remaining row, `s=(2,5^12),rho=(1^4,2,4,5^10)`, was previously covered by the older scalar test. A one-row probe found that `Phi=s*v` alone suffices with suitable resource coefficients. The simplified C1 certificate has `lambda=25,c=28,tau_2=22,tau_4=6` and exact gap two. The proposal and simplified result are preserved in the two `ONE_OLD_SCALAR_ROW_*.json` files.

7. The final **four-formula** file is `JOINT_CERTIFICATES.json`. The independent checker recomputed all four templates on all 211 rows and returned PASS, with minimum assigned gap one. All source and label minima were checked both by full integer-state traversal and by the written endpoint reductions.

## Final validation and trust boundary

`EXACT_AUDIT.json` records 211/211 exclusions, 12,772 direct state checks, 8,069 endpoint checks and 37,128 coordinatewise monotonicity comparisons. It imports no discovery code and uses no floating point or solver.

`audit_acceptance_boundaries.py` confirms that an incomplete cover and a negative potential coefficient are rejected. It also preserves an allowed domain-corner witness with `p=rho+2` whose minimum would be changed by the invalid `p<=rho+1` tightening. This checks the relevant acceptance boundary rather than asserting an actual graph with those parameters exists.

The written proof is an application of the existing three-coordinate incidence lemma with an explicitly justified **individual label-capacity bound**. It uses no new graph assumption or stronger isolated-C degree cutoff. It remains candidate mathematics until independently reviewed; same-assistant separate code is internal corroboration, not external independence.

The exact completeness of the **100 `Q>=18` demand profiles remains a proof premise**. This continuation verifies their scores, reconstructs their tail rows, and supplies finite endpoint certificates. It does not claim a hand proof of their completeness, an unrestricted Murty-Simon result, a minimality theorem for four templates, or any governed ledger promotion.

## New effective frontier

There are no remaining rows requiring the older final endpoint LP/Farkas models *within this supplementary derivation*, conditional on the preserved 100-profile classification and bridge. The earlier 150-row list remains historical evidence, not the current simplification frontier.

The next mathematical task is therefore a **hand classification of the 100 demand profiles**, using the existing monotone-clipping argument, tail-capacity thresholds and low-dimensional preimage analysis. After that, audit the complete N30 assembly before deciding whether its current reviewer-v2 should be superseded by a new edition. N30/Delta17 has separate finite pieces that must also be accounted for; completing Delta16 alone would not establish that the entire N30 paper is computation-free.

## Reproduction commands and environment

The acceptance route needs only Python's standard library:

```sh
python -I -B project/research/n30/2026-09-11-m225-resource-envelope-v1/verify_joint_certificates.py
python -I -B project/research/n30/2026-09-11-m225-resource-envelope-v1/audit_acceptance_boundaries.py
```

Discovery used Python 3.12.14 and SciPy 1.17.0. The programs and exact JSON inputs/outputs are preserved. The principal discovery commands were:

```sh
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/mine_resource_envelope.py
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/mine_joint_potential.py
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/mine_joint_potential.py --rectangles --only-unresolved
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/compress_joint_cover.py
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/compress_joint_cover.py --input project/research/n30/2026-09-11-m225-resource-envelope-v1/JOINT_RECTANGLES_DMAX12_DISCOVERY.json --output project/research/n30/2026-09-11-m225-resource-envelope-v1/JOINT_RECTANGLES_INTEGER_COVER.json
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/simplify_joint_templates.py --kind SMALL
python -B project/research/n30/2026-09-11-m225-resource-envelope-v1/simplify_joint_templates.py --kind RECTANGLES
```

Discovery may return different valid incumbent weights on a different solver build. Final acceptance is reproducible from the small preserved integer certificate file and does not require discovery to return identical weights.
