# Joint quasi-edge degrees and label loads — v7

7 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal checking by ChatGPT/Geeps.

**Candidate mathematics; exact arithmetic internally reproduced; independent mathematical review OPEN.** This checkpoint closes all 388 retained v6 numerical rows for n=28, maximum degree 15 and 196 edges. The separate weak-core reduction in Section 6 extends this particular exclusion to higher edge counts. `N28_CANDIDATE.md` assembles the complete candidate order-28 bound and equality characterization. Nothing here proves the general Murty–Simon conjecture, improves the existing uniform maximum-degree coefficient, establishes priority, supplies external endorsement, or promotes a governed theorem ledger.

## 1. Exact starting point and terminology

The last repository branch read before this continuation was `00ad1a511971397fcd8a4341b021493c2383252e` in `paullenz/MurtySimon25`. Its latest fully published research checkpoint was v5. The supplied original v6 ZIP was used as the immediate research input, not assumed to have been committed. Its SHA-256 is `d00a9627e9ed4d8a6f22ae1f2b194791412ee2d16d502b1968be16e02aa30496`.

The compressed input `dependencies/v6_FINAL_SURVIVORS.json.gz` expands to the exact v6 final list. Its uncompressed SHA-256 is `1c40232b777578b5616e630e86fde2cf815c1a19c6304f3d317983fe94a9f679`. It has 388 rows in 167 demand patterns. Each row contains its demand vector, residual row degrees, individual column domains, previously established selected-source caps and forced selected incidences. These are necessary-condition profiles, not constructed graphs.

Use the inherited decomposition H=the complement of G, with a minimum-degree vertex v, A=N_H(v), B=V(H) minus N_H[v], |A|=a, |B|=b. Write C=H[A], F=the complement of C on A, and d_i=d_F(i). For every missing unordered pair of H[B], choose one cross quasi-edge ui -> w. This is an existing edge ui whose endpoint open neighbourhoods cover every vertex except w. Distinct missing B-pairs have distinct chosen cross-edges. At a fixed source their selected labels and exceptions are distinct.

All remaining A-B edges are residual. Let rho_u and R_i be residual degrees, r their common sum, q_u and p_u the outgoing and incoming degrees of the oriented missing-B-pair graph P, x_i the number of selected edges at i, and Q their total. Put

    t = e(F)-r = m-b(a+1),   ell=b-a-1,
    s_i=max(0,d_i-R_i),     S=sum_i s_i,
    D_i=R_i+x_i,            sigma_u=q_u+p_u.

The finite target is a=12, b=15, t=1, m=196. The inherited nonzero-C-degree reduction supplies d_i<=10. Section 6 identifies exactly where full criticality is used and where it is not.

## 2. Pointwise facts used by the new models

The inherited selected-edge bounds are

    d_i <= rho_u+R_i,
    d_i <= rho_u+rho_w,
    d_i <= rho_u+q_u-1,
    rho_w+q_w >= q_u-1                  for ui -> w.       (2.1)

Also q_u+rho_u<=a, x_i>=s_i, p_u<=rho_u+ell, and q_u+p_u<=b-1. These are consequences of the selected-quasi-edge structure and minimum degree, not extra sufficient conditions for a graph.

### 2.1 The source's complete missing-pair degree

For ui -> w and every z in N_P(u) except w, uz is absent in H. The quasi-edge must dominate z through iz. Together with iu, these give sigma_u distinct B-neighbours of i. Therefore

    D_i = R_i+x_i >= q_u+p_u.                            (2.2)

Two useful zero-support restrictions are

    q_u+rho_u=a  ==>  p_u=0,
    x_i>0       ==>  R_i+x_i<=b-1.                       (2.3)

In the first case u is adjacent to every A-label, and so cannot be a supplement: every incoming selected quasi-edge would need an A-label that misses u. In the second case any selected edge at i has a B-exception not adjacent to i. These restrictions do not assume that the number of actual selected incidences equals the minimum demand.

### 2.2 A pointwise domination inequality

Let S_ui be the selected-edge indicator, A_iw the ordinary A-B adjacency indicator, P_uw the missing-B-pair indicator, and T_uiw the chosen directed triple indicator. For u != w,

    S_ui + P_uw - T_uiw <= 1 + A_iw.                    (2.4)

The only nonautomatic case is S_ui=P_uw=1. If w is not the exception of ui, the selected quasi-edge must dominate w through iw. If w is its exception, T_uiw=1 reduces the left side by one. A missing unordered B-pair has exactly one chosen direction and label, so P_uw is the sum of all chosen triples on the two orientations of that pair.

All statements in this section continue to hold for the weaker cores defined in Section 6.

## 3. First strengthening: joint arc, column-option and endpoint-degree events

The inherited v6 model retains shared fractional column and F-adjacency variables. It also retains source outgoing-degree types q and endpoint-degree pair events. It can still lose correlations: the degree or column choices justifying an arc may differ between those separate marginals.

Let L_g be a class of labels with identical demand, remaining option list and forced-source mask; its size is N_g. Let B_k be a class of sources with identical rho, cap and forced-label membership; its size is M_k. These are classes for averaging, not a claim that the actual graph has those automorphisms. Average graph indicators over all permutations within each class. Every actual labelled core then supplies feasible rational values. When k=l, ordered source-supplement pairs must still have distinct endpoints; their multiplicity is M_l-1, not M_l.

Introduce the joint event

    J_{klgoqv} = average indicator of ui -> w,
        u in B_k, w in B_l, i in L_g,
        column option o at i, q_u=q, q_w=v.

An option o is (d,R,z), with z=R+s-d. Omit J when an endpoint event is disallowed by an inherited necessary condition, when the selected pair type is absent, when d>rho_k+rho_l, or when its endpoints cannot be distinct. Every actual chosen triple is retained.

Write S_{kgoq}, M_{l gov}, T_{klg} and P_{klqv} for the inherited typed-selected, typed-missing, triple and directed pair-type marginals. Add

    J_{klgoqv} <= S_{kgoq},
    J_{klgoqv} <= M_{lgov},
    sum_{l,v}(M_l-[k=l]) J_{klgoqv} = S_{kgoq},
    sum_{g,o} N_g J_{klgoqv} = P_{klqv},
    sum_{o,q,v} J_{klgoqv} = T_{klg},                    (3.1)
    sum_{k,q}(M_k-[k=l]) J_{klgoqv}
        <= (rho_l+ell) M_{lgov}.

The first equalities express unique supplement choice and unique label choice for a chosen pair. The last inequality follows pointwise by conditioning on the label being absent at w, its option and q_w=v: the number of incoming selected triples carrying that label is at most the total p_w<=rho_w+ell. Add the averaged form of (2.4). Nonnegativity and unit upper bounds are explicit.

`joint_triples.py` discovers certificates. `check_joint.py` reconstructs these constraints using a different enumeration order and named variables, atop the independently reconstructed v6 system. Comparing complete constraint sets, rather than just their sizes, gives identical systems for every phase-one rejected input.

This stage supplies exact rejection certificates for 173 of the 388 inputs. The other 215 are passed to Section 4; they are not declared feasible graphs.

## 4. Second strengthening: source (q,p) types and actual label loads x

Merely using a global maximum possible D_i in (2.2) loses too much information. The second model keeps the actual integer values q,p and x as event types, while the probabilities of those events remain fractional.

For each source class k introduce W_{kqp}, the average indicator that a vertex has q outgoing and p incoming selected pairs. Permitted p satisfies

    0<=p<=min(rho_k+ell,b-1-q),
    p=0 if q+rho_k=a.

Its q-marginal equals the inherited outgoing-degree type W_{kq}. Its incoming first moment equals the inherited pair-flow count conditional on q:

    sum_p W_{kqp}=W_{kq},
    sum_p p W_{kqp}
      =sum_{l,v}(M_l-[k=l]) P_{lkvq}.                   (4.1)

For each label class g and option o introduce Y_{gox}, the average indicator of that option and actual selected count x. Its option marginal equals Y_{go}. Permitted x is an integer with

    s_i<=x<=min(b-R, number of eligible selected sources),
    R+x<=b-1 when x>0.                                 (4.2)

The option's eligible-source count is a safe upper bound, not an equality requirement.

Finally let Z_{kgoxqp} average the event that ui is selected, the source has type (q,p), and i has option o and selected count x. Such an event is retained only when its inherited selected event is permitted, x>=1, and

    q+p<=R+x.                                          (4.3)

Add the simultaneous marginal constraints

    sum_{o,x} Z_{kgoxqp} <= W_{kqp}                    for each g,
    sum_{g,o,x} N_g Z_{kgoxqp} = q W_{kqp},
    sum_{q,p} Z_{kgoxqp} <= Y_{gox}                    for each k,
    sum_{k,q,p} M_k Z_{kgoxqp} = x Y_{gox},
    sum_{x,p} Z_{kgoxqp} = S_{kgoq}.                    (4.4)

All are expectations of elementary indicator identities or inequalities. For example, conditioned on a source type, summing over its labels counts q outgoing edges; conditioned on a label option and load, summing over sources counts x selected edges. A graph's extra selected incidences are retained rather than suppressed by replacing x with s.

The production model uses only selected Z-events. An initial, larger sel/residual/missing prototype was stopped after two examples and a timeout on its third row; it is preserved as exploratory material and contributes no additional counted exclusion. The weaker selected-only model completed all 215 remaining rows and rejected every one with an exact certificate.

`degree_load.py` is the discovery builder; `check_load.py` separately reconstructs all admissible values and marginal constraints. Entire variable and constraint sets were compared for each rejected phase-two input. The model is still a fractional relaxation, not a completed integral graph-realization engine. Its infeasibility is sufficient: every actual core has a feasible averaged lift.

## 5. Exact certificates, numerical coverage and reproduction

Each reconstructed system has the form

    A z <= b,   E z=f,   z>=0.

Every retained certificate consists of nonnegative integer inequality weights lambda and integer equality weights mu such that

    A^T lambda + E^T mu >= 0,
    b^T lambda + f^T mu < 0.                            (5.1)

A hypothetical feasible nonnegative z makes the first expression's scalar product nonnegative, while the constraints make it at most the strictly negative second expression: contradiction. Optimisation only searches for coefficients. The checker does not use a solver's status as evidence.

Certificates are stored as sparse integer weights on a canonical sorted list of independently reconstructed constraint signatures. The list's size and SHA-256 fingerprint are checked before reading any index. Duplicate indices, noninteger weights, negative inequality weights, altered right sides or a mismatched reconstructed domain are rejected. The underlying constraint coefficients are reconstructed, not accepted from the certificate.

| New phase | Inputs | Exact exclusions | Remaining |
|---|---:|---:|---:|
| Joint arc / option / endpoint-degree events | 388 | 173 | 215 |
| Source (q,p) and label x consistency | 215 | 215 | 0 |

All 388 inputs are accounted for once and only once. Early test runs overlap these phases and are not added to the count. No new integer branching is needed at v7; the v6 branch trees remain part of the upstream chain.

The earlier numerical chain was rerun, not merely read from its old logs:

- v4: complete 18,645-demand initial screen; all 17,669,896 residual profiles; exact intermediate survivor files and the 24,411-to-13,196 projection;
- v5: independent full-input check of all 13,196 rows and propagated states, then all 807 activation certificates, leaving 6,918 rows;
- v6: all 6,530 exclusions, including 91 complete branching trees with 572 exact leaves, leaving the byte-identical 388-row input;
- v3 (n=28,b=16): all 39 demand profiles and 604 residual profiles, with exact completeness and corrupted-evidence controls.

The adjacent stages' survivor/input bytes were compared explicitly. Their hashes and fresh-run reports are saved. These are separately implemented internal software checks by the same assistant, not independent research authorship.

The standalone v7 checker is invoked with `python3 -I -S -B check_all.py`. `-S` avoids a host-specific startup hook that otherwise preloads NumPy before the script runs. An initial isolated import-path failure and a later startup-import guard failure are recorded; the complete check was then rerun in clean isolation. Neither supplied an accepted mathematical exclusion. The checker asserts that no discovery builder, SciPy or NumPy has been imported.

## 6. A weaker class closed under density reduction

The previous checkpoints correctly left higher-edge-count coverage open: arbitrary deletion does not preserve diameter-two criticality, and the new exact column tests did not have a monotonicity proof. We now avoid both assumptions by proving something about a deliberately weaker class.

### Definition: an active B-quasi-edge core

A core consists of H,v,A,B and a selected quasi-edge assignment as in Section 1, satisfying:

1. N_H(v)=A, |A|=a, |B|=b, and every H-vertex has degree at least a.
2. Every H[B]-nonedge has exactly one chosen cross quasi-edge ui -> w, with open-neighbourhood union V(H) minus {w}. The chosen cross edges are distinct.
3. Each B-vertex has positive residual degree rho_u.
4. For the order-28 degree-15 route only, every vertex of C=H[A] has positive degree.

No other H-nonedge is required to have a quasi-edge. H need not be total-domination edge-critical, and its complement need not have diameter two. Let t=e(F)-r; the exact ledger m=b(a+1)+t follows from counting all existing B-pairs and all selected edges once.

### Density-reduction lemma

Suppose such a core has t>=t0 and t0 is an integer. Delete any t-t0 edges of F, equivalently add those edges to C=H[A]. Leave v-B, all A-B and all B-B adjacencies, and the entire chosen assignment unchanged. There are enough F-edges because e(F)=r+t>=t-t0 whenever r+t0>=0; in our use r>=b>0 and t0=1.

Every chosen quasi-edge remains valid: previously dominated vertices remain dominated when edges are added to H[A], and its unique exception lies in B, whose relevant incidences have not changed. All selected and residual cross edges, hence rho,R,q,p,x and r, are unchanged. A-vertex degrees in H can only increase; B- and v-degrees do not change. Positive C-degree is preserved. The new value is

    t'=e(F)-(t-t0)-r=t0.

Thus the reduced structure is another core with the same a,b and residual degrees. Its F-degrees and demands may change, so they must be recomputed. We do NOT assert that a particular old profile survives with its old d or s. We exclude the entire target core domain after recomputing them.

**Corollary.** If there is no active core of the specified type at t0, there is none at any t>=t0.

### Why all stages of this finite route apply to cores

This is essential: a closure argument for a weaker class is useless if a numerical rejection silently relies on full criticality. `CORE_SCOPE_AUDIT.md` gives the stage-by-stage audit. The initial charging inequalities, selected-edge bounds, support cuts, exact column sums, source matchings, activation costs, adjacency implications and all new marginals require only items 1–3. The bound d_i<=10 and r<=59 requires item 4. The v6 integer branching uses counts of actual vertices, incidences and F-edges, which are integral in a core just as in a critical graph. No finite rejection in the audited (a,b,t)=(12,15,1) route needs criticality of any other H-nonedge.

Consequently the complete arithmetic chain establishes the candidate finite core lemma: **there is no active B-quasi-edge core with a=12,b=15,t=1 and positive C-minimum degree**. The preceding closure then excludes every such core at t>=1.

### Obtaining the core hypotheses from an actual dense critical graph

For a non-bipartite diameter-two-critical G with n=28, Delta=15 and m>=196, the published complement correspondence [1] supplies the required total-domination-critical complement H, after the star and bipartite exceptions are separated. A minimum-degree root gives a=12,b=15. A missing B-pair cannot dominate v; criticality therefore supplies its cross quasi-edge. The inherited all-active argument gives rho_u>=1 when t=m-195>0. Both statements are rederived in `N28_CANDIDATE.md`.

If x had no C-neighbour, let X=A minus {x}. Every F-edge in X has a missing-pair quasi-edge with its auxiliary in B, since that missing pair fails to dominate x. Such a cross edge is residual because its exception is in A. Distinct F-edges give distinct residual cross edges. Each B-endpoint used by these edges also forces a residual x-edge; every unused B-endpoint supplies a residual edge by activity. These give b additional edges, disjoint from the first family. Hence

    r >= e(F[X])+b = r+t-(a-1)+b,
    t <= a-1-b=-4,

contrary to t>=1. This is the one required local use of full criticality before density reduction. Once positive C-degree is obtained, it is maintained by the reduction; it need not be reproved for the reduced, possibly noncritical structure.

Therefore the new 196-edge finite core exclusion covers **every m>=196 at n=28, Delta=15**. This is a new structural reduction, not inherited monotonicity of the v5/v6 column tests, and not a claim that edge deletion preserves criticality.

## 7. Tests and their limits

The saved 916 selected systems (639 distinct labelled original graphs) were lifted into the independent new models with exact rational arithmetic. Singleton and broadened column domains test both integral and genuinely fractional symmetry averages. Additional lifts delete F-edges and recompute demands. Across the recorded test loops there are 4,394 model evaluations and 3,421,141 constraint checks, all passing. Those evaluation counts include repeated zero-deletion cases when F is empty; they are not counts of distinct graphs or independent samples. There are 338 nonzero joint source-type events with both q and p positive, and 62,930 fractional event values.

A separate deduplicated deletion regression performs 672 nonempty F-deletions; 665 retain all-B activity and 182 start with positive C-minimum degree. Every reduced core passes the directly checked core axioms. Every reduced complement fails diameter two, as expected when edges are removed from the original critical graph. An explicit five-vertex example is saved. Thus this test detects exactly why preservation of criticality must NOT be claimed.

There are no positive-surplus original critical graphs in this sample. The dense-core closure and the complete graph theorem are mathematical consequences of their proofs and finite-domain exclusions, not statistical inferences from these examples. The finite deletion tests do not prove universal closure.

Eight corrupted certificate/coverage controls are rejected by the v7 checker. Upstream checks retain their own negative controls. A common mathematical error shared by both implementations remains possible; exact arithmetic validates an inequality certificate only after necessity of its reconstructed system has been justified.

## 8. Status, dependencies and preservation

The finite frontier at (n,Delta,m)=(28,15,196) is empty in this candidate route. The density-reduction argument supplies the newly needed above-target scope. See `N28_CANDIDATE.md` for the remaining degree cases, including the equality characterization. The earlier frozen n=25/n=27 papers and governed ledger are unchanged.

A complete replay bundle contains the original v3/v4/v5/v6 archives and this v7 package, with checksums and a one-command chain wrapper. The original archives and historical timings are preserved unchanged. New reports identify fresh computations separately. Repository publication status is tracked separately from mathematical completion; a downloadable ZIP is not a GitHub commit.

### Primary references

[1] T. W. Haynes, M. A. Henning, L. C. van der Merwe, A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12) (2014), 1882–1889, DOI 10.2478/s11533-014-0449-3. Theorems 3.1–3.2 and Observation 3.4. Primary full text: https://d-nb.info/1372516379/34 . The theorem statements and quasi-edge observation were checked; this continuation does not claim a fresh independent proof of the complete published paper.

[2] A. Dailly, F. Foucaud, A. Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342(11) (2019), 3142–3159. Theorem 4, with its six-vertex H5 exception, is used in the order-28 assembly. Primary preprint: https://arxiv.org/pdf/1812.08420 .

[3] Project residual h-index v1 and demand-support v3; frozen n=27 candidate, Sections 4–11. [4] Project label-tail v4, column-propagation v5 and shared-adjacency v6 original archives. Exact versions, hashes and replay reports accompany this package. No claim of novelty, priority or external acceptance is made.
