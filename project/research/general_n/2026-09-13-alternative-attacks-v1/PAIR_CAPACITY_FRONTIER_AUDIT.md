# Potential-pair capacity frontier audit

13 September 2026. **Canonical internal cross-implementation audit. External mathematical review, novelty assessment and genuinely independent third-party reproduction remain OPEN.**

This record promotes the large frontier consequence of [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md) only after two structurally different exact implementations agreed.

## Result

The ledger-current input before this family promotion contained

```text
4,566 frozen scalar survivors
= 4,488 N34 equality-derived survivors
+    78 N35 m=306-derived survivors.
```

Both exact scans return

```text
943 pair-capacity whole-state exclusions,
3,623 survivors of this relaxation.
```

All 943 exclusions are N34-derived. None of the 78 N35-derived states is closed by this particular relaxation.

After promotion the frozen catalogue accounting is therefore

```text
1,955 exclusions / 3,623 survivors,
3,545 N34 equality-derived survivors,
   78 N35 m=306-derived survivors.
```

These are scalar states in the frozen generalisation experiment, not unresolved fixed-order N34/N35 proof obligations and not actual surviving graphs.

## Mathematical relaxation audited

For each scalar state and each admissible total excess `E`, the scanners quantify every source selected-degree multiset in the deliberately enlarged universe

```text
0 <= q_u <= min(a-rho_u, #{i:s_i<=rho_u}),
sum_u q_u = S+E,
```

up to permutation inside equal-`rho` classes.

No selected-incidence Hall feasibility is assumed. Every legal selected profile lies inside this universe, so exhaustion is safe for exclusion.

Each profile is tested only against the necessary incoming capacities

```text
p_u <= rho_u+b-a-1,
p_u <= b-1-q_u,
```

the applicable total-excess source cap from [`TOTAL_EXCESS_SOURCE_CAP.md`](TOTAL_EXCESS_SOURCE_CAP.md), and the potential-pair capacity

```text
p_u <= d_KD(u)-q_u
```

from [`POTENTIAL_PAIR_CAPACITY.md`](POTENTIAL_PAIR_CAPACITY.md).

A profile survives only if every pointwise capacity is nonnegative and

```text
sum_u P_u >= sum_u q_u.
```

A state is closed only when every enlarged-universe profile at every admissible `E` fails.

## Implementation A — vertex-vector / directed-pair construction

Files:

- [`scan_pair_capacity_frontier.cpp`](scan_pair_capacity_frontier.cpp)
- [`prepare_pair_capacity_frontier.py`](prepare_pair_capacity_frontier.py)
- [`merge_pair_capacity_frontier.py`](merge_pair_capacity_frontier.py)
- [`summarize_pair_capacity_frontier.py`](summarize_pair_capacity_frontier.py)

GitHub Actions run: `34789010347` — success.

The scanner expands each equal-`rho` class as a nondecreasing q-vector, constructs directed compatibility `D(u,w)` pair-by-pair, then derives the undirected potential degree.

Full merged TSV SHA-256:

```text
978b2fbb4755ab5414941b532a217be164298cfecf7828a6ae8cf9b2f606e510
```

It examined `11,639,427,412` source profiles before either exhausting a state or finding its first relaxation witness.

## Implementation B — type-count / closed-form potential degree

Files:

- [`scan_pair_capacity_types.cpp`](scan_pair_capacity_types.cpp)
- the same ledger-current transport layer, but a different profile representation and potential-degree calculation.

GitHub Actions run: `34789193390` — success.

This scanner never expands an equal-`rho` class into a vertex vector and never constructs directed pairs. It enumerates multiplicities of `(rho,q)` types and computes

```text
d_KD(rho,q)
 = sum_(R,Q) m_(R,Q) [Q+R >= q-1 and Q <= q+rho+1]
   - 1
   - sum_(R,Q) m_(R,Q) [Q+R == q-1 and Q == q+rho+1].
```

Full merged TSV SHA-256:

```text
5e78549f249127ef04bb22627ae47ae280a3ce157fcc25ab0844b8c2282a307e
```

It examined `11,770,581,161` source profiles. The larger total is expected because survivor search order differs; both programs exhaust every profile in a closed state.

## Cross-implementation agreement

After sorting by `(layer,state_id)`, the two 4,566-row outputs agree exactly on

```text
S,
Emax,
pair_passes,
status,
witness_E
```

for every state.

The excluded set is identical: **943 states in both implementations**.

More importantly, on every one of the 943 exhaustively closed states the two implementations agree exactly on

```text
profiles_tested,
pre_pair_passes,
pair_passes (=0),
best_pre_margin,
best_pair_margin,
Emax,
status.
```

Thus the exhaustive certificate statistics agree state-by-state despite the different q representation and different computation of `d_KD`.

The ordered promoted state list is preserved in [`PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv`](PAIR_CAPACITY_FRONTIER_EXCLUDED.tsv). Its SHA-256 is

```text
f2f3d581a7bb69749d66fd07d7bfd51e5303cf8d5b4445b9b08c16cb2944e1a1
```

and contains exactly 943 state IDs.

## Margins

Across the 943 exclusions:

```text
profiles exhaustively checked: 2,362,486,577
profiles passing the older pre-pair incoming caps: 976,941,533
minimum pre-pair passes in any closed state: 294
best pair-capacity deficit range: -29 to -1
median best deficit: -6
```

In particular **every one of the 943 states has profiles that pass the older incoming-capacity conditions**. The new potential-pair restriction is genuinely doing work; the family is not being re-labelled from an older aggregate exclusion.

The closest cases are 81 states whose best possible enlarged-universe profile is still one incoming incidence short. The strongest closed state has best deficit `-29`.

## Separate theorem-level verification

The closed-form potential-pair theorem is also protected independently of the frontier scan by [`verify_potential_pair_capacity.py`](verify_potential_pair_capacity.py). GitHub Actions run `34789068799` completed successfully after checking

```text
122,608 small (q,rho) profiles,
2,259,488 ordered source-target pairs,
588,416 potential-degree identities.
```

It verifies the exact symmetric pair criterion, direct-versus-closed-form `d_KD`, and the stated threshold upper bound.

## Trust boundary

The finite arithmetic and cross-implementation agreement are strong internal evidence, but they do not independently validate the graph-to-constraint bridge. The family closures still depend on the canonical selected/residual framework, especially selected-edge forcing, the selected-excess implication used by the total-excess cap, and the supplement/companion endpoint arguments underlying directed compatibility.

Same-assistant derivation, green GitHub Actions and two implementations are not external mathematical acceptance. The unrestricted Murty–Simon conjecture remains unproved by this project.
