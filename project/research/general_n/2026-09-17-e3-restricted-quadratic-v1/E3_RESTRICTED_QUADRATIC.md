# Restricted quadratic endpoint ledger closes total selected excess E=3

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate hand theorem inside the canonical selected/residual bridge; not promoted; external mathematical review remains open.** This continues the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)`. The preceding theorem proved total selected excess `E>=3`. The present argument rules out `E=3` by retaining one demand-restricted piece of the exact selected-incidence matrix.

## 1. Scope

Assume

    a=20, b=23, t=2,

all twenty positive demands satisfy `s_i in {4,5}`, and let `k` be the number of demand-five labels. Put

    x_i=s_i+e_i,
    E=sum_i e_i=3.

As before,

    r=76+k,
    Q=sum_i x_i=83+k,
    sum_u rho_u=r,
    sum_u p_u=sum_u q_u=Q.

For each source write

    g_u=max(0,p_u-rho_u+1),
    w_u=p_u+q_u.

Every selected incidence `ui` obeys

    s_i<=rho_u,
    e_i>=g_u,
    C_i=R_i+x_i>=w_u.                                  (1)

Selected labels at one source are distinct.

## 2. A restricted quadratic endpoint ledger

The global quadratic endpoint lemma is

    sum_u q_u w_u <= sum_i x_i C_i.                    (2)

There is a useful restricted version. Consider only selected incidences sourced at vertices with `rho_u=4`. By demand compatibility in (1), every such incidence has a demand-four label. Summing endpoint load only over these incidences therefore gives

    sum_{u:rho_u=4} q_u w_u
      <= sum_{i:s_i=4} x_i C_i.                        (3)

More generally, the same argument works for any selected-incidence subfamily defined by a source condition whose incidences force membership in a corresponding label class. Equation (3) is the only restricted member needed here.

Multiply (2) by six and add (3). Define

    K_B=sum_u (6+[rho_u=4]) q_u(p_u+q_u),

    K_A=sum_i (6+[s_i=4]) x_i C_i.

Then every real bridge satisfies

>     K_B <= K_A.                                      (4)

This is weaker than the full selected-incidence Hall theorem but stronger than the undifferentiated global quadratic ledger because it remembers that residual-degree-four sources can select only demand-four labels.

## 3. Total excess three gives a sharp local source restriction

At a source with `q_u>0`, its `q_u` selected labels are distinct and each has excess at least `g_u`. Hence

    q_u g_u <= E=3.                                    (5)

Together with the canonical local caps

    p_u<=rho_u+2,
    p_u+q_u<=22,
    q_u+rho_u<=20,

and `q_u=0` when `rho_u<4`, this leaves only four incoming regimes for an active source:

- `g=0`: `p<=rho-1`;
- `g=1`: `p=rho`, `q<=3`;
- `g=2`: `p=rho+1`, `q<=1`;
- `g=3`: `p=rho+2`, `q<=1`.

No active source can have `g>=4`.

## 4. Uniform source potential

For every source satisfying the displayed conditions,

> **Source inequality**
>
>     (6+[rho=4]) q(p+q)
>       >= 60p+102q-79rho-104.                         (6)

This is an elementary local inequality. A compact verification is as follows.

If `q=0`, the incoming cap `p<=rho+2` gives

    60p-79rho-104 <= 60(rho+2)-79rho-104
                    =16-19rho <= -3.

For active sources, split by `rho=4` versus `rho>=5` and by `g=0,1,2,3`. Substitution of the extremal allowed `p,q` reduces to short integer quadratics. The minimum slacks of left side minus right side over the complete allowed ranges are:

| source class | g=0 | g=1 | g=2 | g=3 |
|---|---:|---:|---:|---:|
| `rho=4` | 6 | 21 | 60 | 7 |
| `rho>=5` | 7 | 37 | 79 | 25 |

Thus (6) is strict on every active local state. The replay checker enumerates the same finite local domain independently.

Summing (6) over the 23 B-sources gives

    K_B
      >= 60 sum p +102 sum q -79 sum rho -104*23
      = 162Q-79r-2392.                                (7)

## 5. Uniform label potential

Since positive demand gives

    d_i=R_i+s_i<=19,

we have `R_i<=15` for demand four and `R_i<=14` for demand five. Because total excess is three, each `e_i` lies in `{0,1,2,3}`.

For every label,

> **Label inequality**
>
>     (6+[s_i=4]) x_i C_i
>       <= 112+30R_i+38[s_i=5]+172e_i.                (8)

This can be checked algebraically without enumeration.

If `s=4`, then `x=4+e`, `C=R+4+e`, and right minus left in (8) is

    (2-7e)R +116e-7e^2,

which is nonnegative for `0<=R<=15`, `0<=e<=3`; at `e=3` the worst case `R=15` is equality.

If `s=5`, then right minus left is

    e(112-6R-6e),

which is nonnegative because `R<=14` and `e<=3`.

Summing (8) over the twenty labels gives

    K_A
      <= 112*20 +30r +38k +172E
      = 2756+30r+38k.                                 (9)

## 6. Contradiction

Combine the structural inequality (4) with (7) and (9). A necessary condition for a real bridge would be

    162Q-79r-2392
      <= 2756+30r+38k.

Equivalently,

    162Q-109r-38k-5148 <=0.                           (10)

But at `E=3`,

    Q=83+k,
    r=76+k,

so the left side of (10) is exactly

    162(83+k)-109(76+k)-38k-5148
      = 14+15k.

For every `k=0,...,20`,

    14+15k >0,

contradicting (10).

Therefore no canonical bridge profile exists in this entire `E=3` mixed demand-4/5 scope.

## 7. Bounded theorem

Combining this result with the preceding `E<=2` theorem gives:

> **Four-unit selected-excess barrier.** At `(a,b,t)=(20,23,2)`, suppose all twenty positive demands lie in `{4,5}` and the canonical bridge assumptions above hold. Then any surviving bridge profile must satisfy
>
>     E=sum_i(x_i-s_i) >=4.

The `E=3` argument itself does **not** use the earlier assumption that at least five residual sources have degree at least five; it follows from the exact margins, mixed-demand scope and selected-incidence restrictions stated above. The combined `E>=4` statement inherits whatever scope assumptions are needed for the preceding `E<=2` theorem.

This remains a bridge-level structural result, not an unrestricted Murty-Simon proof and not a promotion of a fixed-order catalogue claim.

## 8. Strategic consequence

The positive-excess frontier has now moved through three units without a broad state census:

- `E=0,1,2` are excluded by the quadratic endpoint potential plus the global excess budget;
- `E=3` is excluded once one demand-restricted quadratic ledger is retained.

The next attack should test whether the same restricted-incidence method admits a stable coefficient family for `E=4` and beyond. In particular, total excess `E` always gives the local restriction

    q_u g_u <= E,

while demand-threshold restricted quadratic ledgers are available at every residual threshold, not just four. A successful parameterized potential in `E` would be substantially more valuable than continuing one excess value at a time.
