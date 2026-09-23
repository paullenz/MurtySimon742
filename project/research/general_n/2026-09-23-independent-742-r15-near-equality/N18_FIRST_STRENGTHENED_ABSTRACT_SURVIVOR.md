# First strengthened n=18, Delta=10 abstract survivor

## Closed disjoint shards

The exact bounded driver closed the following ranges with zero survivors:

- 8,901-10,900 (closest gap 3);
- 14,901-16,900 (closest gap 3);
- 16,901-18,900 (closest gap 4).

The 10,901-12,900 and 18,901-20,900 processes were interrupted after the survivor below appeared. They receive no range-closure credit.

## Survivor at scalar 14,440

The 12,901-14,900 shard stopped at its first survivor:

- demands: `d=(5,5,5)`;
- assigned witness counts: `x=(5,5,5)`;
- overlap caps: `h=(5,5,5)`;
- centre deficits: `(5,5,5)`;
- right types: four copies of `({0,1,2}, deficit 0)` and one copy of `({0,1,2}, deficit 1)`;
- minimum total deficit: `16=Dmax`.

Thus all three labels use exactly the same five assigned witness vertices. Four witnesses have degree 10 and one has degree 9; the three label vertices each have degree 5.

This is only an aggregated incidence-pattern survivor. It does not establish a simple graph, the required exact criticality sources, diameter two, or D2C edge-deletion criticality.

## Next graph-level question

Determine whether three degree-5 label vertices can share the same five witnesses while every assigned label-witness pair has an exact source satisfying the crossed supplement restrictions, with only one deficit unit outside the three centres. A source collision or nested-complement obstruction would exclude the tuple; otherwise build and directly certify an actual D2C graph.
