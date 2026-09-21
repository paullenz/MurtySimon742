# Independent #742 strip attack — session 1

Start with [`THEOREM_INDEX.md`](THEOREM_INDEX.md) for claims, dependencies and
trust levels.

The first focused session produced two candidate-level results:

1. [`FIRST_OBSTRUCTION_AND_39_67.md`](FIRST_OBSTRUCTION_AND_39_67.md)
   identifies a one-parameter uniform-demand plateau that asymptotically
   saturates the decoupled profile integral.  It gives the exact scalar barrier
   `alpha_*=0.5820656900...`; movement toward `1/2` now requires a genuine
   graph-realizability input.
2. The same note sharpens the rational polynomial certificate and derives the
   all-order candidate `Delta>=250n/429 => e(G)<floor(n^2/4)` for `n>=6`.
   This is a strict numerical improvement over `7/12`.  The near-scalar-ceiling
   endpoint `39/67` holds for `n>=4681`.
3. [`FULL_HALL_PLATEAU_OBSTRUCTION.md`](FULL_HALL_PLATEAU_OBSTRUCTION.md)
   proves that a rational plateau on the counterexample side survives the
   full selected-incidence Hall system, graphical residual degrees, global
   orientation balance and pair uniqueness.  The missing input must couple
   physical residual sets/F-neighbourhoods to raw criticality.
4. [`SIGNATURE_UNION_RIGIDITY.md`](SIGNATURE_UNION_RIGIDITY.md) retains that
   missing physical information.  It proves a general union/second-moment
   inequality and forces plateau survivors to have average F-codegree above
   `0.2789a` among co-selected pairs.
5. [`ROBUST_SIGNATURE_STABILITY.md`](ROBUST_SIGNATURE_STABILITY.md) extends
   this to profile bands: bounded selected rows force linear average
   F-codegree, while failure of the row bound identifies selected-source
   concentration as the only escape.  A uniform endpoint cap removes even
   that escape and gives the unconditional band bound `>0.2484a-0.997`.
6. [`POSITIVE_DENSITY_CODEGREE_CLUSTER.md`](POSITIVE_DENSITY_CODEGREE_CLUSTER.md)
   converts the average into a concrete obstruction: asymptotically more than
   21.7% of selected pair occurrences, representing at least `0.00351a^2`
   distinct pairs, have F-codegree at least `a/5`.
7. [`GRAPH_TO_THRESHOLD_HOSTILE_REPLAY.md`](GRAPH_TO_THRESHOLD_HOSTILE_REPLAY.md)
   independently rederives the shared graph-to-profile spine.  It finds no
   blocker and makes the delicate residual-or-selected supplement dichotomy
   explicit; external review remains open.

Run `python3 check_39_67.py` for the exact rational certificate.
Run `python3 check_full_hall_plateau.py` for the exact plateau margins.
Run `python3 check_signature_union.py` for the rigidity constant.
Run `python3 check_robust_signature_stability.py` for the band constants.
Run `python3 check_codegree_cluster.py` for the density conversion.
Run `python3 check_threshold_algebra.py` for the threshold algebra replay.
Run `python3 check_degree_regression.py` for the threshold-ladder consistency
scan through `n=10000` (diagnostic, not a proof premise).

Trust boundary: internal candidate mathematics, exact arithmetic green;
independent/external review open.
