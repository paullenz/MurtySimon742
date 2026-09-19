# Minimal-reservoir pair/residual pinch: interval geometry and exact clamped optimizer

Date: 2026-09-19

Status: continuation of `MINIMAL_RESERVOIR_PAIR_HALL_ALLOCATION.md`, under the same rigid one-code / minimal-reservoir hypotheses and the same 19 September audit boundary.

The purpose is to remove the remaining one-dimensional minimization from `(QE-PAIR)` and expose exactly where the score/Hall and rooted-residual optimizers disagree.

## 1. Inputs

Retain

`c=2k-1`,

`H(A,M)=A+M+[Q-cA-kM]_+`,

`0<=A<=g`, `0<=M<=N`,

and the exact pair budget

`B_P=C0-O_0-sigma_P`.

For fixed M define

> `D(M):=Q-kM`,

and

> `h_A(D)=min_{0<=A<=g}{A+[D-cA]_+}`.

The preceding note proved

> `h_A(D)=0`, if `D<=0`;
>
> `h_A(D)=ceil(D/c)`, if `0<D<=cg`;
>
> `h_A(D)=g+D-cg`, if `D>cg`.                            `(HA)`

Hence the exact pair/Hall cost at fixed M is

> `F(M):=M+h_A(Q-kM)`,                                   `(F)`

and

> `M_adm={M in {0,...,N}:F(M)<=B_P}`.                    `(ADM)`

The rooted residual term is

> `G(M):=E_*+M+ceil([R_0-(k+1)M]_+/2)`.                  `(G)`

---

## 2. Unit VIII — the pair/Hall admissible set is an interval

### Theorem 2.1 — V-shape of `F(M)`

The integer sequence `F(0),...,F(N)` is nonincreasing until the transition where `D(M)` enters the range `D<=cg`, and is nondecreasing thereafter. Consequently every sublevel set of F is an integer interval.

In particular, if `M_adm` is nonempty, there are unique endpoints

> `M_-:=min M_adm`, `M_+:=max M_adm`,

such that

> **`M_adm={M_-,M_-+1,...,M_+}`.**                       `(INT)`

### Proof

If `D(M)>cg`, `(HA)` gives

`F(M)=M+g+Q-kM-cg`

`    =g+Q-cg-(k-1)M`.

Thus F is decreasing there for `k>1` and constant for `k=1`.

If `0<D(M)<=cg`,

`F(M)=M+ceil((Q-kM)/c)`.

Increasing M by one lowers the ceiling argument by k. Since `c=2k-1>=k`, the ceiling can fall by at most one, while the explicit M-term rises by one. Hence F cannot decrease in this middle region.

If `D(M)<=0`, `F(M)=M`, so it is strictly increasing.

At the transitions the same formulas agree in the required weak direction. Therefore F has one valley (possibly a flat valley when `k=1`), and every sublevel set is contiguous. `square`

### Interpretation

The Hall ledger has a preferred M-scale near

`Q-kM ~= cg`.

Before this point all g efficient A-defects are saturated and extra M-defects genuinely relieve a remaining Hall deficit. After this point A-defects are no longer saturated; replacing Hall relief by further M-defects becomes score-inefficient. Thus the pair-local capacity ceiling does not leave an arbitrary scattered set of M-values: it leaves one exact physical interval.

---

## 3. Unit IX — the rooted residual has an exact free optimizer

Put

> `R:=[R_0]_+`,
>
> `M_Q:=ceil(R/(k+1))`.                                  `(MQ)`

### Theorem 3.1 — V-shape of the rooted residual term

Ignoring the pair/Hall restriction for a moment, the integer function

`M -> M+ceil([R_0-(k+1)M]_+/2)`

is nonincreasing for `M<M_Q` and strictly increasing for `M>=M_Q`. In particular `M_Q` is always a global minimizer on the nonnegative integers.

### Proof

While the positive residual remains, increasing M by one costs one explicit unit but decreases the residual numerator by `k+1>=2`; the half-ceiling therefore drops by at least one whenever needed, so the total cannot increase. Once `M>=M_Q`, the positive part is zero and the function is exactly M. `square`

Thus the rooted ledger by itself wants precisely enough M-defects to erase the residual gap at rate `k+1` per defect.

---

## 4. Unit X — exact clamped pair/residual optimizer

Assume `M_adm` is nonempty and write it as the interval `[M_-,M_+] cap Z` from Theorem 2.1. Define

> `M_hat:=min(max(M_Q,M_-),M_+)`.                         `(CLAMP)`

That is, clamp the free rooted optimizer to the pair/Hall-admissible interval.

### Theorem 4.1 — minimization-free `(QE-PAIR)`

The exact intersected rooted lower bound is

> **`q+E_U >= E_*+M_hat`**
> ` **+ceil([R_0-(k+1)M_hat]_+/2).**`                    `(QE-CLAMP)`

No scan over M is required.

### Proof

By Theorem 3.1, G is nonincreasing up to `M_Q` and increasing after it. The minimum of a V-shaped sequence over an interval is attained at the projection of its free minimizer onto that interval, namely `M_hat`. `square`

This is stronger conceptually than writing `min_{M in M_adm}`: it identifies the graph defect count the combined ledgers are trying to force.

---

## 5. The structural pinch

There are now three regimes.

1. **Compatible regime:** `M_Q in [M_-,M_+]`. The rooted optimum is pair/Hall-feasible. The next source of payment must come from the exact A-allocation at `M_Q` and the rooted unused-slot/Hamming ledger.

2. **Hall-left regime:** `M_Q<M_-`. The pair/Hall system forces **more** M-defects than the rooted ledger wants. The residual gap is already extinguished or nearly extinguished, so every additional forced M is essentially pure unmatched-slack cost.

3. **Hall-right regime:** `M_Q>M_+`. The pair/Hall system permits **too few** M-defects to reach the rooted optimum. A positive residual gap survives at the right endpoint and must be paid by q/E_U.

This is the clean opposition foreshadowed in the preceding note. Hall/score values A-defects because they remove `2k-1` units of X-demand per score unit; rooted residual values M-defects because they remove `k+1` residual units per score unit. The admissible interval is where those two economies can coexist.

---

## 6. Exact A-allocation once M is fixed

At `M_hat`, the least A-cost is

> `A_cost=h_A(Q-kM_hat)`.

If `0<Q-kM_hat<=cg`, one may choose

> `A_hat=ceil((Q-kM_hat)/c)`

and the Hall positive part is zero (up to the usual one-unit ceiling overshoot).

If `Q-kM_hat>cg`, all `g` possible A-defects are forced before the remaining Hall deficit can be paid:

> `A_hat=g`,

with leftover X-slack

> `Q-kM_hat-cg>0`.

Thus every extremal survivor now falls into a concrete adjacency statement about `z_*`: either a prescribed number of its `H_M` adjacencies must be missing, or it must be anticomplete to all of `H_M` and still pay positive X-slack.

This is the correct input to the next rooted-slot/Hamming attack.

---

## 7. Audit / diagnostic status

The interval and clamp statements are elementary integer consequences of the already-preserved physical ledgers. A companion finite replay in the pair/Hall checker verifies the closed defect formula; the interval and clamped-optimizer identities have also been independently brute-forced during this run over small integer boxes before preservation.

No graph-realizability inference is made. `X_3` remains outside the branch because `u=0`.

---

## 8. Next move

Do **not** open `m=g+2` yet.

For the extremal `M_hat,A_hat` allocation, return to the rooted unused-slot/direct-Hamming ledger. The target is to show that the forced missing `z_*--H_M` adjacencies or the forced surviving X-slack consume direct/Hamming resource that was not priced in `H(A,M)`. The three pinch regimes above should be treated separately only if the same slot/Hamming lemma does not cover all of them.