# Crossed-supplement lift and the remaining reuse question

23 September 2026. Status: **PROVED_INTERNAL_LOCAL_LIFT; GLOBAL INJECTIVITY UNPROVED**.

Let (ui	o w_i) and (uk	o w_k) be selected incidences at the same physical source (u), with distinct supplements, and suppose (ikin E(F)=E(G[A])). Then
[
w_i kin R,qquad w_k iin R.
]
This is the usual supplement injection applied across the co-selected F-edge: the supplement for one selected label is distinct from the supplement of the other, and the F-edge forces the crossed incidence to be residual. Thus every co-selected F-edge occurrence has an ordered crossed-residual image.

The needed cross-source step would assert enough injectivity, or bounded multiplicity, for these images as (u) varies. That statement is **not proved**. It is materially stronger than the sourcewise pair-lift inequality.

## Actual-graph check

On the 200 highest-ranked saved fixtures from the two fresh independently BFS-certified actual-D2C batches:

- 431 co-selected label-pair occurrences were examined;
- 228 were F-edges;
- all 228 had both crossed residual incidences;
- no fixture had two physical sources with the same unordered label pair and unordered supplement pair;
- the observed maximum multiplicity was one.

The zero-collision observation is only a candidate guide, not a theorem or a graph-realizability substitute. The sample contains repeated ranked selections and does not justify extrapolation.

## Rejected convention error

A first check accidentally treated (F) as the complement of (G[A]). It produced 91 failures among 203 occurrences. Direct comparison with the already verified pair-lift rows exposed the convention error: here (F=G[A]). That false route is retained as a warning and receives no mathematical credit.

## Exact next question

For fixed (ikin E(F)), can two distinct sources (u,u') co-select (i,k) with the same supplement pair? If yes, classify the collision and charge it to additional residual structure. If no, prove injectivity from raw edge-critical domination without assuming profile realizability.
