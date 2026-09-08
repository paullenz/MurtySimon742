# n=29 red-team audit — restarted from first principles

8 September 2026. Red-team restart requested by Paul Lenz. Audit performed by ChatGPT/Geeps against repository `paullenz/MurtySimon25`.

**Baseline audited:** `09fcda0fac794265534511343e4806a3ebd765b5` (`main` at restart).

**Candidate under audit:** every 29-vertex simple diameter-two edge-critical graph has at most 210 edges, with equality exactly `K(14,15)`.

**Status of this file:** live red-team checkpoint, not an independent peer review and not a theorem-ledger promotion. The original candidate proof is deliberately left unchanged. Findings are recorded here separately so that the audit cannot silently repair the object being audited.

## Current verdict

No blocking mathematical defect has been found in the restarted audit so far.

One non-blocking but real traceability defect has been identified in the written n=29 proof: the finite Delta=16 code hard-codes two consequences (`r <= 60-t` and `dmax=10`) whose mathematical bridge is inherited from the earlier small-`k` argument but is not explicitly restated in `project/reviews/n29/2026-09-08-candidate-v1/PROOF.md`. The bridge is valid and is rederived below. This is therefore a documentation/proof-traceability defect, not presently a counterexample or mathematical failure.

The principal remaining trust boundary is the inherited direct197 model implementation inside the hash-pinned n=28 archive. The n=29 wrapper and both residual-row scanners are readable and have been audited; the inherited discovery/joint/LP sources are preserved and clean-replayed, but the restarted audit has not yet completed an independent line-by-line reconstruction of every inherited source routine. The mathematical constraints they are supposed to encode are being rederived independently below.

## 1. Scope split

The n=29 candidate separates naturally into four blocks:

1. `Delta <= 15`: degree sum plus a hand witness-count argument, including equality.
2. `Delta = 16`: complement residual/quasi-edge reduction plus a finite exact certificate calculation at `m=211` (`t=3`) and `m=210` (`t=2`).
3. `Delta = 17`: pointwise charging contradiction.
4. `Delta = 18,...,27`: residual h-index contradiction; `Delta=28` is the universal-vertex/star case.

The restarted audit treats each block as untrusted until rederived.

## 2. Delta=15 hand argument — restarted audit

### 2.1 Witness coverage

For a critical edge `xy`, delete it and choose a pair `u,v` whose distance becomes greater than two. In the original graph that pair had distance at most two and every path of length at most two between it used `xy`.

- If `u,v` are adjacent, their edge must be `xy` and they have no common neighbour. This is a direct witness and can cover only its own edge.
- If `u,v` are nonadjacent, their unique length-two path uses `xy`; a second common neighbour would survive deletion. This is a two-step witness and can cover at most the two edges of its unique length-two path.

This dichotomy is valid and does not assume a globally injective witness assignment.

### 2.2 Degree-sum bound for witnesses

At the dense scopes a dominating edge is excluded by the published dominating-edge result used by the candidate.

- A two-step witness has one common neighbour. Its neighbourhood union lies among the other 27 vertices, hence `d(u)+d(v) <= 28`.
- A direct witness has disjoint neighbourhoods. If their union had all 29 vertices, their edge would dominate the graph; hence again `d(u)+d(v) <= 28`.

With `epsilon_x=15-d(x)`, every witness therefore has deficit sum at least two.

### 2.3 Coverage count

Let `L={x:epsilon_x>=2}`, `O={x:epsilon_x=1}`, `h=|L|`, `o=|O|`, and `T=29*15-2m`. Then `2h+o<=T`.

Assign one witness to each edge having both endpoints outside `L`. A witness in `L-L` covers none of those edges; a missing `L-X` pair covers at most one; an `O-O` witness covers at most two. Adding the edges incident with `L` cancels the actual cross-edge term and gives

`m <= C(h,2) + h(29-h) + o(o-1)`.

The cancellation has been rederived; no hidden injective assignment across witness classes is needed.

For `m=211`, `T=13`; the exact bounds for `h=0,...,6` are

`156, 138, 127, 123, 126, 136, 153`,

all below 211.

For `m=210`, `T=15`; the bounds for `h=0,...,7` are

`210, 184, 165, 153, 148, 150, 159, 175`.

The only coarse equality is `(h,o)=(0,15)`. Every witness is then an `O-O` pair, and distinguishing actual `O`-edges from nonedges gives

`210 <= e(G[O]) + 2(C(15,2)-e(G[O])) = 210-e(G[O])`,

so `O` is independent. Its 15 vertices each have degree 14 and therefore meet all 14 outside vertices; those 210 cross edges exhaust the graph. Hence equality forces `K(14,15)`.

**Restart verdict on Delta=15:** no defect found.

## 3. Complement/quasi-edge reduction — independent rederivation

Let `H=complement(G)`, choose a minimum-degree vertex `v`, put `A=N_H(v)`, `B=V(H)\N_H[v]`, `C=H[A]`, and `F=complement(C)` on `A`. For `Delta=16`, `a=|A|=12`, `b=|B|=16`.

For each missing unordered pair `uw` of `H[B]`, adding `uw` corresponds to deleting the edge `uw` of `G`. Edge-criticality forces a new adjacent total-dominating pair in `H+uw`. It cannot be `{u,w}`, because both still miss `v`. Any new adjacent total-dominating pair must therefore consist of one endpoint of the added edge and an old neighbour, say an existing cross edge `ui`, whose open neighbourhoods cover every vertex except the opposite endpoint `w`. Its auxiliary `i` lies in `A` in order to dominate `v`. Write `ui -> w`.

Choose exactly one such cross edge per missing B-pair. A selected cross edge determines its B-source and unique exception, so two different missing B-pairs cannot select the same cross edge. All other existing A-B edges are residual.

Let `rho_u`, `R_i` be residual row/column degrees, `r=sum rho=sum R`, `q_u` selected outdegree, `p_u` supplement indegree, `x_i` actual selected degree at label `i`, `d_i=d_F(i)`, and `s_i=max(0,d_i-R_i)`.

Direct edge counting gives

- `e(F)=r+t`, where `t=m-b(n-b)`;
- `sum_i d_i = 2(r+t)`;
- minimum H-degree gives `x_i >= s_i`;
- hence `S=sum_i s_i >= r+2t`.

For a selected `ui -> w`, the following necessary inequalities have been independently rederived:

- `d_i <= rho_u + R_i`;
- `d_i <= rho_u + rho_w`;
- `rho_w + q_w >= q_u-1`;
- `R_i + x_i >= q_u+p_u`;
- `q_u+rho_u <= a`;
- `p_u <= rho_u+(b-a-1)`; at n=29, Delta=16 this is `p_u<=rho_u+3`;
- `q_u+p_u <= b-1`.

No direction reversal or multiplicity collision has been found in these rederivations.

## 4. Residual activity and charging — independent rederivation

When `t>0`, every B-row is residual-active. Suppose `rho_u=0`, put `U=N_A(u)` and `T=A\U`. Every `ui`, `i in U`, is selected and there is no F-edge between `U` and `T`. Each F-edge inside `U` forces two distinct residual cross edges using the distinct supplements of its endpoints. Each F-edge inside `T` has a quasi-edge whose auxiliary must lie in `B`, giving a distinct residual cross edge with A-endpoint in `T`. Thus

`r >= 2e(F[U]) + e(F[T]) >= e(F) = r+t`,

a contradiction. Hence `rho_u>=1` for every B-vertex.

For each label choose exactly `s_i` of its actual selected incidences. At a chosen incidence, `rho_u>=s_i`; also `q_u<=a-rho_u`. Charging `(rho_u-1)/(a-rho_u)` per chosen incidence and using monotonicity gives

`r-b >= sum_i s_i(s_i-1)/(a-s_i)`.

Combining with `S>=r+2t` gives the necessary demand inequality

`sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t`.

For `a=12,b=16` this is exactly

`sum_i s_i(13-2s_i)/(12-s_i) >= 16+2t`.

**Restart verdict on residual activity/charging:** no defect found.

## 5. Finding RT-N29-001 — omitted bridge for the finite Delta=16 hard bounds

**Severity:** low / traceability.

**Mathematical impact found:** none; the omitted bridge is valid.

The two independent n=29 residual scanners reject any row with `r>60-t`, and the final joint propagation is called with `dmax=10`. Those constants are not explained in the n=29 proof text.

Let `k=delta(C)`. The inherited small-`k` quasi-edge injection gives, at `k=0`,

`b <= L - C(a-1,2)`,

where `L=C(a,2)-t`. For `a=12,b=16`, this becomes

`16 <= (66-t)-55 = 11-t`,

which is impossible for both `t=3` and `t=2`. Hence `k>=1`.

Therefore `e(C)>=ceil(12/2)=6`. Since `e(C)+r=L=66-t`,

`r <= 60-t`.

Also every vertex of `C` has degree at least one, so every F-degree satisfies

`d_i <= 11-1 = 10`.

This exactly justifies both hard-coded finite-calculation bounds.

**Recommended repair:** in a future revised proof, state this bridge immediately before the finite Delta=16 enumeration. Do not silently modify the currently audited candidate edition.

## 6. Delta=16 demand-domain exhaustiveness — fresh independent reconstruction

Independently of the repository demand generator, enumerate every nondecreasing length-12 integer tuple with `0<=s_i<=10` satisfying the charging inequality above.

The restarted audit obtains exactly:

- `t=3` (`m=211`): **4,867** demand tuples;
- `t=2` (`m=210`): **9,251** demand tuples.

These exactly match the preserved n=29 replay counts. This independently checks the first exhaustiveness boundary rather than merely comparing two implementations descended from the same generator.

The exact feasible residual interval for a demand tuple is also rederived from the charging inequality and `S>=r+2t`:

`r_min = b + ceil(sum_i s_i(s_i-1)/(a-s_i))`,

`r_max = min(S-2t, C(a,2)-t)`.

The later scanner cut `r<=60-t` is the separately justified `k>=1` strengthening above.

## 7. Residual-row and projected screens — restarted review

The two committed residual scanners enumerate sorted length-16 residual rows with values in `1,...,12`. Residual activity justifies the lower bound one; simplicity justifies the upper bound twelve. The implementations use different enumeration schemes (direct monotone recursion versus multiplicity/order-statistics plus an independent dynamic-program count) and their saved outputs agree byte-for-byte.

The initial source-capacity Hall screen is necessary: a source of residual degree `rho` can carry at most `12-rho` selected edges and only labels whose demand is at most `rho`. The prefix inequalities therefore upper-bound the possible supply to the largest demand prefixes.

The iterative source-cap refinement is also necessary: a source with actual selected degree `q` has `q` distinct supplements and each must satisfy `rho_w+q_w>=q-1`. Replacing unknown actual `q_w` by current valid caps preserves an upper bound; monotone iteration therefore cannot delete a real graph state.

The projected zero-slack cut is valid: when every `s_i>0`, `s_i=d_i-R_i` for every label, so `S=sum(d_i-R_i)=r+2t`; a nonzero slack is impossible.

The projected pair-threshold screen is a relaxation of the selected-edge inequality `d_i<=rho_u+rho_w`: high-degree labels require selected incidences mapped injectively to B-pairs whose residual-degree sums cross the same threshold. The implementation uses lower bounds on the number of such required incidences and the exact number of qualifying B-pairs. No unsafe strengthening has been identified.

**Restart verdict through the projected stage:** no blocking defect found.

## 8. Final source-local inequality — independent rederivation

Fix a B-source `u` and partition `A` into selected neighbours `S`, residual neighbours `T`, and missing neighbours `M`.

- There is no F-edge between `S` and `M`.
- Every F-edge in `S` forces two distinct residual cross edges with A-endpoint in `S`.
- Every F-edge in `M` has a quasi-edge auxiliary in `T` or `B`; at most `e_C(T,M)` can use `T`, while the remainder give distinct residual cross edges with A-endpoint in `M`.
- The `rho_u` residual edges at source `u` end in `T` and are disjoint from those families.

Thus

`rho_u + 2e_F(S) + e_F(M) - e_C(T,M) <= r`.

Algebra using `e(F)=r+t`, `|S|=q_u`, `|T|=rho_u`, and the block-size caps gives

`sum_{i in S} d_i <= rho_u(2a-rho_u-3+q_u)-2t`,

and the disjoint residual-column count gives

`sum_{i in S} R_i <= r-rho_u`.

These are the load-bearing local inequalities used in the inherited direct197 final models. The restarted hand derivation finds them necessary.

## 9. Delta=17 and Delta>=18 — restarted hand checks

For `Delta=17`, `a=11`. For every integer `0<=s<=10`,

`s(12-2s)/(11-s) <= 16/7`,

because

`16/7 - s(12-2s)/(11-s) = 2(s-4)(7s-22)/(7(11-s)) >= 0`

at those integer values. Eleven labels therefore contribute at most `176/7`. The required left sides are 29 at `m=210` and 31 at `m=211`; both are impossible.

For the h-index range, let `h` be the largest integer with at least `h` residual rows of degree at least `h`. A label demand `s_i` requires `s_i` distinct selected sources with residual degree at least `s_i`, so `s_i<=h`. Therefore `S<=ah`. Residual activity gives

`r >= h^2+(b-h)=b+h(h-1)`.

With `S>=r+2t`,

`b+2t <= (a+1)h-h^2 <= floor((a+1)^2/4)=floor((29-b)^2/4)`.

Every `b=18,...,27` violates this at `m=210` and `m=211`. `Delta=28` is the universal-vertex case and forces a star.

**Restart verdict on Delta>=17:** no defect found.

## 10. Computational evidence rechecked at the repository boundary

The preserved clean Delta=16 workflow records:

- `m=211`: 4,867 demand tuples; 1,848,957 residual rows; 206 row survivors; 118 projected survivors; 36 joint survivors; all 36 rejected by exact certificates; final survivors 0.
- `m=210`: 9,251 demand tuples; 5,765,218 residual rows; 2,087 row survivors; 1,225 projected survivors; 593 joint survivors; all 593 rejected by exact certificates; final survivors 0.

The workflow compiles both residual scanners, compares their survivor and band files byte-for-byte, partitions every projected position exactly once, and accepts a final LP exclusion only after exact integer Farkas verification against a separately reconstructed named linear system. Floating-point solver status alone is not an exclusion event.

A clean Ubuntu runner replay is preserved as successful. This is strong internal computational assurance, but same-assistant authorship means it is not independent researcher reproduction.

## 11. Open red-team obligations after this checkpoint

The next audit priorities are:

1. reconstruct the inherited demand support/dual pruning from its preserved source and verify that each certificate checker is logically one-way (only necessary-condition exclusions);
2. independently reconstruct the joint-column state semantics and compare every state-field invariant with the hand model;
3. independently reconstruct the shared/source-degree/endpoint LP named systems from the mathematics, not by importing the discovery builders, then compare coefficient sets;
4. check the two endpoint-only `m=210` contradictions especially closely, because they are the deepest branch of the proof;
5. separately verify the external Fan bound and dominating-edge theorem at the exact hypotheses used by n=29;
6. after those checks, issue either a strengthened red-team pass report or a blocking-defect report. Do not promote the theorem ledger merely because this same-assistant audit survives.

## 12. Audit status table

| Component | Restart status |
|---|---|
| Fan numerical reduction | arithmetic checked; external theorem hypotheses still separately reviewable |
| Dominating-edge reduction | hypothesis chain still separately reviewable |
| Delta<=14 | PASS |
| Delta=15 witness coverage/count/equality | PASS |
| Complement selected/residual ledger | PASS under published complement correspondence |
| Selected-edge local inequalities | PASS |
| Residual activity | PASS |
| Charging inequality | PASS |
| Delta16 hard `r/dmax` bridge | PASS mathematically; **RT-N29-001 traceability gap recorded** |
| Demand tuple domain | PASS; independently regenerated counts 4,867 / 9,251 |
| Residual-row source screens | PASS on mathematical necessity/readable code |
| Projected cuts | PASS on mathematical necessity/readable code |
| Final source-local inequality | PASS |
| Inherited joint/LP implementation | clean-replayed and exact-checked; deeper restarted source reconstruction OPEN |
| Delta17 pointwise bound | PASS |
| Delta18-27 h-index | PASS |
| K(14,15) boundary | PASS |
| Independent specialist review | OPEN |
| Full formal verification | NO |

**Current red-team conclusion:** the n=29 candidate remains viable. The restart has strengthened confidence in the hand mathematics and exposed one repairable proof-traceability gap, but it has not yet crossed the remaining independence/source-reconstruction trust boundary at Delta=16.
