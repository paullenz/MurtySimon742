# Two restricted quadratic potentials close total selected excess E=4

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate hand theorem inside the canonical selected/residual bridge; not promoted; external mathematical review remains open.** This continues the mixed demand-4/5 near-Turán attack at `(a,b,t)=(20,23,2)`. The preceding restricted-quadratic argument closed `E=3`. Here two small integer potentials overlap and close `E=4` for every mixture of demand four and demand five.

## 1. Scope and common restricted quadratic ledger

Assume

    a=20, b=23, t=2,

all twenty positive demands satisfy `s_i in {4,5}`, and let `k` be the number of demand-five labels. Put

    x_i=s_i+e_i,
    E=sum_i e_i=4.

Then

    r=76+k,
    Q=sum_i x_i=84+k,
    sum_u rho_u=r,
    sum_u p_u=sum_u q_u=Q.

For every selected incidence `ui`, retain

    s_i<=rho_u,
    e_i>=g_u:=max(0,p_u-rho_u+1),
    C_i:=R_i+x_i>=p_u+q_u.

Selected labels at a fixed source are distinct. Hence every active source satisfies

    q_u g_u <= E=4.                                    (1)

The global quadratic endpoint ledger is

    sum_u q_u(p_u+q_u) <= sum_i x_i C_i.               (2)

Restricting to selected incidences sourced at `rho_u=4` forces `s_i=4`, so

    sum_{rho_u=4} q_u(p_u+q_u)
      <= sum_{s_i=4} x_i C_i.                          (3)

Multiply (2) by six and add (3). Define

    K_B=sum_u (6+[rho_u=4])q_u(p_u+q_u),
    K_A=sum_i (6+[s_i=4])x_i C_i.

Every actual bridge satisfies

>     K_B <= K_A.                                      (4)

The rest of the argument supplies two different linear lower/upper potentials for the same pair `(K_B,K_A)`.

## 2. Potential A — closes k<=13

### Source inequality A

For every local source obeying the canonical caps

    p<=rho+2,
    p+q<=22,
    q+rho<=20 when q>0,

with `q=0` when `rho<4`, and with the exact excess-budget consequence `qg<=4`, one has

>     (6+[rho=4])q(p+q)
>       >= 70p+112q-98rho-112.                         (5)

The finite active local domain splits by `rho=4` versus `rho>=5` and `g=0,1,2,3,4`; condition `qg<=4` makes every branch elementary. The complete replay gives the following minimum slacks for left minus right among nonempty active classes:

| source class | g=0 | g=1 | g=2 | g=3 |
|---|---:|---:|---:|---:|
| `rho=4` | 0 | 0 | 28 | 21 |
| `rho>=5` | 0 | 20 | 54 | 48 |

The `g=4` branch has only `q=1` and also positive slack; inactive `q=0` states are nonnegative, with equality possible at `(rho,p,q)=(1,3,0)`. Representative equality states include `(4,3,6)`, `(4,4,4)`, and `(5,4,7)`.

Summing (5) over all 23 sources yields

    K_B >= 182Q-98r-2576.                              (6)

### Label inequality A

Positive demand gives `d_i=R_i+s_i<=19`, hence

    R_i<=15 if s_i=4,
    R_i<=14 if s_i=5.

Also `0<=e_i<=4`. Every label satisfies

>     (6+[s_i=4])x_i C_i
>       <= 112+28R_i+66[s_i=5]+189e_i.                (7)

For `s=4`, right minus left is exactly

    7e(19-e-R),

which is nonnegative because `R<=15` and `e<=4`.

For `s=5`, right minus left is

    2(14-R)+e(129-6R-6e),

which is nonnegative for `R<=14`, `e<=4`.

Summing (7) over the twenty labels gives

    K_A <= 112*20 +28r+66k+189E
         = 2996+28r+66k.                              (8)

Combining (4), (6), and (8), an actual bridge would require

    182Q-126r-66k-5572 <=0.

Substituting `Q=84+k`, `r=76+k` gives

>     140-10k <=0.                                     (9)

This is impossible for every `k<=13`.

## 3. Potential B — closes k>=9

A second pair of local potentials treats the high-`k` range.

### Source inequality B

Every allowed source satisfies

>     (6+[rho=4])q(p+q)
>       >= 60p+102q-79rho-108.                         (10)

The complete active local-domain replay gives minimum slacks:

| source class | g=0 | g=1 | g=2 | g=3 |
|---|---:|---:|---:|---:|
| `rho=4` | 10 | 0 | 18 | 11 |
| `rho>=5` | 11 | 11 | 35 | 29 |

Again the `g=4,q=1` branch and all inactive states have nonnegative slack.

Summing (10) gives

    K_B >= 162Q-79r-2484.                              (11)

### Label inequality B

Every allowed label satisfies

>     (6+[s_i=4])x_i C_i
>       <= 112+30R_i+38[s_i=5]+182e_i.                (12)

For `s=4`, right minus left is

    (2-7e)R+126e-7e^2,

nonnegative for `R<=15`, `e<=4` (the tightest `e=4,R=15` value is `2`).

For `s=5`, right minus left is

    e(122-6R-6e),

nonnegative for `R<=14`, `e<=4`.

Summing (12) gives

    K_A <= 112*20+30r+38k+182E
         = 2968+30r+38k.                              (13)

Combining (4), (11), and (13) requires

    162Q-109r-38k-5452 <=0.

Substituting `Q=84+k`, `r=76+k` gives

>     15k-128 <=0.                                     (14)

This is impossible for every `k>=9`.

## 4. Complete E=4 closure

Potential A excludes `k=0,...,13`.

Potential B excludes `k=9,...,20`.

The ranges overlap on `k=9,...,13`, so together they cover every mixture `k=0,...,20`.

Therefore:

> **There is no canonical bridge profile at `(a,b,t)=(20,23,2)` with all twenty positive demands in `{4,5}` and total selected excess `E=4`.**

Combining this with the earlier `E<=3` work gives the current barrier

>     E >= 5

for any surviving mixed demand-4/5 bridge in the previously established near-Turán scope.

The E=4 proof itself does not use the earlier `h>=5` assumption; the combined E>=5 statement retains the scope assumptions required by the E<=2 predecessor.

## 5. Audit and strategic consequence

`check_e4_two_potential.py` exhaustively checks the complete integer source domain allowed by the canonical caps plus `qg<=4`, checks every label state with `s in {4,5}`, `d=R+s<=19`, `0<=e<=4`, and verifies the two final gap formulas and their combined coverage of all `k=0,...,20`.

The important pattern is methodological. One restricted quadratic ledger is enough, but no single linear support potential is needed globally: two low-complexity potentials can cover complementary parameter ranges. This suggests treating the next excess values as a small dual-cover problem over a fixed family of restricted incidence ledgers.

The next target is `E=5`. Before launching any graph or histogram census, search for a finite set of small integer source/label potentials whose gap intervals cover all `k`. If such covers persist, attempt to derive a parameterized family in `E`; if they fail, preserve the first exact incidence-level obstruction.
