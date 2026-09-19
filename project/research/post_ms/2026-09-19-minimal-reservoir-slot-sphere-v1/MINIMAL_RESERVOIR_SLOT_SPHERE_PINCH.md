# Minimal-reservoir slot/sphere pinch

Date: 2026-09-19

Status: internal structural theorem package for the eventual / sufficiently-large dense diameter-2-critical programme around

`M(n)=floor((n-1)^2/4)+1`.

Nothing here asserts the false all-order 2019 Dailly–Foucaud–Hansberg Conjecture 3. The published order-12 graph `X_3` with 32 edges remains the mandatory hostile control.

## 1. Audit reconciliation

Before forward mathematics this run reread `CURRENT_STATE.md`, `README.md`, the latest commits, the 19 September daily red-team audit, `SOURCE_PREMISE_REPAIR.md`, and `project/research/post_ms/2026-09-19-rigid-graph-regression-v1/RIGID_GRAPH_LEVEL_REGRESSION.md`.

The audit boundary is unchanged:

- physical beta-source distinctness is established from raw singleton criticality;
- `(source,coordinate)` uniqueness is a selected-representative statement, not raw-witness uniqueness;
- the finite source-tuple theorem is not promoted to unconditional graph-level closure;
- the independent actual-D2C regression still reports 3,540 root-policy instances, 147 exact pair-capacity checks, 36 Hall-cut decompositions and zero recorded graph/formula mismatches, with `X_3` passing;
- no bounded-corpus D2C graph realizes the full rigid complete-cut hypotheses, so the branch below remains a conditional hand implication;
- exact pair-local `Ccap_P` is retained; in the present minimal-reservoir equality geometry `(ONE-P)` and `(CROWD)` are already proved consequences of stronger physical bills once exact crossing capacity is kept;
- the four-exception gate remains subordinate.

The predecessor explicitly asked to intersect the local rooted-slot floor with `r=f+delta` and, if that did not close the branch, classify the Hamming-cheapest geometry. This note follows exactly that priority. It does not open `m=g+2`, `z=2`, loaded buffer, extra buffer slack, or the closed mixed `{4,5}` line.

## 2. Retained minimal-reservoir notation

Stay in the positive-buffer unloaded common-buffer rigid one-code branch with minimal outside reservoir `m=g+1`:

- `X--Y` complete, `x>=3`, `y>0`, `A=X dotcup Y`, `a=x+y`;
- every Y-vertex has code `d`; X contains neither `d` nor `bar d`;
- `g=g_P`, `k=x-g>0`, `t=p-g>=1`;
- `U_-=W_0 dotcup {b}`, `|W_0|=k`, `epsilon_b=t`;
- `X=H_M dotcup H_0`, with sizes `g,k`;
- `H_0` has one code `c_*`, is independent, and uses one common outside witness `z_*` of code `bar c_*`;
- the H_M codes are pairwise distinct singleton A-code classes;
- `A_*:=g-d_{H_M}(z_*)`, abbreviated below to `A`;
- `M_*:=(u_o-1)-d_{U_o\{z_*}}(z_*)`, abbreviated to `M`;
- `N=u-k-2`, so `0<=A<=g`, `0<=M<=N`;
- `epsilon_{z_*}=t+k+A+M`;
- `L_Y>=Y_0:=y(p+2)`.

To avoid confusion with the rooted triangle count, write the Hall-demand constant as

> `Q_H:=x(x-T_0)+k(x-1)+x-g(g-1)+kN`,

where `T_0=a-p`, and put

> `D(A,M):=Q_H-(2k-1)A-kM`.

The predecessor proved

> `L_X>=[D(A,M)]_+`,
>
> `H(A,M):=A+M+[D(A,M)]_+`,
>
> `H(A,M)<=B_P:=C0-O_0-sigma_P`,

where

`O_0=t+k+g[t-k+1]_+`

and `sigma_P` is the least pair-local score `S_P` meeting exact crossing `Ccap_P>=2xy` above the compulsory pair floor.

## 3. Unit I — the slot identity gives a universal rigid-cut imbalance cap

The preserved exact rooted identities are

> `r=f+delta`,
>
> `f=(p-lambda)(p+u)+q+E_U-delta`.

Hence, identically,

> **`r=(p-lambda)(p+u)+q+E_U`.**                         `(R-ID)`

The predecessor local-slot theorem gives `r>=a` on every rigid complete cut. Therefore

> **`q+E_U>=a-(p-lambda)(p+u)`.**                        `(R-A)`

This is the requested direct intersection of the local slot theorem with `r=f+delta`; no estimate for `delta` remains.

For an above-`M(n)` candidate, `S=E_U+L_A<=C0`, so `E_U<=C0`, while trivially `q<=binom(u,2)`. Therefore a rigid-cut survivor must satisfy

> `a <= (p-lambda)(p+u)+binom(u,2)+C0`.                  `(IMB0)`

Using `a=2p+u-lambda-1`, `C0=(lambda+3)p+(lambda+2)u-2H-4`, and `H=floor((lambda+1)^2/4)`, this becomes

> `2p^2+2pu+2p+u^2+u+2lambda-4H-6 >= 0`.               `(IMB1)`

Equivalently,

> `lambda^2 <= 2p^2+2pu+2p+u^2+u-6` if lambda is even,
>
> `lambda^2 <= 2p^2+2pu+2p+u^2+u-7` if lambda is odd.   `(IMB2)`

This applies to the whole rigid complete-cut branch, not merely `m=g+1`. It is a necessary condition, not a closure theorem.

## 4. Unit II — physical U-holes sharpen the slot-capacity gate in `m=g+1`

In the minimal-reservoir geometry the following U--U nonedges are physically distinct:

1. all `binom(k+1,2)` pairs inside the independent set `U_-=W_0 dotcup {b}`;
2. the k pairs `z_*--W_0`;
3. the M missing pairs from `z_*` to `U_o\{z_*}`.

Thus

> **`q <= binom(u,2)-binom(k+1,2)-k-M`.**                `(QMAX)`

Also `L_A=L_X+L_Y>=Y_0+[D(A,M)]_+`, so above threshold

> **`E_U <= C0-Y_0-[D(A,M)]_+`.**                        `(EUMAX)`

Combining `(R-ID)`, `r>=a`, `(QMAX)` and `(EUMAX)` gives the pair-allocation-sensitive necessary condition

> **`a <= (p-lambda)(p+u)`**
> ` **+ binom(u,2)-binom(k+1,2)-k-M**`
> ` **+ C0-Y_0-[D(A,M)]_+.**`                            `(SLOT-GATE)`

The actual graph must realize at least one integer pair `(A,M)` that satisfies both `(SLOT-GATE)` and the exact pair/Hall gate `H(A,M)<=B_P`. This is stronger than using `r>=a` only after all physical allocation information has been erased.

## 5. Unit III — pair-local budget forces X-density

The exact pair box gives

`S-S_P>=O_0+A+M+L_X`

and `S_P>=sigma_P`; hence

> **`L_X<=B_P-A-M`.**                                    `(LX-UP)`

On the other hand the exact rigid Hall identity is

`2e(X)=x(x-T_0)-L_X+Z_X`,

and the minimal-reservoir physical holes give

`Z_X>=k(x-1)+x+A+k(N-M)`.

Therefore

> **`2e(X)>=Q_H+g(g-1)-B_P+2A-(k-1)M`.**                `(EX-LOW)`

Star separation gives

> `e(X)<=E_max(A):=binom(g,2)+kA`.                        `(EX-UP)`

Put `s:=B_P-H(A,M)>=0`. Direct subtraction yields the compact stability form

> **`2(E_max(A)-e(X)) <= s+[-D(A,M)]_+`.**               `(DENSE)`

In particular, while the Hall demand is positive, `D(A,M)>0`, every unit of unused pair/Hall budget can remove at most half an edge from the star-separation maximum:

> `E_max(A)-e(X)<=floor(s/2)`.

At exact pair/Hall saturation (`s=0`, `D>0`) one must have `e(X)=E_max(A)`: H_M is a clique, and every H_M vertex missed by `z_*` is joined to every H_0 vertex. This converts pair-local score tightness into literal graph density.

## 6. Unit IV — Hamming dichotomy

Let

`h_*=d_H(c_*,d)`

and for the g matched heads let

`h_i=d_H(c(h_i),d)`.

All are positive integers, and

`H_X=k h_*+sum_i h_i>=x`.

There are two cases.

### Non-cheapest case

If any one of these distances exceeds one, then `H_X>=x+1`. Every Y-vertex has A-degree x, so the preserved local slot/Hamming theorem gives

`r_y>=ceil(H_X/x)>=2`.

Every X-vertex still pays at least one slot. Hence

> **`r>=a+y`.**                                          `(NONCHEAP)`

Thus a single extra Hamming unit costs an entire additional Y-layer of rooted slots.

### Hamming-cheapest case

Otherwise every distance is one. Then `c_*` and the g distinct H_M codes are `g+1` distinct one-coordinate flips of d. Consequently `g+1<=p` (consistent with `t=p-g>=1`). Since H_0 is independent, every edge of `G[X]` joins two distinct one-flip codes and therefore has Hamming length exactly two.

If `nu_X` is the number of nonisolated vertices of `G[X]`, then for `z in X` with internal degree `d_X(z)>0`,

`sum_{w in N_A(z)}d_H(c(w),c(z)) >= y+2d_X(z)`

and `d_A(z)=y+d_X(z)`, so `r_z>=2`. Isolated X-vertices and all Y-vertices pay at least one. Therefore

> **`r>=a+nu_X`.**                                       `(SPHERE-SLOT)`

This is the first use of the exact graph density forced by `(DENSE)` inside the local slot ledger.

## 7. Unit V — support lower bound from star separation

For any graph obeying the minimal-reservoir star separation, suppose exactly h nonisolated H_M vertices and c nonisolated H_0 vertices occur. Since H_0 is independent and H_0 can meet only the A exceptional H_M vertices missed by `z_*`,

> `e(X)<=binom(h,2)+c min(h,A)`.

Define

> `nu_min(e;g,A,k)`
> ` := min{h+c:0<=h<=g,0<=c<=k, e<=binom(h,2)+c min(h,A)}`. `(NU)`

Then `(EX-LOW)` gives an explicit `E_min(A,M)` and hence

> `nu_X>=nu_min(E_min;g,A,k)`.

In the Hamming-cheapest branch the slot bound is therefore completely finite and explicit:

> `r>=a+nu_min(E_min;g,A,k)`.                             `(SUPPORT-SLOT)`

No graph enumeration is involved; `nu_min` is just the extremal support size of a graph constrained by the star-separation pattern.

## 8. Unit VI — cheapest sphere forces `A=g`

The Hamming-cheapest geometry is substantially more rigid than the predecessor handoff recorded.

Write

`c_*=d xor e_j`,

and for `h in H_M`,

`c(h)=d xor e_i`, with `i!=j`.

Then

`c(z_*)=bar d xor e_j`.

### Theorem 8.1 — the common core witness is anticomplete to H_M

> **`z_*--H_M` is empty. Equivalently, `A=g`.**          `(A=G)`

### Proof

Suppose `z_*h` is an edge. Since b is complete to X and U_o, it lies in the triangle `b z_* h`; criticality therefore requires one of the two singleton orientations.

For an orientation with a witness w adjacent to h, nonadjacent to `z_*`, and `N(z_*) cap N(w)={h}`:

- a B-witness is impossible because two B-vertices share the root (and the root itself cannot have h as a common neighbour);
- a Y-witness shares with `z_*` the matched endpoint in coordinate j;
- an H_0 witness shares b with `z_*`;
- another H_M witness shares with `z_*` the matched endpoint in coordinate j.

So the required singleton cannot occur.

For the reverse orientation, with w adjacent to `z_*`, nonadjacent to h, and `N(h) cap N(w)={z_*}`:

- the root has b as another common neighbour with h;
- Y and H_0 are not adjacent to `z_*`; b is adjacent to h;
- an outside-U witness adjacent to `z_*` shares b with h;
- if a matched endpoint is adjacent to `z_*` but not h, its coordinate is one where their codes differ; there `z_*` selects the `bar d` endpoint, so b (code `bar d`) is also adjacent to that matched endpoint, again giving b as a second common neighbour;
- another H_M witness shares every Y-vertex with h.

No location supplies the required singleton. Contradiction. `square`

Thus the Hamming-cheapest branch does not get to optimize A: it sits at the endpoint `A=g`.

## 9. Unit VII — all selected outside witnesses form an A-anticomplete sphere layer

The preceding argument is not special to `z_*`. In the Hamming-cheapest geometry, every one of the `g+1` selected outside witnesses has code complementary to the one-flip code of the head it serves. Repeating the same wrong-head edge-criticality argument shows that each such witness is nonadjacent not only to its own head but to every vertex of X. The positive-buffer outside-witness theorem already makes it anticomplete to Y.

Therefore:

> **all `g+1` selected outside witnesses are anticomplete to A.** `(SPHERE-A0)`

Each such U-vertex consequently has `epsilon_w>=p`. For the distinguished `z_*`, `(A=G)` strengthens the exact identity to

`epsilon_{z_*}=t+k+g+M=p+k+M`.

The selected sphere layer therefore contributes at least

> `p(g+1)+k+M`

unmatched slack outside the pair `P={d,bar d}`. Since the pair-local score still satisfies `S_P>=sigma_P`, every Hamming-cheapest survivor must obey

> **`p(g+1)+k+M+[D(g,M)]_+ <= C0-sigma_P`.**             `(SPHERE-PAIR)`

This is a much stronger pair-local bill than the generic outside-reservoir slack when g is large. In the slice `t=1`, `g=p-1`, the selected outside witnesses are exactly the p one-coordinate flips of `bar d`, so their slack contribution alone is at least `p^2`.

## 10. Combined structural gate

The minimal-reservoir branch is now split into two explicitly testable geometries.

### Branch N — non-cheapest Hamming geometry

There must exist a pair/Hall-admissible `(A,M)` satisfying `(SLOT-GATE)` with the stronger lower target `r>=a+y`.

### Branch S — Hamming-cheapest sphere geometry

Here necessarily `A=g`; `(SPHERE-PAIR)` holds; the pair-budget density theorem gives a lower bound on `e(X)` and hence `nu_X`; and the exact slot identity plus `(QMAX)/(EUMAX)` must have enough room for

`r>=a+nu_X`.

If neither branch is feasible, the abstract minimal-reservoir parameter state is impossible. This gate keeps exact pair-local `sigma_P/Ccap_P` and physical q/E_U resources separate rather than returning to one total-score scalar.

## 11. Diagnostic replay

The companion checker replays these necessary conditions on the exact same bounded abstract box used by the predecessor (`3<=p<=18`, `u<=18`). It first reconstructs the predecessor population of **110,387** `m=g+1` states surviving the additive Hall and exact pair gate.

Results:

- the first `r>=a` physical slot-capacity gate alone rejects **45,401** states;
- the full Hamming-dichotomy / sphere / X-support gate rejects **45,830** states;
- **64,557** abstract parameter states remain;
- in the `t=1` slice, all **5,404** states still have a surviving non-cheapest relaxation, although the sphere branch itself is eliminated for 1,024 of them.

These are abstract parameter states, not graph counts. The lack of total `t=1` rejection is a useful obstruction: the next work should attack the non-cheapest branch structurally rather than add another coarse scalar inequality.

## 12. Negative control and next move

`X_3` has no active rigid complete A-cut of this type and has `u=0`, so none of these minimal-reservoir hypotheses applies. The hostile control remains untouched.

The next coherent move is still **not** `m=g+2`. Stay at `m=g+1` and attack the non-cheapest branch exposed by `(NONCHEAP)`: use the exact distribution of the extra Hamming units, rather than only the coarse payment `+y`, together with `(DENSE)` and pair-local `Ccap_P`. In parallel, for the surviving sphere branch exploit the stronger fact `(SPHERE-A0)` that `g+1` physical outside witnesses are anticomplete to the entire A-layer. Any new argument must continue to preserve the exact rooted identities and graph-level audit boundary.