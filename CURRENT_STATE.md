# Murty–Simon / Erdős #742 — live current state

> Read this first. The user's theorem-first instruction supersedes the older scan-first next action. The preceding attachment's complete mathematical argument is transcribed below before any extension; original file bytes and test evidence remain in the identified bundle.

<!-- CURRENT-STATUS:START -->
**CHECKPOINT CLASS:** `RECOVERED_INTERNAL_STRUCTURAL_THEOREM_NOT_PROMOTED`.

**WORK MODE:** `RECOVERY`. Preserve the completed attachment-only tight-interface theorem and its priorities before the next mathematical unit. No new catalogue result or promotion.

**INSPECTED PREDECESSOR:** `5ca7a87868ba30bf053e38d3ecbb09fefd39b297`, tree `1ba9086aa5c92da03ad985764c484016e5286f41`, CURRENT_STATE blob `4f6f2c9384e63a5db526fbb052064039153be985`. The prior handoff is retained unchanged at that immutable commit. The current contents update preserves unrelated repository paths.

**USER PRIORITY:** complete a comparatively short structural treatment with explicit scope, indispensable proofs, equality/exceptional cases and a clear external-review surface. Numerical survivor reductions are supporting diagnostics, not the principal milestone.

**LAST VERIFIED RESULT:** recovered internal hand proof below. For the exact canonical tight block |T|=|H|=d>=2, a demand/residual-only top-c capacity W satisfies W>=e_F(T,K)>=d+(d-1)m>=d^2. An exact identity decomposes W-d-(d-1)m into four nonnegative defects. Each tight-destination map properly colours G[H], and E=e(G[H]); therefore E>0 requires W>=d(2d-1). Equality at W=d^2 forces singleton full profile pools, complete F[T], exhausted tight residual occurrences and E=0. Equality at the extra-selection threshold forces two-vertex pools and bipartite G[H]. These are necessary structures, not graph constructions or a global conjecture proof.

**CHECKS:** freshly verified all 16 manifested files and the archived 104373 weight decisions in the 17-file attachment; no fresh mathematical replay claimed. Inherited checks: 104373 Python/C++ weight records; 368911 receiver-map families; 97738 colourings. Inherited exhaustive n<=6 and larger sampled graph checks both have ZERO exact d>=2 blocks; the sampled check does exercise 1078 nonempty forced destination residuals. Both implementations are by the same assistant. Original graph-to-exact-block coverage and external review remain OPEN.

**CANONICAL / PROMOTED STATUS:** unchanged — 4626 exclusions / 952 survivors / 3632 whole-state closures. The preceding 203-key named candidate union, 41 strict/equality certificates and 170-candidate audit retain their trust boundaries. State3349 remains unresolved. No scan, workflow launch, q-enumeration or promotion.

**PRESERVATION:** complete mathematical transcription below; original attachment `MurtySimon742_Structural_Treatment_2026-09-16.zip`, SHA256 `d948e286846e53c569a748cf7bce0f8c3bc4bd5547c6333e46e9ceec0feb6b8e`. Original `STRUCTURAL_TREATMENT.md` SHA256 `bad40486b51182559ec46cc1ca799af3c6d18f6da223872fa2fcaeaca14a1f08`. This transcription does not claim byte identity or transfer of the separate code/table paths. The last session reported no write action; a contents-update action is available in this session. No permanent platform diagnosis is inferred.

**UNPRESERVED WORK:** no mathematical finding remains only in session memory after remote confirmation. Transfer of the original bundle's separate source and evidence files remains pending; its exact bytes are preserved in the delivered attachment. Older attachment transfers remain pending.

**DEFERRED ADMIN:** conventional-path attachment transfers, reviewer/README integration, literature novelty assessment, unrelated CI/status work and promotion.

**NEXT ACTION:** MATH: analyze the zero-defect W=d^2 boundary below. Use its singleton full pools, complete tight graph and exhausted tight residual occurrences to obtain a global contradiction or an explicitly characterized remaining family. Do not revert to the superseded 952-row scan-first plan. Preserve the first result, correction or failed route before another unit.

**PROCESS RULE:** one bounded unit then preservation and one remote confirmation; no background-work claim or automatic promotion.
<!-- CURRENT-STATUS:END -->

## Priorities

1. Complete a self-contained theorem within an explicit structural scope. The first necessary-condition theorem is below; it does not close its entire class.
2. Resolve zero/small defect structurally, rather than collecting further individual exclusions. Separately address configurations without the exact tight-block hypothesis.
3. Challenge the graph-to-representative bridge and each indispensable implication, retaining failures and controls. Finite projections are not graph realizations.
4. Assemble the closed argument and supplements for independent review. External acceptance and novelty are open.

## Recovered theorem: tight-block interface capacity and high-source colouring

This is a complete mathematical transcription of the argument in the identified attachment, not an assertion of new results in this recovery. Research directed by Paul Lenz; internal derivation and implementation by ChatGPT/Geeps.

### 1. Original graph and selected representatives

Let G be a finite simple diameter-two edge-critical graph and J its complement. Choose a minimum-degree vertex p of J. Put A=N_J(p), B=V(J) minus N_J[p], a=|A|, F=G[A]. For each edge uw of G[B], choose exactly one cross-edge ui of J, with i in A, such that N_J(u) union N_J(i)=V(J) minus {w}, interchanging u,w when needed. Denote it (u,i)->w.

Existence follows directly from criticality. Adding uw to J creates an adjacent total-dominating pair; no such pair existed in J because G has diameter two. The new pair uses u or w, cannot be {u,w} because both miss p, and its other endpoint must be in A to dominate p. The added edge repairs only domination of the other B-endpoint. Its existing cross-edge therefore has exactly that unique exception.

Select one representative per unordered edge of G[B]. A selected cross-edge determines its exception and hence its missing unordered pair. Distinct selected labels at one source have distinct destinations, and opposite orientations of one pair are not both selected. At u in B partition its A-neighbourhood in J as S_u disjoint-union R_u, selected versus residual, and put rho_u=|R_u|. At i in A let x_i and R_i count its selected and residual incidences. The scalar R_i is not the set R_u. Write delta_i=deg_F(i), s_i=max(0,delta_i-R_i). Minimum degree gives deg_J(i)=a-delta_i+R_i+x_i>=a, hence x_i>=s_i.

For every selected (u,i)->v:

    i absent at v; S_u minus {i} subset N_J(v);
    S_v subset N_J(u); N_F(i) subset R_u union R_v;
    delta_i<=rho_u+R_i; s_i<=rho_u.

Here and below neighbourhood containments involving label sets refer to A-labels. A different selection (u,j)->w has w!=v, so its quasi-edge dominates v and forces jv present. This gives forward containment. A selection at v cannot have exception u (opposite orientation), so it dominates u and gives reverse containment. For j in N_F(i), quasi-edge domination forces uj present. If residual, charge it at u. Otherwise j is selected at u and jv is present as just shown; both j and v miss the A-label i, so jv cannot be selected and is residual. This proves the SET inclusion. For the scalar label injection, the destination w of selected j satisfies iw present because (u,i) dominates w. Both i and w miss j, so iw is residual. Different selected j have different w. Charging the other j at u proves delta_i<=rho_u+R_i and thus eligibility s_i<=rho_u.

### 2. Definitions and scope

Fix d>=2 and the WHOLE levels

    T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d.

Let K=N_F(T) minus T, c=min_H rho. List low residual degrees outside H as lambda_1>=...>=lambda_l, each <d. For i outside T define

    w_i=d if s_i=0;
    w_i=lambda_(s_i) if 1<=s_i<=d-2, s_i<=l,
                         and lambda_(s_i)>=s_i;
    w_i=0 otherwise.

Let W be the sum of the largest min(c,|A minus T|) weights. Define full profile pools V_t={v outside H:R_v=T minus {t}}, p_t=|V_t|, V=union V_t, m=sum p_t. They include unused full profiles. Set E=sum_H(|S_u|-d).

No positive-surplus premise is used. The result does not establish exact-block coverage for all counterexamples, or graph realization of any scalar tuple.

### 3. Interface theorem and proof

Every tight label has d distinct selected sources and exactly d eligible vertices, so every high vertex selects all T and no low vertex selects T. A tight destination is low, contains the other d-1 tight labels residually, and hence belongs to V_t. Thus p_t>=1, m>=d, and the pools are disjoint.

Every k in K is in every high neighbourhood by domination from a tight F-neighbour. It cannot be selected there: its destination would contain all T, impossible at a low vertex; at a high destination k is already present, contrary to exception absence. Consequently K subset R_u for all high u, |K|<=c and R_k>=d.

When s_k>0, choose a selected incidence of k. Its source and destination are low (k is residual at H and present at every high vertex). The set inclusion gives delta_k<=2d-2, so s_k<=d-2. At each of at least s_k low selected sources its ell_k=|N_F(k) intersect T| tight neighbours are residual. Eligibility also forces their residual degrees to be at least s_k. Hence ell_k<=lambda_(s_k), with that order statistic existing and >=s_k. For s_k=0 use only ell_k<=d. Thus ell_k<=w_k, and

    e_F(T,K)=sum_K ell_k<=sum_K w_k<=W.

Each t occurs residually at all full pools except V_t. Put

    beta=sum_(t in T)[R_t-(m-p_t)]>=0,
    mu=binom(d,2)-e(F[T])>=0.

Since delta_t=d+R_t, exact degree summation yields

    e_F(T,K)=d+(d-1)m+beta+2mu.

Therefore

    W>=e_F(T,K)>=d+(d-1)m>=d^2,

and the exact nonnegative-defect identity is

    W-d-(d-1)m = (W-sum_K w_k)
                 +sum_K(w_k-ell_k)+beta+2mu.

Individual weights are upper bounds, not jointly attainable promises. Zero-demand labels are not subjected to a positive-demand degree cap.

### 4. High-source colouring and scalar bound

Let D_u be the d actual tight destinations of high u. An extra selection (u,j)->w has w high: otherwise all T would be residual at a low vertex. If v belonged to D_u intersect D_w, forward containment from u forces j at v. Its residual set is contained in T, so j is selected at v. Reverse containment from w then puts j at w, contradicting its own destination absence. Thus D_u and D_w are disjoint for every extra edge.

Conversely every G[H] edge has exactly one selected representative with both endpoints high, and its label cannot be tight. Thus E=e(G[H]). For each t the map u to its t-destination is a proper colouring with p_t available colours. If E>0, every p_t>=2, m>=2d, and W>=d(2d-1).

For an entirely scalar bound put M=#{u:rho_u=d-1}, mbar=min(M,floor((W-d)/(d-1))). If mbar<d there is no such realization. Otherwise set rbar=min(d,floor(mbar/d)) and write d=rbar*q+j with 0<=j<rbar. Since the smallest p_t<=floor(m/d), one has

    E<=[d^2-j(q+1)^2-(rbar-j)q^2]/2.

Indeed a graph properly coloured with class sizes n_1,...,n_r has at most (d^2-sum n_i^2)/2 edges. Balancing the class sizes minimizes the sum of squares; allowing more colours only enlarges the bound. This elementary extremal principle is not claimed new.

### 5. Equality and precise limitations

If W=d^2, then m=d, all p_t=1, E=0 and every defect vanishes. In particular F[T] is complete and all tight residual incidences lie in V. If W=d(2d-1) with E>0, then m=2d, all p_t=2, all defects vanish, F[T] is complete, tight residual incidences lie in V and G[H] is bipartite. These are necessary descriptions, not existence assertions or already-derived contradictions.

For d=5, W<25 is an exact-block obstruction and 25<=W<45 forces E=0. Neither W>=25 nor E=0 establishes graph existence or whole-state survival. Six positive-demand eligible labels have total capacity at most 24 and cannot supply the required 25 T-K adjacencies, even though an unweighted count of six exceeds five.

The original finite tests validate named set/weight/colouring steps only. Both actual-graph test families had no exact tight block with d>=2. The larger sampled bridge test is nonvacuous for local residual forcing but not for this entire theorem. External expert review, novelty, sharpness, catalogue application and unrestricted structural coverage remain open.

## Immutable preceding evidence

The 124-record recovery and previous next-action record remain at CURRENT_STATE.md in commit `5ca7a87868ba30bf053e38d3ecbb09fefd39b297`. The recovered structural proof originally used that same head's canonical bridge, spare-receiver, disjoint-receiver, residual-endpoint, residual-union and coverage-diagnostic notes. It rederives every local graph fact it uses above. Original attachment source code, exact decisions, graph lists, audit notes and the obsolete proposed handoff are retained unchanged in the SHA256-identified ZIP; their conventional-path upload is not claimed here.
