# n=29, Delta=16: actual graph to corrected late-LP embedding

11 September 2026. Research directed by Paul Lenz; independent reconstruction and hostile audit by ChatGPT/Geeps.

**Status: candidate mathematical audit.** This note reconstructs the map from an actual selected/residual graph configuration to every variable and every constraint in the corrected grouped late model `independent_threshold_model_v2.py`. The derivation was made from the graph-level quantities first and then compared with the production source. It does not treat the production code as a premise. Independent human review remains open.

## 1. Input supplied by the graph bridge

For the n=29, Delta=16 case we have

```text
|A|=a=12,
|B|=b=16.
```

For labels `i in A` write

```text
d_i = F-degree,
R_i = residual cross-degree,
x_i = selected cross-degree,
s_i = max(0,d_i-R_i).
```

For sources `u in B` write

```text
rho_u = residual cross-degree,
q_u   = selected source degree,
p_u   = selected supplement degree.
```

The selected cross-edges form a simple incidence relation between B and A. The selected missing-B-pairs form an oriented simple relation `u -> w`: every missing unordered B-pair is oriented at most once, and one selected A-B incidence is associated with every outgoing selected pair.

The bridge supplies the local conditions used by the late model:

```text
q_u + rho_u <= 12,
p_u <= rho_u+3,
q_u+p_u <= 15,

for every selected incidence ui:
  s_i <= rho_u,
  d_i <= rho_u+R_i,
  d_i <= rho_u+q_u-1,
  R_i+x_i >= q_u+p_u,

for every selected oriented B-pair u->w:
  rho_w+q_w >= q_u-1.
```

It also supplies

```text
sum_i d_i = 2(r+t),
sum_i R_i = r = sum_u rho_u,
0<=d_i<=10,
0<=R_i<=16,
x_i<=16-R_i.
```

The question addressed here is purely this:

> Given an actual finite configuration satisfying those statements, does it necessarily define a feasible point of the corrected grouped LP?

The answer below is yes.

## 2. Group notation

Partition labels by demand. For each distinct demand value `s_g`, let

```text
G_g = {i in A : s_i=s_g},
n_g = |G_g|.
```

Partition sources by residual degree. For each distinct residual degree `rho_k`, let

```text
K_k = {u in B : rho_u=rho_k},
n_k = |K_k|.
```

The code orders these groups by the numerical value of `s_g` and `rho_k`. That ordering has no mathematical content.

## 3. Label variables Y and T

For a demand group g define

```text
Y(g,d,R)
 = #{i in G_g : (d_i,R_i)=(d,R)} / n_g.
```

For `1<=h<=16-R`, define

```text
T(g,d,R,h)
 = #{i in G_g : (d_i,R_i)=(d,R), x_i>=h} / n_g.
```

Thus Y and T are **fractions within one demand group**. In particular T is not multiplied by `n_g` when it is later interpreted on the label side.

Immediately:

```text
sum_{d,R} Y(g,d,R)=1,
0<=T_h<=T_{h-1}<=Y.
```

Because every label has `x_i>=s_i`, for every `h<=s_g`,

```text
T(g,d,R,h)=Y(g,d,R).
```

The option filter in the production model is exact for an actual label:

- if `s_g>0`, then `d-R=s_g`;
- if `s_g=0`, then `d<=R`;
- `x_i>=s_g` and `x_i<=16-R`, so `16-R>=s_g`.

The global moment identities are

```text
sum_g n_g sum_{d,R} d Y(g,d,R) = sum_i d_i = 2(r+t),
sum_g n_g sum_{d,R} R Y(g,d,R) = sum_i R_i = r.
```

These are exactly the two Y-moment equalities in v2.

## 4. Source variables W

For a residual group k define

```text
W(k,q,p)
 = #{u in K_k : (q_u,p_u)=(q,p)} / n_k.
```

Hence

```text
sum_{q,p} W(k,q,p)=1.
```

The production type domain

```text
0<=q<=12-rho_k,
0<=p<=min(rho_k+3,15-q)
```

is exactly implied by the graph bridge, so every actual source type appears in the model.

## 5. Oriented B-pair density P

For source group k and supplement group l define

```text
P(k,l,q,q2)
 = N(k,l,q,q2) / [ n_k (n_l-delta_kl) ],
```

where `N(k,l,q,q2)` is the number of selected oriented B-pairs `u->w` satisfying

```text
u in K_k, q_u=q,
w in K_l, q_w=q2.
```

This is a density among possible **ordered distinct** source/supplement vertex pairs.

An actual arc exists only when

```text
rho_l+q2 >= q-1,
```

by supplement forcing. Therefore the production model loses no actual arc when it omits incompatible P variables.

### 5.1 Outgoing balance

The number of outgoing selected B-pairs from sources in K_k with q-degree q is

```text
q * #{u in K_k:q_u=q}.
```

Divide by n_k. The left side becomes

```text
q * sum_p W(k,q,p).
```

For target group l, multiplying P by `n_l-delta_kl` converts its ordered-pair density into outgoing arcs per source in K_k. Hence

```text
q sum_p W(k,q,p)
 = sum_l (n_l-delta_kl) sum_q2 P(k,l,q,q2).
```

This is the production outgoing P equality.

### 5.2 Incoming balance

Similarly, selected supplement indegree into targets in K_l of q-degree q2 is

```text
sum_p p W(l,q2,p).
```

Counting the same arcs by source residual group gives

```text
sum_p p W(l,q2,p)
 = sum_k (n_k-delta_kl) sum_q P(k,l,q,q2).
```

This is the production incoming P equality.

### 5.3 Unordered-pair capacity

For `k!=l`, there are exactly `n_k n_l` unordered cross-group vertex pairs. At most one orientation of each can be selected, so

```text
sum_{q,q2}[P(k,l,q,q2)+P(l,k,q2,q)] <= 1.
```

For `k=l`, the exact bound under the chosen ordered-pair normalization is actually

```text
sum_{q,q2} P(k,k,q,q2) <= 1/2.
```

The production model uses only `<=1`. This is deliberately weaker and therefore safe: it may admit fictitious LP states, but it cannot exclude an actual graph.

## 6. Selected source-label density Z

For residual group k, demand group g and exact source/label types define

```text
Z(k,g,q,p,d,R)
 = M(k,g,q,p,d,R) / (n_k n_g),
```

where M counts selected A-B incidences `ui` with

```text
u in K_k, (q_u,p_u)=(q,p),
i in G_g, (d_i,R_i)=(d,R).
```

Thus Z is a density among all possible source/label vertex pairs between those two groups.

An actual selected incidence satisfies

```text
s_g <= rho_k,
d <= rho_k+R,
d <= rho_k+q-1.
```

Also endpoint load gives

```text
x_i >= q+p-R.
```

Since a selected incidence itself gives `x_i>=1`, set

```text
req=max(1,q+p-R).
```

Then every actual incidence satisfies

```text
req <= x_i <= 16-R.
```

These are exactly the compatibility filters used before v2 creates a Z variable.

## 7. Source-side Z equations

Fix source type `(k,q,p)`. The number of selected A-B incidences from actual sources of that type is

```text
q * #{u in K_k:(q_u,p_u)=(q,p)}.
```

Divide by n_k:

```text
q W(k,q,p).
```

For one demand group g, multiplying Z by n_g converts source-label pair density into selected incidences per source in K_k. Therefore

```text
q W(k,q,p)
 = sum_g n_g sum_{d,R} Z(k,g,q,p,d,R).
```

This is exactly the production source selected-degree equality.

For each fixed demand group g, simplicity of the A-B graph gives at most one selected edge for each source/label pair. Hence

```text
sum_{d,R} Z(k,g,q,p,d,R) <= W(k,q,p).
```

This is the production per-demand-group source capacity inequality. It is genuinely necessary, not a heuristic strengthening.

## 8. Label-side Z/T identity: the normalization checkpoint

Fix `(g,d,R)`. Count selected incidences at labels of this subtype.

From Z, multiplying by n_k and summing source groups gives

```text
sum_k n_k sum_{q,p} Z(k,g,q,p,d,R)
 = [sum_{i in G_g, (d_i,R_i)=(d,R)} x_i] / n_g.
```

From the T tails, the elementary identity

```text
x_i = sum_{h=1}^{16-R} 1[x_i>=h]
```

gives

```text
sum_h T(g,d,R,h)
 = [sum_{i in G_g, (d_i,R_i)=(d,R)} x_i] / n_g.
```

Therefore the correct equality is

```text
sum_k n_k sum_{q,p} Z(k,g,q,p,d,R)
 = sum_h T(g,d,R,h).                       (8.1)
```

There is **no additional factor n_g on the T side**.

This is exactly the correction made in `independent_threshold_model_v2.py`. The quarantined v1 multiplied the T side by `n_g`, which is why its certificates are invalid.

## 9. Nested endpoint-load capacity

Again fix `(g,d,R)` and an integer threshold h.

Consider selected incidences whose source type requires

```text
req=max(1,q+p-R) >= h.
```

Every such incidence ends at a label with `x_i>=req>=h`. A label i can host at most its actual `x_i` selected incidences. Hence the number of these high-requirement incidences, divided by n_g, is at most

```text
E[x_i 1[x_i>=h] 1[(d_i,R_i)=(d,R)]].
```

For integer x,

```text
x 1[x>=h]
 = (h-1)1[x>=h] + sum_{j=h}^{U} 1[x>=j],
```

where `U=16-R`. Averaging within the demand group gives

```text
E[x 1[x>=h] 1[subtype]]
 = (h-1)T_h + sum_{j=h}^{U} T_j.
```

The high-requirement incidence density is

```text
sum_{k,q,p:req>=h} n_k Z(k,g,q,p,d,R).
```

Therefore the necessary inequality is

```text
sum_{k,q,p:req>=h} n_k Z
 <= (h-1)T_h + sum_{j=h}^{U}T_j.          (9.1)
```

This is exactly the nested capacity row in v2, including its direction and its multiplicities.

## 10. Variable upper bounds

Every production variable is an actual fraction or pair density:

- `0<=Y,T,W<=1` by definition;
- `0<=Z<=1` because it counts a subset of `n_k n_g` possible simple source-label pairs;
- `0<=P<=1` because it counts a subset of `n_k(n_l-delta_kl)` possible ordered distinct source/target pairs.

Therefore the generic production inequalities `variable<=1` are safe for every actual graph.

## 11. What the model deliberately forgets

The late LP is a relaxation. Among other things, it does not retain:

- full arcwise coupling between P and Z;
- the exact source supplement p-type on P arcs;
- every `d_i<=rho_u+rho_w` correlation at the Z level;
- the exact same-group P capacity `<=1/2`;
- all possible label-side simple-pair capacities such as subtype-specific `Z<=Y`.

Each omission **enlarges** the LP feasible set. These losses can create false LP survivors, but they cannot make an actual graph infeasible. This direction is important: no omitted coupling found in this audit is being used as an unjustified strengthening.

## 12. Exact Farkas endpoint

The production verifier treats every LP variable as nonnegative and every stored inequality as

```text
A_j x <= b_j.
```

A saved certificate uses

```text
lambda_j >=0 on inequalities,
mu_k arbitrary integer on equalities.
```

The exact checker recombines them to obtain

```text
c = sum_j lambda_j A_j + sum_k mu_k E_k,
R = sum_j lambda_j b_j + sum_k mu_k f_k.
```

It accepts only if

```text
c_i>=0 for every variable i,
R<0.
```

For a feasible nonnegative x we would then have simultaneously

```text
c.x >=0
```

and, from the weighted LP rows,

```text
c.x <=R<0,
```

which is impossible. Thus the exact-certificate semantics are sound once the LP embedding above is accepted. Floating-point solver output is used only to propose multipliers.

## 13. Executable normalization regression

`microstate_embedding_audit.py` independently constructs explicit finite selected/residual microstates and maps them into Y/T/W/P/Z using `fractions.Fraction`. It then evaluates **every row of the production model exactly**.

The first clean run produced:

```text
uniform fixture:
  corrected v2: 735 variables, 113 equalities, 1038 inequalities, 0 violations
  quarantined v1: 2 exact equality failures

mixed fixture:
  corrected v2: 14879 variables, 336 equalities, 16958 inequalities, 0 violations
  quarantined v1: 3 exact equality failures
```

The mixed fixture contains two demand groups and two residual-degree groups, so it exercises the group-multiplicity bookkeeping directly. The same assignments deliberately fail against v1. This is important evidence that the regression is sensitive to the historical bug rather than merely reproducing a tautological PASS.

The machine receipt is `MICROSTATE_AUDIT_REPORT.json`.

The fixtures have negative synthetic surplus values. This does **not** test positive-surplus graph existence, residual activity or the earlier bridge. It tests the late averaging map only. The sign of t enters the late model solely through the exact global d-moment equality, which the fixtures satisfy. The proof of the embedding above is symbolic and does not depend on the sign of t.

## 14. Audit verdict

No blocking defect was found in the actual-graph-to-corrected-late-LP embedding.

In particular, this audit found no:

- hidden second label-group multiplicity;
- reversed source/label normalization;
- unsafe same-group P capacity;
- wrong endpoint-tail identity;
- inequality-direction error in the nested capacity;
- solver-status-as-proof dependency;
- exact Farkas sign error.

The principal remaining risk in this layer is no longer an unidentified dimensional ambiguity: the variable meanings and all production rows now have an explicit graph-level derivation plus an executable exact regression. This remains same-project/same-assistant evidence, not independent expert verification.
