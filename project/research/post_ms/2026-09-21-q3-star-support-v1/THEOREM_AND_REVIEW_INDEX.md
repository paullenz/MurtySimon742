# Sharp star-support theorem and graph-level trust boundary

21 September 2026. Internally proved and independently replayed; external review and novelty assessment remain open.

## Compact structural theorem

Let G be a diameter-two-critical graph with a vertex v such that G[N(v)] is Q3 and every outside vertex has an antipodal-transversal neighbourhood in Q3. Such codes are exactly the six coordinate halfcubes, two parity halfcubes and eight closed-neighbourhood stars S_c.

If a star occurs, at least four distinct star centres occur. If exactly four occur, they form an affine plane of F_2^3. In that four-centre case n>=19; equality is attained by an explicit 19-vertex 66-edge graph. At order 19 the support must be a parity plane: either nonparity plane orbit requires n>=20.

The lower bound on star-support size and the lower order bound at exactly four centres are both sharp. In addition, the complete exactly-four-centre branch now satisfies `m<=M(n)` at every order. This does not bound the minimum order at five through eight centres or settle the full eventual second-extremal problem.

## Proof route

1. `RAW_CERTIFICATE_CALCULUS_AND_AUDIT.md`: exhaustive raw edge-deletion certificates; soundness of type-relation elimination for arbitrary physical multiplicities.
2. `AT_LEAST_THREE_STAR_CENTRES.md` and `THREE_CENTRE_SUPPORTS_IMPOSSIBLE.md`: one, two and three centres are impossible, by isolation, clean cube-entry and unique-bridge obstructions.
3. `FOUR_CENTRE_AFFINE_PLANE_NECESSITY.md`: the 56 nonplane four-centre supports are impossible; 14 affine planes remain in three symmetry orbits.
4. `PARITY_PLANE_MINIMUM_ORDER_AND_IMPROVED_FAMILY.md`: missing-coordinate physical matching forces five coordinate codes plus the appropriate parity code; n>=19 and the explicit fixture attains it.
5. `COORDINATE_FACE_ORIENTATION_OBSTRUCTION.md`: coordinate-face support forces the outward face code, four other coordinate codes and both parities; n>=20.
6. `OPPOSITE_EDGE_PLANE_PARITY_OBLIGATION.md`: opposite-edge-plane support forces exactly one direction-0 coordinate code, four other coordinates, both parities and a physical star matching; n>=20.

The earlier opposite-star-pair density bounds are superseded by nonrealizability of that support, rather than promoted into an all-code density theorem.

## Actual dense families and correction

For every n>=19 the five-coordinate family has

    M(n)-m = floor((9n-139)/2).

The six-coordinate family exists for every n>=20 and has

    M(n)-m = 5n-82.

The new five-coordinate family improves minimum order and eventually density. Its edge count minus the six-coordinate count equals ceil((n-25)/2): it is smaller for n=20 through 23, equal at 24 and 25, and larger for n>=26. Earlier shorthand calling it simply denser was too broad; the exact formulas were correct. Historical unit timestamps are unchanged.

Both are quadratic-density, triangle-containing D2C families, with a positive linear gap below M(n). Neither is an eventual counterexample, and neither density formula is an optimality theorem over all graphs in its support class.

## Independent evidence and remaining interface gap

- Raw reachability exactly matches the certificate calculus on 28,934 edge deletions across 916 code populations.
- The five-coordinate family has 30 actual D2C checks and all 66 explicit deletion witnesses at its smallest fixture; the six-coordinate family has 22 actual D2C checks.
- The independent prior Hall checker passes 108 root-policy runs including X3. All 105 runs from the new fixtures have p=0. Zero positive rigid cuts were added.
- `MAXIMUM_ROOT_RESIDUAL_LEDGER.md` proves p=0 throughout the balanced five-coordinate family, with Q=13 and exact positive linear residual defect. Its Q3 construction root is not a qualifying maximum-degree root.
- The finite source-tuple theorem remains conditional on its named global premises. Local certificate validation is not global source-identity closure.
- X3 remains the mandatory 12-vertex, 32-edge negative control to the false all-order conjecture (M(12)=31).

## Prioritized handoff

First hostile-review the two newest nonparity-plane proofs at physical-vertex scope. Then determine realizability of the opposite-edge-plane support with its mandatory matching and isolated coordinate population, or exploit that structure for a density bound. The coordinate-face outward branch remains open; a bounded 1200-trial search found no fixture but supplies no nonexistence proof. In particular, adjacency to one outward-code copy does not exclude a nonadjacent copy from serving as a spoke witness.

Five through eight star centres, nontransversal codes and the general eventual density theorem remain open. Keep rigid Hall work conditional until an actual qualifying graph interface is supplied. This is consistent with the latest audit's priority on raw criticality and graph realizability.

## Five-centre frontier

The 56 labelled five-centre supports reduce to three cube-automorphism orbits. Exact one-copy scanning leaves one feasible orbit: the support whose three-point complement is an independent parity triple, with a unique minimum n=21,m=77 model. This base has a proved one-parameter P1-twin family. A natural complete P0--P1 extension passes every graph-level D2C replay for 1<=r,q<=20 and has n=20+r+q and m=rq+4(r+q)+73. This supplies a quadratic-density positive control with positive linear gap from M(n); a uniform arbitrary-multiplicity proof is the next gate.

Latest continuation: `OPPOSITE_EDGE_PARITY_FACTOR_REDUCTION.md` removes parity multiplicity from opposite-edge-plane core realizability and gives an exact fixed-core expansion gap recurrence. The next search/proof should use one vertex of each parity, preserving arbitrary coordinate/star multiplicities.

## Full four-centre classification and density closure

The nonparity affine-plane orbits are now eliminated for arbitrary multiplicity. Hence exactly four star centres occur only on a parity plane. Order 19 is unique up to cube symmetry and has 66 edges; at order 20 the exact maximum is 73 with the unique six-coordinate-hub plus `K1,3` structure.

For arbitrary parity-plane multiplicities, the star graph is a star forest, parity substitution gives `e(P0)+e(P1)+e(P0,P1)<=rq`, and the complete-parity and parity-star-anticomplete subbranches satisfy `m<=M(n)` at every order. An actual `n=26,m=104` parity-star graph is preserved as a mandatory positive control.

The former matching-one and one-tree-component targets are false, as is universal exact cancellation `e(R∪T∪S)<=rq+s`; actual D2C controls witness every failure. The repaired proof allows excess `epsilon` and derives

    epsilon <= floor(s(r+q-2)/2)   for q>=1,

with `epsilon=0` when `q=0`. The budget `D(u,s)` exceeds this cap by at least 11, proving `m<=M(n)` for every exactly-four-centre graph in the stated scope. `FOUR_CENTRE_COMPLETE_DENSITY_CLOSURE.md` gives the proof and `FOUR_CENTRE_COMPLETE_CLOSURE_HOSTILE_AUDIT.md` independently replays its load-bearing raw inputs. Five through eight centres are now the Q3 star-support frontier.
