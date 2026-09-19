# One-witness polarization pinch in the first-strict funnel

Date: 2026-09-19

Status: **conditional structural theorem** inside the independently re-audited first-strict unloaded common-buffer branch. This note uses the repaired support-block package in `FIRST_STRICT_FUNNEL_REPAIR_AUDIT.md`; it is not a graph-realizability theorem.

## 1. Setup

Retain the first-strict unique-hole geometry:

- `A=X dotcup Y`, `|X|=x>=3`, `|Y|=y>0`, and `X--Y` is complete;
- every Y-code is `d`;
- `b` has a unique X non-neighbour `a_0` and is complete to `X\{a_0}` and to `U_o`;
- every buffer neighbour in `X\{a_0}` has a selected outside witness;
- `S_0={i:c(a_0)_i!=d_i}`, `I_0=[p]\S_0`, and `s=|S_0|`;
- `N=x-1`.

Assume the selected outside-reservoir population has the minimum possible physical size

> `m=1`.

By the audited one-witness polarization theorem, all `N` buffer neighbours have one common tight code `C` and exactly one of two cases holds:

1. **all-F:** their agreement block with `d` is a singleton `I={i} subseteq S_0`;
2. **all-R:** their common nonempty agreement block satisfies `I subseteq I_0`, the common outside witness `z` has `N_A(z)={a_0}`, and `a_0` is isolated from `X\{a_0}` in `G[X]`.

Every X-vertex has an A-neighbour in Y with a different tight code, so the local rooted-slot theorem gives at least one unused rooted slot at every X-vertex.

## 2. Unit I — exact all-F Hamming bill

In the all-F case every buffer head is at Hamming distance `p-1` from `d`, while `a_0` is at distance `s` from `d`. Thus for every `y_0 in Y`,

> `H_Y(y_0)=s+N(p-1)`.

Since `d_A(y_0)=x`,

> `r_{y_0} >= ceil((s+N(p-1))/x)`.

The right side is minimized at `s=1`. Because `N=x-1`,

`ceil((1+(x-1)(p-1))/x)`

`= p-1-floor((p-2)/x)`.

Therefore

> **ALL-F SLOT BILL**
>
> `r >= x + y[p-1-floor((p-2)/x)]`.                    `(F-SLOT)`

In particular, for every `p>=3`,

> `r >= a+y`.                                             `(F+Y)`

So the all-F polarization can never realize the cheapest `r=a` rooted-slot geometry.

## 3. Unit II — exact all-R block formula

In the all-R case put

> `q=|I|`, so `1<=q<=p-s`.

Every buffer head has Hamming distance `p-q` from `d`. Hence for every `y_0 in Y`,

> `H_Y(y_0)=s+N(p-q)`,
>
> `r_{y_0}>=ceil((s+N(p-q))/x)`.                         `(R-HAM)`

Thus

> `r >= x+y ceil((s+N(p-q))/x)`.                         `(R-SLOT)`

This retains the actual block size rather than replacing every Type-R head by the coarse radius floor `s`.

## 4. Unit III — proper-block surcharge

If `I` is a proper subset of `I_0`, then

`q<=p-s-1`,

so

`s+N(p-q) >= s+N(s+1)=xs+N`.

As `N=x-1>0`,

> `r_{y_0}>=s+1`.

Consequently

> **PROPER-R SURCHARGE**
>
> `I proper subset I_0  ==>  r>=x+y(s+1)>=a+y`.          `(R-PROP)`

The extra `+y` is discrete: it comes from one unavoidable extra Hamming unit at every Y-source, not from a continuous score relaxation.

## 5. Unit IV — coincidence arm

The only way the all-R Hamming bill can avoid `(R-PROP)` is

> `I=I_0`.

Then the common buffer-head code equals `c(a_0)`, because a binary tight code is determined by its agreement set with `d`. Therefore:

> **COINCIDENCE ARM.** `I=I_0` implies every vertex of X has one common tight code `C=c(a_0)`.

In this arm `q=p-s` and `(R-HAM)` becomes

`H_Y(y_0)=xs`,

so

> `r>=x+ys`.                                              `(R-COINC)`

If `s>=2`, this again gives `r>=a+y`.

Thus the only all-R geometry that can avoid the `+y` slot surcharge has

> `s=1`, `I=I_0`, and all of X in one code class at Hamming distance one from d. `(R-EQ)`

## 6. Unit V — full-class capacity in the equality arm

The preserved aligned-code self-pricing theorem bounds the size of an A-code class by

`R_A=floor(R_code(C0)/2)`.

The interrupted diagnostic applied this to the `N=x-1` buffer-neighbour class. In the coincidence arm `(R-EQ)`, however, `a_0` belongs to the **same** code class. The physical class has size x, not N.

Therefore the equality arm has the sharper necessary condition

> `x <= R_A`.                                             `(FULL-CLASS)`

This is a structural correction to the equality geometry, not a new scan gate for general all-R blocks.

## 7. Unit VI — one-witness equality-pinch theorem

Combining the two polarizations gives a compact classification.

### Theorem 7.1 — one-witness equality pinch

Inside the audited first-strict branch, if `m=1` and

> `r<a+y`,

then necessarily all of the following hold:

1. the polarization is all-R;
2. `S_0` is a singleton (`s=1`);
3. `I=I_0`;
4. all of X has one common tight code `C` with `d_H(C,d)=1`;
5. `a_0` is isolated in `G[X]` from the other X-vertices;
6. the unique selected outside witness z has `N_A(z)={a_0}`;
7. `epsilon_z>=p-1` and `epsilon_{a_0}>=p-y+1`;
8. the full code class obeys `x<=R_A`.

Equivalently:

> **every other one-witness geometry pays `r>=a+y`.**

This identifies a single literal Hamming equality model rather than a broad all-R family.

## 8. Residual consequence

Using the exact rooted identity

`r=(p-lambda)(p+u)+Q+E_U`,

where `Q=e(G[U])`, every non-equality one-witness geometry satisfies

> `Q+E_U >= a+y-(p-lambda)(p+u)`.                         `(RES+Y)`

The equality arm has only the weaker baseline `r>=a`, but is now forced into `(R-EQ)` plus `(FULL-CLASS)` and the physical neighbourhood conditions above.

## 9. Next target

Do not scatter into the loaded-buffer or larger-reservoir branches yet. The next hand attack should target the single equality model `(R-EQ)`:

- all X one code C at Hamming distance one from d;
- `a_0` isolated in `G[X]`;
- one outside witness z with `N_A(z)={a_0}` and `c(z)=bar C`;
- b adjacent to `X\{a_0}` and z, but not a_0;
- for every `x in X\{a_0}`, `N(x) cap N(z)={b}`;
- for every coordinate in `I_0`, the reverse funnel gives `N(q_i) cap N(a_0)={z}`.

The highest-value next question is whether raw criticality of the remaining `a_0--U`, `X--U`, and same-code X-edges forces additional located U-holes. Any such holes feed directly into `Q-STRICT` and may close the only one-witness arm that avoids the `+y` residual surcharge.
