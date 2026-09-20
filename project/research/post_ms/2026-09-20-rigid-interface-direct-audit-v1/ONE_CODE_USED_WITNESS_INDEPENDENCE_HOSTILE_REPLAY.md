# Hostile replay — used complementary-U witness independence

Date: 2026-09-20

Status: **same-session independent hostile replay** of `ONE_CODE_USED_U_WITNESS_INDEPENDENCE.md`. The conclusion survives, but the proof wording needs an orientation clarification recorded below. This remains conditional on reaching the rigid one-code interface; bounded actual-D2C regression still has zero positive rigid complete Hall-cut fixtures with `x>=3`.

## 1. Setup

Use the rigid one-code notation

- `A_X--Y` complete, `x=|A_X|>=3`;
- `Y=A_d`, `A_bar(d)=emptyset`;
- every selected crossing witness in U for a d-coded source lies in `U_bar(d)`.

Let `W` be the union of all selected `U_bar(d)` crossing witnesses.

If `z in W`, then for some source `s in Y` and head `h in A_X`,

`N(s) cap N(z)={h}`.

Since `s` is adjacent to every vertex of `A_X`, this immediately gives

> `N(z) cap A_X={h(z)}`.                                  `(HR-1)`

Thus every used U-witness has exactly one X-head.

## 2. Orientation issue in the predecessor wording

The raw same-code U--U theorem does **not** say that an arbitrary chosen endpoint of a same-code edge can always be prescribed as the certificate source. It says that one of the two endpoints can be oriented as source.

Therefore the sentence in the predecessor proof

> "after orienting the edge, say with source z"

is safe only because **both endpoints of the edge under consideration lie in W**. One must first choose the valid criticality orientation, and only then rename its source endpoint `z`.

This distinction matters. The argument below proves `G[W]` independent, but it does **not** by itself prove that a used witness is anticomplete to every unused vertex of `U_bar(d)`: if an edge joined used `z` to unused `z'`, the valid orientation could have source `z'`, for which `(HR-1)` is unavailable.

That stronger anticompleteness statement is therefore *not* promoted.

## 3. Independent replay of the theorem

Suppose `zz' in E(G[W])`. Both endpoints have code `bar(d)` and both lie in W.

Apply the raw full coded-layer same-code criticality theorem to `zz'`. It supplies one valid orientation. Rename the source endpoint `z` and the other endpoint `z'`. Because **both original endpoints lie in W**, the chosen source `z` still satisfies `(HR-1)`.

The raw theorem supplies a witness `q` such that

`N(z) cap N(q)={z'}`.

Since the source `z` lies in U, the raw theorem puts `q` in A. Same-code localization gives

`c(q)=d`.

In the one-code branch `A_d=Y`, so `q in Y`.

But `q` is adjacent to every vertex of `A_X`, in particular to `h(z)`. By `(HR-1)`, `z` is also adjacent to `h(z)`. Therefore

`h(z) in N(z) cap N(q)`.

The required common neighbourhood is the singleton `{z'}` with `z' in U`, while `h(z) in A_X`. Contradiction.

Hence

> **`G[W]` is independent.**                              `(HR-2)`

The proof is orientation-safe because whichever endpoint raw criticality chooses as source is a used witness and therefore has a unique X-head.

## 4. Consequences that survive unchanged

Let `w=|W|`, and let `k_P` be the minimum pair-local U-witness requirement used in the predecessor note. The selected source--witness incidences still give at least `y k_P` distinct Y--W nonedges. Summing the U-degree identity over W and using `(HR-2)` gives exactly the predecessor bill

> `E_W >= w(g0+w-2)+y k_P`,                              `(HR-3)`

where `g0=p-y`.

For `g0>=1`, `w>=k_P` yields

> **`E_W>=k_P(p+k_P-2)`.**                               `(HR-4)`

Thus the load-bearing quadratic witness price survives the hostile replay.

## 5. New safe rooted consequence

For any fixed source `s in Y`, let `W_s subseteq W` be its selected U-witness set and put

`k=|W_s|`, `d=u-k`.

Because `W_s` is independent, every U-edge has at least one endpoint in `U\W_s`. Therefore, writing `q=e(G[U])`,

> **`q <= k d + binom(d,2)`**
> `   = d u-d(d+1)/2`.                                   `(HR-Q)`

This is an exact physical U-edge ceiling. In the minimum-source parameterization of the one-code near-rigid branch, `d<=c=lambda+1-g0`, so the rooted triangle channel is controlled directly by the same gap parameter.

The companion note `ONE_CODE_ROOTED_Q_FEEDBACK.md` feeds `(HR-Q)` into the exact rooted residual identity.

## 6. Audit verdict

- `G[W]=empty` **passes** independent replay.
- The quadratic bill `E_W>=k_P(p+k_P-2)` **passes**.
- The proof must be read with the valid orientation chosen first and the source endpoint renamed second.
- No stronger claim `E(W,U_bar(d)\W)=empty` is justified from this argument alone.

This is a strengthening of proof hygiene, not a weakening of the theorem actually used downstream.