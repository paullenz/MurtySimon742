# Source-premise repair: beta orientation, selected semantics, and B_beta counting

19 September 2026. Internal adversarial repair checkpoint for the eventual dense D2C programme.

**Status:** upstream interface repair. This note does not promote an eventual second-extremal theorem. It addresses the two explicit premises isolated by the 19 September daily red-team audit before any further use of the finite source-tuple hierarchy.

## 1. Correction to the first graph-level checker

The first version of `check_source_premises_graph_level.py` labelled one rooted certificate family "beta", but its adjacency conditions were actually the **matched-source / alpha orientation** of a physical P--U edge.

For a physical edge `yq_i`, with `y in U`, tight mate `q_i'`, and `x in A`:

- alpha / matched-source orientation has
  `x~y`, `x!~q_i`, and `N_G(x) cap N_G(q_i)={y}`;
- beta / unmatched-source orientation has
  `x!~y`, `x~q_i`, and `N_G(x) cap N_G(y)={q_i}`.

The old checker implemented the first family. Its earlier zero-collision result therefore was **not evidence for beta-source P1**. That evidence is withdrawn. The corrected checker now computes the two orientation families separately.

This correction is preserved explicitly because the graph-to-constraint interface is the current audit bottleneck.

## 2. P1 follows directly from raw rooted criticality

Recall P1:

> For a fixed A-witness `x`, beta obligations on distinct target fibres use distinct physical unmatched sources.

Suppose instead that the same physical `y in U` and the same `x in A` beta-certify two distinct P--U edges `yq_i` and `yq_j`, where `i != j`.

The beta criticality orientation gives

`N_G(x) cap N_G(y)={q_i}`

from the first edge, and

`N_G(x) cap N_G(y)={q_j}`

from the second.

But `q_i != q_j` because the targets lie in different tight fibres. One fixed common-neighbour set cannot equal two different singletons. Contradiction.

Therefore:

> **DISTINCT PHYSICAL BETA-SOURCE LEMMA.** For fixed `x`, the designated beta sources attached to distinct target fibres are pairwise distinct.

This proof uses only the unique-common-neighbour criticality certificate for the beta orientation. It does not use the source-tuple theorem, Hamming geometry, or any later beta-reuse statement.

Consequently the later notation

`Y_x={y_i:i in I_x}`

really is a set of physical vertices and

`ell_x=|I_x|=|Y_x|<=min(p,u)`.

This repairs the main premise on which the finite source-tuple theorem depends.

## 3. P2 is selected-representative uniqueness, not raw-witness uniqueness

P2 says:

> For a fixed physical source `y` and tight coordinate `i`, at most one **selected** witness uses the source-coordinate obligation `(y,i)`.

There is exactly one physical P--U edge `yq_i` associated with that source-coordinate pair: `y` chooses exactly one endpoint `q_i` of tight fibre `i`.

The canonical selected/residual bridge chooses **one selected representative per physical rooted B-edge** (equivalently one selected representative for the corresponding missing unordered B-pair in the complement), after choosing its orientation. If the representative of `yq_i` is beta-oriented from `y`, it is represented by one selected cross edge `yx`. Hence the selected system contains that physical `(y,i)` obligation once.

Raw beta witnesses need not be unique in principle. The source-tuple proof never needs raw uniqueness: it needs uniqueness of the chosen selected representative. The distinction is now made explicit in the live audit boundary.

## 4. P1 is also consistent with selected-edge simplicity

The canonical bridge gives a second, independent route to the same conclusion.

A selected cross edge recovers the physical rooted B-edge / missing unordered B-pair that it represents. Thus two distinct physical obligations cannot choose the same selected cross edge. In particular, for fixed unmatched source `y`, two beta-oriented obligations at different coordinates cannot both use the same cross edge `yx`.

So P1 is supported twice:

1. directly, by the raw beta common-neighbour singleton argument in Section 2;
2. at the selected-system level, by simple selected-incidence injectivity.

The first route is preferable as the premise proof because it does not depend on importing the broader canonical Hall formalism.

## 5. What B_beta counts

The audit also required checking whether downstream lower bounds called `B_beta` count distinct selected physical obligations or pre-deduplication witness incidences.

In the unmatched-row capacity construction, for each matched endpoint `q` let `h_q` count the physical P--U obligations whose chosen representative is alpha-oriented from `q`. There are exactly `pu` physical P--U edges, one for each unmatched source and tight fibre. Therefore

`B_beta = pu - sum_q h_q`

is exactly the number of physical P--U obligations whose **selected** representative is beta-oriented.

For an A-vertex `x`, let `ell_x` be the number of selected beta obligations using `x). Selected-edge injectivity and the P1 lemma imply that these are distinct physical source-coordinate obligations. Hence

`B_beta = sum_{x in A} ell_x`.

There is no pre-deduplication multiplicity hidden in this identity.

### Alpha-capacity lower bounds

For a fixed matched source `q`, every alpha-oriented selected obligation uses a distinct selected cross edge `qx`, and every such `x` has the forced code `alpha(q)`. Therefore

`h_q <= n_{alpha(q)}`.

Summing gives

`B_beta >= pu - W_alpha`,

where

`W_alpha=sum_{q in P} n_{alpha(q)}`.

If `mu_alpha=max_c |alpha^{-1}(c)|`, then

`W_alpha <= mu_alpha a`,

so

`B_beta >= [pu-mu_alpha a]_+`.

All of these inequalities are therefore lower bounds on the same count of **distinct selected physical beta obligations**.

The commonly used root-imbalance floor is the trivial `mu_alpha<=p` specialization:

`B_beta >= p(lambda+1-2p)_+`,

because `a=2p+u-lambda-1`.

The above-threshold switching/Hall lower bound replaces `p` by the sharper allowed `R_hat` and has the same selected-obligation semantics.

Thus the lower-bound side of the source-tuple applications is compatible with the selected-system quantity appearing in the independently re-derived finite capacity theorem.

## 6. Corrected graph-level regression

The corrected independent checker now:

1. rejects every non-D2C fixture before constructing rooted objects;
2. reconstructs tight antipodes from the raw definition;
3. computes alpha and beta rooted certificate families separately;
4. checks the raw P1 collision condition on the genuine beta family;
5. reports raw P2 multiplicity without conflating it with selected P2;
6. installs the explicit published-figure `X_3` reconstruction as a mandatory hostile control.

Independent local replay of the corrected logic gives on the complete graph atlas through order seven:

- 21 unlabeled D2C classes;
- 126 rooted instances;
- 2 raw beta candidate certificates;
- 1 raw alpha candidate certificate;
- 0 P1 collisions;
- 0 raw P2 collisions in this small sample.

These finite facts are regression evidence only. P1 and selected P2 are established by the hand arguments above, not by absence of a small counterexample.

For `X_3`, the checker verifies:

- `n=12`;
- `m=32>M(12)=31`;
- diameter two and edge criticality;
- at the canonical cube root, `|A|=3`, `|B|=8`, four tight antipode pairs and `u=0`;
- hence no unmatched beta obligation exists.

The hostile control is therefore retained rather than accidentally excluded by the repaired premises.

## 7. Consequence for the source-tuple trust boundary

The daily red-team audit independently re-derived the finite source-tuple capacity theorem conditional on P1 and P2.

This checkpoint supplies internal direct proofs of both named premises at the exact level needed by that theorem:

- P1: raw beta criticality;
- P2: one chosen selected representative for the unique physical `(y,i)` obligation.

It also checks that the principal `B_beta` lower bounds count the same selected physical obligations.

Accordingly, the finite source-tuple theorem no longer needs to be labelled conditional on **unverified P1/P2**. It remains conditional on the broader rooted partial-Boolean and canonical selected-representative construction, whose independent end-to-end graph regression is still incomplete. That broader interface remains an audit priority.

This is a trust-boundary improvement, not an eventual D2C theorem.

## 8. Next work

The red-team priority order can now advance one step:

1. extend the graph-level checker beyond the two source premises into actual selected Hall objects and the rigid-witness quantities, with `X_3` permanently installed;
2. independently replay the exact one-code pair-local quantities `Ccap_P`, `(ONE)`, and `(CROWD)` on graph-derived rooted data wherever their hypotheses occur;
3. only then resume forward one-code rigid-branch mathematics;
4. keep the four-exception gate subordinate unless it becomes load-bearing.

Any future mismatch between graph-derived quantities and the abstract selected-system formulas is a proof blocker and must not be tuned away.
