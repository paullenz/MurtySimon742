# Dense diameter-2-critical research - live current state

> **Active target - 19 September 2026.** Sufficiently-large/eventual second-extremal diameter-2-critical classification around `M(n)=floor((n-1)^2/4)+1`. The false all-order 2019 strengthening is not assumed. The published 2024 `X_3` graph (`n=12,m=32`) remains a mandatory hostile control. Erdős #742 is preserved but is not the live optimization target.

<!-- CURRENT-STATUS:START -->
CHECKPOINT CLASS: `ONE_CODE_Z1_ZERO_BUFFER_REVERSE_COLLAPSE_AND_LAMBDA0_EXCLUSION_2026_09_19`

WORK MODE: `MATH`

INSPECTED PREDECESSOR: `19244c3f44f082c51efb7463f1dc6aeca8a0026d`

LAST VERIFIED RESULT: `In the repaired rigid one-code z=1 common-buffer branch at zero buffer slack g=p, the reverse Orientation-B channel is empty. Every gamma-d crossing endpoint q has one X-neighbour, so its tight gamma-bar-d mate has x-1 X-neighbours; because b is complete to X and x>=3, no mate can satisfy a reverse singleton N(b) cap N(q')={x0}. Thus R_B=empty and d=p. The matched Orientation-A channel is also empty, so all x=p+k buffer-X edges require outside-U witnesses: ell=x. Hence H_core>=k and E_core>=k(p+k); with m distinct outside witnesses, m>=ceil(x/R_A), L_Y>=y(1+m), E_W>=[x-km]_+, S_P>=k(p+k)+y(1+m), and Z>=ka+p+y(1+m). Comparing only the weakest m>=1 pair floor with the preserved above-M score ceiling gives the parameter-only necessary inequality (lambda+1-k)p+lambda u-k^2+2k+2lambda-2 floor((lambda+1)^2/4)-2>=0. For lambda=0 its left side is strictly negative for every k>=1, so the entire balanced zero-buffer rigid one-code common-buffer branch is excluded.`

UNPRESERVED WORK: `None. Main proof is in project/research/post_ms/2026-09-19-zero-buffer-reverse-collapse-v1/ZERO_BUFFER_REVERSE_COLLAPSE.md. The parameter-only score obstruction and lambda=0 closure are in ZERO_BUFFER_SCORECARD_COLLAPSE.md in the same directory.`

DEFERRED ADMIN: `README remains lower-frequency; refresh it at the next daily adversarial audit/reviewer checkpoint if this repaired common-buffer line survives. Do not churn CI merely for bookkeeping.`

NEXT ACTION: `Stay in the reverse-collapsed zero-buffer branch, now restricted to lambda>=1. Attack the lambda=1/small-k strip first with the full m>=ceil(x/R_A), exact Ccap_P, ONE-P, CROWD and rooted q+E_U ledger. For k>=lambda+2 the new necessary inequality already forces a quantitatively unmatched-heavy regime; intersect that with source-tuple/beta capacity before any finite scan. Do not move to z=2 until this branch is exhausted.`

## Mandatory audit reconciliation

Before forward mathematics this run, `CURRENT_STATE.md`, root `README.md`, the latest commits, the 19 September daily adversarial audit/handoff, the source-premise repair, and the independent actual-D2C rigid Hall/pair-capacity regression were reread. No departure from the audit priority order was made.

- Distinct physical beta sources are directly proved from raw rooted criticality.
- Selected `(source,coordinate)` uniqueness is justified at the chosen-representative level for a unique physical P--U obligation.
- The principal `B_beta` lower bounds count those same selected physical obligations.
- The finite source-tuple theorem is not promoted as unconditional graph-level closure.
- The independent actual-graph regression reaches rooted residual identities, tight codes, selected slots, Hall cuts and exact pair-local `Ccap_P`; its recorded run has zero graph/formula mismatches and permanently includes `X_3`.
- No actual rigid complete Hall cut with `x>=3` has yet been found, so the live one-code results remain conditional hand implications of the rigid hypotheses.
- Exact `Ccap_P`, `(ONE-P)` and `(CROWD)` remain load-bearing. The four-exception gate remains subordinate. The mixed `{4,5}` selected-excess ladder stays closed.

The earlier matched-only buffer-X theorem remains withdrawn. Only the corrected matched-or-outside criticality interface may be used.

## Mandatory negative control

`X_3`: `n=12`, `m=32>M(12)=31`, canonical root `a=3,b=8,p=4,u=0,Q=12,r=f=delta=0`. The live common-buffer branch requires `U_-=W_0 dotcup {b}` with `k>0`; neither the reverse collapse nor the lambda=0 exclusion applies to `X_3`.

## Live zero-buffer setup

The branch has a complete rigid cut `X--Y`, `x=|X|>=3`, `y=|Y|>0`; all Y-sources have code `d`; X has neither code `d` nor `bar d`; `g=p`, `k=x-p>0`; `U_-=W_0 dotcup {b}`, `|W_0|=k`, `e(G[U_-])=0`; and `epsilon_b=0`, so `b--X` and `b--U_o` are complete.

The exact common-core identity remains

> `E_core=k(p+k-1)+H_core`,

where `H_core=e_bar(W_0,U_o)`.

The corrected criticality alternatives for an edge `b x` are:

- A: `b z in E`, `x z notin E`, `N(x) cap N(z)={b}`;
- B: `x z in E`, `b z notin E`, `N(b) cap N(z)={x}`.

A is either matched with `gamma(z)=c(x)` or outside unmatched with `c(z)=bar c(x)` and z anticomplete to Y. B, if possible, uses a matched endpoint of gamma-code `bar d`.

## Reverse-channel collapse

For every tight fibre `{q,q'}` with `gamma(q)=d`, `gamma(q')=bar d`, the matched crossing layer and `X--Y` completeness force

> `N_X(q)={h_M(q)}`.

Tight transversality gives

> `N_X(q')=X\{h_M(q)}`,
>
> `d_X(q')=x-1`.

Since b is complete to X,

> `|N(b) cap N(q')|>=x-1>=2`.

Thus no q' can be a reverse singleton witness. Therefore

> `R_B=emptyset`, `r_B=0`, `d=p`.                         `(REV-COLLAPSE)`

The prior scalar observation that score was minimized at `d=0` was arithmetically correct, but that minimizer is not graph-realizable.

## Full outside certification and physical consequences

With g=p, matched gamma support contains only `d,bar d`, while X avoids both codes. Hence matched Orientation A is impossible too. Every x in X has an outside witness z in U_o with

> `bz in E`, `xz notin E`, `N(x) cap N(z)={b}`,
>
> `c(z)=bar c(x)`, and z anticomplete to Y.

No physical-witness injectivity is assumed. The exact selected incidence count is

> `ell=x=p+k`.                                             `(OUT-ALL)`

For each core head `x=h(w)`, the outside certificate forces `wz` to be a nonedge. Distinct W_0 endpoints give k distinct physical missing pairs even if z is reused. Therefore

> `H_core>=k`,
>
> `E_core>=k(p+k)`.                                       `(CORE-NEW)`

Let W be the distinct outside witnesses, m=|W|. One physical z serves only one X-code class. The preserved aligned-code cap gives

> `m>=ceil(x/R_A)`.                                       `(WIT-M)`

Every z is anticomplete to Y, so

> `L_Y>=y(1+m)`.                                          `(WIT-LY)`

If t_z X-sources use z, then `epsilon_z>=[t_z-k]_+`; hence

> `E_W>=[x-km]_+`.                                        `(WIT-E)`

Thus

> `S>=k(p+k)+[x-km]_+ + max{phi(p),y(1+m)}`,             `(S-REV0)`

and on the distinguished pair

> `S_P>=k(p+k)+y(1+m)`.                                   `(SP-REV0)`

The exact pair-local bill remains

> `2xy<=Ccap_P`,
>
> `Ccap_P=R_code(S_P)*(p+2S_P/(lambda+1))`,

simultaneously with `(ONE-P)` and `(CROWD)`.

The physical A--U hole count strengthens to

> `Z>=ka+p+y(1+m)`.                                       `(Z-REV0)`

With

`E0(m)=k(p+k)+[x-km]_+`,

`D(m)=ka+p+y(1+m)-u(p-lambda)`,

the exact rooted minimization is

> `q+E_U>=E0(m)+ceil([D(m)-E0(m)]_+/2)`.                 `(QE-REV0)`

## Parameter-only score gate and balanced closure

For an above-`M(n)` candidate, the preserved score ceiling is

`S<=C0`,

where

`C0=2(D_M-1)+lambda(p+u)-p`,

and

> `D_M=2p+u-floor((lambda+1)^2/4)-1`.

Write `H_lambda=floor((lambda+1)^2/4)`. Since m>=1,

`S>=S_P>=k(p+k)+2y`.

Using `y=p+u-lambda-1-k`, every survivor must satisfy

> `(lambda+1-k)p + lambda u`
> ` -k^2+2k+2lambda-2H_lambda-2 >= 0`.                    `(PARAM-ZB)`

At `lambda=0` this is

`(1-k)p-k^2+2k-2>=0`,

whose left side is negative for every integer `k>=1`. Therefore

> **No above-M rigid one-code zero-buffer common-buffer candidate exists at lambda=0.** `(ZB0)`

For `lambda=1`, the coarse gate is

> `(2-k)p+u-k^2+2k-2>=0`.                                 `(LAM1)`

For general `lambda>0` and `k>=lambda+2`, it forces the unmatched-heavy condition

> `u >= ((k-lambda-1)p+k^2-2k-2lambda+2H_lambda+2)/lambda`. `(UH)`

This gate is deliberately only a first filter; the sharper m, pair-capacity, beta and rooted-residual constraints remain active.

## Preserved comparator

The full-support `z=1,h=0` branch remains valid. Raw criticality still forces `nu=y`, and the corrected rooted triangle baseline remains `Q=p(p-1)+pu+e(G[U])`. No result in this run weakens it.

## Immediate frontier

1. Restrict zero-buffer work to `lambda>=1`.
2. Attack `lambda=1`, especially k=1 and k=2, with the full witness count m and exact `Ccap_P/(ONE-P)/(CROWD)` rather than the coarse parameter gate.
3. For `k>=lambda+2`, intersect the forced unmatched-heavy inequality `(UH)` with source-tuple/beta capacity and `(QE-REV0)`.
4. Seek an explicit sufficiently-large exclusion threshold or a tiny structural residue.
5. If a residue survives, use raw criticality around the forced core--outside missing pairs and the rooted B-edge slots of the buffer--outside edges.
6. Do not move to z=2 until this branch is exhausted.
<!-- CURRENT-STATUS:END -->
