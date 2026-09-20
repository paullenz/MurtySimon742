# Exact second-strict mixed-hole branch: y=1 large-head classification

Date: 2026-09-20

Status: internal conditional structural reduction. This note treats the y=1 tail left open by `SECOND_STRICT_MIXED_YGE2_CLOSURE.md`; it is not a closure. The statements below assume `p>=2` and `x>=5`, so the previously proved exceptional-capacity inequality already gives `|S_0|=1`.

## 1. Setup and transferred facts

Let Y={y}. Put `S_0={j}` and `C=c(a_0)`; thus C differs from d exactly at j. Let `D=bar C`.

The mixed-hole setup still has the unique X-hole `a_0`, unique outside hole `z_0`, and at least `H>=x-2` outside-certified Type-R heads. The following facts from the y>=2 proof do not use y>=2 and remain valid:

- `E(U_o^*,Y)=emptyset` for `U_o^*=U_o\{z_0}`;
- `U_o^*` contains no `bar d` code;
- every `w in U_o^*` is itself an outside certificate for some buffer head;
- `E(a_0,W_0)=emptyset`.

The only new difficulty is the single edge `a_0y`: with no second Y-vertex, its forward orientation can use a complementary X-witness.

## 2. Exhaustive trichotomy for the edge a_0y

The edge `a_0y` lies in the p-1 common tight fibres. Raw criticality has only the following possibilities.

### R — z_0 witnesses y -> a_0

Then

`c(z_0)=bar d`, `z_0a_0 in E`, `z_0y notin E`.

### Fz — z_0 witnesses a_0 -> y

Then

`c(z_0)=D`, `z_0a_0 notin E`, `z_0y in E`, and

`N(a_0) cap N(z_0)={y}`.

### Fx — an X-vertex t witnesses a_0 -> y

Then

`t in X\{a_0}`, `c(t)=D`, `a_0t notin E`, and

`N(a_0) cap N(t)={y}`.

No other location is possible. Ordinary outside vertices miss y; common-core/buffer vertices miss y; a matched endpoint distinguishing C from d acquires an outside Type-R witness as an additional common neighbour; and reverse witnesses other than z_0 would need code `bar d`, absent from the ordinary outside layer and unavailable at the core because `a_0` misses it.

## 3. R case — complete radius-one collapse

If `c(z_0)=bar d`, the pair `(b,z_0)` shares all tight bar-d endpoints and cannot reverse-certify any buffer edge. Hence all `x-1` buffer heads are outside-certified Type R.

Any head of Hamming radius at least two would need z_0 to certify its `S_0` matched edge. The orientation `q_j -> x` is impossible because `z_0q_j in E`; the reverse orientation has at least two tight matched common neighbours with z_0. Therefore every X-head has radius one.

Thus

> all X has the single code C, `|S_0|=1`, and every `a_0--X'` edge is absent.

Any edge inside `X'=X\{a_0}` would be a same-code edge requiring a complementary D-coded witness. There is no A_D vertex; every U_D witness is an ordinary outside b-neighbour, so b would be an extra common neighbour with both endpoints. Therefore

> `G[X]=emptyset` in case R.                              `(Y1-R-X0)`

## 4. Fx case — one complementary exceptional head and no higher-radius R-head

Suppose `t in X` witnesses `a_0 -> y`. Since `c(t)=D`, its difference set from d does not contain j. Hence t cannot be Type R, while Type F is globally impossible. Therefore its buffer edge must be the unique exceptional reverse-certified edge, using z_0.

Consequently

> `c(z_0)=d`, `N(b) cap N(z_0)={t}`.                    `(Y1-FX-Z0)`

There are exactly `H=x-2` outside-certified Type-R heads.

A higher-radius Type-R head h would again need z_0 at its unique S_0 coordinate. With c(z_0)=d, orientation `h -> q_j` is impossible because z_0 misses q_j; orientation `q_j -> h` would require `z_0h in E`. But b is adjacent to h and `N(b) cap N(z_0)={t}`, so z_0 cannot see h. Hence no such head exists.

Thus the X-code multiset is exactly

> `C^(x-1) dotcup D^1`,                                  `(Y1-FX-CODES)`

where the unique D-vertex is t.

The C-class is independent: an internal C-edge cannot use t as its complementary witness because both endpoints and t share y; a U_D witness is a b-neighbour and b is an extra common neighbour for two buffer-head endpoints, while `a_0` is already separated from every Type-R head.

Moreover t has no edge to a C-vertex when p>=2. A direct raw-criticality exhaustion of a hypothetical `tx` edge gives:

- X/Y witnesses fail through the common Y-neighbour;
- the unique core head of x shares additional tight bar-d endpoints with t;
- z_0 shares the p-1 d-coordinates with a C-source;
- ordinary U_o witnesses have code D and are nonadjacent to t because `N(a_0) cap N(t)={y}` while every such witness sees a_0;
- matched witnesses acquire either y or b as an extra common neighbour.

Therefore

> `G[X]=emptyset` in case Fx as well.                     `(Y1-FX-X0)`

The same singleton `N(a_0) cap N(t)={y}` also forces `a_0z_0 notin E`, since z_0t is the reverse buffer edge.

## 5. Fz case — at most one higher-radius head

Suppose z_0 itself witnesses `a_0 -> y`. Then `c(z_0)=D`, `z_0a_0 notin E`, and `z_0y in E`.

Because b has code `bar d`, b and z_0 share p-1 tight bar-d endpoints. For p>=2 this already prevents `(b,z_0)` from having a singleton X common-neighbour set, so no buffer edge uses the reverse exceptional channel. All `x-1` heads are outside-certified Type R.

For any higher-radius head h, the matched edge at j must use z_0. Since z_0 has d at j it misses q_j, so only `q_j -> h` is possible. The fixed ordered pair `(q_j,z_0)` has one graph-fixed singleton head. Therefore

> at most one X-head has radius >=2; every other X-vertex has code C. `(Y1-FZ-ONEEXC)`

The relation `N(a_0) cap N(z_0)={y}` forces z_0 to miss every ordinary outside vertex that is adjacent to a_0, so z_0 is anticomplete to the entire selected Type-R witness population.

This is now the only large-head mixed y=1 geometry not reduced to an independent X-set with at most two complementary code classes.

## 6. Hamming-slot consequences in the two independent-X cases

In case R, every X--Y edge has Hamming distance one and `G[X]=emptyset`, so the local slot theorem gives

> `r>=x+1`.

In case Fx, the `x-1` C-vertices are at distance one from d and t is at distance p-1. Since `G[X]=emptyset`,

- every C-vertex has at least one unused rooted slot;
- t has at least p-1 unused rooted slots;
- the Y-vertex has at least `ceil((x+p-2)/x)` unused slots.

Hence

> `r>=x+p-2+ceil((x+p-2)/x)`.                            `(Y1-FX-R)`

This lower bound should be combined next with the exact score cap and physical U-edge ledger, as in the y>=2 closure.

## 7. Live y=1 frontier

For `p>=2,x>=5`, the mixed y=1 branch is reduced to three explicit geometries:

1. **R:** all X one radius-one code C and `G[X]=emptyset`;
2. **Fx:** `C^(x-1) dotcup D`, `G[X]=emptyset`, with the D-head the unique reverse-buffer head;
3. **Fz:** all but at most one X-vertex have code C; the only unresolved freedom is one higher-radius Type-R head plus the exceptional D-coded vertex z_0.

The `x=3,4` cases remain small-head tails because the earlier `(H-1)(|S_0|-1)<=1` inequality does not force singleton S_0 there.
