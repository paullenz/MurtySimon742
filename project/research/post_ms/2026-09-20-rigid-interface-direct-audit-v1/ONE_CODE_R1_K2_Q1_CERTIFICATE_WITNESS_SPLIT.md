# Residual-one k=2 exact-ray certificate witness split

Date: 2026-09-20

Status: **same-session asymptotic refinement**, conditional on the same pure-F0 / `J2=empty` interface as `ONE_CODE_R1_K2_PURE_F0_Y_EDGE_CERTIFICATE_OBSTRUCTION.md`. No finite scan is used.

This note keeps track of overlap between forward- and reverse-certificate witnesses on the exact low-k stress ray `y=p-1`, instead of bounding both witness sets separately. It exposes the sharp equality geometry behind the golden-ratio density threshold and then prices that geometry in the exact weighted rooted/score currencies.

## 1. Witness classes

Let T be a typical F0 set of density

`tau=|T|/p`.

For the T--Y edge certificates, split the atypical escape witness vertices into three disjoint classes:

- F: used only as forward witnesses, density f;
- R: used only as reverse witnesses, density r;
- B: used in both roles, density b.

All three lie outside T, so

> `f+r+b <= 1-tau+o(1)`.                                `(GS-POP)`

On the exact ray `q=y/p->1`, fixed-pair singleton injection gives capacities

- each F or B vertex can forward-certify at most `tau p+o(p)` T--Y edges;
- each R or B vertex can reverse-certify at most `p+o(p)` T--Y edges.

Since T contributes `tau p^2+o(p^2)` Y-edges, one must have

> `tau(f+b)+(r+b) >= tau`.                               `(GS-CAP)`

## 2. Sharp maximum possible typical density

For a fixed exceptional population `e=f+r+b`, certificate capacity is maximized by putting all exceptional vertices into B, because a B vertex contributes `tau+1` normalized capacity, more than either one-role class.

Thus `(GS-CAP)` and `(GS-POP)` imply

`tau <= (1-tau)(1+tau)=1-tau^2`.

Equivalently

`tau^2+tau-1<=0`,

so

> **`tau <= (sqrt(5)-1)/2 = 0.618033...`.**             `(GS-GOLD-T)`

Hence at least

> **`(3-sqrt(5))/2 = 0.381966...`**                     `(GS-GOLD-E)`

of the escape reservoir must be atypical. This recovers the predecessor golden threshold, but now shows exactly how equality can occur.

Equality in `(GS-GOLD-T)` forces, asymptotically,

- `f=r=0`;
- `b=1-tau=(3-sqrt(5))/2`;
- every exceptional witness is used in **both** orientations at full fixed-pair capacity.

Therefore the minimum-exception endpoint is not an arbitrary atypical reservoir: it is a linear population of dual-role witnesses.

## 3. Dual-role witnesses are simultaneously Y-sparse and X-anticomplete

The predecessor F0--Y classification gives:

- every forward witness is Y-sparse, with `d_Y=o(p)`;
- every reverse witness satisfies `N_X=empty`.

Thus every B-vertex at golden equality simultaneously satisfies

> `d_Y=o(p)` and `N_X=empty`.                            `(GS-DUAL)`

It therefore carries both a `p-o(p)` Y-hole block and a `p+1` X-hole block. The two are physically disjoint.

The exact U-side degree identity is

`p+u-1-epsilon_w=d_{A union U}(w)`.

On the exact ray `u=p+1`. For a dual witness, `d_X(w)=0`, `d_Y(w)=o(p)`, and `d_U(w)<=u-1=p`. Therefore

> **`epsilon_w >= p-o(p)` for every dual witness.**      `(GS-DUAL-SLACK)`

So a dual witness is expensive in all three of the relevant weighted currencies: it has an X-hole block, a Y-hole block, and linear U-slack.

## 4. Minimum located witness-hole cost for fixed tau

The located witness-hole coefficient is

`C=f+r+2b`,

because on q=1 a one-role witness costs one normalized X- or Y-hole block and a dual-role witness costs both.

Minimize C subject to `(GS-POP)` and `(GS-CAP)`.

For `0<=tau<=1/2`, reverse-only witnesses suffice: take `r=tau`, giving

> `C_min(tau)=tau`.                                      `(GS-C1)`

For `1/2<=tau<=rho:=(sqrt(5)-1)/2`, population becomes binding. Forward-only witnesses are dominated by reverse-only witnesses, so set `f=0`. The cheapest feasible choice has

`b=2-1/tau`,

`r=tau-(tau+1)b`,

and therefore

> `C_min(tau)=3-tau-1/tau`.                             `(GS-C2)`

At `tau=rho`, this gives

`C_min(rho)=2(1-rho)=3-sqrt(5)=0.763932...`,

all of it carried by dual-role vertices.

For `tau>rho`, no certificate assignment exists at all.

## 5. Forward certificates also force distinct missing T--witness pairs

A forward certificate for the edge `ty0` uses a witness `w in N(y0)\N[t]`. Hence every forward-certified edge consumes a physical nonedge `tw`.

Because a fixed pair `(t,w)` certifies at most one y0, distinct forward-certified T--Y edges consume distinct T--witness nonedges. If A denotes the number of forward certificates normalized by `p^2`, then

> **`M_U(T,F union B)/p^2 >= A-o(1)`.**                 `(GS-F-MU)`

The typical set T itself is independent in the compressed endpoint, contributing

> **`M_U(T)/p^2 >= tau^2/2-o(1)`.**                    `(GS-T-MU)`

These two missing-U blocks are disjoint.

## 6. Exact weighted-ledger price of the certificate subsystem

The preserved exact combined rooted/score ledger is

`E_U+Z_X+Z_Y+2M_U+2L_A <= p(p+1)+2C0`

on the exact ray, whose right side has leading coefficient 4. Therefore the relevant certificate-side lower functional is weighted, not the unweighted `D_phys` alone.

Let A again be the normalized number of forward certificates. The witness system forces, at leading order,

- `Z_X+Z_Y`: coefficient at least `f+r+2b`;
- `E_U`: coefficient at least b from `(GS-DUAL-SLACK)`;
- `2M_U`: coefficient at least `tau^2+2A` from `(GS-F-MU)` and `(GS-T-MU)`.

Hence the certificate subsystem alone contributes

> `W=tau^2+2A+f+r+3b`                                  `(GS-W)`

on the left side of the exact combined weighted ledger, before the nonnegative `2L_A` term and any other escape-sector costs.

The certificate constraints are

`A<=tau(f+b)`,

`tau-A<=r+b`,

`f+r+b<=1-tau`.

Minimizing `(GS-W)` gives the exact piecewise lower envelope

> **for `0<=tau<=1/2`: `W_min(tau)=tau^2+tau`;**        `(GS-W1)`
>
> **for `1/2<=tau<=rho`:**
> **`W_min(tau)=tau^2+3tau+3-2/tau`.**                 `(GS-W2)`

The first branch uses reverse-only witnesses, `r=tau`. On the second branch population is binding, the optimum has `f=0`, `A=2tau-1`, `b=2-1/tau`, and `r=1-tau-b`.

At the golden endpoint `tau=rho`, all witnesses are dual-role and

> **`W_min(rho)=2`.**                                    `(GS-WGOLD)`

Thus the certificate subsystem already consumes one half of the leading coefficient-4 combined weighted-ledger budget at the extremal feasible typical density.

This is a substantial tightening, but **not a closure**: the exact combined ceiling still has leading coefficient 4, not `3/2`. An earlier same-session heuristic comparison of `D_phys` with the score ceiling `C0` would mix different ledgers and is not valid. The correct comparison is `(GS-W)` against the weighted coefficient-4 ceiling.

## 7. Consequence for the live exact-ray attack

The exact low-k ray cannot preserve an almost-pure F0 reservoir. It must either

1. reduce the typical F0 density to at most `rho=0.618...`, or
2. fail raw D2C edge criticality on the dense T--Y block.

At the extremal feasible density `rho`, the entire exceptional block is forced into the very rigid class `(GS-DUAL)`: X-anticomplete and asymptotically Y-anticomplete, while being used at full capacity in both orientations. Those dual witnesses also have `epsilon_w>=p-o(p)`, and the certificate subsystem has exact weighted leading price 2.

The next literal graph attack should therefore be on dual-role witnesses themselves: classify their edges to the remaining escape reservoir and to H/Y under simultaneous X-antichain/Y-sparsity, and feed any forced additional U-nonedges or A-holes into the still-unspent half of the weighted coefficient-4 budget. The alternative `tau<rho` branch has a smaller certificate price and must be combined with the predecessor departure/support/hub costs rather than ignored.

Global caveat unchanged: the rigid complete Hall-cut reachability problem remains upstream and unresolved; bounded actual-D2C regression has zero positive rigid complete-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.