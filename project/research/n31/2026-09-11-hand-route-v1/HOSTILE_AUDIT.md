# Hostile internal audit: N31 hand route

11 September 2026. Same-assistant hostile review; **not independent external validation**.

Target: `PROOF.md` and the new thirteen-label lemma. The audit deliberately treats historical N31 nonexistence as unavailable and rebuilds the chain from the canonical bridge, the twelve-label transfer, the new thirteen-label argument, and the N29 witness method.

## Verdict

**No blocking flaw found in the reviewed chain.** The audit did find one unnecessary dependency in the first draft: the proof invoked the general `7/12` maximum-degree theorem for `Delta>=19`. This was removed because the source-independent twelve-label theorem already closes every `18<=Delta<=29` branch, while `Delta=30` is the elementary universal-vertex/star case. The current `PROOF.md` is therefore strictly less dependent than the first draft.

Independent specialist review remains open, especially for the canonical selected/residual bridge shared by the twelve- and thirteen-label arguments.

## 1. Global reduction

At 240 edges, average degree is `480/31>15`, so `Delta>=16`.

The published Dailly-Foucaud-Hansberg dominating-edge result states that a non-bipartite D2C graph with a dominating edge, other than their graph `H_5`, has at most `floor(n^2/4)-2` edges. Their paper explicitly records that `H_5` has six vertices. Thus at order 31 every non-bipartite graph in the 240-edge target range has no dominating edge. This is exactly the hypothesis used by the witness-deficit branch.

A bipartite diameter-two graph is complete bipartite, so the bipartite case is independently immediate.

## 2. Delta>=18

For `18<=b<=29`, `a=30-b` lies in `1..12`. The twelve-label transfer gives `e(G)<=b(31-b)`. This concave quadratic is already decreasing on this interval; its maximum is `18*13=234`. Thus no `Delta>=18` graph reaches 240. `Delta=30` has a universal vertex; edge-criticality forbids any edge among the other 30 vertices, so the graph is a star.

This removes all high-degree reliance on the separate `7/12` theorem.

## 3. Thirteen-label score bound

The proof defines

`D=sum_{h=2}^{12}(N_h-gamma_h(W_h))` and `Q=p+D`.

The high-level argument was checked algebraically: for `h>=8`, a hypothetical positive deficit would require

`hN<=C_h(N-1)`,

while writing `N=h+e`, `0<=e<=5`, gives the strict defect

`2hN-2C_h(N-1)=-e^2+3e+2h-2>0`.

The four remaining clipping stages `7->6->5->4->3` were checked two ways:

1. line by line against the capacity values stated in the manuscript;
2. by an exact Python regression over every current-maximum multiset at those stages, 76,960 vectors in total.

The terminal max-three proof reduces to two integers `0<=y<=x<=13`. Its lower bounds on `gamma_2` and `gamma_3` were re-derived from the displayed strict capacity defects. They give `D<=7` for `y<=12`, and direct evaluation at `(x,y)=(13,13)` gives `D=8`.

The equality argument was separately checked on the `3/4` layer. Every nonconstant vector of thirteen threes/fours has `D<=7`, so a pre-clipped `D=8` vector cannot contain an entry above three.

Finally, a separately coded C++ sweep enumerated all **5,200,300** nondecreasing thirteen-demand vectors in `{0,...,12}`. It found

`max Q = 21`

with exactly one maximizer:

`(3,3,3,3,3,3,3,3,3,3,3,3,3)`.

The exhaustive program does not share the clipping proof logic.

## 4. N31 Delta=17 above equality

Here `b=17`, `a=13`, `t=m-238`. The bridge gives `Q>=b+2t`.

At `m>=241`, `t>=3`, hence `Q>=23`, contradicting the hand bound `Q<=21`. No equality reasoning is needed in this range.

## 5. N31 Delta=17 at m=240

At `m=240`, `t=2`, so `Q>=21`; the score lemma forces `Q=21` and the unique demand vector `s=3^13`, with `S=39`.

Threshold capacity gives `z_2,z_3>=9`. Residual activity and the tail identity give

`r=17+sum_{h>=2}z_h>=35`,

while the demand ledger gives `39=S>=r+4`, hence `r<=35`. Therefore equality is forced:

- `r=35`;
- `z_2=z_3=9`;
- every higher `z_h` is zero;
- residual source degrees are exactly nine 3s and eight 1s.

Selected-incidence forcing with demand three then shows every selected edge originates in the nine degree-three sources.

At `h=2`, `W_2=39=C_2(9)`. The complete threshold-capacity chain is therefore equality. If `J` is the set of high sources with more than two selected edges, the scalar equality gap is

`(7-j)(6-j)/2=0`,

so `j=6` or `7`. Equality also makes every high source outside `J` have exactly two selected edges. Consequently the sources in `J` emit at least 33 selected edges. The threshold proof itself forces every exception of an edge emitted from `J` back into the nine high sources, so

`sum_{Z} p_u >= 33`.

The same equality chain gives exactly 39 selected edges in total. Since every one of the 13 labels needs at least three, each label has selected degree exactly three. Thus `R_i+x_i=d_i`. For any selected edge from a high source `u`, endpoint load and source selected-degree forcing yield

`q_u+p_u <= d_i <= q_u+2`,

so `p_u<=2`. Every high source is active, hence

`sum_Z p_u<=18`,

a contradiction.

No circular use of the desired N31 theorem was found in this equality chain.

## 6. Delta=16 witness branch

The N29 witness method transfers with `Delta=16`, `n=31`. With deficits `epsilon_x=16-d(x)`, no dominating edge gives witness deficit sum at least two. Let `h` count deficits at least two and `o` count deficit-one vertices. Then

`2h+o<=T=496-2m`

and the same witness-capacity count gives

`m<=C(h,2)+h(31-h)+o(o-1)`.

At `m>=241`, `T<=14`; the exact maxima for `h=0,...,7` are

`182,162,149,143,144,152,167,189`,

all far below 241.

At `m=240`, `T=16`; the exact maxima for `h=0,...,8` are

`240,212,191,177,170,170,177,191,212`.

Thus equality forces `h=0,o=16`. The direct/two-step witness count then gives

`240<=240-e(G[O])`,

so `O` is independent. Its 16 vertices all have degree 15 and therefore meet all 15 outside vertices, forcing `K(16,15)`.

The arithmetic checker reproduces both tables exactly.

## 7. Remaining review targets

The new work materially reduces the audit surface, but it does not make external review optional. The highest-value external targets are:

1. the canonical graph-to-selected/residual bridge, especially selected-incidence forcing and threshold capacity;
2. the equality interpretation of threshold capacity in the `3^13` endpoint;
3. the witness coverage/capacity statement inherited from the N29 direct proof;
4. novelty/literature status of the fixed-order `n=31` result.

Within those stated dependencies, this audit found no blocking mathematical defect.
