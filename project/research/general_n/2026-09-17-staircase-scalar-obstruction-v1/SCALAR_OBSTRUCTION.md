# Scalar staircase obstruction: why naive repeated peeling cannot close scope

17 September 2026. Research directed by Paul Lenz; derivation and audit by ChatGPT/Geeps.

**Status: clean obstruction inside the current scalar relaxation; not a graph construction, not a counterexample to Murty–Simon, and not promoted mathematics.** The purpose is strategic: test whether the existing layer-cake, staircase-capacity, h-index and heavy-load inequalities can by themselves force the exact square block after repeated peeling.

## 1. Step-back correction

The previous handoff proposed recursively applying the staircase inequalities until either a square exact block appeared at some lower level or residual-tail area became impossible.

There is an immediate conceptual issue. If `h` is the residual h-index and `N_h=h`, then for every lower level `d<h` one automatically has

    N_d >= N_h = h > d.

So the same unreduced graph cannot literally reach another square face `N_d=d` below `h`. A lower-level square block would require a **reduced/peeled graph system**, not merely another scalar inequality on the original tails.

That does not make the staircase theorem useless: it still proves a real top-level dichotomy. But it means the proposed recursion needs a new structural operation or a new coupled inequality, not mechanical iteration of `SC_d`.

## 2. A concrete scalar witness

The stronger obstruction is an exact abstract profile at the first-above-Turan edge count.

Take

    a=20,
    b=23,
    n=44,
    t=2,
    m=b(a+1)+t=485=floor(44^2/4)+1.

Let all 20 labels have demand

    s_i=4,

so

    S=80.

Let the residual source degrees be

    rho = (5^5, 4^11, 1^7),

so

    r=76

and therefore the demand/residual ledger is tight:

    r+2t = 76+4 = 80 = S.

The demand tails are

    K_1=K_2=K_3=K_4=20,
    K_d=0 for d>=5,

while the residual tails are

    N_1=23,
    N_2=N_3=N_4=16,
    N_5=5,
    N_d=0 for d>=6.

Thus the residual h-index is exactly 5, but there are no demand-5 labels:

    N_5=5,
    K_5=0.

The exact five-by-five square face is not approached. The demand mass has stabilized one level lower while the residual tail has expanded from 5 to 16 sources.

## 3. Full staircase-capacity family survives

For `d=1,2,3,4` one has `W_d=80`. The threshold-capacity right sides are

    d=1:  1*23 + C(22,2) = 254,
    d=2:  2*16 + C(14,2) = 123,
    d=3:  3*16 + C(13,2) = 126,
    d=4:  4*16 + C(12,2) = 130.

Hence every nontrivial staircase inequality

    W_d <= d N_d + C(N_d-d,2)

holds, with slacks 174, 43, 46 and 50 respectively.

The layer-cake ledger is also exact:

    sum_d (K_d-N_d)
      = (20-23)+(20-16)+(20-16)+(20-16)+(0-5)
      = 4
      = 2t.

So adding more copies of the existing `SC_d` inequalities cannot by itself rule out this tail geometry.

## 4. Other current scalar bridges also survive

### H-index saturation

At the residual h-index `h=5` one has `u=0` and `k=K_5=0`. The saturation theorem gives

    b+2t = 27 <= (a-5)*4 = 60.

Receiver inflation at the top level is vacuous because there are no demand-5 labels.

### Canonical charging inequalities

The charging bound (10.1) gives

    sum_i s_i(s_i-1)/(a-s_i)
      = 20*(12/16)
      = 15
      <= r-b
      = 53.

The demand-only form (10.2) gives

    sum_i s_i(a+1-2s_i)/(a-s_i)
      = 20*4*13/16
      = 65
      >= b+2t
      = 27.

### Heavy-load/routing family

The obstruction is not an artefact of checking only the simplified `T=4h` corollary.

For each heavy threshold `h=1,2,3,4`, the audit evaluates the **exact restricted local source capacity** `C(h,T,P,c)` from the 12 September heavy-load theorem for every relevant finite cutoff. Here

    P_u = rho_u+b-a-1 = rho_u+2,

and the compatibility capacity is

    c_u=min(a-rho_u, #{i:h<=s_i<=rho_u}).

All finite cutoffs through the point where a direct linear tail estimate takes over pass. The minimum exact slacks are

    h=1: 114 at T=5,
    h=2:  98 at T=8,
    h=3:  84 at T=12,
    h=4:  48 at T=16.

For the infinite tail, the 16 sources with residual degree 4 or 5 have capacities

    c=15 on five sources,
    c=16 on eleven sources.

For `T>=16`, choosing `H=c,p=0` in the exact local domain gives total source contribution at least

    5*15(T-15) + 11*16(T-16)
      = 251T-3941.

Thus the heavy-load right side is at least

    76h + 251T - 3941,

while the left side is `20hT`. This lower bound is already sufficient for

    T>=17 when h=1,
    T>=18 when h=2,
    T>=20 when h=3,
    T>=22 when h=4.

The remaining finite ranges are exhaustively checked by `check_scalar_obstruction.py`. Therefore this abstract profile survives the entire exact restricted heavy-load cutoff family, not only the published `T=4h` specialization.

## 5. Basic degree-sequence compatibility is not the issue

To make clear that the witness is not failing at the first elementary degree check, choose label residual degrees

    R = (4^16, 3^4).

Then `sum R_i=76=r`, and with `d_i=R_i+4` one obtains

    d = (8^16, 7^4),
    sum d_i=156=2(r+t).

Hence `s_i=d_i-R_i=4` exactly for every label.

The audit verifies:

- `(8^16,7^4)` is graphical by Erdős-Gallai;
- the residual bipartite row sequence `(5^5,4^11,1^7)` and column sequence `(4^16,3^4)` is bipartite-graphical by Gale-Ryser.

This still does **not** construct the selected representatives, supplements, criticality witnesses or a diameter-two edge-critical graph. It only shows that the scalar obstruction is not caused by a trivial degree-sequence impossibility.

## 6. What this disproves, and what it does not

This witness disproves the proposed implication

    existing scalar staircase + existing heavy-load inequalities
        => repeated peeling reaches an exact square block or contradiction.

It does **not** disprove any graph theorem already proved. It is an abstract feasible point of the current aggregated relaxation.

The strategic lesson is important: more algebraic recombination of the same tail inequalities is unlikely to bridge exact-block scope. The current relaxation has enough room for demand to sit at level 4 while a broad residual level-4 tail absorbs all existing scalar charges.

## 7. Better next move

The next structural attack should return to information lost by the scalar relaxation.

The most promising candidate is the **joint endpoint-load/orientation coupling** before source capacities are maximized independently. Every selected incidence `ui` satisfies

    R_i+x_i >= q_u+p_u,

while the selected missing-pair orientation globally obeys

    sum_u q_u = sum_u p_u

and uses distinct unordered B-pairs. The current heavy-load theorem replaces this joint system by independent local maxima `C(h,T,P,c)`. The witness above survives precisely after that decoupling.

A useful next theorem would therefore couple:

1. endpoint loads `R_i+x_i`,
2. source outdegrees `q_u`,
3. supplement indegrees `p_u`,
4. the global orientation identity `sum q=sum p`,
5. pair uniqueness,
6. demand compatibility.

Alternatively, a genuine recursive peeling theorem would need to define a reduced graph/representative system whose new residual h-index can fall. Iterating `SC_d` on the original tails cannot do that.

This is a negative result in the productive sense: it closes off a tempting but insufficient route and identifies the information that the next proof must retain.
