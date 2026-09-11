# Editorial and dependency review for N30 reviewer-v3

11 September 2026. Internal review by ChatGPT/Geeps; not an independent specialist review.

The edition assembles the proof preserved at `01d1fb03d5b68ea4494a4ff29cedd0b49cb5dc16` and its input dependencies. The publication baseline is `81f37b80f643dd12f371680e673a95f6de793df2`. The mathematical statement is unchanged. No original mathematical source, certificate, earlier reviewer PDF or governed ledger is edited.

## Full inclusion and transformation record

| Manuscript component | Preserved source | Editorial treatment |
|---|---|---|
| Main proof, Sections 1-8 | ASSEMBLED_PROOF.md | Full degree assembly; replace pre-edition status prose and dependency links with included appendices |
| Appendix A | CANONICAL_BRIDGE.md, Sections 1-9 and 11 | Include all needed proofs; omit unused charging, isolated-C and h-index corollaries; qualify section references |
| Appendix B | TWELVE_LABEL_TRANSFER.md, Sections 1-5 | Include complete unbounded-threshold proof and transfer; omit duplicate N30 consequences already in main proof |
| Appendix C | HAND_CLASSIFICATION.md, Sections 1-6 | Include full classification, including zeros and ones; remove historical open-task framing |
| Appendix D | PREIMAGE_ARITHMETIC.md | Include every five- and six-lift interval unchanged except dash typography |
| Appendix E | Threshold-slack reduction and assembly | Consolidate both t=1 and t=2; state monotonicity, exact reconstruction and positive-demand argument explicitly |
| Appendix F | N30_M226_HAND_ENDPOINT_REDUCTION.md, Sections 2-5 | Include all eight source inequalities and minima; omit the earlier imprecise positivity sentence from its Section 1 |
| Appendix G | FOUR_ENVELOPE_REDUCTION.md, Sections 1-7 | Include all domains, potentials, coefficients, resource signs and minimum endpoint formulas; move replay narrative to companion |
| Appendix H | EXACT_APPENDIX.md | Include all 211 rows, every assigned minimum and gap; landscape layout |

SOURCE_MAP.json records exact paths and hashes. The build script spells out every selection and replacement. It fails if an expected source passage is absent, so source drift is not silently ignored.

## Clarifications checked

- The source-degree identity includes selected cross-edges: `(rho+q)+(b-1-q-p)=rho+b-1-p`. The valid source bound is `p<=rho+2` at `(a,b)=(13,16)`.
- In `uj->z`, z is the unique exception. Both endpoints of the forced edge `iz` miss the A-vertex j, which is why that edge is residual.
- Positive demands imply `s_i=d_i-R_i` without a tightness assumption. At zero demand, equality of the total sums supplies the needed pointwise equality for the envelope argument.
- The twelve-label inverse gamma has no upper source cutoff. Padding by zeros preserves the score and covers every `1<=a<=12`.
- Residual threshold lower bounds need not themselves be monotone. The reconstruction imposes monotonicity on actual residual tails, includes the level-13 tail, and counts ledger slack separately.
- All positive-slack t=1 rows have positive demands: the four profiles containing zero all have Q=18 and thus no available slack. This is now explained directly from the hand table.
- The 272-row count is not asserted to prove completeness by itself. The reconstruction rule and the full 211-row tight list remain explicit proof obligations.
- Finite tables stay inside the manuscript. The full-domain regressions and old LP/Farkas systems remain corroboration only.
- Appendix-local section references and mathematical equation tags are qualified to prevent ambiguous cross-references after consolidation. Histogram and scoped notation conventions are stated at the beginning.
- The renderer disables Markdown's paired-caret superscript extension. Plain histogram cells such as `(1^7,2,3^8)` therefore retain literal multiplicity notation rather than accidentally treating everything between two carets as one exponent. Actual TeX mathematics is unaffected. The source PDF strings are checked against all 211 histogram pairs.
- The elementary Delta=15 argument concerns every edge deletion and every originally adjacent or nonadjacent pair, so it does not rely on an external dominating-edge theorem.

## Review boundary

No blocking flaw was found in the preceding full assembly audit. This turn's work is an editorial consolidation and packaging check; it does not represent a fresh externally independent mathematical audit. The manuscript, tables, companion, ZIP, current navigation and publication hashes are checked as a whole. Internal exact checking remains REPRODUCED, and independent specialist review remains OPEN.
