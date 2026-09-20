# Residual-one k=2 D1 residual-hub spoke dichotomy

Date: 2026-09-20

Status: **same-session raw-criticality lemma**, conditional on the residual-one hub package and the all-radius-one endpoint `J2=empty`. No finite scan is used.

The additive partition theorem isolates the class D1 of W_s-free escape vertices with exactly one K-neighbour. This note begins the promised literal attack. At the all-radius-one endpoint, criticality of a D1 edge to the residual hub `q_j` has only two possibilities: either the D1 vertex becomes Y-anticomplete and anticomplete to the whole K-heavy reservoir, or the edge consumes a matched head in H.

## 1. Setup

Let

`K={a,b}`, `W_s={z_a,z_b}`,

and assume `J2=empty`, so every matched head is radius one. Then the preserved residual-one geometry gives

- `N_A(q_j)=K`;
- `K--H=empty`;
- every Y-vertex is adjacent to both a and b and is nonadjacent to q_j.

Let t be a D1 escape with

`N(t) cap W_s=empty`,

`N(t) cap K={a}`.

Suppose additionally that

`t q_j in E(G)`.                                         `(D1-HUB)`

Apply raw rooted B-edge criticality to the edge `t q_j`.

## 2. Orientation whose A-witness is adjacent to q_j

In the orientation with source t and singleton head q_j, the A-witness must be adjacent to q_j and nonadjacent to t.

Because `J2=empty`, `N_A(q_j)=K`. Vertex a is adjacent to t, so it cannot be the witness. Vertex b is nonadjacent to t and is therefore forced.

Thus this orientation gives

> **`N(t) cap N(b)={q_j}`.**                              `(D1-F)`

Two immediate consequences follow.

Every Y-vertex is adjacent to b. Hence any Y-neighbour of t would be an additional common neighbour in `(D1-F)`. Therefore

> **`N_Y(t)=empty`.**                                     `(D1-FY0)`

Every K-heavy escape w is adjacent to b. Hence any edge tw would again create an additional common neighbour. Therefore

> **t is anticomplete to the entire K-heavy reservoir R.** `(D1-FR0)`

So the forward orientation is physically expensive: it contributes a full Y-hole block and a full t--R missing U block.

## 3. Opposite orientation consumes a matched head

In the reverse orientation, the A-witness must be adjacent to t and nonadjacent to q_j, with singleton equation

`N(q_j) cap N(h)={t}`.                                   `(D1-R0)`

The witness cannot lie in K: a is adjacent to q_j, while b is not adjacent to t.

It cannot lie in Y. Every Y-vertex is adjacent to both a and b, and q_j is also adjacent to a and b, so a and b would be two common neighbours distinct from t.

Hence the witness lies in H. Therefore there is `h_i in H` such that

> **`N(q_j) cap N(h_i)={t}`.**                            `(D1-R)`

For a fixed `h_i`, the graph-fixed common neighbourhood `N(q_j) cap N(h_i)` has at most one singleton head. Consequently distinct D1 vertices using the reverse orientation require distinct H-witnesses.

Thus if T is any set of D1 vertices adjacent to q_j and `T_R` is the reverse-oriented subset,

> **`|T_R|<=|H|=p-1`.**                                  `(D1-RCAP)`

The numerical bound alone is only linear and is not yet restrictive, but the exact singleton equations are now exposed for further intersection with private-coordinate and Y/U incidence structure.

## 4. Structural dichotomy

Every D1 neighbour t of q_j at `J2=empty` satisfies exactly one of the following raw-criticality outcomes:

1. **forward:** `N(t) cap N(b)={q_j}`, forcing `N_Y(t)=empty` and `E(t,R)=empty`;
2. **reverse:** there is a matched head `h_i` with `N(q_j) cap N(h_i)={t}`.

This is the first local D1 compression. A large forward population adds quadratic located defect when R is linear; a large reverse population is indexed injectively by H and should be attacked next by criticality of the `t h_i` / private-coordinate neighbourhoods.

## 5. Next move

Split D1 into q_j-neighbours and q_j-nonneighbours. The nonneighbours already contribute one located B-side hole each. For q_j-neighbours, retain the forward/reverse dichotomy above. Combine forward D1--R holes with the additive partition ledger; for reverse vertices, inspect the forced matched head `h_i` and its private endpoint q_i. The desired next lemma is that repeated reverse use creates either Y-holes, H--D1 holes, or a bounded-multiplicity private-coordinate obstruction.

Global caveat unchanged: bounded actual-D2C regression still contains zero positive rigid complete Hall-cut fixtures with `x>=3`; this remains conditional downstream mathematics pending independent hostile replay.