# General-order residual charging and coupled source–supplement cuts

7 September 2026. Developed by ChatGPT/Geeps for Paul Lenz after the instruction “Go for it.”

**Status: candidate mathematical derivations; internally reproduced exact arithmetic; independent mathematical and computational review OPEN.** No claim of novelty, priority, formal verification or a completed order above 27 is made. The frozen n=25 and n=27 candidates and governed theorem ledger are unchanged.

## 1. Results and provenance

This note develops the general-order programme in `project/research/general_n/2026-09-07-residual-hindex-v1/`, preserved at commit `4bd48b12c6f5953af92adcb614f509b2aa06391a` of `paullenz/MurtySimon25`. Its graph-theoretic inputs come from Sections 4–8 of the n=27 candidate, `project/reviews/n27/2026-09-07-candidate-v1/PROOF.md`, blob `83e09e02918adf461470bf7e70177bad275b57d9`. These remain candidate project lemmas; software tests do not prove them.

The new charging inequality gives the candidate theorem

\[
\Delta(G)\ge\beta n,\qquad \beta=\frac{10-\sqrt2}{14}=0.6132704598\ldots
\quad\Longrightarrow\quad e(G)<\lfloor n^2/4\rfloor\qquad(n\ge4)
\]

for diameter-two edge-critical graphs. The previous project coefficient was `(3+sqrt(2))/7 = 0.630601937...`.

A stronger finite inequality has a strictness proof based on the global source–supplement pair budget. It eliminates additional degree ranges, including maximum degree 18 at n=31, without profile enumeration. A coupled resource separator with exact integer certificates is implemented and tested, but it is not yet a complete integer or graph search engine.

## 2. Setup and the graph-theoretic inputs

Let G be a simple diameter-two edge-critical graph, with n vertices, m edges and maximum degree b. Disconnected pairs after edge deletion have infinite distance. A universal vertex forces G to be a star: an edge between other vertices would be redundant. A bipartite diameter-two graph is complete bipartite. Handle these cases separately.

For the remaining non-bipartite case, the published complement correspondence and the characterization of 4-supercritical graphs [1, Theorems 3.1–3.2] give that H, the complement of G, is 3-total-domination-edge-critical. The published correspondence is a dependency, not a new claim here.

Choose v of minimum H-degree a=n-1-b. Put A=N_H(v), B=V(H) minus N_H[v], C=H[A] and F=complement(C) on A. Thus |A|=a, |B|=b. Write d_i=d_F(i).

For an H-nonedge uw that misses a third vertex, adding uw supplies a total dominating adjacent pair. It cannot be {u,w}, because that pair still misses the third vertex. It therefore uses an existing edge incident with one endpoint of uw, say ui, whose open-neighbourhood union is V(H) minus {w}. Write ui -> w. Its exception w is unique, and both uw and iw are absent.

Each missing unordered B-pair misses v. Its quasi-edge auxiliary must lie in A to dominate v. Choose exactly one such quasi-edge per missing B-pair. Distinct missing pairs select distinct cross-edges, because the B-endpoint and unique exception determine the pair. Call the other A–B edges residual. Selected edges with the same source have distinct supplements.

Write r for the residual count, rho_u for its B-degrees, R_i for its A-degrees, q_u for selected source degrees, and Q=sum q_u. Define

\[
t=m-b(n-b),\qquad L=\binom a2-t.
\]

Selected cross-edges and existing H[B]-edges together number `choose(b,2)`. Hence

\[
e(C)+r=L,\quad e(F)=r+t,\quad
\sum_i d_i=2(r+t),\quad \sum_iR_i=\sum_u\rho_u=r.\tag{2.1}
\]

Minimum H-degree gives d_B(i)>=d_i, since the H-degree of i is a-d_i+d_B(i). Consequently label i needs at least

\[
s_i=\max(0,d_i-R_i)\tag{2.2}
\]

selected sources, and S=sum s_i >= r+2t.

For every selected ui -> w the existing project inequalities are

\[
d_i\le\rho_u+R_i,\qquad d_i\le\rho_u+\rho_w,
\qquad d_i\le\rho_u+q_u-1,\qquad q_u+\rho_u\le a.\tag{2.3}
\]

For completeness, every F-neighbour j of i must be adjacent to u. At most rho_u of these uj edges are residual. Every remaining uj is selected, with a distinct supplement w_j different from w. Selected ui must dominate w_j, forcing iw_j; this is residual because i and w_j both miss j. This proves the first inequality. Alternatively uj must dominate w, forcing jw; it is residual because j and w both miss i. Charging at u or w proves the second. The last two follow from adjacency to i and its F-neighbours and from simplicity.

A selected ui -> w also forces w to be adjacent to the other q_u-1 selected labels at u: their distinct selected quasi-edges must dominate w. Thus

\[
\rho_w+q_w\ge q_u-1.\tag{2.4}
\]

These local ingredients are rederived here, but their universal correctness still requires independent mathematical review.

## 3. Charging lemma without residual activity

For each label i choose exactly s_i of its actual selected incidences. Let q'_u be the number chosen at source u. Then q'_u<=q_u<=a-rho_u. For every chosen incidence, (2.3) gives rho_u>=s_i. A positive s_i must be less than a: it has a selected source with rho_u<=a-1.

At each source with q'_u>0, distribute a cost rho_u/(a-rho_u) to each chosen incidence. Its total assigned cost is at most rho_u. The function x/(a-x) is increasing for 0<=x<a. Each of the s_i chosen incidences of label i therefore receives cost at least s_i/(a-s_i). Summing yields

\[
\boxed{\quad r\ge\sum_{i\in A}\frac{s_i^2}{a-s_i}.\quad}\tag{3.1}
\]

Terms with s_i=0 are zero. A source with rho_u=a has no chosen incidences and its nonnegative residual cost need not be distributed. **No assumption rho_u>=1 is used.**

Since S>=r+2t,

\[
2t\le S-r\le\sum_i\frac{s_i(a-2s_i)}{a-s_i}.
\]

For k=a-s_i>0,

\[
\frac{s_i(a-2s_i)}{a-s_i}=3a-2k-\frac{a^2}{k}
\le(3-2\sqrt2)a.
\]

The last inequality is `2k+a^2/k >= 2sqrt(2)a`. There are a labels, so

\[
\boxed{\quad t\le c a^2,\qquad c=\frac{3-2\sqrt2}{2}.\quad}\tag{3.2}
\]

This proof is algebraic and independent of any finite search.

## 4. The 0.6132704598... candidate maximum-degree theorem

Let beta=(10-sqrt(2))/14. It is the root above one half of

\[
(\beta-\tfrac12)^2=c(1-\beta)^2.
\]

Suppose n>=4, b>=beta*n and m>=floor(n^2/4). Excluding the universal case gives a=n-1-b>=1. Let epsilon be 0 for even n and 1 for odd n. Then

\[
t\ge(b-n/2)^2-\epsilon/4.
\]

For x>=beta, `(x-1/2)^2-c(1-x)^2 >=0`; for example this follows by differentiating on [beta,1], where the derivative is positive. Thus

\[
t\ge c(n-b)^2-\epsilon/4
=ca^2+c(2a+1)-\epsilon/4>ca^2.
\]

Indeed a>=1 and `3c>1/4`, the latter equivalent to `17>12sqrt(2)`, whose squares are 289>288. This contradicts (3.2).

For n>=4, integer b>=beta*n is strictly beyond the balanced complete-bipartite part size. To check the small rounding point: for even n, b>n/2; for odd n>=5, `(beta-1/2)n>1/2` since `beta-1/2>1/10`. Complete bipartite graphs at this degree threshold are unbalanced and have fewer than floor(n^2/4) edges. Stars also have n-1<floor(n^2/4) for n>=4. This completes the candidate proof.

The n>=4 restriction matters: the star on three vertices attains its target. This theorem does not require the positive-surplus residual-activity lemma, Fan's numerical edge bound, the dominating-edge theorem, or the finite N=27 computations. It still depends on the complement correspondence and the residual/selected construction and (2.3).

## 5. Residual activity and a stronger finite charging bound

The earlier project residual-activity argument says t>0 implies every rho_u>=1. Here is its full injection, to expose this dependency.

Suppose rho_u=0. Put U=N_A(u), T=A minus U. Every ui with i in U is selected. No F-edge joins U to T, since such an edge would make ui miss an A-vertex as well as its B-exception. Let w_i be the distinct supplements of those selected ui.

For each F-edge ij inside U, selected uj must dominate w_i, and selected ui must dominate w_j. Thus jw_i and iw_j exist and are residual, since each misses an A-vertex with its partner. The resulting 2e(F[U]) edges are distinct by their A-endpoints and distinct supplement labels.

For each F-edge pq inside T, the H-nonedge pq misses u and has a quasi-edge. Its auxiliary must dominate u. It cannot be u or v. An A-auxiliary would lie in U, but all U–T pairs are C-edges, so it would dominate the supposed exception. The auxiliary lies in B, giving a residual cross-edge with A-endpoint in T. Different pq give different edges, their A-endpoint and unique A-exception identifying pq. These e(F[T]) edges are disjoint from the first family.

Hence `r>=2e(F[U])+e(F[T])>=e(F)=r+t`, a contradiction. Empty U is included. This proves activity under positive t.

Assume now every rho_u>=1 and a>=2. Repeat the charging proof, distributing only rho_u-1. The increasing ratio is `(x-1)/(a-x)` on [1,a). It gives

\[
\boxed{\quad r-b\ge\sum_i\frac{s_i(s_i-1)}{a-s_i}.\quad}\tag{5.1}
\]

Therefore, with

\[
f_a(s)=\frac{s(a+1-2s)}{a-s},\quad
M_a=\max_{s\in\{0,\ldots,a-1\}} f_a(s),
\]

we have

\[
b+2t\le S-(r-b)\le\sum_i f_a(s_i)\le aM_a.\tag{5.2}
\]

M_a is rational and can be maximized using exact integer arithmetic. For a=1 all labels have demand zero, so S>=r+2t gives b+2t<=b-r<=0 whenever activity holds; this covers the remaining small-a weak screen.

## 6. A uniform source–supplement obstruction makes (5.2) strict

**Candidate strictness theorem.** If a>=5 and all B-vertices are residual-active, then

\[
\boxed{\quad b+2t<aM_a.\quad}\tag{6.1}
\]

Proof. For a>=5, f_a(0)=0, f_a(1)=1 and f_a(2)>1. If s>=a/2, then f_a(s)<=1: after multiplying by a-s this is `(s-1)(a-2s)<=0`. Thus every maximizing integer s obeys `2<=s<a/2`.

Suppose equality holds throughout (5.2). Every label demand s_i maximizes f_a and is at least two. Equality in the excess-cost charging forces every source with no chosen incidences to have rho_u=1. For every chosen incidence it forces rho_u=s_i, because the ratio used in (5.1) is strictly increasing. At a source with chosen incidences it also forces q'_u=a-rho_u. Hence actual q_u=q'_u there. A source with rho_u=1 cannot have any actual selected incidence, because every label demands at least two and (2.3) would require rho_u>=s_i.

A chosen source of residual degree s can carry only labels whose demand is s, and needs a-s>a/2 distinct such labels. Two distinct demand classes would require more than a labels. Consequently all a labels share a single maximizing demand s.

Let z be the number of sources with selected incidences. Every one has residual degree s and selected degree a-s, so

\[
Q=as=z(a-s),\qquad z=\frac{as}{a-s}<a.
\]

Every other B-vertex has rho=1 and q=0, hence exactly one A-neighbour. But every supplement of an active source needs at least `q-1=a-s-1>=2` A-neighbours by (2.4). All selected unordered source–supplement pairs must therefore lie among the z active sources.

The global pair injection now demands

\[
z(a-s)=Q\le\binom z2.
\]

This is impossible because `2(a-s)>a>z`. Therefore equality cannot occur. Notice that this argument handles multiple numerical maximizers of f_a; it proves that an equality configuration could use only one. No finite enumeration is part of the proof.

### The n=31 illustration

For n=31, b=18 and m=240, a=12 and t=6. The maximum is at s=4, with aM_a=30=b+2t. Equality would force r=36, six active sources, eight selected edges at each, and hence Q=48. The other twelve B-vertices have one A-neighbour and cannot be supplements. Only `choose(6,2)=15` pairs remain: **48>15**. This degree case is excluded; larger m only increases the left side of (6.1).

## 7. A new supplement-capacity identity

Orient each missing B-pair from its selected source to its supplement. This forms a simple oriented graph on B: outdegree q_u is the selected source degree, indegree p_u counts uses as a supplement, and no unordered pair supports two arcs.

Every B-pair is either an H[B]-edge or one oriented missing pair. Since a B-vertex misses v,

\[
d_H(u)=(b-1-q_u-p_u)+(\rho_u+q_u)
=b-1+\rho_u-p_u.
\]

Minimum H-degree a gives the additional universal resource bound

\[
\boxed{\quad p_u\le\rho_u+b-a-1=\rho_u+2b-n.\quad}\tag{7.1}
\]

For safety the implementation uses the weaker nonnegative cap `max(0,min(b-1,rho_u+b-a-1))`. A negative un-clamped bound already means no graph can realize the profile; clamping up to zero only relaxes it.

## 8. The implemented coupled separator and its exact certificates

For a numeric profile (d,rho,R), the engine computes valid upper bounds c_u for selected source degrees. Initially `c_u=min(a-rho_u,b-1)`. For each trial q<=c_u, admissible labels obey both `d_i<=rho_u+R_i` and `d_i<=rho_u+q-1`. They must match distinct supplements w with `rho_w+c_w>=q-1` and `d_i<=rho_u+rho_w`. Take the largest feasible q, simultaneously refine all caps, and repeat to a fixed point. Every iteration preserves actual q_u<=c_u by induction.

The discovery implementation uses greedy nested-threshold matching. The separate checker, which imports no search code, uses augmenting-path matching. Both have exact integer domains and are written by the same assistant, not independent researchers.

Let E_i be the eligible source set at the final caps. If `s_i=|E_i|>0`, all its sources are forced to select label i. Count forced labels f_u. For any actual triple (u,i,w),

\[
\lambda_{ui}=\max(1,f_u,d_i-\rho_u+1)\le c_u,
\qquad \rho_w+c_w\ge\lambda_{ui}-1.
\]

The permitted triples also enforce the pair bound, distinct source/supplement, source eligibility, and the new exclusion **a supplement cannot itself be a source forced to select the same label i**, because wi must be absent.

A real selected triple consumes source capacity c_u, source–label incidence capacity one, unordered-pair capacity one, and supplement capacity from (7.1). These budgets are coupled in one relaxation rather than used as unrelated optimistic counts.

For nonnegative integer label weights y_i and resource weights alpha_u, eta_ui, gamma_{uw}, delta_w, suppose every permitted triple satisfies

\[
y_i\le\alpha_u+\eta_{ui}+\gamma_{\{u,w\}}+\delta_w.
\]

Summing over actual selected triples proves

\[
\boxed{\sum_i y_i s_i\le
\sum_u\alpha_uc_u+\sum_{u,i}\eta_{ui}
+\sum_{\{u,w\}}\gamma_{\{u,w\}}+\sum_w\delta_w p_w^{cap}.}\tag{8.1}
\]

This is a general coupled cut. A stored set of weights violating it is an exact rejection certificate. The checker recomputes caps, forced sets, the entire permitted domain and resource costs, then checks all covering inequalities and the final strict integer comparison.

Optional SciPy linear programming proposes weights. The engine rationalizes them, repairs any rounding deficit upwards, scales to integers and accepts only after exact checking. A solver's success/infeasibility message, timeout or failure is never itself treated as a proof. The implemented engine is a **fractional-relaxation certificate separator**, not a complete integer-branching solver or a full graph search.

### Regression against a stored hard n=27 profile

The input is the first row of the frozen `d15_182_supplement_certificates.json`, blob `39d9425b8209ecd1c447905279a56b4d64214dc5`:

```
d   = [5,6,6,6,6,6,7,7,8,8,9]
rho = [1,1,1,1,1,1,1,1,3,3,3,4,4,5,5]
R   = [1,2,2,3,3,3,4,4,4,4,5]
```

The final label has d=9, R=5, and demand four. It is forced at the four sources with rho>=4. Any supplement must also have rho>=4, since all sources have rho<=5 and the pair residual sum must reach nine. But each such vertex is already forced to carry the same label and cannot miss it. There is no permissible triple for that label.

The discovered certificate puts weight one on this label and zero everywhere else: **4>0**. Both checkers recalculate all 246 permitted triples of the full profile and accept the certificate. This is a stronger explanation of one already-rejected n=27 profile, not a new completed order or a replay of all N=27 data.

## 9. Exact scalar reach

Apply (6.1), or the weak bound at a<5, at m=floor(n^2/4). Use the previous general witness argument to handle the dense non-bipartite cases with maximum degree at most ceil(n/2); that argument depends on the published dominating-edge reduction [2]. Stars and complete bipartite graphs are handled separately. Remaining degrees are:

| n | Target m | Remaining maximum degrees |
|---:|---:|---|
|27|182|15|
|28|196|15,16|
|29|210|16|
|30|225|16,17|
|31|240|17|
|32|256|17,18|
|33|272|18,19|
|34|289|18,19|
|35|306|19,20|
|40|400|21,22,23|
|50|625|26,27,28,29|
|100|2500|51 through 60|

These are remaining **scalar parameter ranges**, not constructed graphs, complete profile enumerations or complete proofs for these orders. Increasing m increases t while a,b stay fixed, so every scalar exclusion also applies at higher edge counts. This monotonicity is not an assumption that graph edge deletion preserves criticality.

## 10. Tests, review limits and the next mathematical obligation

Exact algebra regressions checked 125,250 pointwise bounds, 496 strict-equality maximizer cases and 192,060 high-degree pairs through n=1000. The scalar/discovery output was reproduced byte-for-byte in the recorded environment.

All 33,864 labelled graphs of orders 3 through 6 were examined. There were 608 diameter-two-critical graphs, of which 552 were non-bipartite. Every minimum-complement-degree root and every quasi-edge selection gave 780 selections. The charging tests passed; 420 were residual-active. The 720 actual selected triples all belonged to the permitted domains.

A seeded construction made 240 graph attempts at orders 7 through 18, producing 174 critical outcomes, 171 non-bipartite. It tested 296 root/selection instances, with 274 residual-active and 161 strict scalar checks, and 813 actual selected triples. This seeded part samples one selection per root, not every selection. The actual adjacency bitmasks are retained in the evidence.

No positive-surplus graph occurred. Therefore these graph tests do not empirically establish the contradiction for hypothetical positive-surplus counterexamples. The mathematical proof, not the tests, carries that universal obligation.

Separately, 551,853 three-state incidence matrices in shapes 2x3, 3x3 and 3x4 were examined. Of these, 70,039 met the selected-source demand hypothesis; 51,563 were residual-active. Both rational charging inequalities held. These abstract tests exercise the local lemma without graph criticality but remain finite falsification tests.

The two domain algorithms agreed on 250 seeded numerical profiles. The exact N=27 certificate passed both checkers, and a forged certificate was rejected. None of this is independent expert review or formal verification.

The remaining programme is to enumerate or structurally eliminate the degree profiles in `ceil(n/2)<Delta<beta*n`, using the coupled certificates and, where needed, justified integer branching or shared-adjacency constraints. The strictness proof identifies a useful next theoretical target: a quantitative stability version that excludes profiles near the maximum, not just profiles attaining it. No such stability theorem or bounded-core theorem is claimed here.

## 11. References and attribution

[1] Teresa W. Haynes, Michael A. Henning, Lucas C. van der Merwe and Anders Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12) (2014), 1882–1889, DOI 10.2478/s11533-014-0449-3. Author repository: https://dc.etsu.edu/etsu-works/15862/ . Full-text copy cited by the prior project: https://d-nb.info/1372516379/34 . The published correspondence is an input; its full original proof was not independently re-audited in this turn.

[2] Antoine Dailly, Florent Foucaud and Adriana Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342(11) (2019), 3142–3159; https://arxiv.org/abs/1812.08420 . Used for the inherited low-degree witness reduction, not for the new coefficient proof.

[3] SciPy `linprog` official documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html . Optional numerical coefficient discovery only; saved execution used SciPy 1.17.0 and CPython 3.13.5. Exact verification uses the Python standard library.

Paul Lenz directed the project. ChatGPT/Geeps developed the derivations, code and internal checks in this session. New here means new to this project workstream, not a priority assertion. Mathematical validity, numerical replay, actual evidence preservation and independent review remain separate status questions.
