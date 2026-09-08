# n=30, Delta=17: early-kernel elimination

9 September 2026. Research directed by Paul Lenz; mathematical development, implementation and internal audit by ChatGPT/Geeps.

**Status: candidate mathematics. Independent expert review remains OPEN.** This note eliminates the two dense `n=30, Delta=17` scopes within the graph-to-demand framework already isolated and hostile-audited for n=29. It does not by itself prove the complete n=30 theorem.

## 1. Scopes

For `n=30`, `Delta=17`, put

```text
a = n-1-Delta = 12,
b = Delta = 17,
t = m-b(n-b).
```

Thus the two dense scopes are

```text
m=226 -> (a,b,t)=(12,17,5),
m=225 -> (a,b,t)=(12,17,4).
```

The important feature is that `a=12`, exactly as in the difficult n=29, Delta=16 case, while only the source side changes from `b=16` to `b=17`.

## 2. Mathematical inputs

No new order-specific graph lemma is introduced here. The calculation uses only the symbolic bridge consequences already isolated in the standalone n=29 bridge:

1. the complement/quasi-edge selected-residual construction;
2. for `t>0`, residual activity: every B-source has `rho_u>=1`;
3. label demand `s_i=max(0,d_i-R_i)` and `S=sum s_i >= r+2t`;
4. selected source demand: a selected source for label i satisfies `rho_u>=s_i`;
5. the charging inequality

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i),
```

and hence

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t;
```

6. the exact threshold-capacity inequality: for

```text
I_h={i:s_i>=h},
W_h=sum_{i in I_h}s_i,
Z_h={u:rho_u>=h},
z_h=|Z_h|,
```

one has

```text
2 W_h <= z_h^2-z_h+h(h+1).              (T_h)
```

The full hand derivation of `(T_h)` is preserved at

[`project/reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md`](../../../reviews/n29/2026-09-09-bridge-standalone-v1/THRESHOLD_CAPACITY_LEMMA.md).

Because residual activity gives every source baseline residual degree one,

```text
r >= b+z_h(h-1),
```

so for any upper bound `r<=rmax`,

```text
z_h <= floor((rmax-b)/(h-1)).             (2.1)
```

The only additional finite cut used at the end is the exact source-capacity Hall relaxation described in Section 5 below.

## 3. Complete demand domain

For `a=12`, every nondecreasing integer demand profile

```text
0 <= s_1 <= ... <= s_12 <= 11
```

that can arise from a graph must satisfy the exact charging inequality

```text
sum_i s_i(13-2s_i)/(12-s_i) >= 17+2t.    (3.1)
```

For a profile s, charging and `S>=r+2t` also give the exact necessary interval

```text
rmin = 17 + ceil(sum_i s_i(s_i-1)/(12-s_i)),
rmax = min(S-2t, C(12,2)-t).             (3.2)
```

The supplied script enumerates the complete sorted integer domain satisfying (3.1), not a sampled or heuristic subset.

Exact counts:

| scope | t | charging-feasible demand profiles |
|---|---:|---:|
| m=226 | 5 | 250 |
| m=225 | 4 | 1,155 |

## 4. m=226: threshold capacity alone closes the scope

For every one of the 250 charging-feasible profiles, combine its exact `rmax` from (3.2) with (2.1) and the threshold inequality `(T_h)`.

Every profile violates `(T_h)` at some threshold. The smallest strict threshold margin

```text
2W_h - [zmax^2-zmax+h(h+1)]
```

is **2**.

Therefore

```text
n=30, Delta=17, m=226
```

is impossible within the audited bridge framework.

No residual-row enumeration, LP model or floating-point infeasibility status is used.

## 5. m=225: thresholds plus 18 exact Hall duals

At `t=4`, the complete charging domain contains 1,155 profiles.

The exact early cuts give:

```text
1,070  threshold-capacity contradictions,
   67  source-count contradictions,
   18  profiles remaining.
```

The 18 remaining profiles are rejected by a source-capacity Hall relaxation.

Let `n_j` be the number of B-sources of residual degree `j`, `1<=j<=12`. For the `k` largest demands let `D_k` be their total demand. A residual-degree-j source has at most `12-j` selected slots and can select only a label whose demand is at most j. Hence its contribution to that prefix is at most

```text
A[k,j] = min(12-j, #{top-k labels with demand <= j}).
```

Every graph-realizable source multiset must therefore satisfy

```text
D_k <= sum_j A[k,j] n_j                 for every k,
sum_j n_j = 17,
sum_j (j-1)n_j <= rmax-17.              (5.1)
```

For each of the 18 profiles the script obtains rational dual weights from a numerical LP only as a proposal. It then scales them to integers and accepts the exclusion only after exact arithmetic verifies

```text
mu + sum_k y_k A[k,j] <= scale*(j-1)    for every j,
```

with `y_k>=0`, together with

```text
sum_k y_k D_k + 17*mu > scale*(rmax-17).
```

Multiplying (5.1) by these weights gives an immediate contradiction.

All 18 exact integer certificates are preserved in

[`D17_EXACT_DUAL_CERTIFICATES.json`](D17_EXACT_DUAL_CERTIFICATES.json).

The weakest exact dual margin is **3**.

Thus

```text
n=30, Delta=17, m=225
```

is also impossible within the audited bridge framework.

## 6. Result

The two Delta=17 scopes identified by the n=30 reconnaissance are eliminated:

```text
m=226, Delta=17: impossible,
m=225, Delta=17: impossible.
```

This leaves the n=30 dense non-bipartite problem with only

```text
m=226, Delta=16  -> (a,b,t)=(13,16,2),
m=225, Delta=16  -> (a,b,t)=(13,16,1).
```

So the parameterisation experiment succeeds in a strong sense: increasing the source side from 16 to 17 does not require the n=29 residual-row or final LP machinery at all. The stronger surplus values `t=5,4` make the early structural inequalities sufficient.

## 7. Clean reproduction

The clean GitHub Actions workflow

```text
.github/workflows/n30-d17.yml
```

completed successfully in run

```text
34292054922
```

at head commit

```text
6b9dc96487c4333c8846e778cf3a7fd59507548f.
```

That run:

1. regenerated both complete demand domains;
2. regenerated exact dual proposals for the 18 `m=225` residual profiles;
3. verified the regenerated duals with a standard-library-only exact checker;
4. independently reconstructed the 18-profile frontier and verified the committed 18 dual certificates exactly;
5. asserted the exact 250 / 1,155 domain counts and zero final survivors.

Different solver runs are not required to produce the same dual ray. The proof invariant is exact coverage of the 18-profile frontier plus direct verification of every integer dual. Earlier failed CI attempts that exposed this distinction, and one stale piece of certificate metadata, are preserved in [`CI_PROVENANCE_NOTE.md`](CI_PROVENANCE_NOTE.md).

Local replay:

```bash
python project/research/n30/2026-09-09-delta17-v1/delta17_kernel.py --output /tmp/n30-d17
python -S project/research/n30/2026-09-09-delta17-v1/verify_committed.py \
  /tmp/n30-d17/D17_EXACT_DUAL_CERTIFICATES.json \
  /tmp/n30-d17/D17_KERNEL_REPORT.json
```

Same-assistant clean replay is not external independent reproduction.

## 8. Review priority

External reviewers should attack the graph-to-demand bridge before spending time on the 1,405-profile arithmetic. In particular, any counterexample to residual activity, selected-source demand, charging, or threshold capacity invalidates the dependent elimination even if the script remains green.
