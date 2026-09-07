# Red-team audit of the direct order-28 candidate

**7 September 2026 — internal adversarial review, not independent expert certification.**  
Research directed by Paul Lenz. Audit, new tests and additional checker written by ChatGPT/Geeps.

## Executive conclusion

**No blocking mathematical, domain-coverage or certificate-arithmetic defect was found in the direct order-28 route examined in this audit.** The original v3–v8 numerical checking sequence was replayed, the equality-stage handoffs were compared byte-for-byte, and a new integer-accumulation kernel verified all 8,983 final certificate leaves across v6, LocalIncidence-v7 and direct197-v8. The order-28 statement remains a **complete candidate argument awaiting independent mathematical review**, not an externally certified theorem.

One reproducible **non-blocking input-validation defect** was found in v8's standalone C++ residual enumerator. An unsupported residual interval can be accepted with a successful empty report. The complete proof driver validates the exact permitted domain and input file before invoking that helper, so this does not affect any admitted proof input or recorded exclusion. An additive guard patch was tested on the entire valid 197-edge residual domain: all counts, survivor bytes and per-demand band bytes remain identical. Four malformed-input controls are rejected by the hardened copy. The frozen original source and archives were not edited.

The previously missing v6, LocalIncidence-v7 and v8 archives were located, matched to the original hashes and relocated unchanged in GitHub. The root README now begins with n=25, followed by n=27 and n=28, then general research, evidence and governance. Preservation is no longer the missing step for these three checkpoints.

## 1. Scope and immutable inputs

The principal target is the **direct** chain proposing that every simple diameter-two edge-critical graph on 28 vertices has at most 196 edges, with equality exactly for K(14,14). Its two numerical density scopes are treated separately:

* Equality: (n,a,b,m,t)=(28,12,15,196,1), using label-tail-v4, column-propagation-v5, shared-adjacency-v6 and **LocalIncidence-v7**.
* Upper-bound counterexample: (28,12,15,197,2), using the freshly generated **direct197-v8** domain.

The v3 n=28/Delta=16 scope is a separate degree-case dependency. The simple low-degree, high-degree and star reductions and Fan's cited upper bound complete the assembly. There is no assumption that deleting an edge preserves criticality, no reuse of the t=1 final survivors as the t=2 domain, and no weak-core reduction in this direct route.

Six original archives were checked: v3, v4, v5, v6, LocalIncidence-v7 and v8. They contain **400 manifested payloads plus six original manifests**. Every payload length and SHA-256 matches; ZIP CRCs, safe paths, duplicate membership and manifest coverage pass. `evidence/ARCHIVE_INTAKE.json` pins each complete ZIP hash and Git blob. `evidence/HANDOFF_AND_SCOPE_REPORT.json` confirms that the original payloads remain unchanged after the replays.

The separate repository **degree-load-v7** route uses a 173/215 final partition and a weak-core density reduction. It is not LocalIncidence-v7's 22/19/347 route. Its readable core-scope audit was inspected for dependency separation; its different complete binary bundle was not available among these six inputs and was **not computationally audited here**. This report neither rejects nor certifies that alternative. Unrelated infinite-profile-family claims, the general coefficient's novelty, and the complete frozen n=25/n=27 proofs are outside this order-28 audit's certification scope.

## 2. Mathematical attack surface

### 2.1 Complement correspondence and exceptional graphs

The published complement correspondence was checked against Haynes–Henning–van der Merwe–Yeo, Theorems 3.1–3.2, including their treatment of stars. Their definition excludes disconnected edge-deletions; allowing infinite diameter adds stars, which our assembly handles explicitly. A bipartite diameter-two graph must be complete bipartite. Its 196-edge extremal case has two parts of size 14. No complement theorem is applied to a graph with an isolated complementary vertex without first removing this exceptional case.

For a missing B-pair, its endpoints miss the chosen root v. Consequently the new edge itself cannot be the total dominating pair, and an existing cross quasi-edge with a unique B-exception exists. Its B-endpoint and exception identify the original missing pair. This justifies selecting one distinct cross edge for each missing unordered B-pair, with distinct labels and supplements at a fixed source. The proof does not assume an arbitrary injection where a quasi-edge could count two different missing B-pairs.

### 2.2 Residual bookkeeping and signs

Selected cross edges and existing H[B]-edges account for exactly choose(b,2) B-pairs. The ledger therefore gives e(F)=r+t and sum d_i=2(r+t), with t=m-b(n-b). Minimum H-degree yields R_i+x_i>=d_i and p_u<=rho_u+b-a-1. These signs and the one-vertex offsets were independently recomputed.

The demand s_i=max(0,d_i-R_i) is a **lower bound** on actual selected degree x_i, not an equality. Zero-demand labels may still carry selected edges. That distinction survives the preliminary caps, v5 matching/network tests and the later actual-x endpoint types; no dense graph is rejected by silently setting x=s.

### 2.3 Residual activity and the degree cap d_i<=10

Positive surplus is necessary for the inherited all-active argument. If a B-vertex has rho=0, all its A-neighbours are selected. No F-edge crosses from that selected set to its complement. Internal selected F-edges yield two distinct residual edges each, while internal missing-set F-edges yield one each through a different A-endpoint class. Their disjointness gives r>=e(F)=r+t, contradicting t>0. Empty selected or missing sets are covered.

A separate low-k injection excludes an isolated C=H[A] vertex. For k=0, the missing pairs in A minus that vertex yield a residual family P. For each B-endpoint used by P an additional residual edge to the isolated C-vertex is forced; each unused B-vertex supplies a residual edge by activity. These b edges lie outside P and are distinguished by B-endpoints. Thus b<=L-choose(a-1,2), where L=choose(a,2)-t. At a=12,b=15 the right side is 10 at t=1 and 9 at t=2: both impossible.

Therefore delta(C)>=1, d_i<=10 and r<=59 or 58 respectively. These numerical bounds are derived necessities, not unexplained solver pruning. The low-degree regular equality case is handled separately and is not forced through a positive-surplus argument.

### 2.4 Demand domains, symmetry and safe relaxations

From the selected-edge charges, rho_u>=s_i at every selected incidence. A demand at least a would require a positive selected degree at a source with rho>=a, which is impossible. Summing the source charge gives

    r-b >= sum_i s_i(s_i-1)/(a-s_i),  S=sum_i s_i >= r+2t.

Combining them yields the exact initial score domain. The independent checks establish tuple membership, uniqueness and equality with an independently computed domain cardinality. That is full domain coverage, not simply agreement of a few aggregate survivor counts.

Sorting demands and residual row degrees is relabelling. Individual (d_i,R_i,z_i) column options remain paired with their demand labels; R-columns are not independently sorted in a way that would lose assignments. Forced labels arise only when a proved superset of eligible sources has exactly the required cardinality. Repeated pruning is justified by the preservation of every actual graph witness at each step.

V5's one-source tests do not require all sources to share a single witnessing assignment. This is a relaxation and can leave spurious survivors, not a reason for a false rejection. Later models strengthen those consistency requirements explicitly. They are not asserted to construct graphs.

### 2.5 Activation costs and shared pair resources

For a selected arc u->w, q_w-l_w >= (l_u-1-rho_w-l_w)_+. Dividing the cost of each incoming arc by a proved incoming cap P_w ensures the sum charged at w is at most q_w-l_w; it does not charge the same necessary outgoing increase separately for every incoming arc. The required-incidence subset has exactly s_i selected edges at each label, while the upper bound on total Q includes all actual selections.

The v5 flow relaxation intentionally omits some opposite-orientation pair and outgoing-total constraints. Since every actual required subset still gives a permitted flow, those omissions only weaken the test. Exact cut and potential certificates remain valid lower bounds for the relaxed problem. The audit found no double-counted resource in this step.

### 2.6 Source-local residual injection

For a source u partition A into selected neighbours S, residual neighbours T and missing neighbours M. Selected-edge domination rules out F(S,M). The new inequality is

    rho_u + 2e_F(S) + e_F(M) - e_C(T,M) <= r.

The proof supplies three disjoint residual-edge families by their A-endpoints in S, M and T. Missing M-pairs may use an auxiliary in T; allowing up to e_C(T,M) such pairs is necessary and is subtracted. The remaining auxiliary is in B and gives a residual cross edge with an A-exception. Unique exceptions and fixed endpoint classes establish the injection.

The degree-only consequences were rederived algebraically:

    sum_{i in S} d_i <= rho_u(2a-rho_u-3+q_u)-2t,
    sum_{i in S} R_i <= r-rho_u.

**Scope boundary:** the derivation for M-pairs uses full criticality, not merely the chosen B-quasi-edges. In the audited direct route it is applied to the original critical graph. This report does not silently import it into the alternative weak-core route.

### 2.7 Event normalisations and branch integrality

Label classes agree in demands, whole column domains and forced-source masks; source classes agree in residual degree, cap and forced-label pattern. Averaging relabelled copies within these classes does not assert that the graph has those automorphisms. Variables are probabilities of events and may be fractional even for an integral graph.

The audit checked the distinct-endpoint corrections, including N_g-1 and M_k-1 within a class, choose(N_g,2) for unordered same-class F-pairs, and both orientations of cross-status events. Source-conditioned ledger totals remain fixed after multiplying by the indicator q_u=q; no unjustified independence of column and source types is introduced.

V6 branches only on genuine integral counts of vertices, F-edges or selected/residual incidences, with their class-size multipliers. Its two branches are <=k and >=k+1. The additional kernel independently reconstructs those count multipliers and checks both children of every closed tree. It does not treat an unscaled averaged coordinate as Boolean. All 91 roots and 572 leaf certificates pass.

### 2.8 Actual endpoint degree types

For selected ui->w, label i neighbours u and every missing-B-pair neighbour of u except w. These are q_u+p_u distinct vertices. Hence

    R_i+x_i >= q_u+p_u.

The endpoint model attaches actual q,p and x types to the same selected incidence. Marginal totals at both ends count the same edges; their class-size factors are not inferred regularity. The allowed x range includes zero-demand extras, and the p range uses both minimum H-degree and the b-1 pair bound.

The final model omits the larger local J-variable extension but retains separately justified degree-only inequalities. The model stages need not be nested: each rejection has its own valid necessary-system certificate and the final disposition partition is complete. No graph-realisation search or unclosed branch is counted as a proof.

## 3. Complete fresh arithmetic replays

All six original checking jobs finished successfully. V4 was run in full `--replay` mode; v5/v6/v7/v8 used their complete `--check` routes, not smoke tests. The v3 checker includes the required order-28/Delta=16 scope. Per-job commands, exit codes, logs and fresh reports are preserved. These are reruns of the original separately written implementations, not additional independent researchers.

### Equality scope: 196 edges

| Stage | Exact recorded outcome |
|---|---|
| Initial score domain | 18,645 demand tuples; 1,976 retained intervals |
| Residual expansion | 17,669,896 rows; 24,411 survivors |
| Projected tests | 13,196 survivors |
| V5 joint and activation tests | 7,725 then 6,918 survivors |
| V6 shared and source-type tests | 4,617 then 479 survivors |
| V6 exact branch trees | 91 rows excluded by 572 leaves; 388 survivors |
| LocalIncidence-v7 | 22+19+347 exclusions; zero survivors |
| Separate Delta=16 scope | All 39 demand profiles and 604 residual profiles excluded |

Five inter-package handoffs, including decompression where appropriate, match byte-for-byte. Their source bytes and hashes are recorded in `HANDOFF_AND_SCOPE_REPORT.json`; they connect the full replayed equality domain to the exact final exclusions.

### Upper-bound scope: 197 edges

| Stage | Exact recorded outcome |
|---|---|
| Fresh t=2 score domain | 12,012 tuples; 1,229 retained intervals |
| Residual expansion | 8,216,928 rows; 5,154 survivors |
| Projected tests | 2,959 survivors |
| Joint column tests | 1,584 survivors |
| Final shared/source-type/endpoint tests | 787+790+7 exclusions; zero survivors |

This route generates and checks its own t=2 domains and every handoff. No equality-only survivor list is used as the new search universe.

## 4. Additional red-team checks

### Third arithmetic kernel

`scripts/third_certificate_kernel.py` uses a fresh dense integer accumulator, rather than the original sparse certificate-verification routine. It recomputes row signatures, multiplier types and signs, all aggregate coefficients and the strictly negative final right side. It also independently rebuilds branch count expressions and branch-path inequalities.

It checked **7,011 v6 leaves, 388 v7 leaves and 1,584 v8 certificates: 8,983 leaf systems and 833,923 cited constraint terms**. These support 6,530, 388 and 1,584 row exclusions in their respective input scopes. No floating-point solver is used. Six deliberate malformed-certificate controls per scope are rejected. Six additional damaged-tree controls reject missing children, invalid or fractional splits, an unscaled probability, a copied wrong child and a forged leaf.

**Independence limit:** this additional kernel imports the preserved checker model constructors. It is independent arithmetic and branch checking, **not a third independent graph-to-model derivation**. The original discovery/checker implementations and mathematical source review remain relevant to that separate obligation.

### Fresh graph regressions

`scripts/graph_stress.py` imports no project graph generator, quasi-edge unpacker or lemma checker. It constructs greedy edge-minimal diameter-two samples, C5 blowups, a Petersen graph and K(14,14), then directly verifies edge-criticality by every edge deletion. A fixed seed and complete encoded input record make the sample replayable.

The sample contains **107 labelled graphs at orders 5–28**, including 102 non-bipartite graphs. It checks **462 selected-system occurrences**, 1,659 selected incidences and 3,147 source-local instances. Nontrivial local terms occur: 145 instances have selected-internal F-edges and 861 have missing-internal F-edges. The shared-neighbourhood union is strictly stronger than a one-source maximum in 463 instances. Sixty-two one-spare-source premises are exercised. All checks pass.

The system occurrences need not all be distinct. The sample is not exhaustive. **None has positive surplus**, so these tests do not empirically validate the hypothetical dense-case exclusion. Universal correctness must rest on the proof. The older saved graph-lift and abstract-system tests were also rerun by their original wrappers; their limitations are unchanged.

## 5. Findings and severity

### RT-01 — non-blocking standalone helper input validation

The frozen v8 `src/check_rows.cpp` reads residual intervals and indexes a fixed bucket array without checking the interval range. A direct invocation with an unsupported 64..64 interval returned success and a report with zero states and zero survivors. A sanitizer run did not issue a diagnostic; absence of that warning does not validate the out-of-range input.

This is **not a failure of the n=28 proof driver**. `check197.py` independently establishes every OPEN interval, explicitly enforces 15<=lo<=hi<=63, verifies the complete retained demand list and checks the exact text file before calling the C++ program. Every actual proof input passes those gates. A zero-row malformed standalone run is not admitted as an exclusion certificate.

`patches/check_rows_input_guard.patch`, generated and tested by `scripts/harden_helper.py`, adds range, ordering, record-count and trailing-input checks to a separate copy. It rejects four malformed cases and processes the full valid 8,216,928-row scope with exactly the original report, survivor bytes and band bytes. The original archived source is retained unchanged. Use the full driver, not a bare helper's exit code, as the proof entry point.

### RT-02 — resolved evidence-publication discrepancy

The three original ZIPs are now present in their dated repository directories with the same Git objects, sizes and payload checksums. The earlier missing-archive statements remain in historical receipts but are explicitly superseded. The separate degree-load-v7 bundle is a different artifact and remains separately tracked; it is not required by the direct route audited here.

### RT-03 — remaining trust boundaries, not failed calculations

The strongest remaining obligations are independent review of the structural injections and graph-to-model lift, independent reproduction by another researcher, and a presentation that keeps the two v7 routes and the two edge densities distinct. Formal-kernel verification has not been performed. Both original implementations and this audit were produced by the same assistant under the same project direction. Repeated agreement is not independence of authorship.

Fan's original 1987 proof was not re-audited: its publisher endpoint returned HTTP 403. The bound was checked in Wang's primary manuscript and recomputed with exact rational arithmetic. The complement correspondence and star convention were checked in the published Haynes et al. paper, including a rendered page. The Wang PDF screenshot endpoint failed; its formula was read from the parsed text. Neither source-access limit is concealed as a completed original-proof audit.

## 6. Assembly and disposition

For m=197, Delta<=14 is excluded by the degree sum; Delta=15 by the fresh complete computation. At Delta=16 the required charging sum is 26, while eleven integer-demand terms supply at most 176/7. The pointwise factorisation proving the maximum 16/7 was checked for every permitted integer. Delta=17 through 26 violate the inherited h-index bound, and Delta=27 forces a star. Fan's strict bound is exactly 78883/400, so integer m<=197 and the candidate upper bound becomes 196.

For m=196, Delta<=14 forces a 14-regular graph. Two nonadjacent vertices have at least two common neighbours, so no edge can rely on a unique two-step witness. Critical edges therefore lie in no triangle. The regular triangle-free graph is K(14,14). The other degrees are excluded by the replayed Delta=15 and Delta=16 scopes and the high-degree/star reductions. K(14,14) is directly verified as diameter-two edge-critical in the fresh graph tests.

**Audit disposition: no blocking defect found in this internal pass; direct order-28 candidate remains supported.** This is not a guarantee that an external reviewer will find no gap. No frozen theorem ledger is promoted, no order above 28 is claimed complete, and no priority, novelty or all-order claim follows.

## Sources and reproducibility

Mathematical sources are the original PROOF.md files and associated checker source in the six hash-pinned archives; the n27 Section 5–7 residual/activity/low-k arguments at repository commit `bdf22db366c66516c2ce21e26fedaa5408c7ce08`; and the following published inputs:

1. Tao Wang, *On Murty-Simon Conjecture*, arXiv:1205.4397, pp. 2–3: https://arxiv.org/pdf/1205.4397 . Used for the reported Fan bound and corroborating complement correspondence; Fan's original proof remains an external input.
2. T. W. Haynes, M. A. Henning, L. C. van der Merwe and A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12) (2014), 1882–1889, Theorems 3.1–3.2 and Observation 3.4: https://d-nb.info/1372516379/34 . Used with the explicit star convention, not a blanket unqualified complement assumption.

The audit package contains scripts, complete fresh reports, command logs, the guard patch, encoded fresh graph inputs, source archive hashes and a replay driver. Original proof archives are required separately and are never recompressed or replaced. See README.md for exact commands. A proof about all relevant graphs and a test run on finitely many examples remain different things.
