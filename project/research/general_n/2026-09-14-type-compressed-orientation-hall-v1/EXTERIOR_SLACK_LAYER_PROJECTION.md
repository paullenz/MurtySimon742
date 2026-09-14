# Exterior-slack layer projection

14 September 2026. **Candidate exact identity plus theorem-safe Murty projection inside the canonical target-Hall framework. External mathematical review and novelty assessment remain OPEN.**

The whole-exterior total-slack inequality is globally redundant once total target capacity and canonical Hall deficiency are known; see [`WHOLE_EXTERIOR_SLACK_REDUNDANCY.md`](WHOLE_EXTERIOR_SLACK_REDUNDANCY.md). The nontrivial content of strict exterior expansion is therefore the correlation between **where residual target slack sits** and **which exterior sources can reach it**.

This note applies the same layer-cake idea as [`LAYERED_RECEIVER_CAPACITY.md`](LAYERED_RECEIVER_CAPACITY.md) to the residual slack network outside the canonical witness.

## 1. Setup

Let `M+` be the canonical maximal minimum Hall witness and let

```text
s_w=(P_w-y_w(M+))_+
```

be the residual receiver slack of a labelled target copy `w`.

Let `O` be the exterior complete-type set. For any nonempty complete-type subset

```text
T subseteq O,
```

let

```text
k_T(w)
```

be the exact number of newly added labelled source copies from `T` which are directed-compatible with target `w`, including the usual diagonal deletion when `w` itself belongs to a newly selected type.

The strict exterior slack-expansion theorem gives

```text
G(T):=sum_w min(s_w,k_T(w)) >= D(T)+1.                  (1)
```

## 2. Exact exterior layer identity

For each integer `j>=1`, define

```text
S_j={w:s_w>=j},
C_j(T)={w:k_T(w)>=j},                                   (2)
```

with counts

```text
sigma_j=|S_j|,
kappa_j(T)=|C_j(T)|.                                   (3)
```

Since

```text
min(s_w,k_T(w))
 =sum_{j>=1} 1_{s_w>=j}1_{k_T(w)>=j},                  (4)
```

we have the exact identity

> **Exterior slack layer identity.**
>
> ```text
> G(T)=sum_{j>=1}|S_j cap C_j(T)|.                      (5)
> ```

Therefore

```text
G(T)<=sum_{j>=1} min(sigma_j,kappa_j(T)).               (6)
```

Combining (1) and (6) gives the theorem-safe necessary condition

> **Exterior layered expansion.** For every nonempty exterior type set `T`,
>
> ```text
> D(T)+1
> <= sum_{j>=1} min(sigma_j,kappa_j(T)).                (7)
> ```

Failure of (7) is incompatible with the existence of a deficient canonical maximal witness having exterior set `O`.

## 3. Murty bounds on slack layers

Because

```text
s_w<=P_w,                                               (8)
```

we have

```text
sigma_j<=alpha_j:=#{w:P_w>=j}.                          (9)
```

The universal Murty target caps give, whenever `P_w>=j`,

```text
q_w<=b-1-j,
rho_w>=a-b+1+j.                                        (10)
```

Define

```text
L_j=#{w:q_w<=b-1-j},
R_j=#{w:rho_w>=a-b+1+j}.                               (11)
```

Then

```text
sigma_j<=min(L_j,R_j).                                  (12)
```

If the potential-pair cap `P_w<=d_KD(w)-q_w` is included, also define

```text
K_j=#{w:d_KD(w)-q_w>=j},                               (13)
```

and obtain

```text
sigma_j<=min(L_j,R_j,K_j).                              (14)
```

Under positive surplus, residual activity gives `rho_w>=1` and `sum rho=r`, hence exactly as in the ordinary receiver-layer projection,

```text
R_j<=Rbar_j,                                            (15)
```

where

```text
Rbar_j = b
         if a-b+j<=0,

Rbar_j = min(b,floor((r-b)/(a-b+j)))
         if a-b+j>=1.                                  (16)
```

Thus

```text
sigma_j<=min(L_j,Rbar_j)                                (17)
```

and optionally `<=K_j` as well.

## 4. Scalar bound on exterior compatibility layers

Let

```text
Y_T=sum_w k_T(w)                                       (18)
```

be the total number of exact directed-compatible labelled incidences from newly added sources in `T` to all targets, with diagonal deletion.

Then Markov counting gives

```text
kappa_j(T)<=min(b,floor(Y_T/j)).                        (19)
```

Substituting (17) and (19) into (7) gives the scalar necessary condition

> **Scalar exterior-layer inequality.** For every nonempty exterior complete-type set `T`,
>
> ```text
> D(T)+1
> <= sum_{j=1}^{b-1}
>      min(
>        L_j,
>        Rbar_j,
>        floor(Y_T/j)
>      ).                                               (20)
> ```
>
> With potential-pair information, insert `K_j` as a further term inside the minimum.

The sum stops at `b-1` because `s_w<=P_w<=b-1-q_w<=b-1`.

## 5. Why this is not the redundant total-slack inequality

Equation (20) still remembers exterior **reachability**, through `Y_T` and the compatibility layers `kappa_j(T)`, and restricts where slack can sit through `L_j,Rbar_j` (and optionally `K_j`).

If one drops all compatibility information and replaces the right side merely by `sum_w s_w`, the whole-exterior case reduces to the identity recorded in `WHOLE_EXTERIOR_SLACK_REDUNDANCY.md` and adds nothing.

Thus the research boundary is precise:

```text
total residual slack alone             redundant,
slack + exterior compatibility layers  potentially new. (21)
```

## 6. Candidate structured choices of T

The universal theorem requires (20) for every exterior complete-type set, but a general proof need not enumerate them all. The next objective is to find a small structured family forced by the canonical staircase, for example:

1. all exterior types at or above a fixed `q` threshold;
2. all exterior types with `c` below a fixed cross-degree threshold;
3. exterior types adjacent to one staircase breakpoint;
4. the whole exterior `O`, retaining `Y_O` rather than dropping compatibility;
5. minimal exterior collections maximizing demand per reachable slack layer.

The frozen receiver-layer exceptions are the preferred empirical testbed for deciding which family has real reach.

## 7. Trust boundary

The exact identities (1) and (5) are finite combinatorics once the canonical witness and target-capacity model are accepted. The Murty bounds use only the stated target caps, positive-surplus residual activity and total residual budget. The scalar projection is necessary, not sufficient, and does not assert graph realizability or prove the unrestricted Murty-Simon conjecture.
