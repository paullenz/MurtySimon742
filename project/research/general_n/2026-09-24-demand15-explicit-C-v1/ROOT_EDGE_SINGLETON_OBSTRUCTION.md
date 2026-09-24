# Root-edge singleton obstruction for the saturated (8,7) profile

24 September 2026. Status: internal graph-level necessary-condition work. This is not a complete realization theorem and does not establish the Murty–Simon conjecture.

Work in the surviving saturated n=18, Delta=10 profile from `EXPLICIT_C_CAPACITY_DIAGNOSTIC.md`. Let v be the maximum-degree root, B=N(v), and use the forced membership notation there: six empty-type vertices E, the unique type-0 vertex p, type-1 vertices q,r, and the unique type-01 vertex s. The forced B-skeleton has p adjacent to all E and s; s adjacent to p,q,r and to no E; p is nonadjacent to q,r; and every e in E is adjacent to exactly one of q,r.

## Root-edge criticality lemma

Let b be any neighbour of the root v in a diameter-two-critical graph. Deleting vb must destroy all length-at-most-two paths for some pair whose unique short route used vb. Therefore one of the following is necessary:

1. v and b have no common neighbour, so the endpoints themselves separate beyond distance two after deleting vb;
2. there is a B-side witness a in B\{b} with ab a nonedge and `N(a) intersect N(b)={v}`;
3. there is an A-side witness y outside B union {v}, adjacent to b, with `N(y) intersect B={b}`.

The third alternative is exactly a singleton B-neighbourhood `C_y={b}`.

For this profile the first alternative is unavailable at p and s because p and s have common neighbours with v inside B.

## Consequence for p

The only B-nonneighbours of p are q and r. But q and r each share s with p, in addition to the root v. Hence neither can be a B-side witness for the root edge vp. The root-edge lemma therefore forces an A-side vertex x_p with

    C_{x_p}={p}.

The two active labels are not candidates: label 0 has C_0={p,s}, while label 1 does not contain p. Thus x_p is one of the five inactive A-vertices.

Moreover p already has nine forced full-graph neighbours: v, active label 0, all six vertices of E, and s. Since Delta=10, x_p is p's unique additional neighbour. Consequently

    d(p)=10=Delta,   delta_p=0,

and p has no other inactive-A neighbour.

## Consequence for s

The B-nonneighbours of s are precisely E. Every e in E shares p and its chosen q-or-r source with s, in addition to the root v. Thus no e can be a B-side witness for vs. Again the first endpoint case is unavailable because s has p,q,r as common neighbours with v. Hence vs forces a second inactive A-vertex x_s with

    C_{x_s}={s}.

The singleton sets differ, so x_s is distinct from x_p.

Thus the surviving local profile consumes at least two of the five inactive A-vertices as distinct singleton-C root-edge witnesses, and p is saturated to full degree. This is a genuine graph-criticality restriction beyond the previous assigned-witness profile model, but it is not yet a contradiction.

## Next bounded step

Classify root-edge witnesses for q,r and the six empty-type vertices. In particular test the optional qr edge and cross-edges inside E against the five available inactive singleton-C witnesses. Preserve any surviving configurations rather than inferring nonrealizability from profile feasibility alone.
