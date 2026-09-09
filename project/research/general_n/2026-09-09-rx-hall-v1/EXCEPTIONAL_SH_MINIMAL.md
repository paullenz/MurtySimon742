# Minimal SH correction for the exceptional n=30 hard state

9 September 2026. Research note inside the stripped selected/residual monotone-coupling framework; not an unrestricted Murty–Simon theorem.

The dominant two-dimensional BC staircase family in coordinates

\[
(d,-h)=(R+s,-(R+x))
\]

closes six of the seven preserved n=30 equality-frontier hard states exactly. The exceptional state is hard position 0, demand id 2094.

For that exceptional state, the full pairwise-ablation run showed that adding the SH family in coordinates

\[
(s,-h)=(s,-(R+x))
\]

closes the state exactly, whereas BC alone, BC plus one-dimensional s-tails, and BC plus the alternate SD family in (s,d) do not.

The instrumented SH separator generated four proof-active ambient upper-set cuts, with minimal generators

\[
C_0=\{(2,-2),(3,-6)\},
\]

\[
C_1=\{(1,-1),(2,-5),(3,-6)\},
\]

\[
C_2=\{(1,-1),(2,-7)\},
\]

and

\[
C_3=\{(1,-1),(2,-2),(3,-11)\}.
\]

An exhaustive exact test of all 16 subsets of these four cuts, always on top of the full preserved BC staircase library, gives:

- no subset of size 0, 1, or 2 rejects the exceptional state;
- among the four size-3 subsets, exactly one rejects it;
- the unique minimum rejecting subset is \(\{C_1,C_2,C_3\}\);
- the exact integer-Farkas contradiction for that minimum subset has RHS -658;
- all four cuts together also reject, with RHS -784.

Hence, within this generated correction family, three SH staircase inequalities are necessary and sufficient, and C0 is dispensable.

The current finite target can therefore be represented by two coupled two-dimensional majorization families sharing h:

1. a BC staircase family in (d,-h), with generator size at most 7 sufficient for all six nonexceptional states;
2. for the exceptional state, three additional SH staircases in (s,-h), of generator sizes 3, 2 and 3.

This is finite exact evidence. No universal bound saying that seven BC steps or these three SH patterns suffice for arbitrary n is claimed. The next research task is to derive a symbolic increasing potential of the form

\[
\Phi(s,d,h)=F(d,h)+G(s,h)
\]

or an equivalent pair of weighted staircase sums from the graph-derived mass identities and threshold inequalities.
