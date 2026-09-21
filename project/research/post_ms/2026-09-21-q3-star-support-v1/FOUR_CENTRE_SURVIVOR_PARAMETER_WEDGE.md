# Exact parameter wedge after budgeted cancellation

21 September 2026. Unconditional necessary conditions for a surviving four-centre counterexample.

Let

    w=r+q,  u=t+w,  U=M-I,

and let `D(u,s)` be the budget from `FOUR_CENTRE_BUDGETED_CANCELLATION_GATE.md`. Any graph with `m>M(n)` in the exactly-four-centre branch must satisfy all of the following:

1. `s<ceil(w/2)`;
2. `U>=D(u,s)+1`;
3. `rq>=D(u,s)+1`;
4. both `r>s/2` and `q>s/2`;
5. writing `k=min(r,q)`,

       k(w-k) >= D(u,s)+1.

Equivalently, when the discriminant is nonnegative,

    k >= ceil((w-sqrt(w^2-4(D+1)))/2).

## Proof

Items 1 and 2 are the contrapositive of the large-star and exact `U<=D` closures. Item 3 follows from `U<=M<=rq`. Since `t>=5`,

    D(u,s) >= floor(s(2w+s+6)/4)-3
           >= floor(sw/2)+7

for `s>=4`. Thus `rq>=U>=D+1>sw/2`. If `k=min(r,q)<=s/2`, then `rq=k(w-k)<=kw<=sw/2`, a contradiction; this proves item 4. Finally `rq=k(w-k)` proves item 5 and the quadratic-root form.

The wedge says a survivor needs a star population smaller than half the combined parity population, yet each parity side must individually exceed half the star population, together with more than `D` unoccupied missing cross pairs. This is the correct narrow regime for the next fan/replication attack; it is independent of the invalidated matching-one conjecture.
