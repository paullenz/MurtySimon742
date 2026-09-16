# Bounded coverage/input diagnostic: scalar witnesses and a projected endpoint obstruction

16 September 2026. Research directed by Paul Lenz; internal diagnostic and conditional derivation by ChatGPT/Geeps.

**Status: INTERNAL_CONDITIONAL_CERTIFICATES_NOT_PROMOTED.** One bounded diagnostic following `a5cf0b19359e357010f0c0167321a6854e964fa2` in `paullenz/MurtySimon742`. This is not a full 952-state coverage census, an old-pipeline replay, a new graph realization, a promotion, or independent acceptance. Its mathematical corollary uses the existing canonical bridge and endpoint-cap proof. External specialist review and novelty assessment remain OPEN.

## 1. What was inspected

The current handoff requested a small named sample to establish whether the new profile-defect envelope has the data it needs. The sample is the first three complete records of

`project/research/general_n/2026-09-15-saturated-receiver-barrier-v1/RESCUE_PROFILES.json`

at the inspected immutable head: state IDs **232, 978, 979**, all in namespace **n34-m289**. The Git blob is `3d683af1884e9b9e6974b69553a5d1246f25f259`. The normalized sample was extracted from connector lines 1–193 and is preserved as `SAMPLE_PROFILES.json`. It is not claimed byte-identical to a slice of the original pretty-printed file. No numerical whole-file digest comparison was performed.

The associated `CERTIFIED_RESCUES.tsv` stores only layer, state ID, witness_q and provenance source. The frozen-state parser in `prepare_scan.py` reads layer, state ID, a, b, t, the s array and the rho array. It then combines them with a q vector. The word “witness” here refers to survival of older necessary-condition screens, not to an original graph or to fully specified selected/residual label sets. The historical package reports old acceptance; that pipeline was NOT rerun in this unit, and historical workflow observations were not treated as current job status.

## 2. Exact input finding

Each sampled JSON record has exactly these keys:

    layer, state_id, a, b, t, s, rho, q.

It supplies labelled positions for demands and source degrees, but not F adjacency, all source selected sets S_u, residual label sets R_u, or destinations of selected obligations. It does not even supply the individual label residual degrees R_i from which F degrees could be recovered by a positive-demand identity.

In particular, s_i is NOT deg_F(i), and q_u is the CARDINALITY of S_u, not the list of labels selected at u. Substituting either would manufacture data. The new load matrix

    n_(u,j) = number of monitored selected labels i at u with j in N_F(i)

cannot be constructed from these fields alone. Nor does the file furnish a useful core C or a certified bound on sum_U |R_u minus C|. A conservative destination superset could be all B with ceilings rho_v+b-a-1, but that does not restore the missing adjacency and incidence information.

Some incidences ARE forced. If q_u equals the number of labels eligible at rho_u, all those eligible labels are selected at u. For states 978 and 979, sources 2–7 select {0}, and source 8 selects {0,1,2}; indices are zero-based. Their exact d=4 block additionally forces labels 11–14 selected at high sources 14–17, independently of q. These partial facts do not determine the full sets or F. State 232 has no saturated-source identity of the first kind and no exact block of the tested kind.

**Diagnostic conclusion:** the general Psi(D) certificate is not directly evaluable on any of the three raw records. This is a specific input limitation of the sampled file and parser, not a claim that no other repository artifact contains richer data.

## 3. A smaller projection is sufficient for two sample states

Missing full identities does not mean all structural conclusions are inaccessible. The existing endpoint cap gives a useful identity-free corollary.

Use the full canonical selected representative system, and let

    s_i=max(0,deg_F(i)-R_i),
    T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d>=2.

Let K be the F-neighbours of T outside T. The existing cap proves

    k in K implies s_k <= d-2.                            (C1)

Therefore |K| is at most the number of labels whose demand is at most d-2. On the other hand,

    |K| >= d.                                            (C2)

Here is a direct proof of (C2), requiring no missing F data to be guessed. Every tight label has demand d and exactly d eligible sources, so it is selected at every high source. Fix one high source u. Its d tight selected labels have d DISTINCT destinations. The destination of label t is not high because every high vertex contains t. It must contain every other tight label by forward containment. Since it is low, none of those other tight labels is selected there; its residual set is exactly T minus {t}.

For any fixed tight label t, the other d-1 destinations thus provide d-1 distinct residual occurrences of t. Consequently R_t>=d-1 and

    deg_F(t)=d+R_t>=2d-1.

All its F-neighbours belong to the other d-1 tight labels or K, so deg_F(t)<=d-1+|K|. Hence |K|>=d.

Combining (C1) and (C2) gives the scalar necessary condition

    |{i:s_i<=d-2}| >= d                                  (C3)

whenever the exact d-by-d tight-block hypotheses hold. This combines already-proved graph constraints; no new novelty claim is made for the counting principle. The local proof does not need positive surplus, extra high selections E>0, an equality value of Omega, a particular q, or an original-graph enumeration.

For clarity, (C1) uses forced residual presence at every high source and the canonical endpoint bound. A selected K-label has both endpoints low, whence deg_F(k)<=2d-2, while R_k>=d. If it is unselected, its demand is zero. The degree bound is not asserted for arbitrary unselected K-labels.

The word “exact” matters: applying (C3) to a chosen subset of a larger demand level or a different number of high sources is not justified by this proof.

## 4. Worked sample certificates

| State | Demand histogram | Residual-degree histogram | Exact block | Result of (C3) |
|---|---|---|---|---|
| 232 | 0:1, 1:2, 3:12 | 1:9, 3:9 | None | Not excluded by this screen |
| 978 | 1:1, 2:2, 3:8, 4:4 | 1:8, 2:1, 3:5, 4:3, 6:1 | d=4 | Needs at least 4 low-demand labels; has 3 |
| 979 | 1:1, 2:2, 3:8, 4:4 | 1:8, 2:1, 3:5, 4:2, 5:2 | d=4 | Needs at least 4 low-demand labels; has 3 |

For either rejected record, T={11,12,13,14} and H={14,15,16,17}. The only permissible K-labels are {0,1,2}. Each tight label must have F-degree at least 7 but can have at most three other tight neighbours plus these three low-demand neighbours, giving degree at most 6. Thus **7<=6** would be required.

This is independent of the saved q vector. Changing q while keeping the state's exact s and rho does not repair the contradiction. Conditional on the canonical interpretation of those state arrays, it is therefore a whole-scalar-state obstruction, not merely a rejection of one saved q witness. It does not establish an unconditional graph theorem independently of the inherited bridge.

The sample is deliberately tiny. “Two out of three” is not an estimated fraction of the full survivor catalogue and must not be reported as such. State 232's non-rejection is retained; it is neither a realized graph nor certified to survive every newer theorem.

## 5. Equality-versus-counterexample scope

All three records have a=15, b=18 and t=1. Therefore

    n=34,
    e(G)=b(a+1)+t=18*16+1=289=floor(34^2/4).

They are **equality-layer records**, not above-bound counterexamples. The pivot-dependent gap is floor((b-a-1)^2/4)=1; an above-bound counterexample at this a,b would require t>=2. Positive pivot surplus t=1 does not mean the conjectured upper bound is violated.

The scalar obstruction is still relevant to these retained equality profiles, and its proof does not need positive surplus. No new graph order is claimed solved. Existing fixed-order packages and their external-review boundaries remain unchanged.

## 6. Executed checks, not an inflated replay claim

Run `python3 check_diagnostic.py` beside `verify_screen.cpp` and `SAMPLE_PROFILES.json`. Python identifies exact label/source sets; C++ independently computes histograms and compares the tight-degree lower/upper bounds. They agree on every one of **seven level decisions across the three sampled records**, including both certificates and every non-applicable level. Five synthetic controls test the boundary count, missing high-source hypothesis, wrong demand-level size, and the need for the d-2 cutoff. These controls are arrays, not canonical graphs.

The Python driver also validates array lengths and nonnegativity, elementary q eligibility/source bounds, edge-layer arithmetic and forced saturated selections. It writes the full result, not only its pass/fail summary. The original result bytes are also preserved in CHECK_RESULTS.json.gz.b64; unpack_results.py decodes them and checks their SHA256 without recomputing decisions. It does not rerun the old relational or forced-core acceptance pipeline.

The optional `--repo-root` argument compares the three normalized records to a locally mounted complete source file. That option was NOT run here: the original sample was obtained using the connector, not by downloading a full repository. Sample provenance and the immutable source blob are recorded. Both new programs are by the same assistant; there is no independent expert verification claim.

The latest Psi theorem was NOT numerically applied, because its missing inputs were not invented. The two certificates instead use the proven scalar consequence (C3).

## 7. What to do next

The next bounded step should apply (C3) to the remaining **124-record rescue-profile file** before building a general graph-lifting system. Its needed fields are already present. Reconcile the flagged keys against earlier strict/equality certificates, the audited forced-core candidates and any later witness replacements. Distinguish genuinely additional state keys from overlap; publish a proposed certificate list and keep promotion separate. This is a cheap scalar screen, not a new q enumeration and not a full 952-state census.

Retain state 232 as a named non-rejection for the next information-rich test. A subsequent Psi application must either construct/verify actual F,S,R data for a permitted candidate or prove sufficient constraints common to all their possible completions. A successful arbitrary completion is a witness only; failure of one completion is not a whole-state exclusion. No completion is constructed in this diagnostic.

Canonical totals remain **4,626 exclusions / 952 survivors / 3,632 whole-state closures**. The 41 strict/equality certificates and 170-candidate audit keep their existing unpromoted status. Whether IDs 978 and 979 overlap any already-recorded candidate exclusions has NOT been checked, so no new aggregate exclusion or projected survivor total is reported. State 3349's open enumeration and all prior pending evidence transfers remain unchanged.

## 8. Immutable source record

All repository reads were at `a5cf0b19359e357010f0c0167321a6854e964fa2` except the initial main read, which resolved to that head.

- Current handoff: blob `90132079b72b9f64c92d8554a933f0eb470b5cc2`; contains the complete preceding profile-defect proof. Preserve it intact by archive or immutable reference when replacing the live handoff.
- `AGENTS.md`: blob `9c5a6f2ac1e36ddc7416a57b6fcc2287600af2c8`.
- `2026-09-15-forced-core-canonical-audit-v1/README.md`: `58b05bac8c53d90283a9a28a51c301347702e4db`.
- That package's `CERTIFIED_RESCUES.tsv`: `5bd64a7ae005735e3234150ccbd6fb776cb4217d` (opening rows inspected).
- `2026-09-15-forced-core-canonical-scan-v1/prepare_scan.py`: `197baa4d7858c0f99da35456150267dfd3c040a6`.
- `2026-09-15-saturated-receiver-barrier-v1/README.md`: `a6b3cf429fd1405834117b2c527b354d3f2f0f54`.
- Its `RESCUE_PROFILES.json`: `3d683af1884e9b9e6974b69553a5d1246f25f259`, first three complete records inspected.
- `2026-09-16-residual-endpoint-cap-v1/PROOF.md`: `9ca15674830462a1ae28fd3acf55dd824a41900f`, Sections 1–3 re-read at point of use.

The research directories above are under `project/research/general_n/`. No external literature claim, workflow status update or platform diagnosis is part of this diagnostic.
