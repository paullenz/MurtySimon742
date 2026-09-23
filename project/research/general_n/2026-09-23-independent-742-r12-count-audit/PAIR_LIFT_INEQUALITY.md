# Pair-lift inequality for co-selected labels

23 September 2026. Status: **PROVED_INTERNAL_LEMMA; insufficient alone for strip closure**.

Fix a physical source u and two labels i,k selected at u. Write S_u for the selected labels at u, P_u for its residual labels, and R for the residual B--A incidence relation. Then

\[
c_F(i,k)\le \rho_u+c_R(i,k),
\]

where c_R(i,k) is the number of B-sources residual to both i and k.

Indeed, take j in N_F(i) intersection N_F(k). The source-demand argument forces uj to be an H-edge. If uj is residual, j lies in P_u. Otherwise uj is selected with a supplement w_j. Supplements at a fixed source are distinct, so w_j differs from the supplements of ui and uk. The usual injection argument applied twice shows that w_j i and w_j k are both residual. The map j -> w_j is injective. Partitioning the common F-neighbours into the residual and selected uj cases proves the inequality.

Summing before relaxing gives the stronger source-level form

\[
\sum_{\{i,k\}\subset S_u}c_F(i,k)
\le
\sum_{j\in P_u}\binom{|N_F(j)\cap S_u|}{2}
+
\sum_{w\in B}\binom{|N_R(w)\cap S_u|}{2}.
\]

For selected j, its supplement w_j is unique and every co-selected F-neighbour of j is a residual neighbour of w_j; hence its pair contribution embeds in the second sum. Residual j contribute to the first sum.

A direct replay on the 200 highest-ranked saved fixtures from the two fresh stress runs found zero violations. The pairwise inequality had minimum slack one in this sample. Several high-load source rows make the summed inequality tight entirely through its direct-residual term, including the exhaustive n=15 local-exclusion witness.

## Consequence and limit

The lemma is genuinely joint selected/residual information, but it does not by itself close the strip. The actual high-load witnesses can saturate the direct term. A successful density argument must therefore control reuse of direct residual labels and common residual source pairs across many physical sources; merely applying the inequality independently at each source returns to a feasible marginal relaxation.
