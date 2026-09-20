# Residual-one k=2 exact-ray certificate witness split

Date: 2026-09-20

Status: **same-session asymptotic refinement**, conditional on the same pure-F0 / `J2=empty` interface as `ONE_CODE_R1_K2_PURE_F0_Y_EDGE_CERTIFICATE_OBSTRUCTION.md`. No finite scan is used.

This note keeps track of overlap between forward- and reverse-certificate witnesses on the exact low-k stress ray `y=p-1`, instead of bounding both witness sets separately. It exposes the sharp equality geometry behind the golden-ratio density threshold.

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

So the smallest possible exceptional population is also the **most locally defective** witness population. This is the exact opposite of a cheap repair reservoir.

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

## 5. Consequence for the live exact-ray attack

The exact low-k ray cannot preserve an almost-pure F0 reservoir. It must either

1. reduce the typical F0 density to at most `rho=0.618...`, or
2. fail raw D2C edge criticality on the dense T--Y block.

At the extremal feasible density `rho`, the entire exceptional block is forced into the very rigid class `(GS-DUAL)`: X-anticomplete and asymptotically Y-anticomplete, while being used at full capacity in both orientations.

This is the next literal graph object to attack. Its degree/slack bill should be inserted into the exact U-side identity before any further scalar relaxation. In particular, the simultaneous X/Y hole block is order `2p` per dual-role witness, so a golden-size dual reservoir already creates a large linear-times-p defect beyond the independent typical-F0 U-hole block.

Global caveat unchanged: the rigid complete Hall-cut reachability problem remains upstream and unresolved; bounded actual-D2C regression has zero positive rigid complete-cut fixtures with `x>=3`, and `X_3` remains the mandatory negative control.