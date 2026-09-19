# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** The live problem is the sufficiently-large/eventual second-extremal D2C classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 Dailly-Foucaud-Hansberg strengthening is not assumed. The published 2024 order-12, size-32 D2C graph is a mandatory hostile control. Murty-Simon / Erdos #742 remains preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `SOURCE_PREMISE_REPAIRED_GRAPH_HALL_REGRESSION_2026_09_19`

WORK MODE: `AUDIT`

INSPECTED PREDECESSOR: `4ab17e6dd1f8d0ca0abeb80d2887ee31e03fc10e`

LAST VERIFIED RESULT: The two named upstream premises isolated by the 19 September daily red-team audit are now internally repaired at the exact level used by the finite source-tuple theorem. P1 (distinct physical beta sources for one A-witness across distinct target fibres) follows directly from raw beta criticality: reuse of one physical pair `(x,y)` at fibres `i!=j` would force the fixed set `N_G(x) cap N_G(y)` to equal both distinct singletons `{q_i}` and `{q_j}`. P2 is selected-representative uniqueness, not raw-witness uniqueness: each physical P--U source-coordinate obligation `(y,i)` is one rooted B-edge and the canonical bridge chooses one representative for that physical edge. The principal `B_beta` lower bounds have also been traced to counts of these distinct selected physical obligations, not pre-deduplication raw witness incidences. The first graph-level checker was found to have mislabeled the alpha/matched-source orientation as beta; that earlier beta-collision evidence is withdrawn and the checker is corrected. The corrected regression separately reconstructs raw alpha/beta certificates, a canonical selected P--U ledger, the canonical selected/residual Hall row/column margins and exact ledger on actual D2C graphs, and the published `X_3` hostile control.

UNPRESERVED WORK: None.

DEFERRED ADMIN: Historical Git-LFS checkout warnings for seven legacy ZIP paths remain preserved and have not been altered because they are not blocking the live mathematics and touch frozen historical evidence.

NEXT ACTION: Extend the independent graph-level regression from the repaired selected/Hall interface into the rigid Hall witness quantities and exact pair-local one-code data; only then resume the one-code branch by combining the exact `Ccap_P` formula with `(ONE)` and `(CROWD)`, feeding any surviving geometry through the rooted residual ledger. Keep the four-exception gate subordinate unless it becomes load-bearing.

## Mandatory audit reconciliation

The most recent daily adversarial audit is:

- `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`
- independent conditional re-proof: `project/research/post_ms/2026-09-19-daily-red-team-audit-v1/INDEPENDENT_SOURCE_TUPLE_REPROOF.md`

The present checkpoint follows that audit's priority order rather than advancing downstream theory prematurely.

### Repair package

- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_GRAPH_AUDIT.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_REPAIR.md`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/check_source_premises_graph_level.py`
- `project/research/post_ms/2026-09-19-source-premise-graph-audit-v1/SOURCE_PREMISE_GRAPH_AUDIT_SUMMARY.json`

A correction trail is intentionally retained. The first graph-level checker called the certificate conditions
`x~y, x!~q, N(x) cap N(q)={y}`
"beta"; these are actually the alpha/matched-source orientation. The corrected beta orientation is
`x!~y, x~q, N(x) cap N(y)={q}`.
The earlier no-collision observation from the mislabeled family is not used as evidence.

## Repaired source-tuple premises

### P1: distinct physical beta sources

For a physical P--U edge `yq_i`, beta orientation from `y` with witness `x` gives

`N_G(x) cap N_G(y)={q_i}`.

If the same `x,y` beta-certified a second target fibre `j!=i`, the same common-neighbour set would have to equal `{q_j}`. Tight fibres are disjoint, hence `q_i!=q_j`; contradiction.

Therefore the source set `Y_x={y_i:i in I_x}` is genuinely a set of distinct physical U-vertices and

`ell_x=|I_x|=|Y_x|<=min(p,u)`.

### P2: selected source-coordinate uniqueness

For fixed unmatched source `y` and fibre `i`, there is exactly one physical P--U edge `yq_i`. The canonical selected/residual bridge chooses one representative for each physical rooted B-edge / missing unordered B-pair. If that edge is beta-oriented, it contributes one selected cross incidence `yx`. Raw candidate witnesses may be non-unique; the source-tuple theorem needs only the chosen selected representative.

Thus selected `(y,i)` uniqueness is built into the one-representative construction.

### B_beta semantics

There are exactly `pu` physical P--U obligations. If `h_q` counts obligations whose selected representative is alpha-oriented from matched source `q`, then

`B_beta=pu-sum_q h_q`

is exactly the count of physical obligations selected in beta orientation.

For each A-label `x`, `ell_x` counts selected beta obligations using `x`, so

`B_beta=sum_x ell_x`.

For fixed matched source `q`, distinct alpha-selected obligations use distinct selected cross edges `qx`, all with A-code `alpha(q)), giving

`h_q<=n_{alpha(q)}`.

Hence

`B_beta>=pu-W_alpha`, with `W_alpha=sum_q n_{alpha(q)}`,

and therefore

`B_beta>=[pu-mu_alpha a]_+`.

The root-imbalance floor `B_beta>=p(lambda+1-2p)_+` is the trivial `mu_alpha<=p` specialization. The sharper switching/Hall lower bound has the same selected-physical-obligation semantics. These quantities are therefore compatible with the independently re-derived finite source-tuple theorem.

## Independent graph-level regression

The corrected checker rejects a fixture unless it is actually D2C before constructing any rooted object.

On all NetworkX graph-atlas D2C graphs through order seven:

- 21 unlabeled D2C classes;
- 126 rooted instances;
- 2 raw beta candidate certificates;
- 1 raw alpha candidate certificate;
- 0 P1 collisions;
- 0 raw P2 collisions in this small sample;
- 30 canonical selected rooted B-edges;
- 3 physical P--U obligations;
- selected P--U split: 1 alpha, 2 beta;
- 50 maximum-degree rooted selected/residual Hall ledgers reconstructed and checked.

The Hall-ledger regression verifies directly from each graph:

- one selected representative per rooted B-edge;
- simple source-label selected incidence;
- exact row/column selected margins equal to `Q=e(G[B])`;
- exact residual row/column margins;
- graph-derived label demand `x_i>=s_i`;
- pointwise selected-edge demand forcing `s_i<=rho_u`;
- exact selected/residual ledger `e(C)+r=C(a,2)-t`;
- summed demand lower bound `sum s_i>=r+2t`.

These small-graph checks are regression evidence only; they are not substitutes for the hand bridge.

### Mandatory X_3 control

The executable fixture reconstructs the published-figure cube-face graph and verifies:

- `n=12`;
- `m=32>M(12)=31`;
- diameter two;
- every edge critical;
- canonical cube root: `a=3,b=8,u=0,p=4`;
- canonical bridge: `Q=12,r=0,t=0,S=0`;
- no unmatched beta obligation exists.

No repaired source-tuple or Hall statement suppresses `X_3`.

## Updated trust boundary

- `X_3`: explicit graph property independently executable; paper-figure identification remains internally figure-based.
- Source-tuple finite capacity / `FDPr`: abstract theorem independently re-derived; the two named premises P1/P2 now have direct internal proofs at the required raw/selected levels.
- `B_beta` root/switching lower bounds: audited to count the same distinct selected physical obligations used by source-tuple.
- Canonical selected/residual Hall inputs: independently reconstructed on 50 maximum-degree small D2C roots plus `X_3`.
- Rigid Hall witness-deficit quantities and exact pair-local `Ccap_P`: hand-derived packages remain to be independently reconstructed from graph-derived data before further forward use.
- Bounded-surplus four-exception gate: strongly supported, not load-bearing at this checkpoint.
- No global eventual second-extremal theorem is claimed.

Key rigid-cut formulas retained but not yet advanced in this checkpoint: `hk<=u`, `Z>=k[y+h(x-1)]`, for `g>=1`, `E_U>=k[y+h(g-1)]`; one-code `(ONE)` is `Ccap_P+L_Y>=y(p+x+k)`, and aligned crowding `(CROWD)` is `S_P>=y(3y-D0)`.

## Next programme and stop/pivot criteria

1. Extend the actual-graph regression into rigid Hall cuts: reconstruct A tight-code classes, complementary-pair unions, exact cut missing-edge/source orientation data, singleton-head matched/U witnesses, and the variables entering the rigid deficit package.
2. Independently reconstruct the explicit pair-local `Ccap_P` ingredients on any realizable small rooted examples satisfying the hypotheses. First graph/formula mismatch is a blocker.
3. Only after that interface survives, combine exact `Ccap_P` with `(ONE)` and `(CROWD)`; classify equality geometry if the inequalities leave room.
4. Feed any survivor back into `delta=b(n-b)-m=r-e(F)`, `Q=e(G[N(v)])`, and the exact rooted residual ledger.
5. Keep the four-exception gate subordinate unless it becomes load-bearing.

Keep the mixed `{4,5}` ladder closed. Do not optimize for first-proof priority on Erdos #742.
<!-- CURRENT-STATUS:END -->
