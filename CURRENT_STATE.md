# CURRENT_STATE.md

**Canonical repository:** `paullenz/MurtySimon742`  
**Date:** 2026-09-19  
**Active target:** eventual / sufficiently-large second-extremal structure for dense diameter-2-critical graphs around

`M(n)=floor((n-1)^2/4)+1`.

The false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3 is **not** the target. The published 2024 graph `X_3` on 12 vertices and 32 edges has `M(12)=31` and remains a mandatory negative control.

The mixed `{4,5}` selected-excess ladder is closed and is not to be restarted. First-proof priority on Erdős #742 is not an optimization target.

---

## 1. Audit gate remains binding

The most recent daily red-team audit is

`project/research/post_ms/2026-09-19-daily-red-team-audit-v1/DAILY_RED_TEAM_AUDIT.md`.

Its requirements remain mandatory.

### Upstream source-tuple premises

`SOURCE_PREMISE_REPAIR.md` independently repaired/reproved the two named premises at the exact level actually used:

1. **distinct physical source identity:** for a fixed A-witness, one physical unmatched source cannot beta-certify two distinct target fibres because its fixed singleton common neighbourhood cannot have two distinct heads;
2. **global selected `(source,coordinate)` uniqueness:** this is a selected-representative statement, not raw-witness uniqueness. One selected representative is chosen for each physical obligation, and the selected pair is used once.

The finite source-tuple capacity theorem remains **conditional on those named premises and the selected-obligation model**. It is not promoted as unconditional graph-level closure.

### Independent graph-level regression

The independent actual-D2C regression in

`project/research/post_ms/2026-09-19-rigid-graph-regression-v1/`

reconstructs, without importing the source-premise checker:

- maximum-degree rooted partition;
- tight antipode pairs and unmatched set;
- A/U Boolean codes;
- rooted B-edge criticality slots;
- direct/non-direct A-edge split;
- matched-foot gamma codes;
- A/U complementary witness localization;
- Hall cut identities;
- pair-local quantities and exact `Ccap_P`;
- rigid singleton-head assertions when their hypotheses occur.

Recorded run: 3,540 root-policy instances, 147 pair-capacity checks, 36 exact Hall-cut decompositions, zero graph/formula mismatches. `X_3` passes.

**Coverage limitation:** no actual D2C fixture with the full rigid complete Hall cut `x>=3`, `M_X=E_X=0` has been found. Every theorem below in that branch remains a hand implication conditional on those rigid hypotheses.

---

## 2. Prior branch status retained

The zero-buffer common-buffer branch `g=p` is closed by

`project/research/post_ms/2026-09-19-zero-buffer-complete-separation-v1/ZERO_BUFFER_COMPLETE_SEPARATION_AND_CLOSURE.md`.

That closure is **not reopened** by the present audit repair. The later zero-buffer proof had already collapsed the reverse channel and then proceeded through raw `X--U_o` / `X--X` criticality and exact degree bookkeeping.

The active branch is now the first **positive-buffer** unloaded common-buffer equality geometry:

- rigid one-code complete cut `X--Y`;
- `x=|X|>=3`, `y=|Y|>0`;
- all `Y` have code `d`, while `X` contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`;
- `U_-=U_{bar d}=W_0 dotcup {b}`, `|W_0|=k`;
- `e(Y)=e(Y,U_d)=e(G[U_-])=0`;
- buffer-load variable `r_b=d_Y(b)=0`;
- positive buffer slack `t:=p-g>=1`;
- first equality layer `epsilon_b=t`, hence `b--X` and `b--U_o` are complete.

Do **not** move to `z=2` while this branch remains live.

---

## 3. New audit repair: the old positive-buffer reverse channel is invalid

A reread of

`COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md`

found a concrete upstream error in its positive-buffer reverse Orientation B.

That orientation required a matched endpoint `z` with

`xz in E`, `bz notin E`, `N(b) cap N(z)={x}`.

But `b` and every matched endpoint lie in `B=N(v)`, so they share the root `v`. Therefore their common neighbourhood cannot be the singleton `{x}`.

### Superseded material

The following must no longer be used:

- the matched Orientation-B reverse channel in `COMMON_BUFFER_X_EDGE_CRITICALITY_REPAIR.md`;
- reverse-head capacity statements derived from it;
- `COMMON_CORE_EXACT_SLACK_AND_REVERSE_DEFICIT.md` Sections 4 onward wherever the scalar reverse-deficit variable treats matched reverse certificates as available.

### Retained material

The following survive:

- unloaded common-buffer source-edge dichotomy;
- graph-fixed common-core head map;
- exact core identity
  `E_core=k(p+k-1)+H_core`;
- later zero-buffer reverse-collapse theorem and final zero-buffer closure;
- one-code pair purification, exact `Ccap_P`, `(ONE-P)`, `(CROWD)`;
- rooted residual / witness-slot identities.

This repair is preserved in

`project/research/post_ms/2026-09-19-positive-buffer-reverse-collapse-v1/POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md`.

---

## 4. Current structural checkpoint: all buffer--X certificates are outside-U

Let `H_M` be the `g` graph-fixed heads of the matched gamma-`d` crossing feet and `H_0` the `k` graph-fixed core heads. Then

`X=H_M dotcup H_0`.

### 4.1 Matched-crossing heads are singleton A-code classes

Every matched crossing foot `q` has `N_X(q)` equal to its single head. If another X-vertex had the same tight code as that head, it would have the same adjacency to `q` and create a second common neighbour with every Y-source.

Therefore:

- every `H_M` head has a code occurring exactly once in `X`;
- the `g` `H_M` codes are pairwise distinct;
- since Y has only code `d`, these are singleton A-code classes.

### 4.2 Core heads cannot use matched buffer certificates

If a core head `x=h(w_0)` used a matched Orientation-A buffer witness `z`, then `b~z`. Since `b,w_0` have the same code `bar d`, `w_0~z` also. But `w_0~x`, giving a second common neighbour of `x,z` besides `b`.

Hence every core head uses `U_o`.

Each such certificate forces a physical core--outside nonedge, so

`H_core>=k`

and therefore

> `E_core>=k(p+k)`.

### 4.3 Matched-crossing heads cannot use matched buffer certificates either

Let `x in H_M` have matched crossing foot `q`, so `gamma(q)=d` and `q~x`.

If a matched buffer witness `z` satisfied `b~z`, then in the fibre of `z`, the endpoint selected by `bar d` is `z`. Since `gamma(q)=d`, `q` is adjacent to that `bar d` endpoint. Thus `q~z`. Together with `q~x`, this makes `q` a second common neighbour of `x,z`, contradicting the buffer certificate `N(x) cap N(z)={b}`.

Hence:

> **every one of the `x` buffer--X edges is outside-U certified.**

There is no matched buffer channel in the first positive-buffer equality geometry.

---

## 5. Outside reservoir consequences

Let `m` be the number of distinct physical outside witnesses in `U_o`.

The `g` singleton-code heads in `H_M` require `g` pairwise distinct outside witnesses, and none can serve a core head. Since `k>0`, the core block requires at least one further witness.

Therefore

> `m>=g+1`.

Since `|U_o|=u-k-1`,

> `u-k-1>=g+1`,
>
> **`u>=x+2`.**

This is now the first gate to apply to the equality geometry. It is a physical-population theorem, not a finite scan.

It also gives

> `y=a-x>=2p-lambda+1`.

Every outside witness is anticomplete to Y, and the exact source-slack identity is

`L_Y=y(p-g+1)+H_Y`.

Thus

> **`L_Y>=y(p+2)`.**

The apparent cheapness of small positive buffer slack disappears on the Y side.

---

## 6. Score and residual ledgers

Define

`phi(g)=g(g-1)` for `g>=3`, and `0` for `g<=2`.

For an outside witness serving `tau` heads,

`epsilon_z >= [p-x+tau]_+=[t-k+tau]_+`.

A safe parameter-only outside-slack floor is

`E_out^0=t+g(t-k+1)` if `k<=t`, and `0` if `k>t`.

Hence the current score floor is

> `S>=k(p+k)+t+E_out^0+max{phi(g), y(p+2)}`.      `(S+)`

The physical A--U hole count satisfies

> `Z>=ka+y(g+2)+g`.                               `(Z+)`

Using

`Z=u(p-lambda)+2q+E_U`,

put

`D_+=ka+y(g+2)+g-u(p-lambda)`

and

`E_0=k(p+k)+t+E_out^0`.

Then

> `q+E_U>=E_0+ceil([D_+-E_0]_+/2)`,

and for an above-`M(n)` candidate with `E_U<=C0`,

> `q>=ceil([D_+-C0]_+/2)`.

Therefore

> `Q=e(G[N(v)])=p(p+u-1)+q`

is explicitly forced upward in the residual-heavy survivors.

The exact residual identity remains

`f=(p-lambda)(p+u)+q+E_U-delta`,

so

> `f >= (p-lambda)(p+u)+E_0+ceil([D_+-E_0]_+/2)-delta`.

This is the current bridge back to the residual defect `delta=r_root-f` / unused rooted-slot programme.

---

## 7. Exact pair-local obligations remain mandatory

For `P={d,bar d}`:

> `Ccap_P=R_code(S_P)[g+2S_P/(lambda+1)]`,

because one-code purity gives `h_P=0`.

Retain simultaneously:

> `2xy<=Ccap_P`,
>
> `Ccap_P+L_Y>=y(p+x+k)`  `(ONE-P)`,
>
> `(CROWD)`.

The outside witnesses forced above have codes outside P, so their slack is outside `S_P`; in an above-threshold graph

`S_P<=C0-E_out^0`.

The P-local baseline already contains

`k(p+k)+t+L_Y`.

A bounded relaxed intersection with these exact pair constraints was run after the new structural gates. It added **zero** exclusions beyond the physical population/score floor on the diagnostic box. This is a negative diagnostic result only: it says another coarse scalarization of `S_P` is unlikely to be the next useful move.

---

## 8. Diagnostic audit

Companion checker:

`project/research/post_ms/2026-09-19-positive-buffer-reverse-collapse-v1/check_positive_buffer_reverse_collapse.py`

Grid:

- `3<=p<=18`;
- `1<=u<=18`;
- all admissible nonnegative `lambda`;
- all `3<=x<a`;
- positive `t=p-g>=1`;
- only the `r_b=0`, `epsilon_b=t` comparator.

These are **abstract parameter states, not graph counts**.

Before the new repair, `320,525` states passed the predecessor equality floor.

New exclusions:

- `146,603` fail the physical population theorem `u>=x+2`;
- of the remainder, `40,087` fail `(S+)`.

Remaining abstract states:

> `133,835`.

For `t=1`:

- predecessor: `20,178`;
- population rejection: `12,307`;
- additional score rejection: `2,056`;
- remaining: `5,815`.

Among all `133,835` remaining states, `(Z+)` plus the above-threshold score ceiling forces `q>0` in `7,274` states; maximum forced `q` in this bounded diagnostic is `48`.

The relaxed `Ccap_P/(ONE-P)/(CROWD)` upper-envelope test adds zero further exclusions.

---

## 9. Mandatory negative control

`X_3` remains allowed and structurally separated:

- `n=12`;
- `m=32>M(12)=31`;
- canonical root `a=3`, `b=8`, `p=4`, `u=0`;
- `Q=12`, `r_root=f=delta=0`.

The current branch requires `k>0`, a common buffer, and now the stronger consequence `u>=x+2`; `X_3` never enters it.

Any future theorem that excludes `X_3` without an explicit size/branch hypothesis is a red flag.

---

## 10. Next action

Stay on the positive-buffer common-buffer branch. Do not move to `z=2`.

The highest-value next target is the **minimal outside-reservoir equality layer**

> `m=g+1`.

At `m=g+1`:

- each of the `g` matched-crossing singleton-code heads has its own outside witness;
- all `k` core heads must reuse the one additional outside witness (unless the core itself splits into more witness-code classes);
- that common core witness therefore forces a common X-code class for every core head it serves, plus k physical `W_0--U_o` holes.

Next run should:

1. classify `m=g+1` directly from raw D2C criticality, starting with the single core outside witness and its `k` singleton buffer certificates;
2. test whether the core heads can in fact all share one tight code and one outside witness without creating a second common neighbour or a forbidden triangle-edge certificate;
3. feed any forced extra outside witness into both `L_Y` and `u_o` immediately;
4. combine the resulting physical geometry with `(Z+)`, rooted unused-slot/Hamming identities, exact `Ccap_P`, `(ONE-P)` and `(CROWD)`;
5. only if `m=g+1` survives should the next equality layer `m=g+2` be considered;
6. keep loaded `r_b>0` and extra buffer slack `epsilon_b>t` subordinate until this first equality reservoir is exhausted.

The four-exception gate remains subordinate unless this classification makes it load-bearing.

---

## 11. Preservation / trust

New package:

`project/research/post_ms/2026-09-19-positive-buffer-reverse-collapse-v1/`

Primary note:

`POSITIVE_BUFFER_REVERSE_COLLAPSE_AND_HEAD_DICHOTOMY.md`

Checker:

`check_positive_buffer_reverse_collapse.py`

Summary:

`POSITIVE_BUFFER_REVERSE_COLLAPSE_AUDIT_SUMMARY.json`

The mathematical promotion level is:

- **hand-proved conditional structural theorem** inside the rigid one-code branch;
- **not** graph-realizability evidence;
- **not** an all-order theorem;
- **not** an eventual theorem yet.

Base repository head inspected before this run:

`3b654a674c3d476588eaa9b461e9cc1a718eb373`.
