# Exact second-strict mixed-hole branch: structural normalization and closure for y>=2

Date: 2026-09-20

Status: internal conditional structural theorem inside the audited rigid one-code complete-cut branch. It does not repair the separate zero-positive-fixture interface gap. `X_3` remains outside scope because the present branch has nonempty unmatched structure.

## 1. Audit reconciliation

This continues `2026-09-20-second-strict-initial-reduction-v1/SECOND_STRICT_INITIAL_REDUCTION.md` after an independent hostile reread of the upstream first-strict closure. The first-strict radius>=2 transfer was rechecked directly against raw triangle-edge criticality and the independently re-derived same-code theorem; no new gap was found. Exact pair-local `Ccap_P/(ONE-P)/(CROWD)` remains mandatory where used, but the closure below is obtained before another pair-capacity relaxation.

Use the exact second-strict mixed-hole setup

- `epsilon_b=p-g+2`;
- `h_X=h_o=1`;
- `a_0` is the unique X non-neighbour of b;
- `z_0` is the unique U_o non-neighbour of b;
- every other `w in U_o^*:=U_o\{z_0}` is adjacent to b;
- at least `H>=x-2` buffer heads are outside-certified and, by the upstream Type-F elimination, are Type R;
- consequently `d_X(a_0)<=1`.

Write `S_0={i:c(a_0)_i!=d_i}` and `I_0=[p]\S_0`.

## 2. Ordinary outside layer remains Y-anticomplete and has no bar-d code

The first-strict proof of `E(U_o,Y)=emptyset` only uses the edge `bw`, the facts `bw in E`, `d_Y(b)=0`, `N_A(b)=X\{a_0}`, nonempty `S_0`, and `x>=3`. Those hypotheses still hold for every `w in U_o^*`.

Hence

> `E(U_o^*,Y)=emptyset`.                                  `(MIX-UY)`

The same-code argument for a hypothetical `c(w)=bar d` also transfers unchanged to any such b-neighbour, so

> `U_o^* cap V_{bar d}=emptyset`.                         `(MIX-NOBARD)`

Moreover raw criticality of the rooted U-edge `bw` cannot orient `b -> w`: a Y witness is impossible by `(MIX-UY)`, while `a_0` shares a tight matched neighbour with b. Therefore it must orient `w -> b` through some `q in X\{a_0}`:

> `wq notin E`, `N(w) cap N(q)={b}`.                     `(MIX-EVERY-UO-CERT)`

Thus every ordinary outside vertex is itself an outside certificate for at least one buffer head.

## 3. The unique X-hole misses the whole common core

Choose any outside-certified Type-R head x and any `i in I_x`, which is nonempty. Its reverse funnel gives

> `N(q_i) cap N(a_0)={z_x}`.

Every common-core vertex `w in W_0` has code `bar d`, so `wq_i in E`. Hence `wa_0` would be a second common neighbour, impossible. Therefore

> `E({a_0},W_0)=emptyset`.                                `(MIX-A0-CORE)`

This uses only one existing Type-R head, and `H>=x-2>=1`.

## 4. For y>=2, criticality of a_0--Y fixes z_0 completely

Assume from now on `y>=2`. Fix `y_0 in Y`. Since `I_0` is nonempty, `a_0y_0` lies in a tight matched triangle and raw triangle-edge criticality applies.

All witness locations except `z_0` can be excluded.

- Root and matched vertices fail by adjacency or an extra common neighbour. In particular, for `j in S_0`, the d-endpoint in fibre j has an outside Type-R witness as an additional common neighbour with `a_0`.
- An X-witness in orientation `a_0 -> y_0` shares another Y-vertex with `a_0` because `y>=2` and `X--Y` is complete.
- Y-witnesses share the full d-code matched support.
- `b` misses both Y and `a_0`.
- Common-core vertices miss `a_0` by `(MIX-A0-CORE)`.
- Ordinary outside vertices cannot witness `a_0 -> y_0` by `(MIX-UY)`; in the reverse orientation `y_0 -> a_0`, avoiding a tight matched common neighbour would require code `bar d`, forbidden by `(MIX-NOBARD)`.

Hence every edge `a_0y` must use the one physical exception `z_0`.

A fixed pair `(a_0,z_0)` can certify at most one head y in the orientation `a_0 -> y`. Since `y>=2`, at least one edge must orient `y -> a_0`. That forces `z_0a_0 in E` and `z_0y notin E`. Once `z_0a_0` is present the opposite orientation is unavailable for every other Y-edge, so all of them orient `y -> a_0`.

The singleton relation then forces

> `c(z_0)=bar d`,
>
> `N_X(z_0)={a_0}`,
>
> `E(z_0,Y)=emptyset`.                                   `(MIX-Z0-NORMAL)`

The code assertion follows because any agreement between `c(z_0)` and d would give a tight matched common neighbour with the Y-source.

## 5. No exceptional reverse buffer edge survives

Since b and `z_0` both have code `bar d`, they share all p tight matched endpoints. Thus the pair `(b,z_0)` cannot have singleton common-neighbour set `{x}` for any X-head.

Therefore the exceptional reverse channel is actually empty:

> every one of the `x-1` buffer edges `b--(X\{a_0})` is outside-certified Type R. `(MIX-ALL-R)`

## 6. All X-codes collapse to radius one

Take any `x in X\{a_0}`. If `|S_x|>=2`, choose `j in S_0 subseteq S_x`. The matched edge `xq_j` must use `z_0` as the unique exceptional witness, by the same radius>=2 exhaustion used in the first-strict closure.

But `c(z_0)=bar d`:

- orientation `q_j -> x` is impossible because `z_0q_j in E`;
- orientation `x -> q_j` is impossible because x and `z_0` share every `q_i` with `i in S_x`, hence at least two matched common neighbours.

Contradiction. Therefore `|S_x|=1`. Since `S_0` is nonempty and `S_0 subseteq S_x`, necessarily

> `|S_0|=1`, and every vertex of X has one common code C at Hamming radius one from d. `(MIX-ONE-CODE)`

## 7. X is independent

Type R already gives `a_0x notin E` for every `x!=a_0`.

Suppose two vertices of `X\{a_0}` were adjacent. They have the same code C, so the independently re-derived same-code theorem requires a complementary-code witness of code `bar C` in `A union U`.

There is no A-vertex of code `bar C`: Y has code d and all X has code C. Any U-vertex of code `bar C` lies in `U_o^*`, because `U_-` and `z_0` have code `bar d`. But every such ordinary outside vertex is adjacent to b, and both endpoints of the putative X-edge are also adjacent to b. Hence b is an additional common neighbour, contradicting the singleton certificate.

Thus

> `G[X]` is edgeless.                                    `(MIX-X-INDEP)`

## 8. Complete-cut criticality saturates the common core

Fix `x in X\{a_0}` and `y in Y`. Their codes C and d differ in exactly the unique coordinate j. The edge xy is triangular in the remaining tight fibres (for p>=2; this is the only range used in the eventual branch).

Orientation `x -> y` has no witness: ordinary/outside U misses Y, the unloaded core and buffer miss Y, an X-witness shares another Y-neighbour when `y>=2`, and the unique matched endpoint distinguishing the codes also shares another Y-neighbour.

Hence the edge must orient `y -> x`. Avoiding a tight matched common neighbour with the d-coded source forces a witness of code `bar d`. The only possible locations are `U_-=W_0 dotcup {b}` and `z_0`.

- b sees all `X\{a_0}`, so its common neighbourhood with y is not the singleton `{x}`;
- `z_0` sees only `a_0` in X;
- therefore a common-core vertex w must witness the edge, and singleton criticality forces `N_X(w)={x}`.

The exact common-core theorem already says every `w in W_0` has exactly one X-neighbour and its head map is injective. Since `(MIX-A0-CORE)` excludes `a_0` from the head image, there are at most `x-1` core vertices. The cut argument requires a distinct singleton-head core vertex for every one of the `x-1` vertices of `X\{a_0}`.

Therefore

> `k=x-1`, `g=1`, and the core head map is a bijection `W_0 <-> X\{a_0}`. `(MIX-CORE-SAT)`

In particular every core vertex is Y-anticomplete and has exactly its matched X-head as A-neighbour.

## 9. Every ordinary outside vertex has code bar-C, and U_o is independent

By `(MIX-EVERY-UO-CERT)`, each `w in U_o^*` certifies some buffer head. All such heads now have code C, so

> `c(w)=bar C`, `wa_0 in E`, and w misses at least one vertex of `X\{a_0}`. `(MIX-UO-CODE)`

Two ordinary outside vertices cannot be adjacent. A same-code U-U edge would require an A-witness of code C. If the witness were `a_0`, it is adjacent to the U-source; if it were in `X\{a_0}`, b would be a second common neighbour. Hence

> `G[U_o^*]` is edgeless.

Nor can `z_0` be adjacent to `w in U_o^*`. The U-U edge lies in the root triangle. In the orientation `w -> z_0`, the only A-neighbour of `z_0` is `a_0`, but `wa_0 in E`, so it cannot be a witness. In the reverse orientation, any A-witness adjacent to w must lie in `X\{a_0}`; it shares the unique bar-d matched endpoint q_j with `z_0`, giving an extra common neighbour.

Thus

> `G[U_o]` is edgeless.                                  `(MIX-UO-INDEP)`

## 10. Physical q and slack bills

Put `omega=|U_o|>=2`. Since `U_-=W_0 dotcup {b}` is independent and `U_o` is independent, all U-edges cross the two parts.

There are `x omega` possible cross pairs because `|U_-|=k+1=x`. At least omega of them are absent:

- the pair `bz_0`;
- for each of the `omega-1` ordinary outside vertices w, if q is one head certified by w, the unique core vertex attached to q must miss w, otherwise it is an additional common neighbour in `N(q) cap N(w)={b}`.

These are distinct physical pairs. Hence

> `q<=x omega-omega=(x-1)omega`.                         `(MIX-Q)`

The same holes sharpen the exact common-core score:

> `E_core >= (x-1)(p+x-2)+(omega-1)`.                    `(MIX-ECORE)`

Further direct degree counting gives

> `epsilon_b=p+1`,
>
> `epsilon_{z_0}>=p+omega-1`,
>
> `epsilon_w>=[p-x+omega+1]_+` for every `w in U_o^*`,
>
> `epsilon_y=p+omega` for every `y in Y`,
>
> `epsilon_x>=p+x-y` for every `x in X`.                 `(MIX-SLACK)`

The last bound locates x U-nonneighbours for every X-vertex: `a_0` misses b and all `x-1` core vertices; each other X-head misses `z_0`, the `x-2` non-head core vertices, and at least one ordinary outside certificate.

## 11. Rooted-slot lower bound

Because `G[X]` and `G[Y]` are edgeless and `X--Y` is complete, every X--Y edge joins codes at Hamming distance one.

The local Hamming slot inequality therefore gives `r_z>=1` for every `z in X union Y`, and hence

> `r>=a=x+y`.                                             `(MIX-RLOW)`

## 12. Above-M algebraic contradiction

For an above-threshold candidate define the standard score cap

`C0=2(D_M-1)+lambda(p+u)-p`,

where `D_M=b(n-b)-M(n)` and `M(n)=floor((n-1)^2/4)+1`.

From `(MIX-CORE-SAT)`,

`u=x+omega`,

`lambda=2p+omega-1-y`.

Let

`P=(omega-1)[p-x+omega+1]_+`.

The score floors above give

`S=E_U+L_A >= S_min`,

where

`S_min=(x-1)(p+x-2)+(omega-1)+(p+1)+(p+omega-1)+y(p+omega)+x(p+x-y)+P`.

Thus a survivor needs

`A:=C0-S_min>=0`.                                         `(A)`

On the other hand the exact rooted identity

`r=(p-lambda)(p+u)+q+E_U`

combined with `(MIX-Q)`, `S<=C0`, and

`L_A>=x(p+x-y)+y(p+omega)`

gives

`r<=R_max=(p-lambda)(p+u)+(x-1)omega+C0-x(p+x-y)-y(p+omega)`.

Together with `(MIX-RLOW)`, a survivor needs

`B:=R_max-(x+y)>=0`.                                      `(B)`

Write `eps in {0,1}` for the parity remainder in

`floor((n-1)^2/4)=((n-1)^2-eps)/4`.

Direct expansion gives the exact identity

> `4B+A=-(F+2P)/2`,                                      `(COMB)`

where

`F=8p^2+6p omega-8py-26p+3omega^2-10omega x+2omega y-6omega+12x^2-8xy-16x+5y^2+8y+42-5eps`.

The integer domain here is

`p>=2, x>=3, omega>=2, y>=2, lambda=2p+omega-1-y>=0`.

### Lemma — F>=0, with a unique zero

For `p>=3`, minimize F over real x,y. The unconstrained minimum is

`[160p^2+200p omega-1016p+35omega^2-536omega+1592-220eps]/44`.

Using `eps<=1`, this is increasing in p throughout `p>=3,omega>=2`; at p=3 it is at least

`(35omega^2+64omega-236)/44 >=32/44>0`.

For p=2 and `omega>=5`, the same real minimum is at least

`(35omega^2-136omega-20)/44>0`.

It remains only `p=2`, `omega=2,3,4`. The constraint `lambda>=0` gives respectively `2<=y<=5,6,7`; minimizing the elementary quadratic in integer `x>=3` for these finitely many y-values gives minima

- omega=2: F_min=2;
- omega=3: F_min=0, uniquely at `(x,y)=(3,2)`;
- omega=4: F_min=2.

At the unique zero `(p,x,omega,y)=(2,3,3,2)`,

`p-x+omega+1=3`, so `P=6>0`.

Therefore

> `F+2P>0` throughout the whole domain.                 `(POS)`

But `(A)` and `(B)` would imply `4B+A>=0`, contradicting `(COMB)` and `(POS)`.

Hence:

> **No above-M exact-second-strict mixed-hole configuration exists when `y>=2`.** `(MIX-YGE2-CLOSED)`

This is an analytic closure. The finite arithmetic appears only in the fixed three cases `p=2,omega in {2,3,4}` of the elementary positivity lemma; there is no parameter scan or realizability enumeration.

## 13. Remaining mixed tail

Only `y=1` remains in the mixed `(1,1)` subtype. The previous exceptional-capacity theorem still gives `|S_0|=1` for `x>=5`, with `x=3,4` retained as small-head tails. Criticality of the single edge `a_0Y` now has one additional possible X-witness channel, so the y>=2 normalization of `z_0` cannot be copied verbatim. That is the correct next target.
