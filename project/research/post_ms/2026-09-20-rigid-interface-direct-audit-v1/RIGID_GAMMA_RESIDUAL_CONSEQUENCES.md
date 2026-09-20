# Rigid Hall cuts — gamma-budget witnesses fed into the rooted residual ledger

Date: 2026-09-20

Status: **same-session structural synthesis** conditional on the exact rigid Hall event. This note feeds `RIGID_GAMMA_BUDGET.md` into the exact A--U nonedge and rooted residual identities. It is not a claim that a rigid cut is realizable.

## 1. Local variables retained

Use the notation of `RIGID_GAMMA_BUDGET.md`:

- D = represented source codes in Y, `h=|D|`;
- `y_d=|Y_d|`;
- `g_d:=g_{P(d)}`;
- `k_d=[x-g_d]_+`;
- `K=sum_d k_d`;
- `H_Y:=sum_d y_d k_d`.

Then

`u>=K`,

`K>=[hx-2p]_+`,

and the physical witness deficits are

> `Z_X >= (x-1)K`,
> `Z_Y >= H_Y`,
> `Z >= Z_gamma:=(x-1)K+H_Y`.                            `(GR-Z)`

Since every represented code has `y_d>=1`,

> `H_Y>=K`, hence `Z_gamma>=xK`.                          `(GR-XK)`

## 2. Immediate diversity bounds before score bookkeeping

Because `Z` counts A--U nonedges, always `Z<=au`. Combining with `(GR-XK)` gives

> `xK<=au`.                                                `(GR-AU)`

With `K>=[hx-2p]_+`, every rigid cut therefore satisfies

> **`x[hx-2p]_+ <= au`.**                                 `(GR-DIV1)`

The simpler population bound from `u>=K` is

> **`hx<=u+2p`.**                                         `(GR-DIV0)`

Using the rooted size identity

`a=2p+u-lambda-1=x+y`,

this becomes the particularly transparent form

> **`(h-1)x <= y+lambda+1`.**                             `(GR-COLL)`

Thus if

> `x>y+lambda+1`,

then necessarily

> **`h=1`.**                                               `(GR-ONECODE)`

This is a score-free one-code collapse criterion. It is complementary to the earlier U-slack/beta-expulsion collapse and remains informative even when `x<=p`.

More generally,

`h <= 1+floor((y+lambda+1)/x)`.

## 3. Exact U-slack input

Put

`g0=x-T0=p-y`.

For `g0>=1`, the code-specific witness-slack theorem gives

> `E_U >= E_gamma:=sum_d k_d(y_d+g0-1)`.

Since `H_Y>=K`,

`E_gamma=(g0-1)K+H_Y >= g0 K`.

Hence

> **`E_U >= g0[hx-2p]_+`** for `g0>=1`.                   `(GR-EU)`

For an above-`M(n)` graph the standard total-score ceiling gives `E_U<=C0`, so a necessary condition is

> **`g0[hx-2p]_+ <= C0`.**                                `(GR-C0)`

This gives the explicit code-diversity bound

`h <= floor((2p+floor(C0/g0))/x)`

whenever `g0>=1` and the numerator is interpreted as an upper relaxation. The exact `k_d,y_d` expression should be retained in any proof-critical optimization.

## 4. Exact nonedge identity and forced q/E tradeoff

The rooted A--U nonedge identity is

`Z=u(p-lambda)+2q+E_U`.

Define

> `D_gamma:=Z_gamma-u(p-lambda)`.                          `(GR-D)`

Every rigid survivor satisfies

> `2q+E_U >= D_gamma`.                                    `(GR-QE0)`

Let `E_gamma` denote the code-specific slack floor when `g0>=1`; for `g0<=1` use the safe truncated floor

`E_gamma=[H_Y-(1-g0)u]_+`.

The exact integer minimization is then

> **`q+E_U >= E_gamma+ceil((D_gamma-E_gamma)_+/2)`.**      `(GR-QE)`

This is the gamma-budget analogue of the earlier uniform-k rigid residual theorem, but it keeps the actual pair-local matched relief and source multiplicities.

## 5. Forced internal-A edge mass above M(n)

The rooted residual identity is

`f=(p-lambda)(p+u)+q+E_U-delta`.

For an above-`M(n)` graph, `delta<=D_M-1`. Therefore `(GR-QE)` gives

> **`f >= (p-lambda)(p+u)-D_M+1`
> `     +E_gamma+ceil((D_gamma-E_gamma)_+/2)`.**           `(GR-F)`

This is proof-level once the rigid event and the upstream rooted identities are assumed. It does not rely on a finite parameter scan.

Likewise, since above M(n) has `E_U<=C0`, `(GR-QE0)` gives

> `q >= ceil((D_gamma-C0)_+/2)`,                           `(GR-Q)`

and hence raises the rooted triangle count Q through the preserved relation

`Q=p(p+u-1)+q`.

## 6. Structural interpretation

The new budget exposes a useful dichotomy before the one-code trap is invoked:

1. **large X relative to Y and lambda:** `(GR-COLL)` forces h=1 immediately, so the exact pair-local `(ONE-P)/(CROWD)/Ccap_P` machinery is the correct next tool;
2. **h>=2:** X must obey `(h-1)x<=y+lambda+1`, while the code-specific witness populations simultaneously force `(GR-DIV1)`, `(GR-C0)` and `(GR-F)`.

Thus the empirical absence of rigid cuts can now be attacked in two sharply separated regimes rather than by another broad total-score scan.

The next proof attempt should ask whether the h>=2 regime is compatible with the Hall near-equality condition that created the rigid event in the first place. If not, the rigid event automatically enters the one-code branch; if it is, the exact `k_d` residual floor above is the correct input rather than the historical uniform-k relaxation.