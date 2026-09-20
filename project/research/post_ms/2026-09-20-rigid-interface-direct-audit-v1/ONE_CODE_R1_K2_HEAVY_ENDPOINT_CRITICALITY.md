# Residual-one k=2 heavy-endpoint criticality

Date: 2026-09-20

Status: **same-session candidate raw-criticality consequence**, conditional on the residual-one hub package and the k=2 one-sided normal form. No finite scan is used. Rigid-interface reachability remains unresolved.

## 1. Setup

Let `K={a,b}` and `W_s={z_a,z_b}` in the residual-one `k=2` branch. The beta map swaps a and b, and

`N_A(z_a)={a}`, `N_A(z_b)={b}`,

`N_Y(z_a)=N_Y(z_b)=empty`.

Call an escape `w in E=U\W_s`

- **K-heavy** if it is adjacent to both a,b and to neither z_a,z_b;
- **W-heavy** if it is adjacent to both z_a,z_b and to neither a,b.

These are the saturated cheap one-sided types from `ONE_CODE_R1_K2_ONESIDED_CONSERVATION.md`.

## 2. An escape anticomplete to K but adjacent to z_h has a forced orientation

Fix `h in K`, its used witness `z_h`, and an escape w such that

`w z_h in E(G)` and `N(w) cap K=empty`.

The edge `w z_h` lies in the rooted B-layer. Apply raw rooted B-edge criticality.

### Reverse orientation is impossible

In the reverse orientation (source `z_h`, singleton head w), the A-witness r must be adjacent to w and nonadjacent to z_h, with

`N(z_h) cap N(r)={w}`.

There are no possibilities:

- `r in K` is impossible because w is anticomplete to K;
- if `r in Y`, then h is adjacent to both z_h and r (the X--Y cut is complete), so h is an extra common neighbour;
- if `r in H`, let i be the private coordinate of r. Every H-head differs from d at i, while z_h has code `bar d`; hence both contain the matched endpoint `q_i`, which is an extra common neighbour distinct from w.

Thus reverse orientation cannot certify `w z_h`.

### Forward orientation is unique

In the forward orientation (source w, singleton head `z_h`), the A-witness must be adjacent to z_h. Since `N_A(z_h)={h}`, the witness is forced to be h. Therefore

> **`N(w) cap N(h)={z_h}`.**                              `(HE-FWD)`

This is a literal singleton equation, not a score relaxation.

## 3. Consequences for W-heavy escapes

A W-heavy w satisfies the hypotheses for both h=a and h=b. Hence

`N(w) cap N(a)={z_a}`,

`N(w) cap N(b)={z_b}`.                                  `(HE-W)`

Every vertex of Y is adjacent to both a and b. Therefore

> **`N_Y(w)=empty`.**                                     `(HE-Y0)`

Also `q_j` is adjacent to both a and b in the residual hub, so

> **`w q_j notin E(G)`.**                                `(HE-J0)`

More generally, w is anticomplete to every neighbour of a other than z_a and to every neighbour of b other than z_b whenever that vertex is also a candidate common neighbour in `(HE-W)`.

In particular, if e is K-heavy then e is adjacent to both a and b, and therefore

> **every W-heavy escape is nonadjacent to every K-heavy escape.** `(HE-KW0)`

Thus the saturated cheap reservoir is not an arbitrary partition: its two heavy sides are physically anticomplete across the partition.

## 4. New located nonedge prices

Let `r_K` and `r_W` be the numbers of K-heavy and W-heavy escapes.

From `(HE-Y0)`, the W-heavy side contributes

> **at least `y r_W` additional Y--U nonedges**            `(HE-ZY)`

beyond the already-known `y k=2y` nonedges from the selected witnesses W_s. Hence, at the level of the rooted physical nonedge ledger,

> `Z_Y >= y(2+r_W)`.                                     `(HE-ZY2)`

From `(HE-KW0)`, the two heavy sides contribute

> **`r_K r_W` missing U--U pairs.**                       `(HE-U0)`

This is especially relevant to the rooted triangle count Q/e(U) ledger: a genuinely mixed one-sided partition loses a quadratic block of possible U-edges.

These are located physical obstructions and should not be collapsed into total score before the rooted residual ledger is applied.

## 5. Strategic consequence

The one-sided degree-conservation endpoint now splits into three regimes:

1. both heavy types occur in linear number: `(HE-U0)` creates a quadratic missing U--U block, while W-heavy vertices also pay `y r_W` Y--U holes;
2. the reservoir is predominantly W-heavy: `(HE-Y0)` gives a large Y--U defect;
3. the reservoir is predominantly K-heavy: the predecessor J2-clean theorem applies to every K-serving escape, so the most permissive remaining endpoint must also drive `J2` small, ultimately toward an all-radius-one matched layer.

Thus the next live endpoint is the **predominantly K-heavy, J2-small (especially J2=0) geometry**. This is substantially narrower than the scalar k=2 ray. The next raw-criticality attack should retain the all-radius-one matched heads and a K-heavy escape adjacent to both same-code C-heads while anticomplete to W_s.