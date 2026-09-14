# Layered receiver-capacity projection of orientation Hall

14 September 2026. **Candidate exact identity plus theorem-safe relaxation inside the directed target-capacity Hall system. External mathematical review and novelty assessment remain OPEN.**

The canonical staircase work identifies exact deficient Hall witnesses. This note projects the receiver side into one-dimensional capacity layers. The aim is to retain much of the Hall obstruction while replacing target-by-target correlation by monotone counting sequences that can be attacked with the Murty-Simon residual budget.

## 1. Exact layer-cake identity

Fix any complete-type source set `S`. For each labelled target copy `w`, let

```text
P_w = target capacity,
y_w = number of selected sources in S directed-compatible with w,
      after deleting the forbidden self source when w in S.          (1)
```

The exact Hall receiving capacity of `S` is

```text
H(S)=sum_w min(P_w,y_w).                                (2)
```

For every integer `k>=1`, define the two target layers

```text
A_k={w:P_w>=k},
B_k={w:y_w>=k}.                                         (3)
```

Since for nonnegative integers

```text
min(P_w,y_w)=sum_{k>=1} 1_{P_w>=k}1_{y_w>=k},          (4)
```

summing over targets gives the exact identity

> **Receiver layer identity.**
>
> ```text
> H(S)=sum_{k>=1}|A_k cap B_k|.                         (5)
> ```

Only finitely many terms are nonzero.

## 2. Comonotone marginal relaxation

Put

```text
alpha_k=|A_k|,
beta_k =|B_k|.                                         (6)
```

Then

```text
|A_k cap B_k|<=min(alpha_k,beta_k),                    (7)
```

so every source set satisfies

```text
H(S)<=U(S):=sum_{k>=1}min(alpha_k,beta_k).              (8)
```

Consequently:

> **Layered receiver exclusion.** If
>
> ```text
> D(S):=sum_{u in S}q_u > U(S),                         (9)
> ```
>
> then `S` is an exact Hall-deficient source set.

This is a theorem-safe relaxation: it forgets whether the high-capacity targets are the same targets that have many compatible selected sources.

## 3. Sorted form

Let

```text
P^(1)>=...>=P^(b),
y^(1)>=...>=y^(b)                                       (10)
```

be the two sequences sorted independently in decreasing order. The layer counts in (6) are their conjugate partitions. Therefore

```text
U(S)=sum_{j=1}^b min(P^(j),y^(j)).                      (11)
```

Thus `U(S)` is the maximum receiver capacity obtainable by pairing the `P`-multiset and the `y`-multiset comonotonically. The exact Hall capacity (2) can only be smaller.

This makes the loss of information explicit: exact target identity is discarded, but the complete marginal distributions of target capacity and incoming compatibility are retained.

## 4. Incoming-compatibility layers

For the orientation relation

```text
D(u,w) iff u!=w,
            q_u<=c_w+1,
            q_w<=c_u,                                  (12)
```

we have

```text
y_w
 = #{u in S:u!=w,
              q_u<=c_w+1,
              q_w<=c_u}.                               (13)
```

So `beta_k` counts targets whose interval

```text
[q_w,c_w+1]
```

meets at least `k` selected source intervals `[q_u,c_u]`.

Let

```text
Y(S)=sum_w y_w.                                        (14)
```

By Markov counting,

```text
beta_k<=min(b,floor(Y(S)/k)).                           (15)
```

The exact `beta_k` sequence is generally much stronger than (15), but (15) gives a scalar projection using only the total number of directed-compatible labelled source-target arcs from `S`.

## 5. Murty-Simon target-capacity layers

For the canonical universal target cap

```text
P_w<=b-1-q_w,
P_w<=rho_w+b-a-1,                                      (16)
```

any target in `A_k` necessarily satisfies

```text
q_w<=b-1-k,                                             (17)
rho_w>=a-b+1+k.                                        (18)
```

Hence, writing

```text
L_k=#{w:q_w<=b-1-k},                                   (19)
R_k=#{w:rho_w>=a-b+1+k},                               (20)
```

we have

```text
alpha_k<=min(L_k,R_k).                                 (21)
```

If the stronger potential-pair cap

```text
P_w<=d_KD(w)-q_w                                       (22)
```

is also used, then additionally

```text
alpha_k<=K_k:=#{w:d_KD(w)-q_w>=k}.                     (23)
```

Thus

```text
alpha_k<=min(L_k,R_k,K_k)                              (24)
```

when all three cap families are available.

## 6. Residual-budget elimination of R_k

Assume `t>0`, so residual activity gives

```text
rho_w>=1 for every w in B,
sum_w rho_w=r.                                         (25)
```

For any integer threshold `h>=2`, if

```text
z_h=#{w:rho_w>=h},                                     (26)
```

then

```text
r>=b+z_h(h-1),                                         (27)
```

and therefore

```text
z_h<=floor((r-b)/(h-1)).                               (28)
```

In (18) put

```text
h_k=a-b+1+k.                                           (29)
```

When `a-b+k>=1`, so `h_k>=2`, we obtain

```text
R_k<=min(b,floor((r-b)/(a-b+k))).                      (30)
```

When `a-b+k<=0`, residual activity alone gives only the trivial bound `R_k<=b`.

Define

```text
Rbar_k = b                                             if a-b+k<=0,
         min(b,floor((r-b)/(a-b+k)))                   if a-b+k>=1. (31)
```

Then universally under the stated hypotheses

```text
alpha_k<=min(L_k,Rbar_k)                               (32)
```

and, with the potential-pair cap, also `<=K_k`.

## 7. A scalar layered exclusion

Combining (8), (15) and (32) yields the theorem-safe upper bound

```text
H(S)
 <= sum_{k>=1}
      min(
        L_k,
        Rbar_k,
        floor(Y(S)/k)
      ).                                                (33)
```

The sum may stop at `k=b-1` because `P_w<=b-1-q_w<=b-1`.

Therefore any source set satisfying

```text
D(S)
 > sum_{k=1}^{b-1}
      min(
        L_k,
        Rbar_k,
        floor(Y(S)/k)
      )                                                 (34)
```

is Hall-deficient.

With potential-pair information available, insert `K_k` as an additional term inside the minimum.

Equation (34) is deliberately weaker than exact Hall but depends only on:

- the demand of `S`;
- the total directed-compatible arc count `Y(S)`;
- the low-`q` target counts `L_k`;
- `a,b,r` through the residual budget;
- optionally the potential-pair layer counts `K_k`.

It removes target-by-target `P/y` correlation and all max-flow computation.

## 8. Relation to the canonical staircase

For `S=M+`, the canonical maximal minimum Hall witness, exact failure is encoded by one monotone staircase. The receiver layers then provide a second compression:

```text
canonical staircase source boundary
 -> incoming overlap distribution beta_k
 -> target-cap distribution alpha_k
 -> scalar layer sum U(M+).                            (35)
```

The immediate empirical question is how often the layered upper bound itself is already below canonical demand on the current Murty-Simon frontier. High retention would give a substantially simpler symbolic target than the full type-level Hall margin.

## 9. Trust boundary

The layer identity and comonotone bound are exact finite combinatorics. The Murty-specific bounds use only the stated universal target caps and residual-activity budget. Passing the layered test does not imply Hall feasibility; failure is a valid Hall certificate.

The result does not prove the unrestricted Murty-Simon conjecture.
