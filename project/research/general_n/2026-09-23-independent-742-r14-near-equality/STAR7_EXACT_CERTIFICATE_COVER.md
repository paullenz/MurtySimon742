# Exact seven-witness certificate-cover minimum

Status: internally verified finite graph-criticality calculation.

For a witness graph F=G[T] on x=7 vertices and a potential certificate vertex z, put S_z=N(z) cap T and l_z=7-|S_z|. The exact edge set certifiable by z consists of edges ts of F with t outside S_z, s in S_z, and t having exactly one neighbour in S_z. Giving this certificate type cost l_z exactly matches its contribution to the missing-incidence term beta.

For each of the 1,044 unlabeled simple graphs F on seven vertices, the verifier solved a binary weighted set-cover problem: cover every edge of F with at most |Z| certificate types while minimizing beta. The star slack is

    2*(21-e(F)) + beta.

Results:

- |Z|<=5: minimum star slack 30.
- |Z|<=6: minimum star slack 30.
- Independent labeled enumeration of all graphs with at most three missing edges also returned minimum 30.

The minimum witness graph has 14 edges, seven missing edges, certificate cost 16, and graph6 code FreVw.

## Consequence for the n=18 tuple

For the seven-witness label j, h_j=7 and |Z| is at most six. Thus sum epsilon_t>=30. Under D<=16, the eight-witness label already forces delta_i>=7. The inequality

    7*delta_j + sum_{t in T_j} delta_t - 21 >= 30

then forces delta_j=7 and at least two endpoint-deficit units. Hence D<=16 forces delta_i=delta_j=7, exactly two endpoint-deficit units in total, and no deficit elsewhere.

The remaining check is the x=8 star with |Z|<=5 and available slack at most 34.
