# Scope audit: matched Orientation-A collapse beyond buffer equality

Date: 2026-09-19

Status: dependency hardening for `BUFFER_FIRST_STRICT_LAYER.md`. The historical matched-channel collapse was stated inside the former buffer-equality geometry. The first-strict theorem needs the same exclusion one layer above equality. This note re-proves exactly that exclusion and records which hypotheses are actually used.

## Setup

Retain the rigid one-code common-buffer crossing system:

- `X=H_M dotcup H_0`;
- `U_-=W_0 dotcup {b}` and `c(b)=c(w)=bar d` for every `w in W_0`;
- every `w in W_0` has its graph-fixed head `h(w) in H_0` with `wh(w) in E`;
- every `x in H_M` has a graph-fixed matched crossing foot `q` with `gamma(q)=d`, `qx in E`, and q is the `bar d` endpoint in its own fibre (the Y-source of code d is nonadjacent to its crossing foot);
- a matched Orientation-A certificate for a buffer edge `bx` would be a matched endpoint z satisfying

`bz in E`, `xz notin E`, `N(x) cap N(z)={b}`.             `(A-M)`

No assumption that b is complete to X or to U_o is made below.

## Core heads

Let `x=h(w_0) in H_0`.

If `(A-M)` used a matched endpoint z, then `bz in E`. Since b and `w_0` have the same tight code `bar d`, they choose the same matched endpoint in every tight fibre. Hence

`w_0 z in E`.

But also `w_0 x in E`. Thus `w_0` is a common neighbour of x and z distinct from b, contradicting `N(x) cap N(z)={b}`.

Therefore no core head admits a matched Orientation-A buffer certificate.

## Matched-crossing heads

Let `x in H_M` and let q be its matched gamma-d crossing foot, so `qx in E`.

Suppose `(A-M)` used matched endpoint z. Since `bz in E` and b has code `bar d`, z is the `bar d` endpoint of its fibre.

If z lies in the same fibre as q, then q itself is the `bar d` endpoint of that fibre, so z=q. But `qx in E`, contradicting the certificate requirement `xz notin E`.

If z lies in a different fibre, `gamma(q)=d` says that q is adjacent in z's fibre to the endpoint opposite d, namely the `bar d` endpoint. That endpoint is z. Hence

`qz in E`.

Together with `qx in E`, q is a common neighbour of x and z distinct from b, again contradicting `N(x) cap N(z)={b}`.

Therefore no matched-crossing head admits a matched Orientation-A buffer certificate.

## Conclusion

> **MATCHED-A SCOPE THEOREM.** In the rigid one-code common-buffer crossing system, no buffer--X edge can use a matched Orientation-A certificate, independently of buffer degree equality or buffer completeness to X/U_o.

This is exactly the extension used in `BUFFER_FIRST_STRICT_LAYER.md`. It depends only on the graph-fixed crossing head systems and tight-code/gamma adjacency. It does not use the source-tuple theorem, pair capacity, finite scans, or cross-source witness injectivity.

The proof also confirms that the new first-strict classification does not accidentally import the closed equality hypothesis through the older matched-channel theorem.
