# Coupled demand/residual staircases and the first peeling inequality

17 September 2026. Research directed by Paul Lenz; derivation and consolidation by ChatGPT/Geeps.

**Status: internal candidate mathematics; not promoted; external mathematical review and novelty remain open.** The genuinely graph-theoretic input is the already-preserved canonical threshold-capacity theorem. This note rewrites that theorem in tail-count form and combines adjacent levels. The aim is to bridge the exact-block scope gap, not to add another finite survivor scan.

## 1. Why this was the next move

The preceding receiver-inflation theorem showed that excess top sources are not free, but a scalar optimizer can still move demand from the h-level to h-1 when the number k of demand-h labels is less than h.

Before building a new routing theorem from scratch, it is better to reuse a stronger fact already present in the canonical bridge:

    W_d <= d N_d + C(N_d-d,2),

where W_d is the total demand carried by labels of demand at least d and N_d is the number of residual sources of degree at least d.

Written in tail coordinates, this is already a multi-level coupling. The point of this note is to expose that coupling explicitly and derive the first adjacent-level peeling bound.

## 2. Tail coordinates

Assume positive surplus t>0, so every B-source is residual-active.

For integers d>=1 define

    K_d = #{i in A : s_i >= d},
    N_d = #{u in B : rho_u >= d}.

Then N_1=b. The ordinary layer-cake identities are exact:

    S := sum_i s_i = sum_{d>=1} K_d,                 (LC-S)

    r := sum_u rho_u = sum_{d>=1} N_d.               (LC-r)

The exact residual ledger gives

    r+2t <= S,

hence

    2t <= sum_{d>=1} (K_d-N_d).                      (LC)

This is a useful way to view the scope problem: dense counterexamples need the demand staircase K_d to exceed the residual staircase N_d by enough total area.

Let h be the residual h-index. The selected-edge compatibility inequality implies every demand satisfies s_i<=h.

## 3. Staircase-capacity theorem

For every d>=1 with K_d>0, the canonical threshold-capacity theorem gives

    W_d <= d N_d + C(N_d-d,2),                       (TC)

and necessarily N_d>=d.

But, because demands are integral,

    W_d := sum_{s_i>=d} s_i
         = d K_d + sum_{j>d} K_j.                    (W)

Therefore every actual realization satisfies the pure staircase inequality

    d K_d + sum_{j>d} K_j
        <= d N_d + C(N_d-d,2).                       (SC_d)

This is the desired multi-level coupling. It contains no individual demand variables and no fixed graph order.

At the top level d=h it reads

    h K_h <= h N_h + C(N_h-h,2).

If N_h=h, this reduces to K_h<=h. Equality K_h=h is exactly the square exact-block face.

## 4. First adjacent-level peeling inequality

Assume h>=3. Write

    k = K_h,
    K = K_{h-1},
    N = N_h,
    M = N_{h-1}.

Thus

    N>=h,     M>=N,     0<=k<=K<=a.

Since all demands are at most h,

    S <= a(h-2)+K+k.                                  (1)

Indeed, give every label a baseline h-2, add one for each label reaching h-1, and one more for each label reaching h.

Residual activity and the two top residual levels give

    r >= b+(h-2)M+N.                                  (2)

Combining (1), (2) and r+2t<=S yields

    b+2t <= a(h-2)+K+k-(h-2)M-N.                     (P1)

Now apply (SC_d) at d=h-1. Since labels at this threshold have demand h-1 or h,

    W_{h-1}=(h-1)K+k,

so

    (h-1)K+k
      <= (h-1)M + C(M-h+1,2).                        (P2)

Equations (P1)--(P2) are the first two-level peeling system.

## 5. Closed non-square bound

Suppose the top demand level is non-square:

    k<=h-1.

Put

    C_M = C(M-h+1,2),

    K_*(M)
      = min(a, M-1+floor(C_M/(h-1))).

Then every actual realization satisfies

    b+2t
      <= a(h-2)-1+K_*(M)-(h-2)M.                     (NS)

Proof. For fixed h,a,M, equation (P2) bounds K as

    K <= min(a,
             floor(((h-1)M+C_M-k)/(h-1))).

Over integers 0<=k<=h-1, the quantity

    k + min(a,
            floor(((h-1)M+C_M-k)/(h-1)))

is nondecreasing in k: increasing k by one raises the first term by one while the floor term can drop by at most one, and the truncation at a cannot reverse this. Hence its maximum is attained at k=h-1. At that endpoint,

    K <= min(a, M-1+floor(C_M/(h-1)))=K_*(M).

Substitute K+k<=K_*(M)+h-1 into (P1), then use N>=h. This gives (NS).

No graph-realizability assumption is introduced in this elimination; the only graph input is (P2).

## 6. Flat-tail consequence: exact block or tail growth

The cleanest case is

    N_h=N_{h-1}=h.

Then M=h, so C_M=0 and K_*(h)=h-1. The non-square bound becomes

    b+2t <= (h-2)(a-h+1).                            (FT)

Compare this with the coarse h-index maximum

    b+2t <= h(a-h+1).

Thus a flat residual staircase together with a non-square top demand level loses

    2(a-h+1)

units from the old h-index maximum.

Equivalently, if N_h=h and

    b+2t > (h-2)(a-h+1),

then one of the following must happen:

1. K_h=h, giving the exact square block |H_h|=|T_h|=h; or
2. N_{h-1}>=h+1, so the residual staircase must grow immediately below the top.

This is the first genuine peeling dichotomy.

For h=5 it says:

    N_5=5 and b+2t>3a-12
       =>  K_5=5  or  N_4>=6.                        (5D)

The first branch is exactly the five-label block covered by the current D>=12 theorem. The second branch is no longer a vague "k<5" escape: it has been converted into an explicit lower-level tail-growth obligation.

## 7. h=5 with a growing level-4 tail

Write

    M=N_4=5+s,     s>=0.

Before the cap K_*(M)=a is reached,

    K_*(M)
      = 4+s+floor(s(s+1)/8),

and (NS) becomes

    b+2t
      <= 3a-12-2s+floor(s(s+1)/8).                   (5NS)

So the first few tail-growth steps do not restore the lost capacity:

    s=0:  b+2t <= 3a-12
    s=1:  b+2t <= 3a-14
    s=2:  b+2t <= 3a-16
    s=3:  b+2t <= 3a-17
    s=4:  b+2t <= 3a-18
    s=5:  b+2t <= 3a-19.

If K_*(M)=a, the alternative form is

    b+2t <= 4a-16-3s.

These are arithmetic consequences of the two-level theorem, not sharpness or realizability claims.

## 8. Relation to receiver inflation and heavy routing

This result does not replace the preceding receiver-inflation theorem.

- h-index saturation penalizes excess top sources N_h>h and missing top labels.
- receiver inflation charges selected top-level mass that cannot fit through high-high B-pairs.
- the present staircase theorem uses the already-proved threshold pair capacity at the next demand level and converts k<h into either a large scalar loss or forced growth of N_{h-1}.
- the older heavy-load/routing family remains a natural tool once the surviving branch has a large lower-level residual tail.

The strategic improvement is therefore a branch reduction:

    excess top sources
        versus
    exact square block
        versus
    forced lower-level tail growth.

That is substantially narrower than the previous undifferentiated "move mass to h-1" escape.

## 9. Arithmetic audit

`check_staircase.py` independently brute-forces the integer elimination in Section 5.

Published range:

    3<=h<=15,
    h<=a<=60,
    h<=M<=min(3a,100).

For every parameter triple it enumerates all integer

    0<=k<=h-1,
    k<=K<=a

satisfying (P2), computes the exact maximum of K+k, and compares it with the closed formula

    h-1+K_*(M).

It checks 50,076 parameter triples and 676 flat-tail specializations with no failure.

This audit checks only the integer elimination and displayed specializations. The canonical threshold-capacity theorem is still a hand graph theorem written by the same assistant and requires independent review.

## 10. Next structural target

Do not return automatically to D=12 exact-block grinding.

The next scope question is now sharper: apply the full staircase system (SC_d), together with receiver inflation and the heavy-load tail inequalities, to the branch in which the residual tail grows below h. In particular, test whether repeated peeling can force either a square block at some level or enough residual-tail area to violate the layer-cake ledger (LC).

A useful next theorem would make that recursion explicit rather than introducing another isolated threshold estimate.
