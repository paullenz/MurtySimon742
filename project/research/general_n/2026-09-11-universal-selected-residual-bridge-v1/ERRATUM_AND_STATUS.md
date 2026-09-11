# Erratum and status note for UNIVERSAL_BRIDGE.md

11 September 2026.

The first version of `UNIVERSAL_BRIDGE.md` contains one **non-blocking displayed-algebra omission** in Section 5.

It writes

```text
d_H(u)=rho_u+(b-1)-(q_u+p_u)>=a.
```

That display omits the `q_u` selected A-neighbours of u. The correct calculation is

```text
d_H(u)
 = (rho_u+q_u) + [(b-1)-(q_u+p_u)]
 = rho_u+b-1-p_u.
```

Therefore the stated consequence

```text
p_u <= rho_u+b-a-1
```

is **correct**. The omission is in the intermediate displayed degree formula, not in the bound used downstream, so no fixed-order result or subsequent inequality changes.

The independently written canonical consolidation

```text
project/research/general_n/2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md
```

already contains the correct derivation in its Section 7 and should be preferred as the current internal canonical review surface. `UNIVERSAL_BRIDGE.md` and its audit are retained as a separately written corroborating reconstruction rather than silently rewritten.

This is candidate mathematics; independent expert review remains open.
