# Local triangle audit and the residual-mass-five equality closure

22 September 2026. Internal candidate proof, independently re-derived from the raw selected/residual bridge. Maximum-degree root and every legal selected assignment remain mandatory. This audits the unpromoted handoff in EQUALITY_SOURCE_HANDOFF.md; it is not external verification and does not close the full strip.

## Local cycle lemma

Let Q be a connected component of F which is a cycle. Assume every label i in Q has R_i=1 and t=f-r=0. If b>|Q|, then this configuration is impossible.

At a selected source u for i in Q, the source-demand injection sends selected F-neighbours of i to distinct residual pairs in column i. Since R_i=1 and d_Q(i)=2, at least one of the two neighbours of i is residual at u. Hence every source selected at a Q-label lies in U, the set of sources of residual pairs in the Q-columns. Since each Q-column has one residual pair, |U|<=|Q|. Every B-vertex outside U is adjacent to every Q-label: a missing pair there would be selected, whose source would have to lie in U. Thus B\U is nonempty.

Delete an edge ij of Q. Its endpoints, and any Q-pair whose old two-path used ij, retain a common B-neighbour outside U. No A-vertex outside Q has an F-edge to Q because Q is a component, so no other A-pair used ij in a length-two path. Root pairs are unaffected. Criticality must therefore produce a newly distant crosspair at i or j. It cannot be selected, because a selected crosspair has its unique common neighbour in B whereas the deleted witness ij lies in A. It is residual at the endpoint.

Assign such a residual witness to each edge of Q. The assignment is injective, since a residual crosspair with a unique common A-neighbour determines the deleted F-edge. There are |Q| edges and |Q| residual pairs in these columns, so the assignment is bijective. Orient every edge from the column of its witness. Every cycle label has outdegree one.

Write z_i for the residual source at i and orient i to next(i). The witness says z_i is adjacent to next(i). The selected-source injection gives X_i subset {z_prev(i),z_next(i)}. The first source is adjacent to i and cannot lie in X_i; because x_i>=d_i-R_i=1, X_i={z_next(i)}. At prev(i), the missing sources are exactly {z_prev(i),z_i}. But the selected source z_next(i) at i must miss prev(i). It equals neither z_prev(i) (adjacent to i) nor z_i (residual at i), contradiction. Repeated residual sources are allowed throughout.

## Application to the last r=5 equality shape

For residual vector (2,1,1,1), the exact core ledger and earlier kernel reductions leave, at f=r=5, the shape consisting of:
- a triangle on the three unit-residual labels; and
- a disjoint two-leaf star centred at the R=2 label, with zero-residual leaves.

The triangle is a component Q of F. Since t=0 and the root has maximum degree, b>=a+1. Here a>=6, while |Q|=3, so b>|Q|. The local cycle lemma excludes it.

The other necessary r=5 equality shapes were already reduced to exact finite source populations:
- both diamond cores have either no source-pattern survivor or one survivor killed by legal-supplement uniqueness;
- the one-link triangle/star shape has six source populations, all killed by the same legal-supplement uniqueness test.

I independently checked the logical interface used by those exclusions. A residual-free source selected somewhere would have a nonempty selected-label set closed under F-neighbourhood. Connectedness forces it to contain the whole modeled component, violating the selected-neighbour injection at a unit or zero column. Thus every unlisted source is adjacent to all modeled labels. In each surviving population, an active source is selected at two labels while every active source misses one of them. Its unique B-supplement must be unlisted and is therefore a common B-neighbour at both selected labels, forcing reuse of the same B-edge as supplement twice. This contradicts selected-triple injectivity. No abstract source survivor is promoted to an actual graph.

Therefore:

    1 <= r <= 5  implies  f <= r-1.

## Consequences and scope

Let D=floor(n^2/4)-b(n-b)>=0 and epsilon=m-floor(n^2/4). Since t=D+epsilon and S>=r+2t:
- any non-bipartite equality case has r>=6 and S>=6+2D;
- any strict counterexample has r>=6 and S>=8+2D;
- S<=7 proves the edge bound;
- S<=5 proves the edge bound with equality exactly balanced complete bipartite, using the r=0 zero-demand theorem.

Equality for S=6,7 and the unrestricted positive-demand strip remain open. The result is internal candidate mathematics pending adversarial audit.
