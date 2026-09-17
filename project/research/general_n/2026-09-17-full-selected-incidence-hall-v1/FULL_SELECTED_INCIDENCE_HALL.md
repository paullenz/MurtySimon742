# Full selected-incidence Hall / row-packing theorem

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate general lemma inside the canonical selected/residual bridge; not promoted; external mathematical review open.** This strengthens the earlier one-witness Hall theorem. The earlier theorem chose one selected witness from every active source. The canonical bridge contains the entire simple selected-incidence matrix, with exact row degrees `q_u` and exact column degrees `x_i`; retaining all of it gives a capacitated Hall system for every selected incidence.

## 1. Eligibility graph

Work in the all-positive-demand canonical branch. For each source `u in B` retain

    rho_u  residual degree,
    p_u    incoming missing-pair orientation load,
    q_u    selected degree / outgoing orientation load.

For each label `i in A` retain

    s_i>0              demand,
    x_i                selected degree,
    e_i=x_i-s_i>=0     selected excess,
    R_i                residual column degree,
    C_i=R_i+x_i        endpoint mass.

Put

    g_u=max(0,p_u-rho_u+1),
    w_u=p_u+q_u.

Every actual selected incidence `ui` obeys the already established conditions

    s_i <= rho_u,
    e_i >= g_u,
    C_i >= w_u.                                         (1)

Define the **eligibility graph** `J*` on `B x A` by declaring `ui` eligible exactly when all three inequalities in (1) hold.

The actual selected incidences form a simple bipartite subgraph `J` of `J*`. By definition of the canonical bridge,

    deg_J(u)=q_u,
    deg_J(i)=x_i,
    sum_u q_u=sum_i x_i=Q.                              (2)

## 2. Full capacitated Hall theorem

For `S subseteq B`, let

    N_i(S)={u in S : ui is eligible}.

A label `i` can receive at most `x_i` selected incidences in total, and because the incidence graph is simple it can receive at most one from each source. Hence its capacity available to the source set `S` is at most

    min(x_i, |N_i(S)|).

Therefore every actual canonical bridge satisfies

> **Full selected-incidence Hall inequality.** For every `S subseteq B`,
>
>     sum_{u in S} q_u
>       <= sum_{i in A} min(x_i, |N_i(S)|).             (3)

This is the standard capacitated Hall/max-flow condition. Conversely, because the source-label edges have unit capacity and the total row and column demands are both `Q`, the complete family (3) is also sufficient for realization of the selected incidence matrix inside `J*` (as an incidence-level object; it does not by itself realize the original graph or supplements).

The proof may be seen directly by cloning label `i` into `x_i` capacity slots, while remembering that the simple source-label edge has capacity one, or by the max-flow network

    source -> u  capacity q_u,
    u -> i       capacity 1 on eligible pairs,
    i -> sink    capacity x_i.

## 3. Immediate row-packing corollary

Taking `S={u}` in (3) gives the especially cheap necessary condition

>     q_u <= #{i : s_i<=rho_u, e_i>=g_u, C_i>=p_u+q_u}.    (4)

Thus a source with selected degree `q_u` needs `q_u` **distinct** compatible labels. Merely having one favourable label is insufficient.

This is strictly stronger than the earlier one-source endpoint envelope, which maximized the possible `q` using the best compatible label, and stronger than the one-witness Hall theorem, which reserved only one selected incidence per active source.

## 4. Threshold projection

Let `U(d,g,w)` be any collection of sources satisfying

    rho_u<=d,
    g_u>=g,
    w_u=p_u+q_u>=w.

Every selected incidence sourced in `U(d,g,w)` must use a label satisfying

    s_i<=d,
    e_i>=g,
    C_i>=w.

Applying (3) and discarding source-specific eligibility information gives the cheap threshold cut

>     sum_{u in U(d,g,w)} q_u
>       <= sum_{i:s_i<=d, e_i>=g, C_i>=w} min(x_i, |U(d,g,w)|).   (5)

Dropping the `min` gives the still cheaper but weaker bound by the sum of the compatible `x_i`.

The pure excess-level capacity family is the special projection

    sum_{u:g_u>=h} q_u <= sum_{i:e_i>=h} x_i,           (6)

already suggested by the small-excess continuation. Equation (3) is stronger because it retains demand compatibility, endpoint thresholds and the one-edge-per-source/label restriction simultaneously.

## 5. Strictness example at E=3

The following abstract near-Turan profile is useful because it passes the aggregate quadratic endpoint/excess ledgers and the pure excess threshold capacities, yet fails the single-source row-packing condition (4).

Take

    a=20, b=23, t=2,
    k=12 demand-five labels,
    E=3,
    r=88,
    Q=95.

### Sources `(rho,p,q)`

    3 x (1,3,0)
    2 x (4,6,1)
    5 x (4,3,5)
    1 x (4,3,7)
    7 x (4,3,8)
    5 x (5,7,1)

These give

    sum rho=88,
    sum p=sum q=95,

with exactly five sources of residual degree at least five.

### Labels `(s,R,e)`

    4 x (4,0,0)
    3 x (4,2,0)
    1 x (4,3,0)
    1 x (5,0,0)
    5 x (5,1,0)
    5 x (5,12,0)
    1 x (5,14,3)

Thus there are eight demand-four labels and twelve demand-five labels,

    sum R=88,
    sum e=3,
    sum x=95.

The endpoint masses `C=R+s+e` are respectively

    4,6,7,5,6,17,22

on the displayed label classes.

### Aggregate ledgers pass

For the weighted endpoint/excess ledger

    L_lambda=sum_i x_i(C_i+lambda e_i),
    W_lambda=sum_u q_u(p_u+q_u+lambda g_u),

one gets

    lambda=0:  L=940,  W=940,
    lambda=1:  L=964,  W=961,
    lambda=2:  L=988,  W=982,
    lambda=3:  L=1012, W=1003.

The pure excess thresholds also pass:

    h=1: 7<=8,
    h=2: 7<=8,
    h=3: 7<=8.

So neither the aggregate quadratic family nor the projected excess-capacity family rejects this profile.

### Row packing rejects immediately

Consider any of the seven sources with

    (rho,p,q)=(4,3,8).

For every selected incidence at such a source, (1) requires

    s_i<=4,
    e_i>=0,
    C_i>=p+q=11.

Only the eight demand-four labels can satisfy `s_i<=4`, but their endpoint masses are `4,6,7`; **none** has `C_i>=11`. Hence the right side of (4) is zero while the source requires `q=8` selected labels:

    8 <= 0,

impossible.

Thus the full selected-incidence theorem separates the exact incidence bridge from an abstract profile that survives the aggregate weighted ledgers exactly at `lambda=0` and with slack for positive weights.

This profile is not a graph realization and not a counterexample to Murty-Simon; it is a strictness witness for the projection hierarchy.

## 6. Strategic consequence

At total selected excess `E=3`, aggregate endpoint/excess accounting is no longer the right final projection. The next attack should retain at least the row-packing condition (4), and preferably the full capacitated Hall system (3), before launching any broader search.

A diagnostic integer transport screen using (4), (6), the quadratic endpoint ledger, exact margins and the mixed `{4,5}` assumptions has so far found the apparent `E=3` aggregate obstructions to be non-realizable at the selected-incidence level. That diagnostic is **not yet promoted here as a complete hand closure of E=3**; the next task is to extract a compact proof or a frozen complete finite certificate before claiming `E>=4`.
