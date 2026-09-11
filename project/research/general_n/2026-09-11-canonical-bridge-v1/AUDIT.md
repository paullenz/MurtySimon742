# Hostile audit of the canonical selected/residual bridge

11 September 2026. Research directed by Paul Lenz; hostile re-derivation by ChatGPT/Geeps.

**Verdict: PASS as candidate mathematics. No blocking defect found.** This is an internal same-assistant audit, not independent peer review. The purpose was to rederive the dangerous implications without treating `CANONICAL_BRIDGE.md` as authoritative and to look specifically for orientation mistakes, injection collisions, hidden selected/residual overlap, inequality reversals, and parameter-specialisation errors.

## 1. Audit method

The following steps were reconstructed independently from the diameter-two-critical definition and complement notation:

1. edge deletion in `G` -> edge addition in `H` -> new adjacent total-dominating pair;
2. existence and orientation of one cross quasi-edge for each missing unordered `B`-pair;
3. selected-edge injectivity and unique-B-exception semantics;
4. the exact edge ledger;
5. every selected-edge residual injection;
6. endpoint-load counting;
7. residual activity for `t>0`;
8. charging and denominator safety;
9. threshold-capacity counting;
10. isolated-`C` residual families;
11. residual h-index;
12. fixed-order parameter specialisations used at `n=28,29,30`.

The late LP is not part of this audit; that interface is separately reconstructed and tested in the n=29 and n=30 late-LP embedding audits.

## 2. Complement / total-domination step — PASS

Let `uw` be an edge of G. In `G-uw` choose `x,y` with distance greater than two. They cannot be adjacent in `G-uw`, so they are adjacent in `H+uw`. They have no common neighbour in `G-uw`; equivalently every vertex belongs to the open neighbourhood of x or y in `H+uw`. Thus `{x,y}` is an adjacent total-dominating pair.

Such a pair cannot already have existed in H: adjacent total domination in H would mean a nonadjacent G-pair with no common G-neighbour, contradicting `diam(G)=2`.

Only the neighbourhoods of u and w change when `uw` is added to H. Hence a newly total-dominating adjacent pair must contain u or w.

For a missing pair `u,w in B`, the pair cannot be `{u,w}` because both miss v. If the new pair is `{u,i}`, it must dominate v; u misses v, so `iv in E(H)` and `i in A`. Therefore

```text
N_H(u) union N_H(i) = V(H) \ {w}.
```

No omitted case was found.

## 3. One representative per missing unordered B-pair — PASS

A cross-edge `ui` satisfying the displayed quasi-edge relation has a fixed source u and a unique exception w determined by the set `V(H)\(N(u) union N(i))`. Therefore one cross-edge cannot represent two different missing B-pairs. Choosing one orientation/representative for each missing **unordered** B-pair is well-defined and injective.

At a fixed source u, distinct selected labels have distinct exceptions, because two selected edges with the same exception would represent the same missing unordered pair `{u,w}` twice.

The orientation convention is used consistently downstream.

## 4. Exact ledger — PASS

Selected representatives and existing edges of `H[B]` partition `C(b,2)`. Re-expanding

```text
e(H)=a+e(C)+r+#selected+e(H[B])
```

and using `e(H)=C(n,2)-m`, `n=a+b+1`, `m=b(a+1)+t` gives exactly

```text
e(C)+r=C(a,2)-t,
e(F)=r+t,
sum_i d_i=2(r+t).
```

No sign or off-by-one error was found.

## 5. Demand — PASS

Minimum H-degree gives

```text
1+(a-1-d_i)+R_i+x_i >= a,
```

hence `x_i>=d_i-R_i`, so `x_i>=s_i=max(0,d_i-R_i)`. Summing `s_i>=d_i-R_i` yields

```text
S>=2(r+t)-r=r+2t.
```

A demand `s_i` therefore uses at least `s_i` distinct selected A-B incidences and hence distinct B-sources because H is simple.

## 6. Pointwise selected-edge forcing — PASS

Fix `ui->w` and an F-neighbour j of i.

### 6.1 `d_i<=rho_u+R_i`

Because j is not the B-exception w, `uj` is an H-edge. If residual, charge to rho_u. If selected, write `uj->z`. The exception z differs from w. Since `ui->w` must dominate z and `uz` is missing, `iz` is an H-edge.

It is residual: `ij` is absent and `jz` is absent because z is the unique exception of `uj->z`; therefore endpoints i,z jointly miss the A-vertex j. A selected A-B edge has its unique exception in B and must dominate every A-vertex.

Distinct selected j at source u have distinct exceptions z, so the forced `iz` edges are distinct. This proves

```text
d_i<=rho_u+R_i,
s_i<=rho_u
```

at a selected incidence.

### 6.2 `d_i<=rho_u+rho_w`

In the selected `uj->z` case, `{u,j}` must dominate w because `z!=w`. Since `uw` is missing, `jw` is an H-edge. It is residual because j and w jointly miss i (`ij` and `iw` are absent). Distinct j give distinct edges at w. Hence

```text
d_i<=rho_u+rho_w.
```

### 6.3 `d_i<=rho_u+q_u-1`

All F-neighbours j are A-neighbours of u. Source u has `rho_u+q_u` A-neighbours total, one being i. Hence the inequality follows directly.

### 6.4 Supplement forcing

Every other selected `uj->z` at u has `z!=w`; therefore `{u,j}` dominates w, so `jw` is an H-edge. The `q_u-1` other selected labels are distinct A-neighbours of w and are partitioned into residual and selected edges from w:

```text
rho_w+q_w>=q_u-1.
```

No injection collision was found in any of these four steps.

## 7. Source capacities — PASS

Every missing unordered B-pair incident with u is oriented exactly once, so

```text
q_u+p_u = missing degree of u in H[B].
```

Hence

```text
d_H(u)=rho_u+q_u+(b-1-q_u-p_u)=rho_u+b-1-p_u.
```

Minimum H-degree gives

```text
p_u<=rho_u+b-a-1.
```

Also `q_u+p_u<=b-1` and `q_u+rho_u<=a` are immediate capacities. A negative right side in the p-bound simply means the corresponding parameter state is impossible; it is not an algebraic reversal.

## 8. Endpoint load — PASS

For selected `ui->w`, label i is adjacent to:

- source u;
- each supplement z of another selected edge `uj->z` from u, because `ui->w` must dominate z and `uz` is missing;
- each source y of a selected pair `y->u`, because y differs from w and `ui->w` must dominate y while `uy` is missing.

The outgoing-supplement and incoming-source families cannot collide: a collision z=y would orient the same missing unordered pair `{u,z}` both `u->z` and `z->u`. Thus

```text
R_i+x_i>=q_u+p_u.
```

## 9. Residual activity for `t>0` — PASS, high-priority external target

Assume `rho_u=0`. Put `U=N_A(u)` and `T=A\U`. Every cross-edge at u is selected.

There is no F-edge between U and T: for `i in U`, selected `ui` must dominate every A-vertex; if `ij in F` with `j in T`, this forces `uj`, contradiction.

### 9.1 F[U] family

For `ij in F[U]`, write selected edges `ui->w_i`, `uj->w_j`. Their exceptions are distinct. The selected pair `{u,j}` must dominate `w_i`, giving residual `jw_i`; symmetrically `iw_j` is residual.

Residual status is forced because `jw_i` has endpoints jointly missing i, and `iw_j` has endpoints jointly missing j.

The injection is on **ordered F-edge endpoints**. With u fixed, an exception `w_i` determines its selected label i, so a residual edge `jw_i` recovers the ordered endpoint pair `(i,j)`. Thus the family has exactly `2e(F[U])` distinct residual edges.

### 9.2 F[T] family

For `ij in F[T]`, adding ij creates a new adjacent total-dominating pair using i or j. It cannot be `{i,j}` because both miss u. The auxiliary cannot be u because neither endpoint is adjacent to u. It cannot be v: v already neighbours the other endpoint, so adding ij cannot newly repair `{i,v}` or `{j,v}`.

If an auxiliary z lay in A, domination of u would force `z in U`. The unique exception is the opposite endpoint in T, so z would miss that T-vertex, creating an F(U,T) edge, impossible. Hence the auxiliary lies in B.

The resulting cross quasi-edge has its unique exception in A, so it cannot be one of the selected representatives, whose exception lies in B. It is residual. The cross-edge plus its unique A-exception recovers the original F[T]-edge, so this is injective. Its A-endpoint lies in T, making it disjoint from the F[U] family.

Therefore

```text
r>=2e(F[U])+e(F[T])>=e(F)=r+t,
```

contradicting `t>0`.

This proof survived the audit, but remains one of the highest-value points for independent human review because several downstream inequalities use `rho_u>=1`.

## 10. Charging — PASS

Choose `s_i` selected incidences at each label. A chosen source satisfies `rho_u>=s_i`. Also `q_u<=a-rho_u`. Because a chosen source has `q_u>=1`, `rho_u<=a-1`, so the denominator in

```text
(rho_u-1)/(a-rho_u)
```

is strictly positive.

A source contributes to at most `a-rho_u` chosen incidences, so its total charge is at most `rho_u-1`. Residual activity makes that budget nonnegative. The charge function is increasing on `1<=rho<a`, giving

```text
r-b>=sum_i s_i(s_i-1)/(a-s_i).
```

Combining with `S>=r+2t` gives the displayed demand inequality. Zero demands contribute zero and cause no denominator problem.

## 11. Threshold capacity — PASS

For heavy labels `s_i>=h`, chosen incidences use only sources with `rho_u>=h`.

Let `ell_u` be the number of heavy actual selected incidences from u and let `J={u:ell_u>h}`. For `u in J` and heavy `ui->w`, every other heavy selected label k at u forces `kw`.

If none of these edges is selected from w, at least h are residual and `rho_w>=h`. If one is selected from w, its heavy label k has `s_k>=h`, and the selected-source demand inequality gives `rho_w>=s_k>=h`. Hence every supplement of a heavy edge from J lies in Z_h.

Selected-pair injectivity bounds heavy arcs from J by unordered pairs in Z_h incident with J:

```text
j(z_h-j)+C(j,2)=j z_h-j(j+1)/2.
```

Other Z_h sources contribute at most h. Thus

```text
W_h<=(z_h-j)h+jz_h-j(j+1)/2.
```

Writing `q=z_h-h`, the desired target exceeds this right side by

```text
(q-j)(q-j-1)/2>=0
```

for every integer q-j, including negative integers. Therefore

```text
2W_h<=z_h^2-z_h+h(h+1).
```

No sign reversal remains after the 11 September proof-text correction.

## 12. Isolated-C lemma — PASS, high-priority external target

Let x be isolated in C and X=A\{x}. From the exact ledger the number of missing H-pairs inside X is

```text
P0=r-(a-1-t).
```

Every such missing pair ij produces a cross quasi-edge with auxiliary in B and unique exception in A. The auxiliary cannot be v because v already covers the opposite endpoint; it cannot lie in A because x would remain undominated (and z=x is not adjacent to i). Thus the edge is cross, and because its exception lies in A it is residual. Distinct missing X-pairs give distinct residual cross-edges. Call the family P.

Let Z be the B-endpoints used by P. For used z, a member `iz->j` of P forces `xz`: `{i,z}` must dominate x. The edge xz is residual because x and z jointly miss j. These edges are outside P because their A-endpoint is x.

For unused `z in B\Z`, residual activity supplies some residual edge at z, automatically outside P. Different B-endpoints give distinct edges, and used/unused families are disjoint. Hence there are at least b residual edges outside P:

```text
r>=|P|+b,
```

giving

```text
b<=a-1-t.
```

No accidental double count was found.

## 13. Residual h-index — PASS

Let h be the residual h-index. A label demanding s selected sources needs s distinct sources of residual degree at least s, so `s_i<=h` and `S<=ah`.

Residual activity supplies baseline degree one to every B-source. At least h sources have degree at least h, hence

```text
r>=h^2+(b-h)=b+h(h-1).
```

Together with `S>=r+2t` this gives

```text
b+2t<=(a+1)h-h^2<=floor((a+1)^2/4).
```

## 14. Fixed-order specialisations — PASS

### n=29, Delta=16

```text
a=12,b=16,
p_u<=rho_u+3.
```

The isolated-C conclusion would require

```text
16<=11-t,
```

impossible for positive t. Therefore `delta(C)>=1`, `d_i<=10`, and

```text
r<=C(12,2)-t-ceil(12/2)=60-t.
```

This matches the reviewer-v3 bridge.

### n=30, Delta=16

```text
a=13,b=16,
p_u<=rho_u+2.
```

Isolated C would require

```text
16<=12-t,
```

impossible for positive t. Thus `delta(C)>=1`, `d_i<=11`, and

```text
r<=C(13,2)-t-ceil(13/2)=71-t.
```

Hence t=1 gives r<=70 and t=2 gives r<=69, matching the n=30 implementation.

### n=28, Delta=15

```text
a=12,b=15,
```

and the same isolated-C argument applies throughout positive surplus. The later pointwise charging cap is a corollary of the canonical charging inequality, not an additional graph-theoretic assumption.

## 15. Interaction with the late LP audits

The canonical bridge ends before the grouped late LP. Two separate executable audits now cover that interface:

- n=29 corrected production model: exact graph-level microstate averaging satisfies every v2 LP row; the same assignments detect the quarantined v1 multiplicity bug.
- n=30 separately written production model: the same independently derived Y/T/W/P/Z meanings satisfy every production LP row under exact rational evaluation.

Thus the current common trust boundary is split cleanly into:

```text
canonical graph bridge
 -> explicit graph-to-grouped-LP embedding
 -> exact finite LP/Farkas endpoint.
```

No blocking defect was found in either of the first two layers during the 11 September audits.

## 16. Remaining review priorities

The audit does **not** promote the bridge to externally established mathematics. The highest-value external targets remain:

1. Section 2 complement/total-domination conversion;
2. Section 6 selected/residual injections;
3. Section 9 residual activity;
4. Section 11 threshold capacity;
5. Section 12 isolated-C;
6. the separate actual-graph-to-averaged-LP embedding.

A valid counterexample to any one of these universal steps invalidates every dependent route regardless of computational replay status.
