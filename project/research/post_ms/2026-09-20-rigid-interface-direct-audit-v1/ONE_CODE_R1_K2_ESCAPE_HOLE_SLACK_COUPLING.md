# Residual-one k=2 escape hole/slack coupling

Date: 2026-09-20

Status: **same-session exact bookkeeping consequence** of the global H/Y polarization on the exact low-k ray. No finite scan is used.

The purpose is to keep the new located A--U hole theorem in the correct rooted/score currencies rather than returning to an undifferentiated physical-defect coefficient.

## 1. Exact per-U degree identity on the low-k ray

On

`lambda=p`, `u=p+1`, `x=p+1`, `y=p-1`,

we have `a=x+y=2p` and, for every U-vertex t,

`d_{A union U}(t)=p+u-1-epsilon_t=2p-epsilon_t`.

Let

- `z_A(t)` be the number of nonneighbours of t in A;
- `m_U(t)` be the number of nonneighbours of t in `U\{t}`.

There are

`a+u-1=3p`

possible neighbours in `A union (U\{t})`. Therefore

> **`z_A(t)+m_U(t)=p+epsilon_t`.**                        `(HS-ID)`

Summing over all U gives the familiar global identity

> **`Z_X+Z_Y+2M_U=u p+E_U`.**                            `(HS-GLOBAL)`

On the ray, `u=p+1`.

This explains why the rooted and score ceilings must not be compared to an unweighted defect total independently: the currencies are coupled exactly.

## 2. Insert the new escape polarization

For every escape `t in E=U\W_s`, the global H/Y polarization gives

`z_A(t)>=p-2`.

Substitute into `(HS-ID)`:

`p-2+m_U(t) <= p+epsilon_t`,

so

> **`epsilon_t >= m_U(t)-2`.**                           `(HS-LOCAL)`

Thus an escape cannot be simultaneously A-hole-minimal, U-sparse and low-slack.

Summing over E,

> **`E_E >= 2M_U(E)+M_U(E,W_s)-2|E|`.**                 `(HS-E)`

Here `M_U(E)` counts missing pairs internal to E and `M_U(E,W_s)` missing escape--selected-witness pairs.

The lower-order term is only `2(p-1)` on the exact ray.

## 3. Consequence for a compressed independent escape sector

If a linear subset `P subseteq E` is independent, the missing-P incidences force slack as well as rooted missing-edge cost.

In the extreme compressed endpoint `P=E`,

`M_U(E)=binom(p-1,2)`.

Then `(HS-E)` gives

> `E_E >= (p-1)(p-4)+M_U(E,W_s)`.                       `(HS-INDEP)`

So an independent escape reservoir has, simultaneously,

- the global located A-hole block `(p-1)(p-2)`;
- weighted rooted cost `2M_U(E)=(p-1)(p-2)`;
- U-slack `E_E=(1-o(1))p^2`.

The three leading contributions lie in the three distinct terms `Z`, `2M_U`, and `E_U` of the combined weighted ledger. Their total leading coefficient is already three before `2L_A` and before any class-specific extra hole/slack price.

This does **not** yet contradict the legitimate combined ceiling, whose leading coefficient is four. It does, however, reduce the remaining gap to a single leading coefficient and identifies exactly what must supply it: A-side slack or an additional disjoint class-specific price.

## 4. Strategic normal form

The new accounting gives a sharp pivot.

A hypothetical asymptotic survivor must avoid paying the coefficient-three compressed-independent package in one of two ways:

1. make E substantially U-dense, which by `(HS-GLOBAL)` forces the compulsory `~p^2` A-hole block to account for almost all of the baseline `up` term; or
2. retain a large independent/proper-support sector and then find a way to keep A-side slack `L_A` and all class-specific costs below the remaining coefficient-one budget.

The cross-code complement-capacity theorem is naturally suited to branch (1): U-density requires a large population whose complementary A-code is represented. At `J2=empty`, the only A-code classes available are `d`, `d xor e_j`, and `d xor e_i`, so only their complementary U-code classes can source U--U edges.

The next high-value attack should therefore retain the actual complementary-code source population while optimizing `(HS-GLOBAL)`, rather than adding another scalar lower bound on `D_phys`.

## 5. Trust boundary

All statements are conditional on the same residual-one rigid interface and exact low-k ray. No graph-realizability claim is made; the zero-positive rigid-fixture gap and mandatory `X_3` control remain unchanged.