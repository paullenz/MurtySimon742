# Unmatched internal-edge capacity and the sparse-U consequence

18 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**Status:** internal candidate structural theorem; external mathematical and novelty review remain open. This note is a direct continuation of `BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md` and the augmented orientation system in `NEAR_FULL_TIGHT_MATCHING_NORMAL_FORM.md`.

The new point is that the U--U part of the augmented orientation graph has a very simple capacitated interpretation. Once combined with the newly proved complementary-code mass cap, it makes a linear unmatched layer asymptotically sparse inside `G[U]`.

Retain the near-full notation:

- `p` tight antipode pairs;
- unmatched set `U`, `|U|=u`;
- `A`, `|A|=a`;
- partial Boolean multiplicities `t_c=|{y in U:c(y)=c}|` and `n_d=|{x in A:c(x)=d}|`;
- `q=e(G[U])`;
- `s=e_G(A,U)`;
- `E_U=sum_{y in U} epsilon_y`;
- `mu_alpha` is the projective alpha / switching true-twin cap.

---

## 1. U--U selected edges orient into complement-code capacity

For every physical edge `yz in E(G[U])`, the augmented orientation constraint is

`{bar c(y), bar c(z)}`.

Choose the canonical selected representative for that rooted B-edge and orient `yz` toward the B-source which supplies the selected cross edge. If it is oriented from `y`, the selected A-witness has code exactly `bar c(y)`.

For a fixed source `y`, distinct selected obligations use distinct physical cross edges `yx`. Therefore the number of U--U edges oriented out of `y` is at most

`n_{bar c(y)}`.

This gives an orientation of `G[U]` satisfying

> `d^+(y)<=n_{bar c(y)}` for every `y in U`.             (1.1)

Consequently, for every subset `S subseteq U`, every internal edge of `G[S]` has its tail in `S`, and therefore

> **U-EDGE CAPACITY THEOREM**
>
> `e(G[S]) <= sum_{y in S} n_{bar c(y)}`.                (1.2)

For `S=U`,

> `q <= sum_c t_c n_{bar c}`.                            (1.3)

This is an exact selected/Hall capacity inequality; it uses multiplicity, not merely the existence of complement codes in A.

---

## 2. Combine with the complementary-code mass cap

Let

`t_max=max_c t_c`.

Since the complement map on Boolean codes is a bijection,

`sum_{c:t_c>0} n_{bar c} <= a`.

Hence (1.3) gives

> `q <= t_max a`.                                        (2.1)

The companion note proves, for every occupied complement pair,

`p(t_c+t_bar c) <= (mu_alpha+1)a`.

In particular

`t_max <= floor((mu_alpha+1)a/p)`.

Therefore:

> **SPARSE-U CAP**
>
> `q <= a floor((mu_alpha+1)a/p)`                        (2.2)
>
> and in particular
>
> `q <= (mu_alpha+1)a^2/p`.                              (2.3)

For an above-threshold candidate, the preserved switching-stability theorem gives

`mu_alpha<=R_*`,

so

> `q <= (R_*+1)a^2/p`.                                   (2.4)

If `u=O(p)` and `lambda` is fixed, then `a=O(p)` and `R_*=O(sqrt(p))`. Thus

> `q=O(p^(3/2))`.                                        (2.5)

In particular, if `u=cp+O(1)` for fixed `c>0`, then

> `q/binom(u,2)=O(p^(-1/2))`.                            (2.6)

So the high-complexity linear-unmatched regime is forced to be **asymptotically sparse inside U**. This is a new qualitative restriction: the unmatched vertices may be numerous, but they cannot form a positive-density graph among themselves.

---

## 3. The same theorem forces a dense A--U cross layer

The exact unmatched-slack identity is

`E_U=u(p+u-1)-2q-s`.

Rearranging,

`s=u(p+u-1)-2q-E_U`.                                    (3.1)

Use the sparse-U cap (2.3):

> `s >= u(p+u-1)-2(mu_alpha+1)a^2/p-E_U`.                (3.2)

In an above-`M(n)` candidate the exact scorecard gives

`E_U+L_A<=S_req-2`,

so in particular `E_U<=S_req-2`. Hence

> `s >= u(p+u-1)-2(mu_alpha+1)a^2/p-(S_req-2)`.          (3.3)

Using `mu_alpha<=R_*` gives the entirely parameter-level necessary condition

> `s >= u(p+u-1)-2(R_*+1)a^2/p-(S_req-2)`.              (3.4)

For `u=cp+O(1)`, fixed `c>0` and fixed `lambda`, the leading term is

> `s >= c(1+c)p^2-O(p^(3/2))`.                           (3.5)

Since

`a=(2+c)p+O(1)`,

the average A-side U-degree satisfies

> `s/a >= [c(1+c)/(2+c)]p-O(sqrt(p))`.                  (3.6)

Thus the same surviving regime has a sharp two-layer shape:

- U itself is sparse: `q=O(p^(3/2))`;
- the A--U cross graph is quadratically large: `s=Theta(p^2)` when `u=Theta(p)`.

The unmatched vertices must therefore replace almost all of their missing U-neighbours by A-neighbours.

---

## 4. Rooted-triangle consequence

The exact rooted-triangle count is

`Q=p(p+u-1)+q`.

Therefore (2.4) gives

> `Q <= p(p+u-1)+(R_*+1)a^2/p`.                         (4.1)

In the linear-unmatched high-complexity regime,

> `Q=p(p+u-1)+O(p^(3/2))`.                              (4.2)

So almost all rooted triangles come from the forced tight-pair / unmatched-transversal skeleton; the extra contribution internal to U is lower order.

---

## 5. Strategic consequence

The aggregate Hall problem has now produced a concrete global shape rather than only local row restrictions.

A linear unmatched layer in a putative above-threshold graph must simultaneously satisfy

1. linearly many complementary U-code-pair types (`BETA_MULTIPLICITY_CODE_PAIR_STABILITY.md`);
2. only `O(sqrt(p))` vertices in any one complementary code pair;
3. only `O(p^(3/2))` edges inside U;
4. `Theta(p^2)` A--U edges.

The next useful attack should therefore move onto the **dense A--U bipartite layer**. In particular, beta-selected criticality witnesses already occupy a large collection of A--U edges, and the beta-target uniqueness condition says that reuse of one A-vertex across many unmatched sources imposes coordinatewise exclusions on all its other U-neighbours. Pricing those exclusions against the forced cross density is a more promising next step than further classifying `G[U]` itself.

No eventual second-extremal theorem is claimed. The `u=0` order-12/32 `X_3` hostile control is outside this unmatched-layer argument and remains untouched.