# Cross-source collision classification

23 September 2026. Status: **UNRESTRICTED INJECTIVITY REFUTED; DEMAND-RESTRICTED VERSION OPEN**.

The hoped-for global injectivity of the crossed-supplement image is false. Reconstructing every endpoint-label certificate on 41 distinct actual-D2C graph/root states recovered all 204 (B)-edges, with no missing certificate and no mismatch against any saved selected triple. Among 339 possible same-source candidate pairs, 151 were F-edges and every one satisfied the crossed-residual lift.

However, six cross-source collision images occur already in this bounded actual-graph population. The first is the (n=16), seed 55, root 7 graph. Sources 3 and 12 can both select labels ({10,13}) with supplements ({0,14}). Choosing
[
(3,10,0),(3,13,14),(12,10,0),(12,13,14)
]
on the four corresponding (B)-edges, together with one legal certificate on every other (B)-edge, gives a fully legal selection. Thus unrestricted source-to-image injectivity receives no proof credit.

## Exact collision motif

If sources (u,u') collide on an F-edge (ik) with supplements (p,q), raw certificate uniqueness forces:

- (up,uq,u'p,u'q) are G-edges;
- (ui,uk,u'i,u'k) are selected complement incidences;
- (pi,qk) are G-edges while (pk,qi) are residual incidences;
- (N_G(u)cap N_G(i)=N_G(u')cap N_G(i)={p}) and analogously the unique common neighbour for (k) is (q).

So a collision is not free reuse: it creates a selected (K_{2,2}), a G-(K_{2,2}) on sources and supplements, and a crossed residual matching.

## Demand-restricted check

The collision above has only label 10 demand-positive; label 13 has demand zero. More generally, for all six collision images, a dynamic program over every legal certificate choice found no selection making both collided labels demand-positive. Individual maximum selected counts already fail one or both demand inequalities in every row.

This is finite evidence, not a theorem. The useful narrowed target is:

> prove that a crossed-supplement collision cannot occur when both labels have positive demand, or charge each such collision to enough additional residual degree to cancel its multiplicity.

That demand-restricted statement is exactly aligned with the robust lower bound and is not refuted by the local counterexample.
