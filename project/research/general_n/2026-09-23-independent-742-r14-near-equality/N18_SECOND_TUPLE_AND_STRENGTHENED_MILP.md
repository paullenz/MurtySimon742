# n=18: second tuple excluded and strengthened abstract MILP

Status: internal graph-level and exact finite computation.

## Second tuple

For d=(8,7), x=(8,8), h=(8,9), the certified star floors and D<=16 force centre deficits (8,8), zero endpoint deficits, and eight shared witness endpoints.

Let T be the common witness set. Then C_i=B\T has size two while C_j has size one. Write C_i=C_j union {p}. Every t in T has its j-source in C_j. Since that source also lies in C_i, the unique-common-neighbour condition for i forces the same source and makes t nonadjacent to p. Thus p misses all eight vertices of T. It also misses j, because p is outside C_j. Hence degree(p)<=8, contradicting its forced zero deficit and degree ten.

## Strengthened abstract model

The model now enforces the graph identity |R_i|=h_i-delta_i>=0, hence delta_i<=h_i. For n=18,Delta=10 it also uses the certified necessary star floors:

- x=7: star slack at least 30;
- x=8: star slack at least 35 (because any slack <=34 implies at most six missing witness edges, while the exhaustive dense certificate cover has minimum 40).

Consequences:

- d/x=(8,6,1): minimum deficit 17;
- d/x=(8,5,2): minimum deficit 18.

Both exceed Dmax=16. A subsequent complete-row replay reached 850 scalar candidates with no new survivor before it was stopped for immediate preservation; this partial run is not credited as row closure.
