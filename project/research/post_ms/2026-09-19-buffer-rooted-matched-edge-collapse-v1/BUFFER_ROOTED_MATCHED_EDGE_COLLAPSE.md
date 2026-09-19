# Buffer rooted matched-edge collapse

Date: 2026-09-19

Status: internal conditional structural theorem inside the audited rigid one-code `z=1` positive-buffer common-buffer branch. This note does **not** assert graph realizability, the false all-order 2019 Dailly–Foucaud–Hansberg conjecture, or a global eventual theorem. The published order-12 graph `X_3` remains the mandatory negative control and is outside the present hypotheses (`u=0`).

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, the root `README.md`, the latest commit chain through `7b5dc8c2d0d511d87981080ae5c2cceb953807b0`, the 19 September daily adversarial audit, the independent source-tuple re-proof, the source-premise repair / graph-level regression status, and the current shared-core handoff.

The binding trust boundary is unchanged:

- distinct physical beta-source identity is accepted at the raw singleton-criticality level established by the repair;
- `(source,coordinate)` uniqueness is selected-representative uniqueness, not raw-witness uniqueness;
- the finite source-tuple capacity theorem remains conditional on those premises and is not unconditional graph-level closure;
- the actual-D2C regression retains `X_3`, records zero known graph/formula mismatches, but has no positive bounded fixture realizing all rigid complete-cut hypotheses;
- exact pair-local `S_P/Ccap_P` remains mandatory downstream, with `(ONE-P)` and `(CROWD)` dominated only in the sublayers where that has already been proved;
- the four-exception gate remains subordinate.

The predecessor handoff asked to continue inside the unmatched-heavy shared-core tail using its located U-nonedges and source capacity. Before doing that, I rechecked the tail's **parent equality geometry** against the raw rooted B-edge criticality theorem. That upstream check closes the parent geometry outright. This is therefore a mathematically necessary departure from the predecessor's downstream priority: once the parent hypothesis is impossible, source-tuple or pair-capacity optimization inside it is no longer the highest-value move.

No source-tuple theorem, selected-incidence injectivity, finite scan or pair-capacity relaxation is used in the closure below.

---

## 2. Parent equality geometry

Retain the first positive-buffer equality setup from `POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md`.

- The A-layer is `A=X dotcup Y`, with `X--Y` complete, `x=|X|>=3`, `y=|Y|>0`.
- Every vertex of `Y` has tight code `d`.
- Every vertex of `X` has code different from both `d` and `bar d`.
- `g=g_P`, `k=x-g>0`, and `t=p-g>=1`.
- `U_-=U_{bar d}=W_0 dotcup {b}`, with `|W_0|=k`.
- The common buffer is unloaded, `d_Y(b)=0`.
- The buffer reaches its degree floor, `epsilon_b=t=p-g`.

The last equality implies

> `b--X` is complete and `b--U_o` is complete.             `(B0)`

The repaired raw criticality analysis already proved that every edge `bx`, `x in X`, has **no reverse certificate and no matched Orientation-A certificate**. Hence every such edge must have an outside unmatched witness `z in U_o` satisfying

> `bz in E`, `xz notin E`, `N(x) cap N(z)={b}`,            `(OU1)`
>
> `c(z)=bar c(x)`,                                         `(OU2)`
>
> `z` is anticomplete to `Y`.                              `(OU3)`

The new obstruction comes from applying raw rooted criticality to a matched edge incident with such a `z`.

---

## 3. Unit I — every outside certificate exposes a shared matched endpoint

Fix `x in X` and an outside certificate `z` satisfying `(OU1)--(OU3)`.

Since `c(x) != bar d`, there is at least one tight coordinate `i` for which

> `c(x)_i=d_i`.                                            `(M1)`

Let `q_i` be the matched endpoint selected by `z` in fibre `i`.

By `(OU2)`,

`c(z)_i=bar c(x)_i=bar d_i`.

The buffer has code `bar d`, so `b` selects the same endpoint in fibre `i`. Therefore

> `z q_i in E` and `b q_i in E`.                          `(M2)`

Both `z` and the matched endpoint `q_i` lie in the rooted neighbourhood `B=N(v)`. Thus `zq_i` is a rooted B-edge. The rooted triangle-edge witness theorem must orient it and provide an A-witness whose common neighbourhood with the source is the singleton head.

This observation is physical: no selected representative convention enters.

---

## 4. Unit II — the forward rooted orientation is impossible under buffer equality

Suppose `zq_i` is oriented with source `z` and head `q_i`. Then raw rooted criticality requires some `a in A` with

> `N(z) cap N(a)={q_i}`.                                  `(F)`

There are two possible A-locations.

### `a in X`

By `(OU1)`, `bz in E`; by buffer equality `(B0)`, `ba in E`. Hence `b` is a common neighbour of `z` and `a`, distinct from the prescribed matched head `q_i`. This contradicts `(F)`.

### `a in Y`

Every Y-code is `d`. At coordinate `i`, the matched endpoint `q_i` is the endpoint selected by `bar d`, whereas a Y-vertex selects the opposite endpoint `d`. Hence

`a q_i notin E`,

so `q_i` cannot be the singleton common neighbour in `(F)`.

Therefore the forward rooted orientation of `zq_i` is impossible.

---

## 5. Unit III — the reverse rooted orientation is also impossible under buffer equality

Suppose instead `zq_i` is oriented with source `q_i` and head `z`. Then raw rooted criticality requires some `a in A` with

> `N(q_i) cap N(a)={z}`.                                  `(R)`

In particular `az in E`.

### `a in Y`

This is impossible by `(OU3)`: `z` is anticomplete to `Y`.

### `a in X`

By `(M2)`, `bq_i in E`; by buffer equality `(B0)`, `ba in E`. Thus `b` is a second common neighbour of `q_i` and `a`, distinct from the prescribed head `z`, contradicting `(R)`.

Therefore the reverse rooted orientation of `zq_i` is impossible as well.

Since every rooted B-edge must admit one of these two singleton orientations, `zq_i` cannot exist in a D2C graph under the equality hypotheses. But `(M2)` forced it. Contradiction.

---

## 6. Unit IV — general outside-certificate self-pricing lemma

The previous contradiction has a useful stability form which does **not** assume `b--X` complete.

Retain an outside certificate `(OU1)--(OU3)` for a buffer edge `bx`, and choose a coordinate `i` satisfying `(M1)`. The same shared matched edge `zq_i` is forced by `(M2)`.

Apply rooted B-edge criticality to `zq_i` without assuming buffer equality.

- In the forward orientation, a Y-witness still cannot contain the head `q_i`; therefore the witness must lie in `X`. If that X-witness `a` were adjacent to `b`, then `b` would be a second common neighbour of `z,a`. Hence `ba` must be a nonedge.
- In the reverse orientation, a Y-witness is still impossible because `z` is anticomplete to `Y`; therefore again the witness lies in `X`. If it were adjacent to `b`, then `b` would be a second common neighbour of `q_i,a`. Hence again `ba` must be a nonedge.

Thus:

> **OUTSIDE-CERTIFICATE SELF-PRICING.** Every outside-U certificate for a buffer--X edge forces at least one physical buffer--X nonedge. `(SP)`

Equivalently, if

`h_b=e_bar({b},X)`,

then the existence of even one outside certificate implies

> `h_b>=1`.                                                `(SP1)`

This is a raw graph statement. It is upstream of Hall score, source tuples and pair capacity.

---

## 7. Unit V — complete closure of the first positive-buffer equality layer

In the first positive-buffer equality geometry, `(B0)` gives `h_b=0`.

But the predecessor matched-channel collapse says **every one** of the `x` buffer--X edges must use an outside certificate. By `(SP1)`, any one of those certificates forces `h_b>=1`.

Contradiction.

Therefore:

> **ROOTED MATCHED-EDGE COLLAPSE.** There is no rigid one-code common-buffer survivor with
>
> `d_Y(b)=0` and `epsilon_b=p-g`.                          `(CLOSE)`

This closes the entire first positive-buffer equality layer, for every `t=p-g>=1`, before any minimal-reservoir, Hamming-excess, pair-capacity or source-tuple subdivision.

Consequently all downstream descendants of this parent layer — including the `m=g+1`, `E=1`, shared-core `E=2`, one-core `R2+R2`, and core-containing `R3` equality analyses — are no longer live realizability branches. Their preserved conditional lemmas and arithmetic identities remain valid as implications inside their stated hypotheses, but the present raw-criticality theorem proves that those hypotheses cannot simultaneously occur in a D2C graph.

In particular, the unmatched-heavy shared-core asymptotic resource cone from the immediately preceding checkpoint is a faithful relaxation of its conditional algebra, but it is **not a live graph tail** once the omitted rooted matched-edge criticality is imposed.

---

## 8. Unit VI — the live buffer frontier moves up by one physical defect

The established unloaded-buffer degree floor is

`epsilon_b>=p-g`.

The equality case has just been excluded. Hence every unloaded common-buffer survivor satisfies the strict integer bound

> **`d_Y(b)=0  =>  epsilon_b>=p-g+1`.**                   `(STRICT)`

Equivalently, the next unloaded layer contains at least one physical defect beyond the former equality geometry. The self-pricing lemma identifies the natural location of that first defect whenever an outside certificate is used: a buffer--X hole.

This gives a precise next equality/stability problem. In the first strict layer, if there is exactly one buffer--X hole `ba_0`, then every outside certificate must route the rooted criticality of at least one shared matched edge through that unique hole `a_0`. That creates a **unique-hole funnel** for all outside witnesses. The fixed-pair singleton principle then implies that, for a fixed outside witness `z`, at most one of its shared matched edges can use the forward orientation with witness `a_0`; any additional shared-coordinate matched edges must use the reverse orientation and therefore require `a_0 z in E`.

This funnel is not yet promoted to a closure of the first strict layer; it is the clean next object to classify.

The other live alternative is a loaded buffer `d_Y(b)>0`. It remains separate and is not touched by `(CLOSE)`.

---

## 9. Audit / preservation consequences

The new theorem strengthens, rather than weakens, the current audit position:

1. It uses the independently audited raw rooted B-edge criticality mechanism directly.
2. It does not use either source-tuple premise, so no new dependence on selected-representative uniqueness is introduced.
3. It does not use finite scans as proof.
4. It does not replace exact `Ccap_P` by total score slack; instead it closes the parent layer before pair capacity becomes relevant.
5. `X_3` is unaffected because its canonical root has `u=0` and does not enter the positive-buffer common-buffer setup.

The correct next priority is no longer the shared-core asymptotic tail. It is the first strict unloaded buffer layer `d_Y(b)=0`, `epsilon_b>=p-g+1`, beginning with the unique-hole funnel, followed by the loaded-buffer alternative if that strict layer survives. The four-exception gate, `z=2`, and further minimal-reservoir expansions remain subordinate unless the new buffer-stability analysis makes them load-bearing.
