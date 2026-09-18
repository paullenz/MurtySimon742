# Zero-signing subcores force quadratic A-slack; all `tau<=2` unmatched rows are priced

18 September 2026. Research directed by Paul Lenz; derivation and regression design by ChatGPT/Geeps.

**Status: internal candidate structural theorem; not externally reviewed.** This note generalises `MATCHED_PRIVATE_FOOT_SLACK_AND_COMPLETE_ROW_QUADRATIC_EXCLUSION.md`, then applies the exact `tau(Psi(K_y))<=2` row classification from `UNMATCHED_ROW_KERNEL_CAPACITY_STABILITY.md`.

The point is that the quadratic A-side payment does not require the whole matched 2-lift to be zero-signed. A large zero-signed **subcore** is enough, because its two physical cliques manufacture their own singleton/co-singleton support through edge criticality.

---

## 1. Zero-signing subcore

Fix a maximum-degree root `v`, tight fibres

`P_i={q_i,q_i'}`, `i=1,...,p`,

and unmatched set `U`.

Let `R subseteq [p]`, `|R|=s>=3`, and suppose the matched 2-lift restricted to the fibres in `R` is parallel after switching. Equivalently

`Q_R={q_i:i in R}`

and

`Q_R'={q_i':i in R}`

are both cliques `K_s`.

No condition is imposed on signs involving coordinates outside `R`.

---

## 2. The two cliques manufacture the support needed for amplification

Apply the rooted clique-private-foot theorem to `Q_R`. All but at most one source `q_i` has an A-private foot for some critical edge of `Q_R`.

If `h` is private to source `q_i`, then restricted to the coordinates in `R` its Boolean code is exactly the co-singleton

`R\{i}`.

Indeed `h` is adjacent to `q_i` and to no other vertex of `Q_R`, while every A-vertex chooses exactly one endpoint of each tight fibre.

Thus A realises at least `s-1` distinct restricted co-singleton classes on `R`.

Applying the same theorem to the mate clique `Q_R'` shows that A realises at least `s-1` distinct restricted singleton classes on `R`.

So, without using the full orientation-code graph, the two physical cliques themselves supply precisely the support pattern used in the complete-row sphere-amplification argument.

---

## 3. Edge-by-edge slack inside the subcore

Choose, for every physical edge of `Q_R`, one valid critical orientation and one A-private foot certifying it. Group the chosen oriented edges by the actual private foot.

For a Q-side foot `h` from source `q_i`, let `T(h) subseteq R\{i}` be the target coordinates of the chosen edges assigned to `h`, and put `t=|T(h)|`.

For every target `j in T(h)`, private-foot criticality gives

`N(h) intersect (A union U) subseteq H_j^1`,

where `H_j^1` is the A/U halfspace selecting the mate `q_j'`. Hence

`N(h) intersect (A union U) subseteq H_T^1 := intersection_{j in T} H_j^1`.

As before,

`|H_j^1|=p+u-epsilon_{q_j'}`.                                  `(ZS1)`

If `t=1`, the matched-target private-foot slack transfer already gives `epsilon_h>=1`.

Assume `t>=2`. Among the restricted singleton classes on `R`, at most one is missing. Choose `j_0 in T` whose singleton class is realised. This realised vertex lies in `H_{j_0}^1` but outside `H_T^1`.

For every other target `k in T\{j_0}`, the restricted co-singleton `R\{k}` also lies in `H_{j_0}^1\H_T^1`; at most one such co-singleton class is missing. Therefore at least `t-1` distinct realised A-vertices lie in

`H_{j_0}^1\H_T^1`.

Together with `(ZS1)`, this yields

`epsilon_h>=t`.

The mate-clique argument is symmetric: a Q'-side private foot certifying `t` selected clique edges also has `epsilon_h>=t`.

Because `s>=3`, Q-side feet have restricted weight `s-1`, while Q'-side feet have restricted weight `1`; the two populations are disjoint.

Summing over the assigned physical edges of the two cliques gives

`sum_{h in H_Q} epsilon_h >= binom(s,2)`,

`sum_{h in H_Q'} epsilon_h >= binom(s,2)`.

Hence:

> **ZERO-SIGNING SUBCORE QUADRATIC SLACK THEOREM.**
>
> If the matched tight-pair core contains a zero-signed subcore on `s>=3` fibres, then
>
> `L_A >= s(s-1)`.                                               `(ZS2)`

This is a hand D2C theorem. The finite regression below audits only the support bookkeeping and integer arithmetic.

---

## 4. Exact second-extremal region for a subcore of size s

Recall

`S_req = p lambda + 3p + u lambda + 2u - c_lambda - 2`,

where

`c_lambda=ceil(lambda(lambda+2)/2)`.

Above `M(n)` the parity gap forces

`E_U+L_A <= S_req-2`.

Since `E_U>=0`, `(ZS2)` excludes an above-threshold graph whenever

`s(s-1)>=S_req-1`.                                              `(ZS3)`

If `s=p-k`, this is equivalent to

> `(lambda+2)u <= (p-k)(p-k-1)-p(lambda+3)+c_lambda+3`.          `(ZS4)`

The cases `k=0,1,2` are the ones needed below.

---

## 5. Application to the complete-bipartite complement row

For a fixed unmatched row `y`, let

`L_y=bar K_y`

be the sign graph of the matched 2-lift in the coordinate system centred at `y`.

If `L_y` is complete bipartite, then it is a cut. Switching one side removes every sign, so the whole matched core is zero-signed. Thus `s=p`, recovering

`L_A>=p(p-1)`.

This includes all one-code rows as special cases.

---

## 6. Application to star-plus-isolates

Suppose `L_y` is a star together with isolated vertices, one of the exact `tau(Psi(K_y))<=2` families.

Delete the star centre coordinate. Among the remaining `p-1` coordinates there are no sign edges at all. Hence they form a zero-signing subcore with

`s=p-1`.

For `p>=4`, `(ZS2)` gives

> `L_A >= (p-1)(p-2)`.                                         `(STAR1)`

Therefore such a row is excluded above `M(n)` whenever

> `(lambda+2)u <= p^2-(lambda+6)p+c_lambda+5`.                  `(STAR2)`

In particular:

- `lambda=-1`: excluded if `u<=p^2-5p+5`;
- `lambda=0`: excluded if `2u<=p^2-6p+5`;
- `lambda=1`: excluded if `3u<=p^2-7p+7`.

The star size itself is irrelevant to this bound.

---

## 7. Application to the two-centre leaf family

In the third exact `tau<=2` family, every sign edge is incident with one of two centre coordinates (with the centre-centre edge optional).

Delete both centres. The remaining `p-2` leaf coordinates have no sign edges among themselves, so they form a zero-signing subcore of size

`s=p-2`.

For `p>=5`, `(ZS2)` gives

> `L_A >= (p-2)(p-3)`.                                         `(TC1)`

Hence a two-centre row is excluded above `M(n)` whenever

> `(lambda+2)u <= p^2-(lambda+8)p+c_lambda+9`.                  `(TC2)`

In particular:

- `lambda=-1`: excluded if `u<=p^2-7p+9`;
- `lambda=0`: excluded if `2u<=p^2-8p+9`;
- `lambda=1`: excluded if `3u<=p^2-9p+11`.

---

## 8. Unified low-row-cover consequence

The exact row theorem says every `tau(Psi(K_y))<=2` kernel belongs to one of:

1. complete-bipartite sign graph;
2. star plus isolates;
3. two-centre leaf graph, optional centre edge.

The three cases contain zero-signing subcores on at least `p`, `p-1`, and `p-2` fibres respectively. Therefore, for `p>=5`, any unmatched row satisfying

`tau(Psi(K_y))<=2`

forces the uniform lower bound

> `L_A >= (p-2)(p-3)`.                                         `(LOW2)`

Consequently, throughout the quadratic region `(TC2)`, an above-`M(n)` near-full configuration must satisfy

> `tau(Psi(K_y))>=3` for **every** unmatched row `y`.            `(LOW3)`

This is the main structural gain: the complete exact `tau<=2` row classification is now priced on the global second-extremal defect scale.

---

## 9. Regression

Companion checker:

`check_zero_signing_subcore_quadratic_slack_and_tau2_rows.py`.

It independently checks:

1. the restricted singleton/co-singleton exclusion count for every `s=3,...,9`, every possible omitted singleton class, every possible omitted co-singleton class, every source, every nonempty target set, and both clique sides;
2. the equivalence of `(ZS3)` and `(ZS4)` for `k=0,1,2`, all valid `p<=100`, `u<=200`, and `-1<=lambda<=min(u+1,20)`.

Finite totals:

- support configurations: `705,356`;
- minimum support margin: `0`;
- support failures: `0`;
- arithmetic configurations: `1,230,639`;
- arithmetic failures: `0`.

Again, these checks audit bookkeeping only; the private-foot/slack theorem is the mathematical argument.

---

## 10. Strategic consequence

The row frontier has moved from the exceptional cheap cases to the genuinely generic regime. Within `(TC2)`, every unmatched row of an above-threshold candidate would have local row cover at least three.

The next high-value target is therefore a **many-row Hall-capacity theorem for `tau>=3` kernels**, rather than more case-by-case treatment of cheap row graphs. One promising formulation is to lower-bound the aggregate number/multiplicity of A code classes required by the beta obligations when every U-row has cover at least three, while charging repeated classes through the existing per-source capacity inequalities and the fan true-twin/Hamming-sphere dichotomy.

The published 2024 `n=12,m=32` graph remains untouched: it is full-tight (`u=0`) and has no unmatched rows.

No all-order second-extremal theorem is claimed.
