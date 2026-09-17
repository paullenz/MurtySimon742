# Quadratic endpoint-load ledger and zero-excess mixed 4/5 closure

17 September 2026. Research directed by Paul Lenz; derivation and internal audit by ChatGPT/Geeps.

**Status: candidate general lemma plus a bounded near-Turán application inside the canonical selected/residual bridge; not promoted; external mathematical review remains open.**

## 1. Step-back: retain the exact selected row degrees

The recent excess-aware and selected-witness projections deliberately weakened the canonical bridge to the implication `q_u>0 => u has a selected incidence`. The canonical bridge contains more: by definition,

`q_u = number of selected A-B edges with source u`,

while `x_i` is the selected degree of label `i`. Thus the selected incidence matrix has exact row degrees `q_u` and exact column degrees `x_i`.

That exact identity makes the endpoint-load inequality accumulate once for **every** selected incidence, not just once per active source. This yields a quadratic global ledger.

## 2. General quadratic endpoint-load lemma

For every selected incidence `ui`, the canonical endpoint-load theorem gives

`R_i+x_i >= p_u+q_u`.

Write `C_i=R_i+x_i`. Sum this inequality over all selected incidences. Label `i` occurs exactly `x_i` times and source `u` occurs exactly `q_u` times. Therefore every canonical bridge satisfies

**`sum_i x_i C_i >= sum_u q_u(p_u+q_u)`.**        (1)

Equivalently,

**`sum_i x_i(R_i+x_i) >= sum_u q_u(p_u+q_u)`.**  (2)

No optimization, graph-order enumeration, h-index assumption or heavy-load theorem is used in (1). It is simply endpoint load summed with the exact selected row and column multiplicities.

This is stronger in a different direction from the one-witness Hall theorem. Hall prevents a favourable selected label from witnessing too many active sources; (1) charges **all** `q_u` selected incidences at source `u` at the endpoint threshold `p_u+q_u`.

## 3. Near-Turán zero-excess mixed 4/5 band

Fix

`a=20, b=23, t=2`.

Assume all 20 demands are in `{4,5}` and selected excess is zero, so `x_i=s_i`. Let `k` be the number of demand-five labels. Then

`Q=sum_i x_i=80+k`.

All demands are positive, so `s_i=d_i-R_i`; with `x_i=s_i`, summing `d_i=R_i+x_i` and using `sum d_i=2(r+t)` gives

`r=Q-2t=76+k`.                                      (3)

Assume also that at least five residual sources satisfy `rho_u>=5`. This includes the residual-h-index-five scope that motivated the calculation, but the argument below does not require the h-index to be exactly five.

### 3.1 Upper bound the label side of (1)

The selected-square contribution is

`sum_i x_i^2 = 16(20-k)+25k = 320+9k`.

Let `R_5` denote the total residual degree on the `k` demand-five labels. Then

`sum_i x_i R_i = 4r+R_5`.

A demand-five label already has five selected B-neighbours, and selected and residual incidences are disjoint among the `b=23` B-sources. Hence every such label has `R_i<=18`. Also `R_5<=r`. Therefore

`R_5 <= min(18k,76+k)`

and (1) has the universal upper bound

**`sum_i x_i C_i <= U(k):=624+13k+min(18k,76+k)`.**    (4)

Thus

`U(k)=624+31k` for `0<=k<=4`,

and

`U(k)=700+14k` for `5<=k<=20`.                         (5)

## 4. A short local support inequality

For every source, the canonical incoming cap is

`p_u<=rho_u+b-a-1=rho_u+2`.                            (6)

If `q_u>0`, at least one selected incidence exists. Zero selected excess and the established selected-excess condition then force

`p_u<=rho_u-1`.                                        (7)

Also selected labels at a source are distinct, compatibility gives `s_i<=rho_u`, and `q_u+rho_u<=a`. Hence:

- if `rho_u<4`, then `q_u=0`;
- if `rho_u=4`, then `q_u<=min(16,20-k)`;
- if `rho_u>=5`, then `q_u<=20-rho_u`.

Define

`delta_k = 6` for `0<=k<=14`,

`delta_15=5`, `delta_16=2`, and `delta_k=0` for `17<=k<=20`.

For every source obeying the displayed local constraints,

**`10p_u+15q_u-q_u(p_u+q_u)
   <= 10rho_u+20+delta_k [rho_u=4]`.**                  (8)

Proof. If `q=0`, (8) is immediate from (6). If `rho>=5` and `q>0`, then for `q<=10` the coefficient of `p` is nonnegative, so (7) gives

`10p+15q-q(p+q) <= 10rho-10+q(16-rho-q)`.

For integer `q` and `rho>=5`, the last quadratic term is at most 30. For `q>=10`, setting `p=0` only increases the expression and gives `q(15-q)<=50`, also below `10rho+20`. Thus the right side is `10rho+20` for every `rho>=5`.

For `rho=4` and `q>0`, (7) gives `p<=3`. For `q<=10`,

`10p+15q-q(p+q) <= 30+q(12-q)`.

Relative to the baseline 60, the largest integer bonus permitted by `q<=20-k` is 6 when `20-k>=6`, 5 when `20-k=5`, 2 when `20-k=4`, and 0 when `20-k<=3`. This is exactly `delta_k`. For `q>10`, `q(15-q)<60`. This proves (8).

Sum (8) over all `b=23` sources. Since `sum p=sum q=Q`, if `c_4=#{u:rho_u=4}`, then

**`sum_u q_u(p_u+q_u)
   >= 25Q-10r-20b-delta_k c_4
   = 780+15k-delta_k c_4`.**                            (9)

## 5. Residual mass bounds the number of degree-four sources

There are at least five sources with residual degree at least five, and positive surplus gives `rho_u>=1` for every source. Therefore, if `c_4` sources have residual degree four,

`r >= 5*5 + 4c_4 + 1*(23-5-c_4)
   = 43+3c_4`.

Using (3),

**`c_4 <= floor((33+k)/3)`.**                           (10)

## 6. Contradiction for every mixture k=0,...,20

Combine (4), (9) and (10).

For `0<=k<=4`, `delta_k=6`, so (9)-(10) give the relaxed lower bound

`sum q(p+q) >= 714+13k`,

whereas (5) gives `U(k)=624+31k`. The gap is at least `90-18k>0`.

For `5<=k<=13`, the same lower bound applies while `U(k)=700+14k`; the gap is at least `14-k>0`.

For `k=14`, (10) gives `c_4<=15`, hence the lower side is at least 900 while `U(14)=896`.

For `k=15`, `c_4<=16` and `delta_15=5`, giving lower side 925 versus `U(15)=910`.

For `k=16`, `c_4<=16` and `delta_16=2`, giving lower side 988 versus `U(16)=924`.

For `17<=k<=20`, `delta_k=0`, giving lower side `780+15k` versus `U(k)=700+14k`, a gap `80+k>0`.

Thus (1) cannot hold in any case.

### Bounded closure

**There is no canonical bridge profile with `a=20,b=23,t=2`, zero selected excess, all twenty demands in `{4,5}`, and at least five residual sources of degree at least five.**

In particular the entire zero-excess mixed demand-4/5 residual-h-index-five band is empty. This includes the earlier uniform demand-four band (`k=0`) and does not need the previous heavy-load histogram census, staircase inequalities, common-margin cut or selected-witness Hall theorem.

This is a scope result inside the canonical bridge, not a proof of Murty-Simon and not a promotion of any fixed-order theorem.

## 7. Audit and strategic consequence

`check_quadratic_endpoint.py` independently enumerates every local integer `(p,q)` state for `rho=1..20` and `k=0..20`, verifies the exact support constants in (8), and checks every displayed global arithmetic gap. The hand proof above is primary; the script is a replay guard.

The structural lesson is broader than the bounded closure: preserving the exact identity `q_u = selected row degree at u` makes endpoint load accumulate quadratically. The recent one-witness Hall and one-source-envelope relaxations intentionally discarded that multiplicity. Future scope work should therefore keep the full selected-incidence row/column ledger before introducing additional projected Hall or survivor scans.

The next natural target is **positive selected excess**. There `x_i>s_i` can raise the label-side endpoint budget, while the excess condition simultaneously permits larger incoming `p_u` on selected sources. The correct question is whether a weighted version of (1), together with the total excess budget and exact selected row degrees, still forces either an exact block or a quantitatively large excess penalty.