# N34: complete candidate bound and equality classification

12 September 2026. Research direction: Paul Lenz. Mathematical development,
computation and internal audit: ChatGPT/Geeps.

**Candidate theorem.** Every simple diameter-two edge-critical graph G on
34 vertices has `e(G)<=289=floor(34^2/4)`, with equality if and only if
`G is isomorphic to K(17,17)`.

The finite certificate package is internally complete and replayable.
Independent specialist review, novelty assessment and independent external
reproduction remain OPEN. This is a fixed-order candidate result; no
unrestricted Murty–Simon proof is claimed.

## 1. Complete proof assembly

The [preceding bound package](../2026-09-12-m290-v1/README.md) establishes
the candidate bound m<=289. Its proof uses the original
[N34 degree reduction and upper layers](../2026-09-12-frontier-v1/README.md),
the canonical bridge, the fixed-label tail bounds, and the complete
1,614-state exclusion at m=290. Those arguments and their certificates
remain required dependencies and are preserved.

Suppose now m=289. Average degree gives Delta>=17. The original target-range
degree reduction excludes every Delta>=19, so Delta is 17 or 18.

At Delta=18 the bridge has `(a,b,t,dmax)=(15,18,1,13)`. The preserved complete
frontier has 1,296 demand profiles and 13,546 conservative residual states:
12,926 positive-demand and 620 zero-demand states. Sections 2–4 below exclude
every state. Hence Delta=18 is impossible.

At Delta=17, the degree sum is `2m=578=34*17`, so the graph is 17-regular.
The [balanced-degree theorem](../../general_n/2026-09-12-balanced-degree-v1/BALANCED_DEGREE_THEOREM.md)
forces equality to be K(17,17). Conversely, K(17,17) has 289 edges, diameter
two, and every edge is critical: removing a cross-edge makes the distance
between its endpoints three. This establishes the candidate theorem. QED.

## 2. Disjoint equality ledger

| Stage | States excluded | States remaining |
|---|---:|---:|
| Exact positive-demand degree mass | 4,768 | 8,778 |
| Tight heavy-label subset hand lemma | 1,510 | 7,268 |
| Fixed nine-term exact-budget envelopes | 2,559 | 4,709 |
| Fixed 13-term exact-budget envelopes | 784 | 3,925 |
| Source-capped threshold hand bound | 430 | 3,495 |
| Adaptive monotone exact-budget envelopes | 3,494 | 1 |
| Heavy-outdegree split, exact integer Farkas certificate | 1 | 0 |

The total is **6,708 hand/accounting exclusions and 6,838 exact certificates**.
The ledger orders disjoint classes by method; the discovery programs may
interleave methods while traversing states. No graph is excluded merely
because a numerical solver reported infeasibility.

All 620 zero-demand states are covered separately in the recorded accounting:
159 tight-subset hand exclusions, 24 source-capped hand exclusions, 80 fixed
nine-term certificates, 41 fixed 13-term certificates and 316 adaptive
certificates. The heavy-split exception has positive demands only.

## 3. General structural input

The [exact demand-deficit identity and subset lemma](../../general_n/2026-09-12-exact-budget-threshold-v1/BRIDGE_REFINEMENTS.md)
give `E=S-r-2t=sum_{s_i=0}(R_i-d_i)`. Positive-demand states require E=0.
With one zero label, d=R-E for that label. With several zero labels and E=0,
every deficit is zero separately, so each such label has d=R. The new model
permits the latter case explicitly. Every state entering an envelope has
either E=0 or exactly one zero label; no unsupported deficit allocation is used.

The [new source-capped threshold lemma](../../general_n/2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md)
retains each source's capacity to serve heavy labels. It is a universal hand
consequence of the canonical bridge and supplies the 430 additional hand
exclusions after the fixed-potential stage.

The exact-budget envelopes use free real residual and incidence balance
multipliers, nonnegative transport multipliers, and nonnegative combinations
of BC, SH and diagonal monotone indicators. `envelopes.py` defines the
discovery domain; `verify.py` separately enumerates every local label/source
option and checks the saved integers. The 3,494 adaptive certificates use
14–74 nonzero potential weights each. These are proof-critical finite
certificates, not a uniform formula valid for arbitrary order.

## 4. The single difficult state

Both the adaptive envelope and the older full RX/Hall relaxation leave

`s=(1^2,2^13)`, `rho=(1^10,2^8)`.

The old relaxation's numerical feasible point is preserved in
`low_state_rx.json`; it is not a graph. The new model records each source's
actual heavy selected outdegree H_u and imposes the universal inequality

`sum_{H_u>2}H_u <= sum_{rho_u>=2}p_u`.

The [complete grouped graph-image argument](HEAVY_SPLIT.md) justifies all
normalizations, balances, compatibility conditions and unit upper bounds.
The resulting exact integer Farkas certificate checks 12,570 columns and
has right-hand side -998,530. Its full coefficients and model specification
are preserved; this closes the last state.

## 5. Replay and storage

From the repository root:

```sh
python project/research/n34/2026-09-12-equality-v1/verify.py
```

The standard-library replay passed **3,018,781 local envelope inequalities**,
the 12,570-column heavy-split certificate, and complete disjoint coverage of
all 13,546 states. Worst integer envelope gaps are -9,874, -9,760 and -9,355
for the nine-term, 13-term and adaptive families respectively. See
[verification.json](verification.json) and [verification.log](verification.log).

The two complete JSONL streams are stored losslessly as gzip/base64 text.
`CERTIFICATE_STORAGE.json` records both original byte hashes and stored byte
hashes. `certificate_io.py` decodes and verifies them before any mathematical
check. The streams retain every input state, full nonzero integer coefficients,
failed proposal status and intermediate unresolved state. No hash-only proof
claim replaces the actual evidence bytes.

Optional rediscovery, requiring NumPy and SciPy, is:

```sh
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-equality-v1/sweep.py fixed
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-equality-v1/sweep.py adaptive
OPENBLAS_NUM_THREADS=1 python project/research/n34/2026-09-12-equality-v1/certify_heavy.py
python project/research/n34/2026-09-12-equality-v1/pack_certificates.py
python project/research/n34/2026-09-12-equality-v1/verify.py
```

Sweeps resume existing raw JSONL checkpoints. In a clean checkout they
generate fresh streams. Packing is required after rediscovery so verification
reads the new stored bytes. Solver versions may produce different valid
coefficients; exact acceptance and complete coverage are mandatory.

The [current reviewer package](../../../../releases/n34-reviewer-v1/README.md)
collects full-route replay commands, hashes and publication provenance.
The [internal audit](AUDIT.md) distinguishes internal replay from the still
OPEN external mathematical review.
