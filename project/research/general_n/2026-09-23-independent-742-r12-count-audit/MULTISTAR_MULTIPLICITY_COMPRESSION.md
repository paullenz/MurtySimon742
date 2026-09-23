# Multiplicity-compressed multi-star slack

23 September 2026. Status: internally proved for the assigned-witness obstruction. It remains conditional on the audited bridge into that interface.

Retain the deletion-minimal normal form with total demand 15 or 16. For each demand-positive label i let x_i be its assigned-witness degree, h_i=2x_i-d_i, and let r_t be the assigned-witness degree of endpoint t. Put X=sum_i x_i, D=sum_z delta_z, and rho=2Delta-n.

The quadratic star theorem gives, label by label,

x_i delta_i + sum_{t in N(i)} delta_t
 >= x_i(rho+1)+binom(x_i,2).

Summing over labels yields

sum_i x_i delta_i + sum_t r_t delta_t
 >= X(rho+1)+sum_i binom(x_i,2).

Let q=max(max_i x_i,max_t r_t). Every vertex coefficient on the left is at most q, hence the left side is at most qD. Therefore

qD >= X(rho+1)+sum_i binom(x_i,2).

The assigned-witness collision lemma gives r_t<=h_i on every incidence, while x_i<=h_i. Thus q<=h_max=max_i h_i=max_i(2x_i-d_i), and the fully scalar necessary condition is

h_max D >= X(rho+1)+sum_i binom(x_i,2).

This is stronger than collapsing each star separately whenever no single vertex absorbs all multiplicity.

As an immediate finiteness bound, if m=max_i x_i then h_max<=2m-1 and

D(2m-1)>=binom(m,2).

Hence m<4D+1. Together with the absolute demand totals 15/16, every fixed (n,Delta) row now has a finite exact integer screen over demand partitions and witness counts.

This does not yet rule out the strip. The next step is to enumerate those finite patterns with the exact parity deficit budget, preserving every surviving pattern for realizability testing.
