# Supplement-cap scalar cutoff lemma

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: elementary structural lemma about the monotone supplement-cap refinement used by the RX-Hall residual scanner. It is independent of the n=29 numerical certificate, but it does not by itself prove any Murty–Simon case. The accompanying finite replay is a regression test of the implementation.**

## Setup

Let the residual source set be `B`, with positive integers `rho_u >= 1` for `u in B`. Let `C_u >= 0` be any initial upper cap on the selected degree at source `u`.

For a cap vector `q=(q_u)`, define one refinement step by

```text
F_u(q) = max { k : 0 <= k <= q_u and
                   #{w != u : rho_w + q_w >= k-1} >= k }.
```

Start from `q^(0)=C` and iterate `q^(m+1)=F(q^(m))`. Since the vector decreases coordinatewise in nonnegative integers, it stabilizes. Write the terminal vector as `q*`.

## 1. Threshold form

For `j>=0`, put

```text
H_j = #{w in B : rho_w + q*_w >= j}.
```

Then for every source `u` and integer `k>=1`,

```text
q*_u >= k
    iff
C_u >= k and H_{k-1} >= k+1.                    (1)
```

### Proof

If `q*_u>=k`, then at the fixed point candidate `k` is feasible, so at least `k` other sources satisfy `rho_w+q*_w>=k-1`. Source `u` itself also satisfies that inequality because `rho_u>=1`; hence `H_{k-1}>=k+1`. Also `C_u>=q*_u`.

Conversely assume `C_u>=k` and `H_{k-1}>=k+1`. Since every iterate dominates `q*`, every iterate has at least `H_{k-1}` sources at threshold `k-1`. Inductively, if the current cap at `u` is at least `k`, then `u` is one of those sources and at least `k` other supporters remain, so candidate `k` survives the next refinement. Starting from `C_u>=k`, it survives every iteration. Thus `q*_u>=k`.

## 2. Ascending threshold reconstruction

The condition `rho_w+q*_w>=k-1` asks only whether

```text
q*_w >= max(0,k-1-rho_w) <= k-2,
```

because `rho_w>=1`. Thus level `k` depends only on already-determined cap levels below `k`.

Writing `B_{u,k}=1[q*_u>=k]` and `B_{u,0}=1`, one may reconstruct the terminal vector in ascending `k` by

```text
H_{k-1} = sum_w B_{w,max(0,k-1-rho_w)},
B_{u,k} = 1[C_u>=k] * 1[H_{k-1}>=k+1].          (2)
```

At each level the supplement condition is therefore one **global gate** shared by every source.

## 3. Stronger scalar-cutoff form

Define

```text
Z_u = rho_u + C_u,
A_j = #{u in B : Z_u >= j}.
```

The sequence `A_j` is nonincreasing. Define, with `K=max_u C_u`,

```text
L = max { k in {1,...,K} : A_{k-1} >= k+1 },     (3)
```

and put `L=0` if the set is empty.

Then

```text
q*_u = min(C_u,L)                                (4)
```

for every source `u`.

### Proof

The gate condition at level `k` is monotone in `k`: once it fails, all higher gates fail because the relevant support tail cannot increase while the required count does increase.

Before the first failed gate, all lower cap levels have survived. Therefore, when testing level `k`, the predicate needed from source `w` is a cap threshold at most `k-2`, and it is equivalent simply to the corresponding initial-cap predicate. Hence

```text
H_{k-1}=#{w:rho_w+C_w>=k-1}=A_{k-1}
```

for every level reached before the first failure. Consequently the open gates are exactly the initial segment `1,...,L` determined by (3). A source keeps precisely the levels `k<=C_u` that lie in this common open segment, which is (4).

Equivalently, if

```text
h_2 = max { j>=0 : #{u:Z_u>=j} >= j+2 },
```

then `L=min(K,1+h_2)`. This is a two-shifted h-index (descriptive terminology) of the initial support scores `Z_u`.

## 4. RX-Hall specialisation

In the RX-Hall residual scanner, if `a` is the number of demand labels and

```text
D_r = #{i : s_i <= r},
```

then the initial cap is

```text
C_u = min(a-rho_u, D_{rho_u}).                   (5)
```

Therefore

```text
Z_u = rho_u + C_u
    = min(a, rho_u + D_{rho_u}).                 (6)
```

Since `D_r` is nondecreasing, `Z(r)=min(a,r+D_r)` is nondecreasing in the residual degree `r`. Thus the shifted-h-index cutoff couples only two one-dimensional cumulative profiles: the demand lower tails `D_r` and the source upper tails of `rho`.

This is much smaller than the original vector fixed-point description.

## 5. Hall-supply corollary

For any subset `P` of demand labels, let

```text
E_P(r) = #{i in P : s_i <= r}.
```

A source of residual degree `r` contributes at most

```text
min(q*_u, E_P(r))
 = min(L, a-r, D_r, E_P(r))
 = min(L, a-r, E_P(r)),                          (7)
```

because `E_P(r)<=D_r`.

Hence after the supplement refinement the Hall upper supply for `P` is exactly represented by the scalar-cutoff expression

```text
sum_u min(L, a-rho_u, E_P(rho_u)).               (8)
```

For the audited scanner it is enough to apply this to the largest-demand prefixes. The iterative supplement-cap vector has disappeared completely; its effect is carried by the single integer `L`.

## 6. Finite n=29,t=2 replay

`n29_t2_supplement_threshold_replay.py` independently computes

1. the original iterative C++-equivalent refinement;
2. the ascending threshold recursion (2); and
3. the scalar cutoff (3)-(4).

GitHub Actions run `34584456716` passed with **0 mismatches on all 902 regenerated frontier profiles**. The finite cutoff census is

```text
nu1=0: L=6 (110), L=7 (703), L=8 (12)
nu1=1: L=6 (21),  L=7 (55)
nu1=2: L=6 (1)
```

These counts are diagnostics, not universal statements.

## 7. Relation to the earlier residual h-index attack

The 7 September general-order attack used the ordinary h-index of the residual degree sequence `rho` to aggregate the selected-edge inequality. The present lemma produces a shifted h-index of

```text
Z_u = rho_u + C_u,
```

where `C_u` is the demand-induced selected-degree cap.

These are not the same invariant, and no theorem connecting the two has yet been proved. But they now arise from two independent parts of the same residual ledger:

- the ordinary `rho` h-index controls how many labels can demand many distinct residual-active sources;
- the shifted `rho+C` h-index controls how far the distinct-supplement source caps can survive.

This makes a combined two-index inequality a concrete next target rather than a vague analogy.

## 8. Relevance to the general-N attack

The failed coarse relaxation in `N29_T2_SYMBOLIC_RELAXATION_FALSIFICATION.md` proved that degree sums plus first-stage Hall bounds do not capture enough geometry. The scalar cutoff lemma identifies the missing information in a compact form.

The next proof target is now:

1. express `L` from the demand and residual-degree cumulative counts using (5)-(6);
2. replace the iterative refinement everywhere by the scalar Hall inequalities (8);
3. combine those inequalities with the ordinary residual h-index bounds;
4. seek a regime-wise inequality proving the fixed `T0/T1/T2` certificates, then parameterise the resulting count argument in surplus `t`.

This is a structural simplification of the audited RX-Hall machinery, not yet a general Murty–Simon theorem.
