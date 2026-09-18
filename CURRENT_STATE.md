# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `DAILY_RED_TEAM_AUDIT_RECONCILED_2026_09_19`

WORK MODE: `AUDIT`

INSPECTED PREDECESSOR: `3d17a816eb4f95b149a5f02ef1fc36bc298b6bae`

LAST VERIFIED RESULT: No fatal mathematical contradiction was found in the current load-bearing rooted-witness/Hall/rigid-U-witness spine. The finite source-tuple capacity theorem, including its finite arbitrary-subset layer-cake deficit form, has now been independently re-derived conditional on two explicit shared premises: each witness source set contains distinct physical sources, and the selected-representative system gives global uniqueness for each physical source-coordinate obligation. These two premises and the wider graph-to-constraint interface remain the principal end-to-end verification gap. The explicit `X_3` construction has independently replayed as a 12-vertex, 32-edge D2C graph. Repository audit also found and repaired status-parser, valid-directory-link, and protected-review-index regressions.

UNPRESERVED WORK: None.

DEFERRED ADMIN: Historical Git-LFS checkout warnings for seven legacy ZIP paths remain preserved and have not been altered because they are not blocking the live mathematics and touch frozen historical evidence.

NEXT ACTION: Verify the distinct-source and selected source-coordinate uniqueness premises directly from the rooted criticality construction; then attack the one-code rigid branch with the exact `Ccap_P` formula plus `(ONE)` and `(CROWD)`; in parallel build a genuinely graph-level regression on realizable small D2C graphs including `X_3`.

## Audit interval and evidence

The preceding 24-hour interval was compared from `f2e85599491d9804084e9739e1cfcdc6cc088a29` to pre-audit head `0060acd80a376074486563bc537386fe130459d2`, a span of 216 commits. Detailed audit:

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Independent source-tuple re-proof:

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`.

Process follow-up:

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/FOLLOW_UP_PROCESS_REPAIR.md`.

No global eventual second-extremal theorem is claimed.

## Current mathematical trust boundary

The active structural spine is

`rooted witness-slot residual -> local A-coordinate Hamming budget -> complementary-pair Hall demand -> exact cut decomposition -> Hall-density rigidity -> beta/source-tuple localization -> rigid-cut code collapse -> singleton U-witness deficit/slack -> one-code outside pair-capacity/crowding trap`.

- **Verified as explicit graph fact:** the repository's `X_3` adjacency reconstruction has `n=12`, `m=32`, diameter 2, and deletion of every edge raises diameter above 2. Its identification with the published Figure 1 remains an internal figure-based certification rather than an author adjacency-list comparison.
- **Independently re-derived conditional theorem:** fixed-source r-tuple capacity, the bounded-excess support count `FDPr`, and the finite arbitrary-subset deficit/layer-cake theorem. The remaining dependency is precisely the distinct-source and selected source-coordinate uniqueness premises inherited from the rooted selected-certificate construction.
- **Hand/algebraically verified conditional lemmas:** rooted witness-slot residual identities, Hall exact-cut decomposition, Hall-density rigidity, rigid code-collapse counting, and the rigid U-witness deficit/slack inequalities. These remain conditional on the graph-theoretic rooted/certificate premises.
- **Strongly supported supporting result:** the bounded-surplus four-exception direct-fan gate; not every kernel-specific subcase was independently re-derived in this audit.
- **Not verified end-to-end:** there is still no independent graph-level implementation that takes arbitrary realizable D2C graphs through the complete rooted-slot/Hall/rigid-witness chain.

## Independent source-tuple re-proof boundary

Fix an r-set `R` of physical sources. For each common witness `x`, every `y in R` is assigned a target coordinate `i_x(y)` on which `y` is the unique bit among the sources in `R`. Distinct-source geometry makes these target roles well-defined; global selected source-coordinate uniqueness means a fixed source `y` cannot reuse the same coordinate across two common witnesses.

Let `a_y(R)` be the number of coordinates at which `y` is unique among `R`, and let `T(R)` be the number of nonconstant coordinates on `R`. Then the number `M_R` of common witnesses satisfies

`M_R <= min_y a_y(R) <= T(R)/r`,

because a binary coordinate makes at most one member of `R` unique. For every common witness, the nonconstant coordinates on `R` lie among its `r` assigned target coordinates and its `k_x` non-target excess coordinates, so

`T(R) <= k_x+r`.

Hence `1/(k_x+r) <= 1/T(R)`, and summing over the `M_R` common witnesses gives

`sum_{x:R subset Y_x} 1/(k_x+r) <= M_R/T(R) <= 1/r`.

Summing over r-subsets gives `FDPr`; the integrated finite deficit follows by the integer layer-cake identity `sum k_x=sum_{K>=0} #{x:k_x>K}`. The detailed proof note records edge cases and the exact conditional premises.

## Mandatory hostile control

Keep `X_3` active in every relevant regression. The explicit reconstruction uses a cube `Q_3`, a root adjacent to all cube vertices, and three A-vertices adjacent to the three coordinate-zero faces. It has 12 vertices and 32 edges, while `M(12)=31`. The new rigid-U mechanism is inactive at its canonical root (`u=0`), so none of the newest inequalities may be interpreted as an all-order exclusion.

Reference: `project/research/post_ms/2026-09-17-stronger-pivot-v1/PUBLISHED_12_VERTEX_EXCEPTION_FIGURE_CERTIFICATION.md`.

## Load-bearing formulas retained after audit

For the rooted residual setup:

`Q=p(p+u-1)+q`, `delta=b(n-b)-m=r-f`, `E_U=u(p+u-1)-2q-s`, `L_A=a(p+u)-s-2f`, `delta+Q=L_A+f`, and `f=(p-lambda)(p+u)+q+E_U-delta`.

For a rigid Hall family `X`, with outside layer `Y`, `x=|X|`, `y=|Y|`, `k=(x-mu_X)_+`, and `h` distinct outside tight codes:

`hk<=u`, `Z>=k[y+h(x-1)]`, and for `g=x-T0=p-y>=1`, `E_U>=k[y+h(g-1)]`.

In the one-code case (`h=1`), `Ccap_P+L_Y>=y(p+x+k)` `(ONE)`. When the aligned same-code threshold applies, `S_P>=y(3y-D0)` `(CROWD)`.

These are not by themselves a global contradiction; the next forward session should combine the exact pair-local quantities before any further scalar relaxation.

## Repository and CI audit

Preserved deterministic failures:

1. Pre-audit Status synchronization run `35402717100`, job `105785888407`: old non-schema work mode and missing required fields.
2. Audit-head Status synchronization run `35405621026`, job `105794668021`: parser rejected human-readable Markdown-bold `AUDIT`; fixed by allowing the closing `**` before the value without enlarging the allowed mode set.
3. Audit-head N30 run `35405621004`, job `105794668117`: navigation checker treated valid README directory links as broken; fixed by checking target existence rather than regular-file status.
4. First-repair N30 run `35406193034`, job `105796333427`: after the directory fix, the checker exposed that the daily README compression had removed protected direct reviewer-PDF links. Those direct links are restored in this checkpoint in accordance with `AGENTS.md`; the integrity check itself is not weakened.

First-repair Status synchronization run `35406192884` passed. This checkpoint must itself clear status and N30 package workflows before the repository hygiene issue is considered closed.

## Next programme and stop/pivot criteria

1. **Premise audit.** Re-derive distinct-source and selected source-coordinate uniqueness directly from the rooted criticality/selected-certificate definitions. Any counterexample, ambiguity in the identity of a physical source, or possibility of reusing `(source,coordinate)` is a blocker for source-tuple applications.
2. **Exact one-code branch.** Combine actual `Ccap_P`, `(ONE)` and `(CROWD)` before replacing pair-local terms by global bounds. A useful outcome is either an asymptotic contradiction or a sharply classified equality geometry.
3. **Graph-level regression.** Implement the rooted partition, criticality slots, A-codes, Hall terms and rigid-witness quantities directly from realizable D2C graphs. Include `X_3`. The first mismatch is a proof/checker blocker; do not tune the test around it.
4. **Supporting-gate review only if load-bearing.** Complete the omitted four-exception kernel audit only if the one-code route actually depends on it; otherwise keep it demoted to supporting status.
5. **Pivot rule.** If the exact one-code inequalities still leave an asymptotic family, classify that geometry and feed forced `q,E_U,f` through the rooted residual identities. Do not continue accumulating weaker scalar relaxations.

Keep the mixed `{4,5}` ladder closed. Do not optimize for first-proof priority on Erdos #742.
<!-- CURRENT-STATUS:END -->
