# Rigid Hall cuts — rooted corollary and one-code U-occupancy refinement

Date: 2026-09-20

Status: **same-session scope correction and corollary**. During hostile reconciliation I found that commit `92d1808` / `RIGID_SINGLETON_GAMMA_BUDGET_REPAIR.md` had already proved the sharp global singleton budget `hx<=u+p` and its rooted collapse `(h-1)x+g0<=lambda+1`. Those facts are therefore **not new in this note**. The useful new content here is the one-code interpretation of the residual gap as an explicit bound on how many U vertices can escape the mandatory complementary witness population.

The zero-positive-fixture caveat remains binding.

## 1. Predecessor theorem retained

For an exact rigid Hall cut `M_X=E_X=0`, `x=|A_X|>=3`, with `h` distinct source codes in `Y`, commit `92d1808` already establishes

> `h x<=u+p`,

and, using `x+y=2p+u-lambda-1` and `g0=p-y`, equivalently

> **`(h-1)x+g0<=lambda+1`.**                              `(SRC-COLL)`

Hence `g0<=lambda+1`, and `h>=2` requires `lambda+1-g0>=x`. These are predecessor results, not a new claim of this note.

## 2. One-code U-occupancy corollary

Set

`c:=lambda+1-g0>=0`.

In the one-code case `h=1`, the predecessor singleton budget gives a mandatory complementary-code U-witness population of size

`K>=[x-p]_+`.

The rooted size identity gives

`u=x-p+c`.

Therefore

> **`K >= [u-c]_+`.**                                      `(SRC-U1)`

So whenever `x>p`, **all but at most `c=lambda+1-g0` vertices of U** belong to the mandatory complementary witness population for the outside source code.

Since each such physical U witness has exactly one `A_X` neighbour, the located-hole consequence is

> **`Z_X >= (x-1)[u-c]_+`.**                              `(SRC-ZX1)`

This is the genuinely useful refinement preserved here. It turns the rooted collapse gap `c` into a physical outside-reservoir statement rather than just a code-count inequality.

## 3. Strategic use

The correct near-rigid front end is therefore:

- predecessor: `c=lambda+1-g0>=0`;
- predecessor: `c<x` forces one-code;
- new corollary: in that one-code regime, if `x>p`, at most `c` U vertices escape the mandatory complementary-code witness population;
- combine this with the distinct-singleton-head refinement `rho` and the near-rigid private-coordinate / Hamming-slot price before invoking pair-local `Ccap_P`, `(ONE-P)` and `(CROWD)`.

This note deliberately does not duplicate the proof of the sharp `p` singleton budget already present at `92d1808`.