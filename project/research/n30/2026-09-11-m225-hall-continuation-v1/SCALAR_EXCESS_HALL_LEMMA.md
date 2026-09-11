# A scalar selected-excess / supplement-Hall test

11 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status: candidate analytic reduction with REPRODUCED exact arithmetic. No governed theorem-ledger promotion or independent specialist review is claimed.**

This note continues the saved N30 equality-branch work from repository commit `b104846d222f09cb0d8bbf25ff9f51f6d1165bdf`. It gives a parameterised scalar test and seven explicit instances excluding 57 of the 207 positive ledger-tight rows at `(n,Delta,m)=(30,16,225)`. The 100-profile input remains a finite dependency. The remaining 150 positive rows continue to require the stronger preserved methods. This is not a full hand proof of the equality branch.

## 1. Precisely which bridge facts are used

Use the established complement/selected/residual construction. There are `a` labels and `b` sources. Let `kappa=b-a>=1`. For label `i`, let `d_i,R_i,x_i` be its F-degree, residual degree and selected degree, and let `s_i=max(0,d_i-R_i)`. At a source `u`, write `rho_u,q_u,p_u` for residual degree, selected outdegree and selected indegree as a supplement.

Assume positive surplus, residual activity `rho_u>=1`, and **ledger tightness**

```text
S=sum_i s_i = sum_i(d_i-R_i) = r+2t.
```

Then `d_i=R_i+s_i` for every label, including a zero-demand label: equality between the sum of positive parts and the original sum forces every summand to be nonnegative. Also `x_i>=s_i`. Put

```text
e_i=x_i-s_i>=0,
M=sum_i x_i=sum_u q_u,
E=sum_i e_i=M-S.
```

The following bridge implications hold for a selected incidence `ui->w`:

```text
s_i <= rho_u,
d_i <= rho_u+q_u-1,
q_u+p_u <= R_i+x_i,
rho_w+q_w >= q_u-1.
```

These are the selected-incidence and supplement-forcing arguments in Sections 4--5 of the [frozen bridge](../../../reviews/n29/2026-09-11-reviewer-v3/GRAPH_TO_MODEL_BRIDGE.md), with `a,b` left as parameters. The degree identity needed for the source bound is

```text
deg_H(u)=(rho_u+q_u)+(b-1-q_u-p_u)
        =rho_u+b-1-p_u >= a,
```

so

```text
p_u <= rho_u+kappa-1.
```

The frozen bridge's displayed intermediate degree identity omitted `+q_u`; the resulting bound was nevertheless the correct one. The [source-degree erratum](../../../reviews/cross-cutting/2026-09-11-source-degree-erratum-v1/ERRATUM.md) records the exact correction without altering the frozen source.

Because selected labels at a source are distinct, the demand forcing improves the source domain to

```text
0 <= q_u <= Q_rho,
Q_rho = min(a-rho, #{i:s_i<=rho}).                 (1)
```

Together these imply `q_u+p_u<=b-1`; that constraint is redundant in the rectangular domain used below. In particular, the correct N30 bound is `p_u<=rho_u+2`. The rejected tightening to `rho_u+1` is not used.

## 2. An upper bound from selected excess

Substitute `d_i=R_i+s_i` and `x_i=s_i+e_i` in the incidence inequalities. They give

```text
q_u+p_u <= R_i+s_i+e_i <= rho_u+q_u-1+e_i,
```

hence `e_i>=p_u-rho_u+1`. Define

```text
alpha_u=max(0,p_u-rho_u+1),
0<=alpha_u<=kappa,
B0=sum_u q_u alpha_u,
c=max_i s_i+kappa.
```

Every selected incidence at label `i` has `alpha_u<=min(e_i,kappa)`. Therefore

```text
B0 <= sum_i x_i min(e_i,kappa)
   <= sum_i (s_i+kappa)e_i
   <= cE.                                           (2)
```

The middle inequality is elementary. If `e<=kappa`, it reduces to `(s+e)e<=(s+kappa)e`; if `e>=kappa`, it reduces to `kappa*s<=s*e`. It is valid also when `s=0` or `e=0`.

## 3. Supplement Hall tails

For each positive integer `j`, define

```text
H_j = sum_{u:q_u>=j+1} q_u
      - sum_{w:rho_w+q_w>=j} p_w.
```

Every selected arc from a source with `q_u>=j+1` lands at a supplement with `rho_w+q_w>=q_u-1>=j`. Its incoming capacity is counted by `p_w`, exactly once per selected arc. Thus

```text
H_j<=0.                                            (3)
```

This is a direct necessary counting inequality. No independence assumption between labels and sources, graph reconstruction, grouped LP normalization or fractional matching assertion is required here.

## 4. Three endpoints suffice for the pointwise source bound

Choose an integer `D>0` and finitely supported integers `z_j>=0`. Write

```text
Z(l)=sum_{1<=j<=l} z_j,
Z(l)=0 when l<=0.
```

At a source of residual degree `rho`, define

```text
F(rho,q,p)
 = D*q*(max(0,p-rho+1)-c)
   + q*Z(q-1) - p*Z(rho+q).                        (4)
```

For fixed `q`, the expression is linear on each of `0<=p<=rho-1` and `rho-1<=p<=rho+kappa-1`. Its minimum over the allowed integer interval is therefore attained at one of

```text
p=0, rho-1, rho+kappa-1.                            (5)
```

All three endpoints are admissible; (1) ensures `q+p<=b-1` even at the largest endpoint. At `rho=1` the first two coincide, which causes no problem. Consequently the exact pointwise minimum is the explicit one-variable expression

```text
L_rho = min_{0<=q<=Q_rho} [
    q*(Z(q-1)-D*c)
    + min(0,
          -(rho-1)*Z(rho+q),
          D*kappa*q-(rho+kappa-1)*Z(rho+q))
].                                                  (6)
```

At N30, `a=13,b=16,kappa=3`, so there are at most thirteen possible `q` values for any residual degree. Formula (6) replaces the old source/supplement transport optimization with a small explicit arithmetic expression.

Sum (4) over all sources. By (3) and nonnegativity of the weights,

```text
D*(B0-cM) + sum_j z_j H_j >= sum_rho n_rho L_rho,
D*(B0-cM) >= sum_rho n_rho L_rho,
D*(B0-cE) >= D*c*S + sum_rho n_rho L_rho,             (7)
```

where `n_rho` is the source multiplicity. This contradicts (2) whenever

```text
D*c*S + sum_rho n_rho L_rho > 0.                    (8)
```

Equations (1)--(8) prove the scalar test, conditional on the listed universal bridge facts. They apply beyond these 57 finite rows; no unrestricted coverage statement is implied.

## 5. Seven instances at m=225

Here `S=r+2`. Use the following fixed weights, with all unlisted `z_j=0`.

| Template | D | Nonzero integer weights | Assigned rows | Minimum gap after dividing by D |
|---|---:|---|---:|---:|
| T1 | 12 | z2=26, z3=11, z4=5, z5=9, z6=5, z7=3 | 30 | 5/12 |
| T2 | 24 | z2=38, z3=24, z4=10, z5=13, z6=9, z7=7, z8=5, z9=3 | 20 | 1/2 |
| T3 | 12 | z2=21, z3=12, z4=4, z5=10, z6=11, z7=1 | 3 | 5/12 |
| T4 | 24 | z2=75, z5=10, z6=9, z7=6, z8=5, z9=4 | 1 | 1/12 |
| T5 | 3 | z2=7, z3=3, z5=2, z6=1, z7=1, z8=1 | 1 | 1 |
| T6 | 6 | z2=14, z3=12, z6=1, z7=2 | 1 | 2/3 |
| T7 | 60 | z2=120, z3=56, z4=59, z6=26, z7=20, z8=16, z9=12 | 1 | 1/10 |

The assignments are disjoint and total 57. The complete [exact appendix](EXACT_APPENDIX.md) lists every demand/residual row, its source minima and its positive numerator. The [certificate file](SCALAR_CERTIFICATES.json) contains only explicit integer weights and the assigned profiles, rather than solver duals or optimizer states.

For example, T1 excludes

```text
s=(2,4^6,5^6), rho=(1^5,3,4^4,5^6), S=56, c=8.
```

Equation (6) gives `L1=0,L3=-270,L4=-457,L5=-533`. The numerator in (8) is

```text
12*8*56 -270 -4*457 -6*533 = 80 > 0.
```

So `B0-cE>=80/12>0`, contradicting the label inequality `B0-cE<=0`.

## 6. Audit, limitations and remaining frontier

The [acceptance checker](verify_scalar_certificates.py) imports no discovery script or historical verifier. It independently regenerates the 272 tail-slack rows from the preserved 100-profile input and checks the 211 tight rows. Every template is tested against every row before its total coverage is compared with the stated assignments. This avoids circular acceptance of an assignment list.

The checker uses only integer arithmetic and `fractions.Fraction`, and compares (6) with a separate full `(q,p)` evaluation. The saved [audit](EXACT_AUDIT.json) records 200,043 integer source-case evaluations, 143 label-algebra cases, seven valid templates and 57 distinct exclusions. Its minimum assigned gap is `1/12`.

This is a small explicit certificate family with a hand-derived validity argument. It is **not** a claim that the entire m225 endpoint has become computation-free. In particular:

- the exact completeness of the 100 `Q>=18` demand profiles remains an input;
- the universal graph-to-model lemmas still require independent mathematical review;
- 150 positive tight rows are not excluded by these seven formulas and remain in [the saved residual frontier](REMAINING_150_POSITIVE_ROWS.json);
- the four zero-demand rows retain their existing exact Hall/Farkas treatment;
- the existing fixed-order reviewer-v2 proof is preserved, and no governed ledger status is upgraded.

The discovery LP achieved positive exact reconstructed gaps on 57 rows, and nonpositive bounds on the other 154 tight rows. Those negative optimizer outputs are reconnaissance, not a proof that no better scalar formula exists. The seven-template count is a convenient cover, not a minimality theorem and not evidence for a universal `t+1` pattern.

The next analytic target is a shared inequality for the remaining 150 positive rows, using the residual-column budget and joint label/source information omitted by this scalar excess test. Simply adding further supplement-tail weights to the same relaxation has no demonstrated route through the surviving frontier.
