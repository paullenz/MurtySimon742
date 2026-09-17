# Murty–Simon / Erdős #742 — live current state

> **Current review entry: [STRUCTURAL_REVIEW.md](STRUCTURAL_REVIEW.md).** The five-label exact block has D>=12. Scope work now has an exact excess-aware endpoint envelope and a certified empty near-Turan h=5 uniform band: once common-margin orientation is restored, the symmetric zero-excess demand-four obstruction disappears completely.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `INTERNAL_UNIFORM_H5_EMPTY_BAND_NOT_PROMOTED`.

**WORK MODE:** `MATH`. Completed a bounded abstract frontier census after the excess-aware theorem; no canonical survivor scan or workflow launch.

**INSPECTED PREDECESSOR:** `1bc7569712ad7441fbdf29ba9c3dfbfa43b209c8`, tree `6f152333933f1345503fb2f1f97a06701749d93e`, confirmed main before this transaction. Its excess-aware source envelope, preceding common-margin cut, scalar obstruction, staircase/heavy-load theory, five-label D>=12 theorem and canonical counts remain unchanged.

**LAST RESULT:** fix `a=20,b=23,t=2`, all twenty labels `s=x=4`, positive residual activity on all 23 B-sources, total residual count 76 and residual h-index exactly five. Allow every residual degree from 1 through the natural maximum a=20. There are exactly **127,885** residual-degree histograms satisfying those conditions. Independent Python/C++ enumerators apply the published exact restricted heavy-load capacity for every `h=1..4` and every integer cutoff `h<=T<=60`. Exactly one histogram survives this finite necessary subset:

`rho=(5^5,4^11,1^7)`.

Any profile satisfying the **full** heavy-load family must pass that finite subset and hence must equal this unique candidate. But the predecessor global endpoint-orientation theorem already excludes it by `2Q=160>149=sum B`. Therefore the intersection of this whole uniform h=5 band with the full heavy-load family and the common-margin cut is empty. Staircase and excess-aware cuts can only shrink it further and are not needed for this bounded conclusion.

**AUDIT:** `project/research/general_n/2026-09-17-h5-uniform-band-v1/` contains the proof, independent Python/C++ histogram enumerators and summary. Both enumerate 127885 histograms and return the same unique finite-heavy survivor count vector `(c1,...,c20)=(7,0,0,11,5,0,...,0)`.

**STEP-BACK CONSEQUENCE:** the next genuine non-square obstruction must change at least one frozen coordinate: demand distribution, selected excess, `(a,b,t)`, or residual h-index geometry. The symmetric all-demand-four zero-excess near-Turan band is closed at the aggregated bridge level. This is meaningful scope progress, but not graph-level exact-block coverage.

**FIVE-LABEL STATUS:** every actual whole exact block `|T|=|H|=5` still satisfies `D>=12`, hence `W>=37` or `W>=57` with extras.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. No canonical catalogue scan, q-enumeration or promotion.

**PRESERVATION:** empty-band package is in `project/research/general_n/2026-09-17-h5-uniform-band-v1/`; the excess-aware envelope is in `project/research/general_n/2026-09-17-excess-aware-endpoint-v1/`. All earlier proofs, counterexamples and failed routes remain preserved.

**UNPRESERVED WORK:** None for this bounded theorem/enumeration after remote confirmation.

**DEFERRED ADMIN:** older archive transfers, PR #2, unrelated CI/root historical narrative maintenance; external review, novelty and promotion.

**NEXT ACTION:** MATH: expand the empty-band census one coordinate at a time, starting with small positive selected excess and mixed demand 4/5 profiles at the same near-Turan `(a,b,t)` values. Retain the full excess-aware envelope. Preserve the first exact survivor as the next structural obstruction, or another certified empty sub-band. Do not jump to the canonical 952-state catalogue until the general obstruction is understood.
<!-- CURRENT-STATUS:END -->
