# Focused hostile internal audit

12 September 2026. No blocking flaw found in the stated parameter family,
its demand-only consequences, or the exact recorded applications. This is
same-assistant internal audit. External review and novelty assessment OPEN.

## Graph implication checks

1. **Heavy degree is H, not q.** Routing uses H>h because it guarantees h
   other heavy labels at the selected arc's source. Replacing it by q>h
   would permit those other labels to be light and invalidate the implication.
2. **Every incoming source in Z is counted.** The correction includes -p
   even at a source with H=0. Deleting those states would overstate the bound.
3. **Load transport has the right direction.** R+x>=q+p and a decreasing
   ramp imply f(R+x)<=f(q+p). Then q>=H implies f(q+p)<=f(H+p), giving an
   upper bound on source cost. Both directions are required.
4. **Residual budgets are not guessed.** The basic theorem uses r_h<=r.
   The demand-only version uses r<=S-2t. It does not assert equality with
   zero demands or set their residual degree to zero.
5. **The parameter band is explicit.** The penalty can be bounded by rho-h
   only when delta=b-a<=2h+1. Outside that band, take delta=2h+2,rho=h:
   the penalty is one but rho-h is zero. At h=2 this is delta=6,rho=2.
   This witnesses failure of that proposed aggregation outside its hypothesis;
   it is not a graph or a disproof of some other possible theorem there.
6. **Tail indexing is complete.** With positive surplus, rho>=1 and
   r=b+sum_{h>=2}z_h. Each new load bound is combined with the ordinary
   capacity bound and monotonicity. A contradiction of the total budget
   excludes a whole demand profile, without claiming the remaining profiles
   are graph-realizable.

## Local formula and symbolic checks

The label inequality covers s<=L<=T, L>=T, and s>=T. The source formula
covers H<=h with three load intervals and H>h with active/inactive ramp.
The exact global maximum is max(hT,h(h+P),floor(T^2/4)); its local extremizers
are explicitly exhibited. The individual-capacity maximum uses three lower
H pieces and two upper H endpoint choices in p. Its quadratic maximum is
evaluated at the clipped integer vertex. No floating coefficients occur.

`check_local.py` independently evaluates the potential as a sum of indicators.
It passes 15,201,197 source options, 589,457 exact capped maxima, 17,042 exact
uniform maxima and 2,556,945 label inequalities. The finite ranges corroborate
the symbolic proof; they are not the basis for extrapolating to all parameters.

The low-demand corollary is checked algebraically in the proof. From demands
in {0,1,h}, S<=a+(h-1)k and G=4hk. Rearranging the demand inequality and
using k<=a gives (10h-2)t+4h(b-a)<=h(h-1)a. The h=2 specialization is
9t+4(b-a)<=a. No restriction on the residual-degree alphabet survives in
the final argument. The Turan-count identity is
floor((2a+delta+1)^2/4)-(a+delta)(a+1)=floor((delta-1)^2/4).

## Exact application and search-scope checks

The state experiment includes all 13,546 preserved N34 equality states and
all 485 N35 states, including zeros and states already excluded by the exact
positive-demand budget. Inputs are checked against their original tuples and
methods. Of 14,031 records, 4,880 fail that earlier budget identity, 871 have
new family witnesses, and 8,280 survive the searched family.

The new family witnesses include 595 states formerly handled by envelopes:
543 at N34 equality, four at N35 m=307, and 48 at N35 m=306. The other 276
were already hand-excluded. No fixed-order proof package is silently reissued
or assigned a changed ledger; these are alternative exclusions in this study.

Every recorded exclusion is checked by `verify_applications.py`, which imports
neither `bounds.py` nor either discovery program. It checks 883,922 local
source inequalities for the actual witnesses and verifies the full state
domain, original-method mapping and strict gaps.

The profile experiment includes every original retained profile at each
tested layer: 1,296, 13 and 144. The new joint tail closure excludes 30, three
and 12 respectively, counting layer/profile instances separately. Of these,
seven, two and six already fail a single new threshold inequality; the
remaining 23, one and six require combining tails. The separate checker
reconstructs all capacity/load tails directly and checks all 1,453 records.

All 871 state witnesses use the simple cutoff T=4h. On the remaining states,
integer T=h..4a in the uniform and individually capped versions produces no
additional exclusions. This is an observed limit of the stated search, not
a proof that all cutoffs or other potentials are powerless.

## Failure and provenance preservation

The local check records 24 explicit failed extensions: increasing T to 4h+1
while retaining cap hT, and dropping the penalty at p=3h+1, for h=1..12.
It also preserves the earlier h=2,T=6,p=5 failure. All are failures of local
inequalities; none is an actual graph counterexample.

The wider-cutoff and individual-capacity negative results, full survivor
records, source code, exact parameters, discovery logs, summaries and replay
outputs are retained. Large streams are stored losslessly using gzip/base64;
their original and encoded hashes, record counts and decoding code are
committed. The hand theorem does not depend on the encoding or on any solver.

The implementation is new work based on commit
398b8d949c244f7229a8ba723fb11b5fbdb7c536. It preserves the original p<=4 proof,
model normalization audit, fixed-order certificates and all historical logs.
Specialist scrutiny of the shared canonical bridge, supplement routing and
the new penalty aggregation remains essential.
