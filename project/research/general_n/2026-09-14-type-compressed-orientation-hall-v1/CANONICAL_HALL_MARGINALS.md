# Marginal optimality conditions for the canonical Hall witness

14 September 2026. **Candidate exact structural corollary for the directed target-capacity Hall relaxation. External mathematical review and novelty assessment remain OPEN.**

This note adds local optimality information to the canonical maximal minimum Hall witness `M+`. The existing staircase theory describes the shape of `M+`; the present result constrains how much target capacity is gained by crossing its boundary.

## 1. Setup

Let the complete type table consist of distinct types

```text
tau=(q_tau,c_tau,P_tau)
```

with multiplicities `n_tau`.

For a complete-type source set `S`, let

```text
y_sigma(S)
```

be the number of selected source copies numerically compatible with a fixed target copy of type `sigma`, after deleting its own source copy when `sigma in S`.

Thus the target-capacity term and Hall margin are

```text
H(S)=sum_sigma n_sigma min(P_sigma,y_sigma(S)),         (1)
F(S)=H(S)-sum_{tau in S} n_tau q_tau.                  (2)
```

Let

```text
m=min_S F(S),                                           (3)
```

and let `M+` be the union of all minimizers, equivalently the unique maximal minimizer.

## 2. Type-incidence increment

For types `tau,sigma`, let

```text
A_{tau,sigma}=1
```

when the numerical directed compatibility inequalities hold:

```text
q_tau<=c_sigma+1,
q_sigma<=c_tau.                                        (4)
```

In the canonical setting `A_{tau,tau}=1`.

Define

```text
k_{tau,sigma}
 = n_tau A_{tau,sigma} - 1_{tau=sigma}.                (5)
```

If `tau notin S`, adding the complete type class `tau` changes every target incoming count by exactly

```text
y_sigma(S union {tau})
 = y_sigma(S)+k_{tau,sigma}.                            (6)
```

If `tau in S`, removing it changes the count by exactly

```text
y_sigma(S \ {tau})
 = y_sigma(S)-k_{tau,sigma}.                            (7)
```

For `sigma=tau`, the increment/decrement is `n_tau-1`, correctly accounting for deleted self-arcs.

## 3. Addition gain outside the canonical witness

For `tau notin M+`, define the target-capacity gain

```text
G^+_tau
 = H(M+ union {tau})-H(M+)
 = sum_sigma n_sigma [
     min(P_sigma,y_sigma+k_{tau,sigma})
     -min(P_sigma,y_sigma)
   ],                                                   (8)
```

where `y_sigma=y_sigma(M+)`.

Because `M+` is a minimizer,

```text
F(M+ union {tau})>=m.                                  (9)
```

Equality is impossible: if it held, `M+ union {tau}` would be a minimizer strictly containing the union of all minimizers. Hall margins are integers, so

```text
F(M+ union {tau})>=m+1.                                (10)
```

Using (2) and (8):

> **Strict exterior marginal inequality.** Every type `tau notin M+` satisfies
>
> ```text
> G^+_tau >= n_tau q_tau + 1.                          (11)
> ```

Equivalently, if

```text
s_sigma=(P_sigma-y_sigma(M+))_+                        (12)
```

is the unsaturated target slack at the canonical witness, then

```text
sum_sigma n_sigma min(k_{tau,sigma},s_sigma)
 >= n_tau q_tau+1.                                     (13)
```

Thus every excluded type sees strictly more currently usable compatible receiver capacity than the demand carried by adding its complete class.

## 4. Removal loss inside the canonical witness

For `tau in M+`, define

```text
G^-_tau
 = H(M+)-H(M+ \ {tau})
 = sum_sigma n_sigma [
     min(P_sigma,y_sigma)
     -min(P_sigma,y_sigma-k_{tau,sigma})
   ].                                                   (14)
```

Minimality gives

```text
F(M+ \ {tau})>=m.                                      (15)
```

Therefore:

> **Interior marginal inequality.** Every type `tau in M+` satisfies
>
> ```text
> G^-_tau <= n_tau q_tau.                              (16)
> ```

Let `M-` be the intersection of all minimizers. If `tau in M-`, removing `tau` cannot leave another minimizer, so integrality strengthens (16) to

```text
G^-_tau <= n_tau q_tau-1.                              (17)
```

## 5. Singleton exterior corollary

Suppose an exterior type has multiplicity

```text
n_tau=1.                                               (18)
```

Then `k_{tau,tau}=0`, and for every other target copy the addition contributes at most one unit. Equation (13) therefore says that there are at least

```text
q_tau+1                                                (19)
```

compatible target copies outside the forbidden diagonal which are still unsaturated at `M+`.

In particular its raw directed-compatible target degree satisfies

```text
d_D(tau)>=q_tau+1.                                     (20)
```

This is stronger than the ordinary singleton Hall requirement `d_D(tau)>=q_tau` and arises solely from maximality of the canonical minimizer.

For general multiplicity, since `G^+_tau` is at most the total number of labelled directed-compatible arcs leaving the `n_tau` source copies, (11) still implies

```text
e_D(tau,all targets)>=n_tau q_tau+1,                   (21)
```

and hence each symmetric source copy has directed-compatible degree at least `q_tau+1`.

## 6. Closure interpretation

The exterior inequality gives a useful fixed-point view of `M+`.

Starting from `M+`, no outside complete type can be added at zero or negative marginal Hall cost. Conversely, if a minimizer `S` is not maximal and an outside type can be added while preserving the minimum, repeated zero-marginal additions eventually reach `M+`.

Thus the canonical witness is simultaneously:

- a sharp-hardness up-set;
- a monotone generator staircase;
- the union of all minimum Hall cuts;
- a complete-type set with strictly positive one-type addition marginal everywhere outside its boundary.

The last property is new information not contained merely in the staircase ordering.

## 7. Research use

For a candidate Murty-Simon profile, the unsaturated slack field

```text
s_sigma=(P_sigma-y_sigma(M+))_+
```

must support every exterior type according to (13). Since compatibility is the interval-intersection relation

```text
[q_tau,c_tau] intersects [q_sigma,c_sigma+1],          (22)
```

(13) is an interval-capacity covering condition along the outside of the canonical staircase.

A promising next step is to combine these strict exterior requirements with the Murty-specific bounds

```text
q+rho<=a,
P<=b-1-q,
P<=rho+b-a-1,
```

and the residual budget `sum rho=r`. The aim is to show that a long or complicated canonical staircase would require more unsaturated receiver capacity than those budgets allow.

## 8. Trust boundary

These inequalities are exact consequences of the finite Hall margin and the canonical maximal-minimizer definition. Their Murty-Simon application inherits the target-capacity model and the upstream graph-to-constraint bridge.

They do not assert that target-flow feasibility implies graph realizability and do not prove the unrestricted Murty-Simon conjecture.
