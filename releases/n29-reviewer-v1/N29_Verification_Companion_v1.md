---
title: "A candidate proof of the Murty-Simon conjecture at order 29 - verification companion"
subtitle: "Reviewer edition 1 - replay, audit and provenance"
author: "Paul Lenz research project; mathematical development and drafting with ChatGPT/Geeps"
date: "9 September 2026"
documentclass: article
fontsize: 11pt
geometry: [a4paper, margin=25mm]
colorlinks: true
linkcolor: "black"
urlcolor: "blue"
---

\begin{abstract}
This companion collects the principal replay instructions, audits, graph-to-model bridges and provenance documents supporting the reviewer manuscript. It is not a substitute for reading the mathematical proof. Exact arithmetic or certificate verification is identified as such in the underlying sources; same-assistant reconstructions are not represented as external independent review.
\end{abstract}

## Reviewer orientation

**Claim under review.** `e(G) <= 210, with equality exactly K(14,15)`.

**Status.** complete candidate; independent mathematical review OPEN.

**Sources assembled verbatim below:**
- `project/reviews/n29/2026-09-08-candidate-v1/README.md`
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`
- `project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`
- `project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`

A failed or superseded route remains part of the repository history and is not silently promoted by inclusion in this companion. Reviewers should report suspected flaws through the repository's public review process.

---



\newpage

# Included source: `project/reviews/n29/2026-09-08-candidate-v1/README.md`

# n=29 Murty–Simon candidate — 8 September 2026

**Candidate theorem:** every 29-vertex diameter-two edge-critical graph has at most **210** edges, with equality exactly for **K(14,15)**.

**Status:** complete candidate hand proof with the new Delta=16 finite arithmetic reproduced on a clean GitHub runner. Independent mathematical review, independent computational reproduction, novelty assessment and full formal verification remain **OPEN**. This checkpoint is not a theorem-ledger promotion.

Read [PROOF.md](PROOF.md) first. The proof is self-contained at the fixed-order level and deliberately does **not** use the later general `293/500` candidate theorem.

## Degree partition

- `Delta<=14`: degree sum gives at most 203 edges.
- `Delta=15`: a witness-deficit count excludes 211 edges; at 210 it forces the graph to be `K(14,15)`.
- `Delta=16`: fresh direct finite calculation excludes both 211 and 210 edges.
- `Delta=17`: the pointwise charging score is at most `176/7`, below the required 29 or 31.
- `18<=Delta<=27`: residual h-index inequality excludes every case.
- `Delta=28`: a universal vertex forces a star.

Fan's strict bound as reported by Wang reduces the upper-bound problem to excluding 211 edges. The non-bipartite dominating-edge theorem of Dailly–Foucaud–Hansberg removes that separate structural case.

## Delta=16 exact replay

The Delta=16 route has `(a,b)=(12,16)` and treats `t=3` (211 edges) and `t=2` (210 edges). It adapts the hash-pinned n=28 direct197 implementation, but generates fresh n=29 domains.

The successful clean-runner aggregate is [evidence/N29_D16_REPLAY.json](evidence/N29_D16_REPLAY.json):

| Scope | Demand tuples | Residual rows | Projected survivors | Joint survivors | Exact final split | Final |
|---|---:|---:|---:|---:|---:|---:|
| m=211 | 4,867 | 1,848,957 | 118 | 36 | 13 shared + 23 typed | 0 |
| m=210 | 9,251 | 5,765,218 | 1,225 | 593 | 213 shared + 378 typed + 2 endpoint | 0 |

Two independent C++ row scanners agree. Joint states are independently reconstructed. A floating-point solver proposes only candidate Farkas multipliers; every counted LP exclusion is checked as an exact integer contradiction against a separately rebuilt named constraint system.

## Reproduce the non-Delta16 arithmetic

Standard library only:

```sh
python3 -I -B check_all_degrees.py > /tmp/n29-all-degrees.json
cmp /tmp/n29-all-degrees.json ALL_DEGREES_CHECK.json
```

This checks the Fan substitution, both Delta=15 witness tables, the exact Delta=17 factorisation, every Delta=18..27 h-index arithmetic case, the degree-sum bound, and an explicit graph check that `K(14,15)` is diameter-two edge-critical.

The full Delta=16 rerun is `.github/workflows/n29-d16.yml`; it uses the source in `project/research/n29/2026-09-08-delta16-direct-v1/` and the archived n=28 implementation antecedent. SciPy is used only for discovery/proposal; exact certificate verification is the proof-producing step.

## Audit trail

[FAILURE_HISTORY.json](FAILURE_HISTORY.json) records three failed hosted Delta=16 attempts before the successful run. They were environment/setup failures (missing SciPy, isolated Python hiding a user-site install, missing Boost headers); none is reported as a mathematical pass or counterexample.

[AUDIT.md](AUDIT.md) records the same-assistant adversarial review and remaining trust boundaries. [PROVENANCE.json](PROVENANCE.json) identifies source commits and preserved ancestors. [MANIFEST.json](MANIFEST.json) hashes the point-in-time review payload.

Frozen n=25/n=27/n=28 proofs, their archives, and the governed theorem ledger are unchanged.


\newpage

# Included source: `project/reviews/n29/2026-09-09-bridge-standalone-v1/GRAPH_TO_MODEL_BRIDGE.md`

# n=29, Delta=16: standalone graph-to-model bridge

9 September 2026. Research directed by Paul Lenz; mathematical development and internal audit by ChatGPT/Geeps.

**Status: candidate mathematics.** This note isolates the hand graph-theoretic bridge used before the finite `Delta=16` calculation in the n=29 Murty–Simon candidate. It is intentionally independent of the old n=28 inherited LP/joint machinery. External mathematical review remains open.

## 1. Scope and notation

Let `G` be a simple diameter-two edge-critical graph on `n=29` vertices with `Delta(G)=16`. Let `m=e(G)` be either `211` or `210`.

Put `H = complement(G)`. Choose a minimum-degree vertex `v` of `H`. Since `Delta(G)=16`,

```text
d_H(v)=29-1-16=12.
```

Set

```text
A = N_H(v),                 |A| = a = 12,
B = V(H) \ N_H[v],          |B| = b = 16.
```

Let `C=H[A]` and let `F` be the complement of `C` on the vertex set `A`. For `i in A`, write `d_i=d_F(i)`.

Define

```text
t = m - b(n-b) = m - 16*13,
```

so

```text
m=211 -> t=3,
m=210 -> t=2.
```

The purpose of this note is to derive the exact necessary conditions passed to the finite trusted-kernel calculation.

## 2. Complement form of edge-criticality

For an edge `uw` of `G`, the pair `uw` is a missing pair of `H`. Deleting `uw` from `G` is the same as adding `uw` to `H`.

Because `G` is diameter-two edge-critical, after deleting `uw` there is a pair of vertices at distance greater than two. Equivalently, in `H+uw` there is a new adjacent pair whose open `H+uw`-neighbourhoods together contain every vertex. Call such a pair an **adjacent total-dominating pair**.

Now take a missing pair `uw` of `H[B]`.

The new total-dominating pair in `H+uw` must use at least one endpoint of the newly added edge, since no other adjacency changed. It cannot be `{u,w}`, because both `u` and `w` miss `v`. Hence, after interchanging `u,w` if necessary, there exists a vertex `i` such that

```text
ui is already an edge of H,
N_H(u) union N_H(i) = V(H) \ {w}.
```

The vertex `i` must lie in `A`, because the pair must dominate `v` and `u` does not neighbour `v`.

We write

```text
ui -> w.
```

Thus every missing unordered pair `{u,w}` in `H[B]` admits at least one selected cross-edge of this form.

## 3. Selected-edge injection

Choose exactly one such cross-edge for every missing unordered pair in `H[B]`.

A selected edge `ui -> w` determines both its source `u` and its unique exception `w`: by definition `w` is the unique vertex not covered by `N_H(u) union N_H(i)`. Therefore two different missing unordered `B`-pairs cannot select the same cross-edge.

Hence the choice gives an injection

```text
{missing unordered pairs of H[B]} -> E_H(A,B).
```

Call the chosen cross-edges **selected**. Call all other existing `A-B` edges of `H` **residual**.

For `u in B` define

```text
rho_u = residual degree of u into A,
q_u   = number of selected edges with source u,
p_u   = number of selected missing B-pairs whose supplement/exception is u.
```

For `i in A` define

```text
R_i = residual degree of i into B,
x_i = selected degree of i into B.
```

Let

```text
r = sum_{u in B} rho_u = sum_{i in A} R_i.
```

## 4. Exact edge ledger

Every unordered pair of `B` is exactly one of:

1. an edge of `H[B]`; or
2. a missing pair of `H[B]`, and therefore corresponds injectively to one selected cross-edge.

Thus

```text
#selected cross-edges + e(H[B]) = C(b,2).
```

On the other hand, counting missing edges of `H` relative to the complete bipartite cut determined by `v,A,B` gives the standard surplus identity

```text
e(F)=r+t.
```

Therefore

```text
sum_i d_i = 2(r+t).                    (4.1)
```

This identity is exact, not an inequality.

## 5. Label demand

Since `v` has minimum degree `a=12` in `H`, every `i in A` has `d_H(i)>=12`.

The neighbours of `i` in `H` are:

- `v`;
- the `C`-neighbours of `i` inside `A`, of which there are `a-1-d_i`;
- `R_i` residual neighbours in `B`;
- `x_i` selected neighbours in `B`.

Hence

```text
1 + (a-1-d_i) + R_i + x_i >= a,
```

so

```text
x_i >= d_i-R_i.
```

Define

```text
s_i = max(0,d_i-R_i),
S   = sum_i s_i.
```

Then

```text
x_i >= s_i.                              (5.1)
```

Summing and using the selected-edge ledger gives

```text
S >= r+2t.                               (5.2)
```

Thus a label of demand `s_i` genuinely requires at least `s_i` distinct selected source incidences.

## 6. Forcing from a selected edge

Fix a selected edge

```text
ui -> w.
```

By definition,

```text
N_H(u) union N_H(i) = V(H) \ {w}.
```

We now derive the pointwise inequalities used later.

### 6.1 `d_i <= rho_u + R_i`

Let `j` be an `F`-neighbour of `i`, so `ij` is missing in `H[A]`.

Since `j != w`, the covering property forces `uj in E(H)`.

Among such `uj` edges, at most `rho_u` are residual. Every remaining one is selected from source `u`; its supplement is a `B`-vertex adjacent to `i`, and distinct selected edges at source `u` have distinct supplements. Those supplement incidences are residual at label `i`.

Hence the `d_i` different `F`-neighbours are accounted for by at most `rho_u` residual source incidences plus `R_i` residual label incidences:

```text
d_i <= rho_u + R_i.                     (6.1)
```

### 6.2 `d_i <= rho_u + rho_w`

For the same `F`-neighbour `j` of `i`, the covering property also forces the corresponding residual incidence at the supplement side unless `uj` itself is residual. Distinct `F`-neighbours give distinct incidences. Therefore

```text
d_i <= rho_u + rho_w.                    (6.2)
```

### 6.3 `d_i <= rho_u + q_u - 1`

Every `F`-neighbour `j` of `i` forces `uj in E(H)`. Source `u` has exactly `rho_u+q_u` cross-neighbours in `A`, one of which is `i` itself. Therefore

```text
d_i <= rho_u + q_u - 1.                  (6.3)
```

### 6.4 Supplement forcing

Consider any other selected edge `uj -> z` at the same source `u`. Since `ui -> w` covers every vertex except `w`, the supplement `w` must be adjacent in `H` to `j` unless `j` is already covered by `u`; tracking the distinct selected labels yields

```text
rho_w + q_w >= q_u - 1.                  (6.4)
```

In particular, a source with large `q_u` requires many compatible supplement incidences.

## 7. Exact missing-degree identity in B

For a fixed `u in B`, every missing pair of `H[B]` incident with `u` is oriented exactly one of two ways by our selected choice:

- outward from `u`, counted by `q_u`; or
- inward to `u`, counted by `p_u`.

Therefore

```text
q_u+p_u = missing degree of u in H[B].   (7.1)
```

Consequently

```text
d_H(u) = rho_u + (b-1) - (q_u+p_u).
```

Since `d_H(u)>=a`,

```text
p_u <= rho_u + (b-a-1) = rho_u+3.        (7.2)
```

Also trivially

```text
q_u+p_u <= b-1 = 15.                     (7.3)
```

And because source `u` has only `a` cross-neighbours available,

```text
q_u+rho_u <= a = 12.                     (7.4)
```

## 8. Endpoint load at a selected label

Again fix `ui -> w`.

The following are distinct `B`-neighbours of label `i` in `H`:

1. the source `u` itself;
2. the `q_u-1` supplements of the other selected edges from source `u`;
3. the `p_u` sources of selected pairs oriented into `u`.

The last two families cannot collide: such a collision would orient the same missing unordered `B`-pair in both directions.

Hence label `i` has at least

```text
q_u+p_u
```

cross-neighbours in total. Since its residual and selected cross-degrees are `R_i` and `x_i`,

```text
R_i+x_i >= q_u+p_u.                      (8.1)
```

## 9. Residual activity when `t>0`

We prove that every `B`-vertex has positive residual degree.

Suppose, for contradiction, that `rho_u=0` for some `u in B`.

Let

```text
U=N_A(u),
T=A\U.
```

Every cross-edge from `u` is then selected. There is no `F`-edge between `U` and `T`: if `i in U`, `j in T`, and `ij in F`, then the selected edge at `ui` would have to cover `j`, forcing `uj in H`, contradiction.

Now count residual cross-edges forced by `F`.

- Each `F`-edge inside `U` forces two distinct residual cross-edges through the distinct supplements of its endpoints.
- Each `F`-edge inside `T` is a missing pair of `H[A]`. Its quasi-edge auxiliary cannot be `v` or `u`; an auxiliary in `A` would contradict the absence of `F(U,T)`. Therefore it yields a distinct residual cross-edge with `A`-endpoint in `T`.

These families are disjoint. Hence

```text
r >= 2e(F[U]) + e(F[T]).
```

Since there are no `F`-edges between `U` and `T`,

```text
e(F)=e(F[U])+e(F[T]),
```

so

```text
r >= e(F)+e(F[U]) >= e(F)=r+t.
```

But `t>0`, contradiction.

Therefore

```text
rho_u >= 1 for every u in B,             (9.1)
r >= b = 16.                             (9.2)
```

## 10. Charging inequality

For each label `i`, choose exactly `s_i` of its selected source incidences; this is possible by (5.1).

If source `u` is chosen for label `i`, then (6.1) gives

```text
s_i <= d_i-R_i <= rho_u,
```

so

```text
rho_u >= s_i.                             (10.1)
```

Also `q_u<=a-rho_u` by (7.4).

Assign to each chosen incidence from source `u` the charge

```text
(rho_u-1)/(a-rho_u).
```

A source contributes to at most `q_u<=a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Summing over all `B`-sources gives total charge at most

```text
sum_u (rho_u-1) = r-b.
```

For a label of demand `s_i`, every chosen source has `rho_u>=s_i`, and the function

```text
(rho-1)/(a-rho)
```

is increasing for `1<=rho<a`. Therefore that label receives charge at least

```text
s_i(s_i-1)/(a-s_i).
```

Hence

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i).         (10.2)
```

Combining (10.2) with `S>=r+2t` yields

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t.     (10.3)
```

For `a=12,b=16`,

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 16+2t.
```

This is the principal demand-domain inequality.

## 11. Threshold-capacity inequality

For an integer `h>=1`, define

```text
I_h = {i in A : s_i>=h},
W_h = sum_{i in I_h} s_i,
Z_h = {u in B : rho_u>=h},
z_h = |Z_h|.
```

Every selected incidence used to satisfy the demand of a label in `I_h` must come from a source in `Z_h`, by (10.1).

A source in `Z_h` can contribute at most one selected orientation to any unordered `B`-pair. Counting the available oriented pair capacity among the high-residual sources, together with the unavoidable low-end contribution from the threshold itself, gives the necessary inequality

```text
2W_h <= z_h^2-z_h+h(h+1).                (11.1)
```

This is a necessary Hall-type capacity bound; it is not asserted to be sufficient.

Residual activity and an upper bound `r<=r_max` also give, for `h>=2`,

```text
z_h <= floor((r_max-b)/(h-1)).            (11.2)
```

Conversely, if `max_i s_i=H`, then necessarily

```text
z_H>=H.                                   (11.3)
```

These threshold bounds replace the older pair-capacity support formula in the minimal trusted kernel.

## 12. Excluding `delta(C)=0`

The finite calculation also requires an explicit upper bound on `F`-degrees. We now derive it directly.

Suppose `C` has an isolated vertex `x`. Let `X=A\{x}`.

Every missing pair of `H` inside `X` has a quasi-edge whose auxiliary must lie in `B`; otherwise the required covering of `x` fails. Distinct such pairs force distinct residual cross-edges with `A`-endpoint in `X`.

For each `B`-endpoint already used by one of these residual edges, the quasi-edge structure forces a further residual edge incident with `x`. For every unused `B`-endpoint, residual activity supplies at least one residual edge. Thus there are at least `b` additional residual edges disjoint from the first family.

Writing

```text
L = C(a,2)-t,
```

we obtain the necessary inequality

```text
b <= L - C(a-1,2).                        (12.1)
```

At `a=12,b=16`,

```text
L=66-t,
L-C(11,2)=11-t,
```

so (12.1) would require

```text
16 <= 11-t,
```

impossible for both `t=3` and `t=2`.

Therefore

```text
delta(C)>=1.                              (12.2)
```

Consequently every `F`-degree satisfies

```text
d_i<=10.                                  (12.3)
```

Also `e(C)>=6`. Since

```text
e(C)+r = C(a,2)-t = 66-t,
```

we get

```text
r<=60-t.                                  (12.4)
```

This is the previously implicit bridge behind the old scanner bounds; it is now explicit.

## 13. What is passed to the finite trusted kernel

A graph in either dense `Delta=16` scope must therefore induce integer data satisfying all of the following:

```text
a=12, b=16, t in {3,2};
1<=rho_u<=12;
0<=d_i<=10;
r=sum rho=sum R;
e(F)=r+t;
s_i=max(0,d_i-R_i);
S>=r+2t;
q_u+rho_u<=12;
p_u<=rho_u+3;
q_u+p_u<=15;
for selected ui->w:
  d_i<=rho_u+R_i,
  d_i<=rho_u+rho_w,
  d_i<=rho_u+q_u-1,
  rho_w+q_w>=q_u-1,
  R_i+x_i>=q_u+p_u;
charging inequality (10.3);
threshold-capacity inequalities (11.1)-(11.3);
r<=60-t.
```

The minimal finite pipeline deliberately enumerates a **superset** of graph-realizable data satisfying these necessary conditions. Rejecting every such arithmetic state is therefore sufficient to exclude an actual graph, provided every pruning step is itself a necessary relaxation and every final infeasibility certificate is checked exactly.

## 14. Trust boundary

This note does not claim to prove the finite LP/certificate stage. It isolates the graph-theoretic bridge that an external reviewer should attack first.

The highest-value possible falsifications are:

1. a missing `B`-pair for which the selected cross-edge construction fails;
2. a collision invalidating selected-edge injection;
3. a counterexample to residual activity;
4. a label demand `s_i` that cannot be tied to `s_i` distinct sources of residual degree at least `s_i`;
5. a charging-budget failure;
6. a counterexample to the threshold-capacity inequality;
7. a configuration with `delta(C)=0` escaping (12.1).

Until those points receive independent expert review, the n=29 result remains a candidate theorem.


\newpage

# Included source: `project/reviews/n29/2026-09-09-bridge-standalone-v1/BRIDGE_REDTEAM.md`

# Hostile audit of the standalone n=29 Delta=16 graph-to-model bridge

9 September 2026. Audit performed by ChatGPT/Geeps. Same-assistant red-team only; independent expert review remains open.

## Verdict

No blocking counterexample has been found in the bridge after rederiving the implications from the graph definitions.

One real exposition defect was found immediately in the first standalone draft: the threshold-capacity lemma was stated with an over-compressed justification. It is now expanded separately in `THRESHOLD_CAPACITY_LEMMA.md`. The defect was in exposition/traceability, not a discovered reversal of the inequality.

The current highest-risk hand obligations remain the quasi-edge injection, residual-activity lemma, and the `delta(C)=0` exclusion. These should receive external review before any theorem promotion.

## Audit method

For every displayed implication in `GRAPH_TO_MODEL_BRIDGE.md`, the audit asked:

1. Is the conclusion necessary for every actual graph, or only typical?
2. Is an injection being assumed where only a many-to-one map is known?
3. Can two forced residual edges collide?
4. Can a cross-edge counted as residual actually be selected in the opposite orientation?
5. Does a selected-edge claim rely on the exception being in `B`?
6. Is an upper bound substituted where a lower bound is required, or vice versa?
7. Does grouping or sorting silently assume graph symmetry?

## RT-BRIDGE-001 — complement/quasi-edge construction

**Attack.** After adding a missing `B`-edge `uw` to `H`, could the new adjacent total-dominating pair avoid both `u,w`, or equal `{u,w}`, or use an auxiliary outside `A`?

**Resolution.** No other adjacency changes, so a genuinely new adjacent pair must use `u` or `w`. The pair `{u,w}` still misses `v`. If the pair is `{u,i}`, then `u` misses `v`, so domination of `v` forces `iv in H`, hence `i in A`. Before insertion `{u,i}` covered every vertex except `w`, otherwise it would already have been total-dominating in `H`.

**Verdict:** survives.

## RT-BRIDGE-002 — selected-edge injection

**Attack.** Could two missing unordered `B`-pairs select the same cross-edge `ui`?

**Resolution.** The cross-edge determines its `B` source `u`; the unique vertex omitted by `N_H(u) union N_H(i)` determines the supplement `w`. Thus the missing pair `{u,w}` is recovered from the selected edge.

At a fixed source, selected labels are distinct because the selected objects are edges. Supplements are distinct because the same source-supplement pair is one missing unordered `B`-pair, for which only one selected orientation is chosen.

**Verdict:** survives.

## RT-BRIDGE-003 — exact ledger

Starting from

```text
q_total + e(H[B]) = C(b,2),
```

and

```text
e(H)=a+e(C)+r+q_total+e(H[B]),
```

with `e(C)=C(a,2)-e(F)` and `n=a+b+1`, direct simplification gives

```text
m=e(G)=b(n-b)+e(F)-r.
```

Therefore

```text
t=m-b(n-b)=e(F)-r,
e(F)=r+t.
```

No approximate or asymptotic identity is used.

**Verdict:** survives.

## RT-BRIDGE-004 — demand implication

Minimum `H`-degree gives

```text
x_i >= d_i-R_i,
```

hence `x_i>=s_i=max(0,d_i-R_i)`.

Also

```text
S=sum s_i >= sum(d_i-R_i)
             =2(r+t)-r
             =r+2t.
```

The inequality is in the safe direction: replacing `max(0,d_i-R_i)` by `d_i-R_i` only lowers the sum.

**Verdict:** survives.

## RT-BRIDGE-005 — source-demand injection `s_i<=rho_u`

Fix selected `ui->w` and an `F`-neighbour `j` of `i`. Then `uj in H` because `{u,i}` must dominate `j`.

If `uj` is residual, charge `j` to one of the `rho_u` residual source slots.

If `uj` is selected, write `uj->z`. Distinct selected labels at source `u` have distinct supplements. Since `ui->w` must dominate `z != w` and `uz` is missing in `H[B]`, `iz in H`. Moreover `iz` cannot itself be selected: both `i` and `z` miss `j` (`ij` is an `F`-edge and `z` is the exception of `uj->z`), whereas a selected cross-edge has its unique exception in `B`, not in `A`. Thus `iz` is residual.

This injects every `F`-neighbour not charged to a residual source edge into a distinct residual edge at label `i`, yielding

```text
d_i<=rho_u+R_i,
s_i<=rho_u.
```

**Verdict:** survives; this is one of the most important bridge steps.

## RT-BRIDGE-006 — pair residual inequality `d_i<=rho_u+rho_w`

Again fix `ui->w` and `F`-neighbour `j`.

If `uj` is residual, charge to `rho_u`. Otherwise `uj->z` with `z!=w`. Since that quasi-edge must dominate `w` and `uw` is missing, `jw in H`.

The edge `jw` cannot be selected from source `w`: both `w` and `j` miss `i` (`wi` is missing because `w` is the exception of `ui->w`, and `ji` is an `F`-edge), which would leave an `A`-vertex undominated. Therefore `jw` is residual.

Distinct `j` give distinct residual `w-j` edges, proving

```text
d_i<=rho_u+rho_w.
```

**Verdict:** survives.

## RT-BRIDGE-007 — supplement forcing

For every other selected `uj->z` at source `u`, `z!=w`. The pair `{u,j}` must dominate `w`; since `uw` is missing, `jw in H`. The `q_u-1` other selected labels are distinct, so `w` has at least `q_u-1` cross-neighbours among those labels. They are partitioned into residual and selected edges at source `w`, hence

```text
rho_w+q_w>=q_u-1.
```

**Verdict:** survives.

## RT-BRIDGE-008 — exact `q+p` missing degree and endpoint load

Every missing unordered `B`-pair incident with `u` is oriented either outward from `u` or inward to `u`, exactly once. Thus `q_u+p_u` is exactly the missing degree of `u` in `H[B]`.

For selected `ui->w`, the following `B`-vertices are distinct neighbours of `i`:

- `u`;
- supplements of the other `q_u-1` outward arcs at `u`;
- sources of the `p_u` incoming arcs into `u`.

An incoming source cannot equal an outgoing supplement, because that would assign both orientations to the same missing unordered pair. For an incoming source `z`, the pair `uz` is missing and `z!=w`; since `ui->w` must dominate `z`, `iz in H`. The same covering argument handles outgoing supplements.

Therefore

```text
R_i+x_i>=q_u+p_u.
```

**Verdict:** survives.

## RT-BRIDGE-009 — residual activity

Assume `rho_u=0`, put `U=N_A(u)`, `T=A\U`.

Because every `u-i` with `i in U` is selected, an `F`-edge from `U` to `T` would contradict the selected quasi-edge's need to dominate its `T` endpoint. Hence `F(U,T)` is empty.

For each `F`-edge `ij` in `U`, the two selected edges from `u` to `i,j` have distinct supplements. Cross-domination forces two residual edges `i-w_j` and `j-w_i`. They are residual because each would otherwise fail to dominate the opposite `A` endpoint. The mapping from the ordered endpoints of `F[U]` to these residual edges is injective.

For an `F`-edge `ij` in `T`, adding `ij` to `H` creates a quasi-edge. Its auxiliary cannot be `v` (the pair would miss `u`), cannot be `u` (no adjacency), and cannot lie in `A`: to dominate `u`, an `A` auxiliary would have to lie in `U`, but being the auxiliary for exception in `T` would require an `F(U,T)` edge. Therefore an auxiliary lies in `B`, producing a residual cross-edge with `A` endpoint in `T`. Different `F[T]` pairs give different cross-edges because the edge plus its unique `A` exception recover the pair.

The `F[U]` and `F[T]` residual families are disjoint by their `A` endpoints. Hence

```text
r>=2e(F[U])+e(F[T])>=e(F)=r+t,
```

contradicting `t>0`.

**Verdict:** survives after explicit collision audit.

## RT-BRIDGE-010 — charging inequality

For each label choose `s_i` actual selected incidences. Each chosen source satisfies `rho_u>=s_i`. A chosen source also has `q_u>=1`, so `rho_u<=a-1`; the denominator `a-rho_u` is never zero.

Source `u` has at most `a-rho_u` selected incidences in total. Charging each chosen incidence by

```text
(rho_u-1)/(a-rho_u)
```

therefore charges source `u` by at most `rho_u-1`. The charge function is increasing in integer `rho` on `[1,a-1]`, so a demand-`s_i` label receives at least

```text
s_i(s_i-1)/(a-s_i).
```

Summation gives the claimed inequality.

**Verdict:** survives.

## RT-BRIDGE-011 — threshold-capacity proof compression

**Finding:** the first standalone draft did not contain enough detail to justify

```text
2W_h<=z_h^2-z_h+h(h+1).
```

This was an exposition/traceability failure and was not accepted silently.

**Repair:** `THRESHOLD_CAPACITY_LEMMA.md` now gives the complete high-load-source/unordered-pair proof. It uses only:

- `s_i<=rho_u`;
- distinct selected labels and supplements;
- one selected orientation per missing unordered `B`-pair.

No old `pair_capacity()` implementation is a dependency.

**Verdict after repair:** no mathematical defect found.

## RT-BRIDGE-012 — `delta(C)=0` exclusion

This remains the least compact bridge step. The hostile audit rechecked the counting logic used to obtain

```text
b<=[C(a,2)-t]-C(a-1,2).
```

For `a=12,b=16,t in {2,3}` the right side is only `9` or `8`, respectively, so any valid version of the injection has large slack.

The proof depends on separating a family of residual cross-edges forced by missing pairs inside `A\{x}` from an additional family covering all `B` endpoints, using residual activity. No collision was found in the rederivation, but this is specifically marked for external review because it compresses several quasi-edge uniqueness arguments.

**Verdict:** no defect found; elevated review priority.

## Overall conclusion

The bridge has now been reduced to a small set of hand obligations with explicit injection/collision arguments. The finite trusted kernel begins only after these obligations.

No theorem status is promoted. A single counterexample to any universal bridge lemma overrides every green workflow downstream.


\newpage

# Included source: `project/reviews/n29/2026-09-08-redteam-restart-v1/PUBLIC_RELEASE_AUDIT.md`

# N=29 public-release audit and corrected trusted-kernel status

8 September 2026.

**Status:** public-release preparation note. The n=29 result remains a **candidate theorem**, not an externally reviewed theorem. This file records the late hostile audit, the defect found in an auxiliary verifier, the correction, and the reduced proof-critical computational path.

## 1. Purpose

Before public release, the n=29 argument was attacked from the graph-to-model bridge rather than by merely rerunning the original computation. The goal was to identify the smallest set of mathematical lemmas and exact computational steps that an external reviewer must trust.

The audit deliberately treated implementation agreement as secondary evidence. A repeated calculation is not useful if two programs encode the same invalid mathematical implication.

## 2. Graph-to-model bridge: current audit outcome

No blocking defect was found in the following proof-critical graph implications after fresh hostile rederivation:

- complement/quasi-edge construction from a missing pair in `H[B]`;
- uniqueness of the exception and injection from missing unordered `B`-pairs to selected cross-edges;
- distinction between selected and residual cross-edges;
- exact edge ledger `e(F)=r+t`, `sum d_i=2(r+t)`, `sum R_i=r`;
- minimum-degree implication `x_i >= s_i`, where `s_i=max(0,d_i-R_i)`;
- source/supplement forcing inequalities, including `s_i <= rho_u` for a selected source;
- residual activity for `t>0`: every `B`-source has `rho_u>=1`;
- source and supplement capacity bounds;
- charging inequality and its summed demand consequence;
- threshold-capacity inequality for high-demand labels and high-residual sources;
- source-local degree-load inequality used by the stronger endpoint formulations.

This is still same-assistant mathematical review. It materially increases confidence but does not replace an independent mathematician.

## 3. A real defect was found in the additional threshold verifier

The hostile dimensional audit found a genuine normalization error in the first cumulative-threshold verifier:

- historical source: `independent_threshold_model.py`;
- affected evidence: the first cumulative-threshold v1 certificates;
- nature of error: a grouped label multiplicity was applied twice in the label-side selected-incidence/tail equation.

The grouped selected-incidence variable is normalized per source-label pair. Therefore the correct per-label identity is schematically

```text
sum_k n_k Z_kg = sum_h T_h,
```

whereas v1 encoded

```text
sum_k n_k Z_kg = n_g * sum_h T_h.
```

For any label group of multiplicity `n_g>1`, this can overconstrain the relaxation.

### Consequence

The v1 cumulative-threshold certificates are **invalid as proof evidence** and should not be cited.

The defect is confined to that additional verifier. It does not occur in:

1. the original n=29 direct197-derived route;
2. the separate fully fresh n=29 Delta=16 implementation; or
3. the corrected cumulative-threshold v2 model.

The flawed v1 file is intentionally retained so the failure history remains auditable.

## 4. Corrected v2 threshold verifier

The corrected implementation is:

- `independent_threshold_model_v2.py`.

The replay workflow was changed to use v2 and completed successfully.

Corrected v2 results:

| Edge count | Projected rows | Exact rejections | Final survivors | Exact certificate RHS range |
|---:|---:|---:|---:|---:|
| 211 | 118 | 118 | 0 | -795 to -40 |
| 210 | 1,225 | 1,225 | 0 | -999801 to -1 |

Every exclusion was re-verified after aggregation using exact integer arithmetic. The report is `INDEPENDENT_THRESHOLD_REPORT.json` with schema `n29-independent-threshold-flow-complete-v2`.

Evidence commit:

```text
18937b3ef39b1f73bac1af718c3064b257b6e53d
Preserve corrected v2 n29 threshold-flow certificates
```

## 5. Minimal trusted kernel

After the graph-to-model audit, several older finite stages were found to be unnecessary for a proof-critical n=29 Delta=16 route.

The preferred reduced chain is now:

```text
quasi-edge / selected-residual construction
        -> residual activity
        -> charging inequality
        -> exact threshold-capacity inequality
        -> exact source-capacity dual pruning
        -> simple residual-row Hall/refinement scanner
        -> corrected v2 cumulative-threshold/source-q-flow LP
        -> exact integer Farkas checker
```

The following older machinery is no longer required by this reduced route:

- old pair-capacity support formula;
- projected pair screen;
- joint propagator;
- shared-adjacency LP;
- degree-typed LP;
- old endpoint LP.

Those stages remain preserved as independent/redundant assurance and as research history.

## 6. Minimal-kernel clean replay

The clean GitHub Actions workflow `n29-minimal-kernel.yml` completed successfully.

Its exact result is recorded in `MINIMAL_KERNEL_REPORT.json`:

| Edge count | `t` | Retained demands | Residual rows | Exact Farkas rejections | Final survivors |
|---:|---:|---:|---:|---:|---:|
| 211 | 3 | 72 | 126 | 126 | 0 |
| 210 | 2 | 367 | 1,467 | 1,467 | 0 |

The aggregate checker rebuilt the corrected v2 model for every residual row and re-verified every saved integer certificate.

The report explicitly records:

```text
uses_projected_screen = false
uses_joint_propagator = false
uses_old_shared_typed_endpoint_models = false
uses_old_pair_capacity_support_formula = false
all_late_exclusions_exact_integer_farkas_reverified = true
final_survivors = 0
```

Clean workflow run:

```text
34274211354
```

## 7. Interpretation

The late audit changed the evidence hierarchy in a useful way:

- one auxiliary verification route was shown to contain a genuine bug;
- that route was corrected and still closes the full frontier;
- the proof-critical finite chain was then simplified substantially;
- the simplified chain also closes cleanly with exact certificates.

This does **not** upgrade n=29 from candidate to theorem. The principal remaining risk is the correctness and novelty of the hand graph-theoretic bridge, not whether the existing finite arithmetic can be rerun.

## 8. What an external reviewer should check first

Highest priority:

1. quasi-edge construction and injection;
2. residual-activity lemma;
3. `s_i<=rho_u` source-demand implication;
4. charging inequality;
5. threshold-capacity lemma;
6. exact source-capacity Hall relaxation;
7. dimensional normalization and necessity of every corrected-v2 LP constraint;
8. exact Farkas verification logic.

A counterexample to any one of the universal graph lemmas should be treated as a blocking result even if all workflows remain green.

## 9. Public-review status

Independent mathematical review: **OPEN**.

Independent external computational reproduction: **OPEN**.

Novelty assessment: **OPEN**.

Unrestricted Murty–Simon conjecture: **NOT CLAIMED SOLVED**.
