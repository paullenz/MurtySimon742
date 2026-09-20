# Maximal outside-witness selection and the true m=1 residue

Date: 2026-09-20

Status: internal conditional selection theorem inside the audited first-strict unloaded branch. This is a statement about freedom to choose valid representatives, not a raw-witness uniqueness claim.

## 1. Every outside vertex is an available buffer-edge certificate

`BUFFER_UO_REVERSE_FAN.md` proves that for every physical `w in U_o` there exists `x_w in X'=X\{a_0}` such that

`bw in E`, `wx_w notin E`, and `N(w) cap N(x_w)={b}`.

Therefore w is itself a valid outside-U certificate for the buffer edge `b x_w`.

This is important because the parameter m in the funnel package counts **selected physical outside witnesses** after choosing one valid certificate for each buffer--X edge. The selected representatives are not graph-invariant, and the audited P2 statement is selected-representative uniqueness rather than raw-witness uniqueness. We are therefore free to choose a representative system that maximizes the number of distinct physical outside witnesses.

Call such a choice a **maximal-witness selection**.

## 2. Any one-witness all-F graph with a second outside vertex admits m>=2

Assume the graph is in the one-witness all-F polarization for some initial selection, with selected witness z. Then z certifies every edge `bx`, `x in X'`, and `|X'|=x-1>=2`.

Suppose `u_o=|U_o|>=2`, and choose `w in U_o\{z}`. By the reverse-fan theorem, w certifies at least one edge `b x_w`.

Choose w as the representative for `b x_w`. Since `|X'|>=2`, choose a different head `x'!=x_w` and retain z as its representative (and, if desired, for all remaining heads). The resulting valid representative system uses at least the two distinct physical outside witnesses w and z.

Hence any graph with `u_o>=2` admits a valid selection with

> `m>=2`.                                                `(MAX-M2)`

The re-selection stays on the same physical graph. In the all-F geometry, `BUFFER_UO_REVERSE_FAN.md` gives every outside vertex code `bar C`, while `ALL_F_OUTSIDE_LAYER_COLLAPSE.md` gives `wa_0` a nonedge, so the newly selected witness is still a valid Type-F representative.

## 3. Canonical consequence

From now on, whenever the funnel machinery is invoked, choose a maximal-witness representative system before splitting by m. Then

> `m=1  =>  |U_o|=1`.                                   `(MAX-M1)`

Since `|U_o|=u-k-1=T+1`, the true one-witness branch under maximal selection satisfies

> `T=0`, `u=k+2`.                                       `(MAX-T0)`

Thus there is **no positive-T one-witness all-F tail at graph level**. Any graph previously represented by the algebraic m=1 all-F formulas with `T>=1` must be reclassified into the `m>=2` selected branch.

This does not invalidate the old all-F residual algebra: it remains correct conditional mathematics for a non-maximal representative choice. It does change the efficient graph-level partition and removes that noncanonical T-tail from the live m=1 realizability branch.

## 4. Evidence boundary

This theorem uses only representative freedom explicitly allowed by the audited selected-system semantics. It does not assert raw witness uniqueness and does not identify different physical witnesses. It should therefore be checked in the next adversarial audit specifically against the selection conventions used by the downstream Hall/source-tuple machinery; until then it is an internal structural simplification, not a publication-grade normalization.

## 5. Next consequence

Under maximal selection the surviving `m=1` branch has a single outside vertex z. Together with all-F isolation,

- `U=W_0 dotcup {b,z}`;
- `G[U_-]` is empty;
- `zW_0` is empty;
- `bz` is the only U-edge, hence `q=1` exactly;
- for `y>=2`, head saturation still gives `g in {0,1}`.

The correct next target is this literal `T=0`, `q=1` one-witness geometry; every graph with a larger outside layer belongs to the now-live `m>=2` branch instead.
