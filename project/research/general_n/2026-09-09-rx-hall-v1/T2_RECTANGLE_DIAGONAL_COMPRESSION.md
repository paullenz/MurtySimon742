# The n=29, t=2 rectangle–diagonal compression

10 September 2026. RX-Hall research programme.

**Status.** This note records a post-hoc compression of the already resolved finite
`n=29, t=2` frontier. The 38-profile hard-core result below has an exact integer
certificate and a separate arithmetic replay. The all-902 three-diagonal result
is currently floating reconnaissance unless a later section/checkpoint explicitly
upgrades it. Nothing here is an unrestricted proof of the Murty–Simon
conjecture, and the fixed-order n=29 candidate proof does not depend on this
compression.

## 1. BC transport generators

Use the BC coordinates

\[
d=R+s,\qquad v=b-(R+x)
\]

for a selected label incidence and

\[
\alpha=\rho+q-1,\qquad w=b-(q+p)
\]

for a source state. The candidate source–label compatibility bridge gives

\[
(d,v)\le(\alpha,w)
\]

coordinatewise on every selected incidence. Consequently every coordinatewise
nondecreasing function `F(d,v)` gives

\[
\sum_i x_iF(d_i,v_i)\le\sum_u q_uF(\alpha_u,w_u).
\tag{BC-F}
\]

### 1.1 Orthant rectangles

For integer thresholds `D,V`, put

\[
B_{D,V}(d,v)=\mathbf 1[d\ge D,\ v\ge V].
\]

Writing `H=b-V`, `(BC-F)` becomes

\[
\boxed{
\sum_i x_i\mathbf1[R_i+s_i\ge D,\ R_i+x_i\le H]
\le
\sum_u q_u\mathbf1[\rho_u+q_u-1\ge D,\ q_u+p_u\le H].
}
\tag{BC-D,H}
\]

Thus the rectangle generators are ordinary cumulative low-height transport
inequalities. A nonnegative sum of these is precisely a nonnegative monotone
supermodular BC potential on the finite grid.

### 1.2 Diagonal slack thresholds

For `c\in\mathbb Z`, put

\[
J_c(d,v)=\mathbf1[d+v\ge b-c].
\]

Since

\[
d+v=b-(x-s),\qquad \alpha+w=b-(p-\rho+1),
\]

this gives the exact cumulative slack inequality

\[
\boxed{
\sum_i x_i\mathbf1[x_i-s_i\le c]
\le
\sum_u q_u\mathbf1[p_u-\rho_u+1\le c].
}
\tag{DST-c}
\]

The derivation and stochastic-dominance interpretation are recorded separately in
`DIAGONAL_SLACK_THRESHOLD.md`.

For `c=0`, the label threshold is simply `x_i=s_i` and the source threshold is
`p_u\le\rho_u-1`.

## 2. Why this route was tried

The successful `t=3` compression used nine slope-one min-hinges

\[
H_{D,V}(d,v)=\min((d-D)_+,(v-V)_+).
\]

A natural attempt was to extend that analytic dictionary to `t=2`. The attempt
failed decisively: the full nonnegative grid of 187 min-hinges (`D=0..10`,
`V=0..16`) is infeasible even for demand 45, and remains infeasible after adding
all 12 canonical SH corrections. See

`checkpoints/N29_T2_FULL_MIN_HINGE_RUN_34388929974.json`.

The inverse search then allowed an arbitrary monotone BC potential. Demand 45
and the common 38-profile hard core both produced the same seven negative mixed-
difference locations

\[
(3,12),(4,11),(5,10),(6,9),(7,8),(8,7),(9,6),
\]

all on `d+v=b-1=15`. The full preserved surface is

`checkpoints/N29_T2_BC_FUNCTION_HARD38_RUN_34417897481.json`.

This strongly suggested adding a diagonal monotone generator to the ordinary
rectangle cone.

## 3. Failed one-dimensional simplifications

Two tempting scalar reductions were deliberately falsified before proceeding.

First, adding arbitrary nonnegative capped sums

\[
\min(d+v,K)
\]

to the rectangle/supermodular cone still leaves the common hard-38 system
infeasible, even when every finite `K` is available. See

`checkpoints/N29_T2_BC_CAP_CORRECTION_RUN_34418165165.json`.

Second, using only arbitrary diagonal threshold steps `J_c`, with no two-
dimensional rectangle term, fails demand 45 itself and hence the hard core. See

`checkpoints/N29_T2_SLACK_THRESHOLD_ONLY_RUN_34418684338.json`.

So the `t=2` obstruction is neither a pure min-hinge phenomenon nor a purely
one-dimensional slack-majorization phenomenon. It requires two-dimensional BC
content plus a small diagonal correction.

## 4. One diagonal repairs the 38-profile hard core

The full rectangle cone plus only

\[
J_0(d,v)=\mathbf1[d+v\ge b]
\]

is feasible for all 38 hard `t=2` profiles with **no SH correction**. The focused
floating diagnostic is

`checkpoints/N29_T2_BC_DIAGONAL_HARD38_RUN_34418796732.json`.

A direct rectangle-coordinate sparse solve then reduced the global potential to
10 rectangle generators plus `J_0`. A fixed-support exactifier and a separate
integer replay established exact finite rational feasibility:

- `checkpoints/N29_T2_RECTDIAG_EXACT_RUN_34419202027.json`;
- `checkpoints/N29_T2_RECTDIAG_EXACT_REPLAY_RUN_34419202027.json`.

The replay checks 17,621 finite model rows, all 38 contradiction margins and all
bounds using Python integer arithmetic, with no row or bound violations.

## 5. Small-integer global potential

The sparse floating coefficients suggested a much cleaner integer ray. It was
then fixed to the following normalized weights and re-solved only for the
profile-specific scalar dual variables:

\[
\begin{aligned}
F(d,v)= {}&72B_{2,11}+72B_{2,12}+126B_{2,13}\\
&+366B_{3,0}+61B_{3,5}+48B_{3,6}+48B_{3,7}+48B_{3,8}\\
&+54B_{3,9}+72B_{3,10}+90J_0.
\end{aligned}
\tag{T2-hard-F}
\]

This is now **exact finite evidence**, not merely a fit. The canonical result is

`checkpoints/N29_T2_RECTDIAG_INTEGER_PATTERN_RUN_34419905353.json`

and the separate arithmetic replay is

`checkpoints/N29_T2_RECTDIAG_INTEGER_PATTERN_REPLAY_RUN_34419905353.json`.

The replay reports 38/38 contradiction margins strictly negative, zero
homogeneous-row violations, zero bound violations, no missing variables, and a
worst normalized contradiction margin of `-0.999976`. It does not reuse the
exactifier's acceptance code. It does reuse the same finite state-model
constructor, so this is not claimed as external independent reproduction.

### 5.1 Original-variable form

Since `v=b-h`, the ten rectangles in `(T2-hard-F)` are equivalently

\[
\begin{array}{c|c|c}
D&H=b-V&\text{weight}\\ \hline
2&5&72\\
2&4&72\\
2&3&126\\
3&16&366\\
3&11&61\\
3&10&48\\
3&9&48\\
3&8&48\\
3&7&54\\
3&6&72
\end{array}
\]

plus 90 times `(DST-0)`. In particular `B_{3,0}` is simply the tail
`\mathbf1[d\ge3]` because `v\ge0` automatically on the finite BC state space.
The genuinely two-dimensional component therefore lives on only the two
`d`-threshold layers `D=2,3`.

## 6. Exactifier audit trail

The small-integer ray was subjected to two self-detected acceptance corrections,
both preserved rather than overwritten.

1. Run `34419331064` used an invalid rounding boost: profile-specific duals were
   doubled while the pinned global potential was not. Its `FAIL_EXACT` is not a
   mathematical falsification.
2. Run `34419636242` fixed that scaling, but still demanded that integer-rounded
   contradiction margins meet the arbitrary floating normalization `-C` exactly.
   The reported margins were all still strictly negative. The Farkas logic only
   requires strict negativity once the homogeneous rows are exact.
3. Run `34419905353` uses the correct logical acceptance criterion and passes,
   followed by a separately coded integer replay which also passes.

This history is relevant to robustness: the positive result was promoted only
after the acceptance semantics themselves were audited.

## 7. Extension from the hard 38 to all 902 t=2 profiles

A single diagonal `J_0` is **not** sufficient for a common all-902 potential, even
when the entire rectangle cone is available.

However, the full rectangle cone plus only the three neighboring diagonal
thresholds

\[
J_0,\qquad J_1,\qquad J_2
\]

is numerically feasible for all 902 regenerated `t=2` profiles with no SH
correction. In `K=d+v` language these are `K=16,15,14`. The floating run is

`checkpoints/N29_T2_BC_DIAGONAL_STEP_RUN_34418430767.json`.

Its active diagonal weights in the `near` solve are approximately

\[
\gamma_2=0.15986470,\qquad
\gamma_1=0.22381058,\qquad
\gamma_0=0.32950648.
\]

This is currently a **floating finite proposal**, not an exact certificate. The
active combinatorial statements themselves are nevertheless exact:

\[
\sum_i x_i\mathbf1[x_i-s_i\le c]
\le
\sum_u q_u\mathbf1[p_u-\rho_u+1\le c],
\qquad c=0,1,2.
\]

A current high-priority test asks whether the rectangle part for all 902 profiles
can also be restricted to the same two `d` layers `D=2,3` seen in the exact
hard-core potential. Its durable result, when complete, is expected under

`checkpoints/N29_T2_LAYER23_DIAG012_RUN_*.json`.

## 8. What this changes conceptually

The original finite RX-Hall machinery looked like a large staircase/Hall
dictionary. The inverse search now suggests a much smaller analytic language:

\[
\boxed{
\text{a few cumulative }d/h\text{ rectangle tails}
\; + \;
\text{a few cumulative slack tails}.
}
\]

For the hardest 38 `t=2` profiles the global potential is already an exact,
small-integer combination of ten rectangles on only two `d` layers plus one
slack threshold. For all 902 profiles, three slack thresholds suffice alongside
the unrestricted rectangle cone.

The next proof-oriented questions are:

1. does the two-layer rectangle restriction also cover all 902 profiles?
2. how sparse can the rectangle support be made without losing common coverage?
3. can the two layer functions be expressed by a short parameter rule rather
   than a table of thresholds?
4. how does this rectangle decomposition relate to the diagonal-chain rectangle
   decomposition of the successful `t=3` min-hinge potential?
5. can the resulting family be proved directly from the graph model and then
   optimized symbolically in `n,b,t`, rather than rediscovered at each fixed
   order?

Those questions are now higher priority than adding more ad-hoc finite features.
