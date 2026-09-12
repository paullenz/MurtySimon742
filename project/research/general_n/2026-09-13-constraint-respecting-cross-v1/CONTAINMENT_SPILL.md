# Co-singleton trace and receiver-containment spill

13 September 2026. **Candidate general hand lemmas.** External mathematical review and novelty assessment remain OPEN. These lemmas use the canonical selected/residual bridge and the exact fixed-neighbourhood compatibility implication; they do not prove the unrestricted conjecture.

## 1. Co-singleton trace

Fix the canonical selected/residual cross-neighbourhoods. For `u in B` write

```text
S_u = selected A-labels at u,
R_u = residual A-labels at u,
N_u = S_u union R_u,
q_u = |S_u|,
rho_u = |R_u|.
```

For every `i in S_u`, let `w_i` be the actual exception of the selected edge `ui`. The fixed-neighbourhood compatibility lemma gives

```text
S_u \ N_(w_i) = {i},
S_(w_i) subset N_u.                                      (1)
```

The exceptions `w_i` are distinct as `i` varies, because distinct selected edges at one source represent distinct missing unordered B-pairs.

Thus the traces of the B cross-neighbourhoods on `S_u` contain every co-singleton `S_u-{i}`. This is stronger information than the scalar condition `rho_v+q_v>=q_u-1`.

### Common-neighbour corollary

Let `T subset S_u` have size `k>=1`, and let

```text
Gamma_B(T)={v in B : T subset N_v}.
```

The source `u` lies in `Gamma_B(T)`. In addition, for each `i in S_u\T`, the exception `w_i` contains every label of `T` by (1). These `q_u-k` exceptions are distinct and different from `u`. Therefore

```text
|Gamma_B(T)| >= q_u-k+1.                                (2)
```

Moreover every one of those exception rows satisfies `S_(w_i) subset N_u`.

## 2. Moment hierarchy

For each `k`-set `T` of A define

```text
M_k(T)=max({q_u-k+1 : T subset S_u} union {0}).
```

Equation (2) gives `|Gamma_B(T)|>=M_k(T)`. Summing over all `k`-sets and double-counting pairs `(v,T)` with `T subset N_v` gives

```text
sum_(|T|=k) M_k(T)
    <= sum_(v in B) binom(q_v+rho_v,k).                  (3)
```

For `k=1`, this is only the aggregated minimum endpoint-load information: a selected label at source u must have B-degree at least `q_u`. For `k>=2`, (3) retains higher-order overlap information lost by individual endpoint loads.

A local containment-weighted form is also immediate. For each source `u` and `1<=k<=q_u`, summing (2) only over rows whose selected sets fit inside `N_u` gives

```text
sum_(v: S_v subset N_u) binom(|S_u intersect N_v|,k)
    >= binom(q_u,k)(q_u-k+1).                            (4)
```

This explicitly retains the second compatibility condition in (1).

## 3. Endpoint load does not imply the pair moment

The higher-order trace is genuinely additional abstract cross-neighbourhood information.

Take five A-labels `0,1,2,3,4` and seven B-sources. Let source 0 have

```text
S_0={0,1,2,3}, R_0={4}.
```

Let the other six B-sources have empty selected sets and residual sets equal to the six unordered pairs of `{0,1,2,3}`.

Then every selected label `0,1,2,3` has B-degree 4, so the minimum endpoint load `D_i>=q_0=4` holds exactly. Source capacities also hold with `a=5`.

But every pair inside `S_0` would need common B-degree at least `q_0-1=3`. There are six such pairs, so the pair-trace requirement totals at least 18. The actual total pair moment is

```text
binom(5,2)+6 binom(2,2)=16.
```

Hence the pair moment fails although all four individual endpoint loads pass. This is an abstract cross-data separation example, not a D2C graph or a counterexample to any theorem.

## 4. Projecting receiver containment to `(s,rho,q)`

The local moment (4) still uses the actual sets. A weaker but profile-level consequence can eliminate them.

Put

```text
n_u = q_u+rho_u = |N_u|,
Q   = sum_v q_v = sum_i x_i,
```

where `x_i` is the actual selected degree of label i.

For fixed source u, the number of selected incidences whose labels lie outside `N_u` is

```text
L_u = sum_(i notin N_u) x_i.
```

Any compatible destination for an obligation from u must satisfy both

```text
q_v+rho_v >= q_u-1,
q_v <= n_u.                                               (5)
```

The first condition is needed to contain `S_u-{i}`; the second follows from `S_v subset N_u`. Also a destination must have positive incoming capacity `rho_v+b-a-1>=1`.

Define the scalar candidate receiver set

```text
C_u={v != u : q_v+rho_v>=q_u-1,
                  q_v<=n_u,
                  rho_v+b-a-1>=1}.
```

The `q_u` selected incidences at u have distinct exceptions, so at least `q_u` members of `C_u` must have their selected sets contained in `N_u`. If `|C_u|<q_u`, the profile is impossible.

Now let

```text
h_u=a-n_u,
g_v(u)=min(q_v,h_u).
```

If `S_v` is not contained in `N_u`, at most `g_v(u)` selected incidences at v can use labels outside `N_u`, because there are only `h_u` outside labels. A contained receiver contributes zero to `L_u`.

To maximize the amount of outside selected mass while still leaving `q_u` scalar candidates contained, leave contained the `q_u` members of `C_u` having the smallest `g_v(u)` and allow every other source except u to be non-contained. Therefore every actual realization satisfies

```text
L_u <= G_u

G_u = sum_(v != u) g_v(u)
      - sum_(q_u smallest values of g_v(u), v in C_u).    (6)
```

This uses no placement of labels.

### Eliminating the actual selected degrees

Let

```text
S = sum_i s_i,
e_i = |{v in B : rho_v>=s_i}|.
```

The canonical bridge gives

```text
s_i <= x_i <= e_i.
```

For any `n_u`-element set `N_u`, let `S_top(n_u)` be the sum of the `n_u` largest demands `s_i`, and let `E_top(n_u)` be the sum of the `n_u` largest eligibility counts `e_i`. Then

```text
L_u >= S-S_top(n_u),
L_u >= Q-E_top(n_u).
```

Consequently the following is a necessary profile-level condition:

```text
lambda_u := max(0,
                S-S_top(n_u),
                Q-E_top(n_u))
          <= G_u.                                        (7)
```

Together with `|C_u|>=q_u`, this is a receiver-containment spill test depending only on `a,b,s,rho,q`. It retains information from `S_v subset N_u` that the earlier scalar destination condition does not.

## 5. Bounded reconnaissance

[`check_containment_spill.py`](check_containment_spill.py) tests (7) on deterministic randomized exact-demand selected patterns from the same six frozen pilot states. It is reconnaissance only: the random generator does not enumerate all q-profiles.

For 2,000 sampled selected patterns per state, the test found no violations in five states. In N34 m289 state 13537, **173 of 2,000** sampled patterns violate (7), comprising 183 source-level violations.

This is evidence that the new inequality can cut selected-degree configurations before any residual-placement search. It does **not** exclude state 13537, change the N34 proof, or establish any whole-state count.

## 6. Next mathematical question

The spill inequality is now a natural candidate cut for the existing compatible-routing q-domain. The useful next test is not another random sample: add (7) to the preserved q/source-option enumeration and determine, with exact arithmetic and complete coverage, whether it removes any of the 4,584 generalisation survivors or tightens the closed potential.

If it does, inspect the first exact witnesses for a simpler demand/tail projection. If it does not, preserve that negative result: it would locate another limit of projection from exact set containment to scalar q-data.
