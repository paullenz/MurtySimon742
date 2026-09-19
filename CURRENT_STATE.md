# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_COMMON_CORE_EXACT_SLACK_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `7404da5f72867c8e28847e7aa4bb23dddb31d07f`

LAST VERIFIED RESULT: `The unloaded common-buffer core slack can be counted exactly, not merely bounded by k(p+k-2): every common core witness w has exactly one X-neighbour, no Y-neighbours, no U_- neighbours, and epsilon_w=p+k-1+h_w where h_w is its number of missing U_o edges. Thus E_core=k(p+k-1)+H_core. In the zero-buffer g=p subbranch, if r_B is the number of reverse gamma-bar-d singleton X-heads and d=p-r_B, then at least k+d buffer-X edges require outside-U witnesses and H_core>=[k-p+d]_+. The cheapest geometry therefore saturates all p reverse matched slots (d=0), and if H_core=0 it forces k<=p plus a graph-fixed head partition. The sharpened arithmetic reduces the coarse z=1 support union from the immediately preceding 64,867 to 64,079 abstract states.`

UNPRESERVED WORK: `None. The exact core identity, reverse-deficit theorem, equality head partition and diagnostic checker are preserved in project/research/post_ms/2026-09-19-common-buffer-criticality-repair-v1/.`

DEFERRED ADMIN: `README remains lower-frequency; refresh it at the next daily adversarial audit/reviewer checkpoint if the repaired common-buffer branch survives. Do not spend this mathematics cadence on CI churn unless integrity fails.`

NEXT ACTION: `Attack the cheapest d=0 zero-buffer head-partition geometry directly. In that geometry all p reverse gamma-bar-d endpoints have distinct singleton X-heads; the p gamma-d crossing endpoints and k core witnesses give a disjoint graph-fixed partition X=H_M dotcup H_0; if H_core=0 then H_0 is contained in the reverse-head set and all k compulsory outside-certified buffer edges lie in H_M. Test coexistence of those heads with W_0--U_o completeness, tight-pair adjacency, exact pair Ccap/ONE/CROWD and rooted residual QE. If it survives, quantify the first H_core>0 stability layer. Do not move to z=2.`

## Mandatory audit reconciliation

Before forward mathematics this run, the live `CURRENT_STATE.md`, root `README.md`, recent commits, the 19 September daily red-team audit/handoff, the source-premise repair, and the independent actual-D2C Hall/pair-capacity regression were reread. The audit priority order remains binding: the two source-tuple premises are repaired at the raw/selected interface; the finite source-tuple capacity theorem is not promoted as unconditional graph closure; the graph-level regression includes `X_3` and still records zero graph/formula mismatches; no actual rigid complete Hall cut with `x>=3` has been found, so the live one-code results remain conditional hand implications; exact pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)` stay load-bearing. The four-exception gate remains subordinate and the mixed `{4,5}` ladder stays closed.

The previous handoff's matched-only buffer-X theorem was invalidated earlier in this session because its raw criticality orientation was inconsistent. That line remains withdrawn. The corrected matched-or-outside theorem is the only permitted common-buffer interface.

## Negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. Every theorem below requires a nonempty `U_-` with `k+1<=u`, so `X_3` is untouched.

## Corrected buffer-X interface retained

In the unloaded common-buffer branch, with `X--Y` complete, all Y-sources of code d, `g=g_P`, `k=x-g>0`, `U_-=W_0 dotcup {b}` and `e(G[U_-])=0`, the corrected orientations for `b x` are:

- A: `b z in E`, `x z notin E`, `N(x) cap N(z)={b}`;
- B: `x z in E`, `b z notin E`, `N(b) cap N(z)={x}`.

At most g heads use B. A is either matched with `gamma(z)=c(x)` or outside unmatched with `c(z)=bar c(x)` and z anticomplete to Y. The invalid old claim that all A-certificates are matched remains withdrawn.

For an above-threshold candidate with `lambda>=0`, aligned-code self-pricing gives `n_c<=R_A=floor(R_code(C0)/2)`, so matched A-certificates occupy at most `2(p-g)R_A` X-sources. Hence

`ell >= [k-2(p-g)R_A]_+`.

At zero buffer slack, `g=p`, so all forced A-certificates are outside-U.

## New exact common-core identity

Fix `w in W_0`. Since w is used by every source in Y and Y is complete to X, the singleton common-neighbour property forces exactly one X-neighbour. It is nonadjacent to all Y-sources, and `e(G[U_-])=0` gives no other U_- neighbour.

Let

`h_w=u_o-d_{U_o}(w)`.

Using `d_{A union U}(w)=p+u-1-epsilon_w`, one gets the exact identity

> `epsilon_w=p+k-1+h_w`.                                  `(CORE-1)`

The core head is graph-fixed. For a fixed Y-source the k core witnesses certify k distinct crossing heads, so the head map

`h:W_0 -> X`

is injective. Write `H_0=h(W_0)`, `|H_0|=k`.

Summing `(CORE-1)` gives

> `E_core=k(p+k-1)+H_core`,                               `(CORE-2)`

where

`H_core=e_bar(W_0,U_o)`.

Therefore

> `E_core>=k(p+k-1)`,                                     `(CORE-3)`

with equality iff `W_0--U_o` is complete.

This exact identity applies throughout the unloaded common-buffer branch, including `r>0`; it is not restricted to zero buffer slack. The predecessor floor `k(p+k-2)` was safe but one unit per core vertex too weak.

## Zero-buffer reverse deficit

Now set `g=p`, `k=x-p`, `epsilon_b=0`. Let `R_B` be the set of X-heads with a reverse Orientation-B certificate and put

`r_B=|R_B|<=p`,

> `d=p-r_B>=0`.                                           `(REV-D)`

Every X-head outside `R_B` must use an outside-U certificate, so

> `ell>=x-r_B=k+d`.                                       `(REV-ELL)`

If a core head `x=h(w)` is not in `R_B`, its outside witness z satisfies `N(x) cap N(z)={b}`. Because w is adjacent to x, w-z must be a nonedge. The injectivity of the core-head map makes these physical pairs distinct. Hence

> `H_core>=|H_0\R_B|>=[k-p+d]_+`.                        `(REV-H)`

Combining with `(CORE-2)`:

> `E_core>=k(p+k-1)+[k-p+d]_+`.                          `(REV-E)`

The aligned-code reuse cap gives

> `m>=ceil((k+d)/R_A)`                                    `(REV-M)`

for the number of distinct outside witnesses, and each is anticomplete to Y, so

> `L_Y>=y(1+m)`.                                          `(REV-LY)`

Thus the zero-buffer score floor is

> `S>=k(p+k-1)+[k-p+d]_+`
> `   +max{phi(p),y(1+ceil((k+d)/R_A))}`.                `(REV-S)`

The right side is nondecreasing in d. Therefore the cheapest scalar geometry has

> `d=0`, i.e. `r_B=p`.                                    `(REV-SAT)`

All p reverse gamma-`bar d` physical matched endpoints then have distinct singleton X-heads.

## Sharpened rooted residual

The repaired A--U hole count is

`Z>=k(a-1)+y+ym+ell`.

Using `(REV-ELL)` gives

> `Z>=ka+y(1+m)+d`.                                       `(REV-Z)`

Put

`m_d=ceil((k+d)/R_A)`,

`E0_d=k(p+k-1)+[k-p+d]_+`,

`D_d=ka+y(1+m_d)+d-u(p-lambda)`.

Then

> `q+E_U>=E0_d+ceil([D_d-E0_d]_+/2)`.                   `(REV-QE)`

Again d=0 is the cheapest scalar possibility; unused reverse matched capacity worsens both score and residual ledgers.

## Cheapest equality head partition

The p gamma-d matched endpoints used by every Y-source also have graph-fixed singleton X-neighbours, because Y is complete to X. Their p selected heads are distinct. Together with the k core heads they cover every vertex of X:

> `X=H_M dotcup H_0`,
>
> `|H_M|=p`, `|H_0|=k`.                                  `(HEAD-PART)`

If `d=0` and `H_core=0`, then `(REV-H)` forces every core head into the reverse-head set `R_B`. Consequently `k<=p`, and the k outside-certified buffer edges `X\R_B` lie entirely in `H_M`.

Thus exact cheapest zero-buffer geometry has a concrete head pattern:

1. p distinct matched-crossing heads `H_M`;
2. k distinct common-core heads `H_0`;
3. p distinct reverse gamma-`bar d` heads, containing all of `H_0` if core slack is minimal;
4. k outside-certified buffer edges, all in `H_M` in the minimal-core case;
5. `W_0--U_o` complete.

For `k>p`, minimal core slack is impossible and at least `k-p` core--outside holes are mandatory.

## Local pair theorem retained

At zero buffer slack the pair traffic identities remain

`P_P=yp`, `C_P=yk`, `t_P=xy`.

The exact directed A/U floor, exact `Ccap_P`, and `(CROWD)` remain simultaneous local constraints. The previous bounded diagnostic showed directed A/U capacity raises the local pair floor in 5,280 zero-buffer branches but does not add scalar exclusions after the repaired geometry; therefore the current head partition, not another scalar stack, is the next target.

## Diagnostic update

New checker:

`project/research/post_ms/2026-09-19-common-buffer-criticality-repair-v1/check_common_core_exact_slack.py`.

On the same coarse abstract box:

- predecessor common-buffer survivor states: `64,892`;
- immediately preceding orientation-repaired common-buffer states: `64,867`;
- after exact core slack plus zero-buffer reverse-head surcharge: `64,079`;
- additional exclusions versus the immediately preceding repaired diagnostic: `788`;
- exclusions versus the predecessor common-buffer score theorem: `813`;
- full-support remains contained in the sharpened common-buffer survivor set on this grid, so the coarse z=1 support union is also `64,079`.

Within zero-buffer g=p abstract branches, `17,174` passed the old floor; exact core slack plus repaired outside-witness geometry rejects `594`; adding `(k-p)_+` rejects `644`, leaving `16,530`.

These are parameter diagnostics, not graph counts.

## Preserved full-support comparator

The full-support `z=1,h=0` branch remains valid. Raw criticality still forces `nu=y`, and the rooted triangle baseline remains `Q=p(p-1)+pu+e(G[U])`. No common-core correction weakens it.

## Immediate frontier

Do not perform a larger blind scan. Attack `(HEAD-PART)` directly:

1. assume d=0 and, first, `H_core=0`;
2. exploit `W_0--U_o` completeness together with an outside witness z for a head in `H_M`;
3. track the tight fibre whose gamma-d endpoint has that H_M head and its gamma-`bar d` mate;
4. test the resulting common-neighbour sets against the outside singleton `N(x) cap N(z)={b}` and reverse singleton conditions;
5. keep exact pair traffic and `(REV-QE)` active;
6. if `H_core=0` is impossible, quantify the first positive `H_core` layer rather than moving to z=2.
<!-- CURRENT-STATUS:END -->
