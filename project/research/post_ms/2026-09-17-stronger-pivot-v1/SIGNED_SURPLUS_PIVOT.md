# Signed-surplus pivot toward the eventual dense D2C problem

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal hand mathematics; not promoted; external mathematical review and novelty review open.

> **Literature correction — 17 September 2026.** The first version of this note treated Dailly–Foucaud–Hansberg Conjecture 3 (2019) as a viable all-order target. A published 12-vertex, 32-edge D2C graph exceeds `floor((n-1)^2/4)+1`, so that all-order conjecture is false. The mathematics below does **not** use Conjecture 3 as a premise: `M(n)=floor((n-1)^2/4)+1` is retained as a comparison threshold for the sufficiently-large/eventual problem. See `LITERATURE_CORRECTION_2024_EXCEPTION.md` and `DEPENDENCY_AUDIT_2019_FALSE_CONJECTURE.md`.

## 1. Why the project target changes

A public repository, `Erdos742/Erdos742`, created before the present project, contains a Lean formalisation claiming the full Erdős #742 inequality and a separate equality-clause formalisation. Source-level audit has not found a dependency gap on the target chain; the one visible `sorry` in the inequality file is an unused negative statement. A clean independent recompilation has not yet been performed here, so this is not treated as peer-reviewed acceptance. It is nevertheless enough to remove any sensible assumption of first-proof priority for the original Murty–Simon target unless the external proof later fails audit.

The existing project mathematics remains useful because it is structurally different. The active target is now the **sufficiently-large/eventual second-extremal problem** around the threshold proposed in 2019, not the false all-order form.

Dailly, Foucaud and Hansberg's Conjecture 3 (Discrete Mathematics 342 (2019), 3142–3159, DOI 10.1016/j.disc.2019.06.023) proposed:

> If `G` is a non-bipartite diameter-2-critical graph of order `n`, and `G` is not the exceptional six-vertex graph `H5`, then
>
> `e(G) <= floor((n-1)^2/4)+1`,
>
> with equality exactly for their expanded-five-cycle family `C5+` and thirteen listed small graphs.

That statement is now known to be false in all orders because of the published 12-vertex exception. It remains mathematically natural as an eventual comparison threshold.

Qiao Lin and Xiaolin Wang, Discrete Applied Mathematics 375 (2025), 332–337, DOI 10.1016/j.dam.2025.06.025, prove that every sufficiently large `C5`-free D2C graph at or above this threshold is complete bipartite. Thus any sufficiently large non-bipartite equality example or counterexample to an eventual form must contain a `C5`.

This file asks what survives from our residual/Hall framework when the edge count is lowered from the Turán level to this second-extremal threshold. None of the algebra below assumes the threshold is a universal theorem.

## 2. Residual setup without assuming positive surplus

Use the canonical general-order setup already preserved in

`project/research/general_n/2026-09-07-residual-hindex-v1/README.md`.

Let `b=Delta(G)`, `a=n-1-b`, and

`t=m-b(n-b)`.

For the complement-root construction, let `F` be the graph on the `a` A-labels, `r` the number of residual A–B edges, `rho_u` the residual degree of a B-source, `R_i` the residual degree of an A-label, and

`s_i=max(0,d_i-R_i)`.

The bookkeeping identities themselves do not need `t>0`:

`e(F)=r+t`,

`sum_i R_i = sum_u rho_u = r`.

The selected-edge inequality also does not use positive surplus: for every selected incidence `(u,i)->w`,

`d_i <= rho_u+R_i`,

so a positive demand `s_i=q` needs at least `q` distinct selected sources with residual degree at least `q`.

The earlier proof used `t>0` only to eliminate sources with `rho_u=0`. At the second-extremal threshold those sources can no longer be discarded; they become a main structural object.

## 3. Zero-source defect lemma

Let `u in B` satisfy

`rho_u=0`.

Put

`S=N_A(u)`, `T=A\S`.

Then:

1. every cross-edge `ui`, `i in S`, is selected;
2. there is no `F`-edge between `S` and `T`;
3. `e(F[S]) <= -t`.

In particular, a zero-residual source can exist only when `t<=0`.

### Proof

Because `rho_u=0`, every A-neighbour of `u` is a selected edge. Let `w_i` be the B-supplement of the selected edge `ui`; the supplements are distinct at a fixed source.

If `i in S`, `j in T`, and `ij in E(F)`, the selected edge `ui` would have to dominate the A-vertex `j` in addition to its designated B-exception. But `uj` is absent by definition of `T`. Hence

`E_F(S,T)=empty`.                                                    (Z1)

Now let `ij` be an `F`-edge inside `S`. The selected edge `uj` must dominate the supplement `w_i`, forcing the cross-edge `jw_i`; symmetrically `iw_j` exists. Both are residual, and the resulting `2e(F[S])` residual edges are distinct.

For every `F`-edge `pq` inside `T`, the H-nonedge `pq` misses `u` and therefore has a quasi-edge. Its auxiliary cannot lie in A: an A-auxiliary able to dominate `u` lies in `S`, while (Z1) says every S–T pair is an H-edge, so it would also dominate the supposed A-exception. Thus the auxiliary lies in B. This supplies a residual cross-edge whose A-endpoint lies in `T`. Distinct `F[T]` edges give distinct residual edges, and these are disjoint from the preceding S-endpoint family.

Therefore

`r >= 2e(F[S])+e(F[T])`.

By (Z1),

`e(F)=e(F[S])+e(F[T])=r+t`.

Hence

`r >= e(F)+e(F[S]) = r+t+e(F[S])`,

so

`e(F[S]) <= -t`.                                                     (Z2)

This proves the lemma.

### Structural corollaries

- `S` is a union of connected components of `F`.
- For every connected component `C` of `F` and every zero source `u`, either all vertices of `C` are H-adjacent to `u` or none are. Thus zero sources give binary signatures to the components of `F`.
- `t>0` implies there are no zero sources, recovering the old residual-activity theorem.
- At `t=0`, every zero source has `e(F[S])=0`; its selected side can contain only edgeless components of `F`.

This component-signature formulation is the main new object for the eventual second-extremal problem.

## 4. Signed h-index inequality

Let

`z=#{u in B:rho_u=0}`.

Assume the residual h-index `h` is positive. Write

`|{u:rho_u>=h}|=h+eta`

and

`k=#{i:s_i=h}`.

Then

> `b+2t <= (a-h-eta)(h-1)+k+z`.                     (SH)

A coarser form is

> `b+2t <= (a+1)h-h^2+z`.                            (SH0)

Thus the exact cost of dropping positive-surplus activity from the old h-index argument is an additive `z`.

### Proof

The selected-edge inequality implies `s_i<=h` for every label. Only `k` labels attain `h`, so

`sum_i s_i <= kh+(a-k)(h-1)=a(h-1)+k`.              (1)

The exact residual ledger still gives

`r+2t=sum_i(d_i-R_i)<=sum_i s_i`.                    (2)

There are `h+eta` residual degrees at least `h`. Outside those vertices there are exactly `z` zero sources, while every remaining source has residual degree at least one. Hence

`r >= h(h+eta)+(b-h-eta-z)`

`  = b+h(h-1)+eta(h-1)-z`.                           (3)

Combining (1)–(3) yields (SH). Replacing (1) by the coarser `sum_i s_i<=ah` and (3) by `r>=b+h(h-1)-z` yields (SH0).

When `z=0`, (SH) is exactly the earlier saturation inequality. The point is not to weaken the old theorem, but to identify the missing state variable in the signed-surplus regime.

## 5. Where the second-extremal threshold sits in `t`

Define

`M(n)=floor((n-1)^2/4)+1`

and write

`e=m-M(n)`.

Thus `e=0` is the **2019 proposed / eventual comparison level**. `e>=1` means the graph lies above that threshold; because the 2019 all-order conjecture is false, this is not by itself a contradiction to any valid theorem.

Let

`d=Delta-floor(n/2)`.

### Even order

If `n=2s`, then `M=s^2-s+1`, `Delta=s+d`, and

`Delta(n-Delta)=s^2-d^2`.

Therefore

> `t=e+d^2-(s-1)`.                                    (T-even)

At the first above-threshold level `e=1`, positive surplus is automatic only once

`d^2>=s-1`.

### Odd order

If `n=2s+1`, then `M=s^2+1`, `Delta=s+d`, and

`Delta(n-Delta)=s(s+1)+d-d^2`.

Therefore

> `t=e+d(d-1)-(s-1)`.                                 (T-odd)

At the first above-threshold level `e=1`, positive surplus is automatic only once

`d(d-1)>=s-1`.

So the existing positive-surplus Hall/residual machinery remains potentially powerful in the high-degree branch, but it cannot by itself address the balanced-degree branch of the eventual problem.

## 6. The expanded-`C5` comparison family lies on the negative side

Take an expanded 5-cycle from `C5+`. Let three consecutive cycle vertices be replaced by nonempty independent twin classes `X1,X2,X3`, with the other two cycle vertices left single. Put

`q=|X2|`, `r=|X1|+|X3|=n-q-2`.

The edges are exactly the complete joins along the five cyclic adjacencies, so

`m=q r+r+1=(q+1)r+1`.

The defining condition for `C5+` is

`q in {floor((n-3)/2),ceil((n-3)/2)}`.

The degrees are:

- `r` on `X2`;
- `q+1` on `X1` and `X3`;
- at most `r` on the two singleton cycle vertices.

Hence:

- for `n=2s`, `Delta=s` and `m=s^2-s+1=M(n)`;
- for `n=2s+1`, `Delta=s` and `m=s^2+1=M(n)`.

In both parities,

> `t=m-Delta(n-Delta)=1-s<0`                          (C5)

for `s>1`.

This is the decisive strategic fact: the natural expanded-`C5` eventual equality model is not a small perturbation of our `t>0` regime. It lives a linear distance into negative surplus. Continuing the old selected-excess ladder would therefore optimize the wrong coordinate system for the new problem.

## 7. New decomposition of the research problem

The residual/Hall programme should now split into two branches.

### Branch A — positive surplus / high maximum degree

When (T-even) or (T-odd) is positive, the existing activity theorem gives `z=0`; all h-index saturation, receiver inflation, exact-incidence Hall and Hall-ramp machinery remain available. The all-E mixed `{4,5}` closure from predecessor `7e1c9409...` is preserved as a strong local engine here.

### Branch B — nonpositive surplus / balanced degree

Here zero sources are possible and are not noise. By the zero-source defect lemma, each one selects a union of `F`-components and gives a binary component signature. The selected sides have internal `F`-edge budget at most `-t`.

The next theorem should couple **two or more zero sources**. Their selected component unions cannot be arbitrary because:

- every A-edge at a zero source is selected;
- supplements at a fixed source are distinct;
- unordered B-pairs are represented in only one orientation;
- selected-edge forward/reverse containment still applies;
- each selected side is a union of entire F-components.

The objective is to show that many zero sources force a small cyclic/twin block system, plausibly matching the expanded-`C5` construction, while too few zero sources leave enough positive residual mass for a quantitative h-index/Hall penalty.

### `C5` as the structural anchor

Lin–Wang's 2025 theorem says that, for sufficiently large order at this density, the `C5`-free branch is already complete bipartite. Thus a sufficiently large non-bipartite extremal or counterexample to an eventual classification must contain a `C5`. A promising route is to combine an actual `C5` with the zero-source component signatures rather than trying to recover `C5` indirectly from scalar inequalities.

## 8. Exact next target

Take two zero-residual sources `u,v`. Let

`S_u=N_A(u)`, `S_v=N_A(v)`.

Both are unions of connected components of `F`, and both satisfy

`e(F[S_u]), e(F[S_v]) <= -t`.

Classify the four component-signature types

`00, 01, 10, 11`

according to adjacency to `(u,v)`. Use selected-pair orientation uniqueness and forward/reverse containment to determine which pairs of component types can simultaneously carry F-edges and selected supplements.

A useful outcome would be either:

1. a forbidden signature pair / laminarity theorem;
2. a lower bound on residual mass in terms of the number of nontrivial signature classes; or
3. a forced cyclic five-block quotient matching `C5+` at equality.

Any failure or counterexample to these possibilities should be preserved rather than hidden. Do not return to `E=10`-style enumeration: predecessor `7e1c9409...` already closes that entire axis.
