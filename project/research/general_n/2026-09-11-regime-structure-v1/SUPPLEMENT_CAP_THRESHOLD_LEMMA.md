# Supplement-cap threshold recursion lemma

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: elementary lemma about the monotone supplement-cap refinement used by the RX-Hall residual scanner. It is independent of the n=29 numerical certificate, but it does not by itself prove any Murty–Simon case. The accompanying finite replay is a regression test of the implementation.**

## Setup

Let the residual source set be `B`, with positive integers `rho_u >= 1` for `u in B`. Let `C_u >= 0` be any initial upper cap on the selected degree at source `u`.

For a cap vector `q=(q_u)`, define one refinement step by

```text
F_u(q) = max { k : 0 <= k <= q_u and
                   #{w != u : rho_w + q_w >= k-1} >= k }.
```

(If the displayed set has no positive `k`, the maximum is 0.)

Start from `q^(0)=C` and iterate

```text
q^(m+1) = F(q^(m)).
```

Since `F(q) <= q` coordinatewise and all coordinates are nonnegative integers, the sequence stabilizes after finitely many steps. Write its terminal vector as `q*`.

For `j >= 0`, define the terminal supplement-support count

```text
H_j = #{ w in B : rho_w + q*_w >= j }.
```

## Lemma

For every source `u` and every integer `k >= 1`,

```text
q*_u >= k
    iff
C_u >= k  and  H_{k-1} >= k+1.                 (1)
```

### Proof: forward direction

Assume `q*_u >= k`. At the terminal vector, `F(q*)=q*`. Since the support condition is monotone downward in the candidate degree, feasibility of the terminal selected cap `q*_u` implies feasibility of candidate `k`. Hence there are at least `k` distinct sources `w != u` with

```text
rho_w + q*_w >= k-1.
```

Also `u` itself satisfies

```text
rho_u + q*_u >= 1+k > k-1
```

because `rho_u >= 1`. Thus `H_{k-1} >= k+1`. Finally the refinement never increases a coordinate, so `C_u >= q*_u >= k`.

### Proof: reverse direction

Assume `C_u >= k` and `H_{k-1} >= k+1`.

The refinement sequence is coordinatewise decreasing, so for every iteration `m`,

```text
q^(m) >= q*
```

coordinatewise, and therefore the corresponding support count at threshold `k-1` is at least `H_{k-1}`.

We prove inductively that `q^(m)_u >= k` for every `m`. This is true at `m=0` because `C_u >= k`. If it holds at iteration `m`, then `u` itself is among the sources satisfying

```text
rho_w + q^(m)_w >= k-1.
```

There are at least `H_{k-1} >= k+1` such sources in total, so after excluding `u` at least `k` supporters remain. Candidate degree `k` is therefore feasible in the definition of `F_u(q^(m))`, giving

```text
q^(m+1)_u >= k.
```

By induction the inequality survives every refinement step and hence `q*_u >= k`.

This proves (1).

## Corollary: non-iterative ascending reconstruction

Equation (1) appears implicit because `H_{k-1}` contains the terminal caps. However

```text
rho_w + q*_w >= k-1
```

is equivalent to

```text
q*_w >= max(0, k-1-rho_w).
```

Since `rho_w >= 1`, the required cap threshold satisfies

```text
max(0, k-1-rho_w) <= k-2.
```

Therefore `H_{k-1}` depends only on terminal cap-threshold predicates strictly below level `k`.

Define Boolean tail variables

```text
B_{u,k} = 1[q*_u >= k],   B_{u,0}=1.
```

Then the terminal refinement can be reconstructed in ascending `k` by

```text
H_{k-1}
  = sum_w B_{w, max(0,k-1-rho_w)},

B_{u,k}
  = 1[C_u >= k] * 1[H_{k-1} >= k+1].            (2)
```

Thus no fixed-point iteration is mathematically necessary: each new cap level is determined by lower cap levels already computed.

A particularly useful consequence is that at a given level `k` the supplement condition is a **single global gate**. If the gate `H_{k-1} >= k+1` is open, every source whose initial cap reaches `k` keeps level `k`; if it is closed, no source keeps level `k`.

## Relevance to the general-N attack

The failed coarse symbolic relaxation documented in `N29_T2_SYMBOLIC_RELAXATION_FALSIFICATION.md` showed that the supplement refinement carries information not recoverable from degree sums and first-stage Hall bounds alone.

The lemma above compresses that missing geometry from a vector fixed-point process into a short sequence of threshold counts. This gives a plausible symbolic language for the next step:

1. express each initial cap `C_u` from the demand threshold counts and `rho_u`;
2. propagate the global gates (2) in ascending `k`;
3. combine the resulting source-cap tails with the largest-demand-prefix Hall inequalities;
4. ask whether the `T0/T1/T2` certificate inequalities can be derived regime-by-regime from those scalar count relations.

This is a structural simplification of the audited RX-Hall machinery, not yet a general Murty–Simon theorem.
