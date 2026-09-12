# A general heavy-load and routing family

12 September 2026. Candidate graph inequalities, with hand proofs and exact
internal checks. Paul Lenz directed the research; ChatGPT/Geeps supplied the
development and internal audit. External mathematical review and novelty
assessment remain OPEN. No unrestricted Murty–Simon solution is claimed.

## 1. Graph data and routing

Use the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md).
There are a labels and b sources. Label i has demand s_i, residual degree R_i
and selected degree x_i. Source u has residual degree rho_u, selected outdegree
q_u and supplement indegree p_u. Let r=sum_i R_i=sum_u rho_u.

Fix an integer h>=1. Put

`I_h={i:s_i>=h}`, `k_h=|I_h|`, `Z_h={u:rho_u>=h}`, `z_h=|Z_h|`,

and let H_u count the selected incidences from u to I_h. The bridge gives

`x_i>=s_i`, `q_u>=H_u`, `R_i+x_i>=q_u+p_u` on a selected incidence.

Compatibility s_i<=rho_u implies H_u=0 outside Z_h. The heavy-label forcing
argument gives

`sum_{u in Z_h} H_u [H_u>h] <= sum_{u in Z_h} p_u`.        (1)

To see this, the supplement of a heavy selected arc from u with H_u>h is
adjacent in H to at least h other heavy labels selected by u. If all those
cross edges are residual, its residual degree is at least h. If one is
selected, compatibility with its heavy label gives the same conclusion.
Thus the supplement is in Z_h. Distinct selected arcs represent distinct
selected B-pairs and their incoming incidences are counted by p. The argument
is the one proved in the [source-capped threshold lemma](../2026-09-12-source-capped-threshold-v1/SOURCE_CAPPED_THRESHOLD.md).

This counts actual selected heavy degree H, not total selected degree q.
Sources in Z_h with H=0 are still included in the incoming sum.

## 2. An arbitrary integer cutoff

Let T>=h be an integer and define the decreasing ramp

`f_(h,T)(L)=max(0,T-max(h,L))=sum_{j=h}^{T-1}[L<=j]`.

For every heavy label, x>=s>=h and L=R+x>=s. Therefore

`hR+hx+x f_(h,T)(R+x) >= h max(T,s)`.                   (2)

If s>=T, the first two terms give hL>=hs. If s<=T and L>=T,
they give hL>=hT. If s<=L<=T, then
`hL+x(T-L)>=hL+h(T-L)=hT`. These cases cover all R>=0 and x>=s.

For nonnegative integers H,p define the local source cost

`g_(h,T)(H,p)=hH+hp+H f_(h,T)(H+p)-hH[H>h]`.

Suppose C_u is an upper bound on that cost over all allowed H_u,p_u for a
source u in Z_h. Since q_u>=H_u and the ramp is decreasing,

`hH_u+H_u f_(h,T)(q_u+p_u) <= C_u+h(H_u[H_u>h]-p_u)`.

Transport the label potential along actual selected incidences, sum (2),
and apply (1). With `r_h=sum_{i in I_h} R_i<=r`, this proves

**`h sum_{i in I_h} max(T,s_i) <= h r_h+sum_{u in Z_h} C_u
                                      <= h r+sum_{u in Z_h} C_u`.** (3)

No fixed graph order, positive-demand assumption, grouping or optimization
solver is used. Zero-demand labels are harmless because they are outside I_h.

## 3. A closed source bound for every incoming cap

If 0<=p<=P and H is any nonnegative integer, the exact maximum is

**`C(h,T,P)=max(hT, h(h+P), floor(T^2/4))`.**              (4)

For H<=h, the source cost is nondecreasing in p. More directly, with L=H+p:

- If L<=h, `g=HT+hp<=hT`, since p<=h-H and T>=h.
- If h<=L<=T, `g=HT+(h-H)L<=hT`.
- If L>=T, `g=h(H+p)<=h(h+P)`.

For H>h, if H+p<=T then
`g=H(T-H)+(h-H)p<=H(T-H)<=floor(T^2/4)`.
If H+p>=T, then g=hp<=hP. This proves the upper bound.

It is the exact maximum of this local domain: hT is attained at H=h,p=0;
h(h+P), whenever it exceeds hT, is attained at H=h,p=P. If the quadratic
term dominates, T>=4h and an integer nearest T/2 is greater than h; that H
with p=0 attains floor(T^2/4). These are local-domain witnesses, not claimed
graph realizations or extremizers for the original conjecture.

Equation (3), with a different P_u for each source, is a universal profile
inequality. In the canonical bridge one may use

`P_u=rho_u+b-a-1`,

provided these caps are nonnegative. Actual graph data necessarily satisfy
that condition. The positive-surplus frontiers tested here all do so.

## 4. The cutoff T=4h and an explicit excess penalty

Set T=4h in (4). Since floor(T^2/4)=hT=4h^2,

`C(h,4h,P)=4h^2+h(P-3h)_+`, where `(v)_+=max(v,0)`.

Write `G_h(s)=sum_{s_i>=h} max(4h,s_i)`. Equation (3) yields

**`G_h(s) <= r_h+4h z_h+sum_{u in Z_h}(p_u-3h)_+`.**    (5)

Here take P_u equal to each source's actual p_u in the pointwise bound.
Replacing actual p by any proved upper cap gives a directly checkable version.
In particular the canonical source bounds imply

**`G_h(s) <= r+4h z_h+
            sum_{rho_u>=h}(rho_u+b-a-1-3h)_+`.**          (6)

Thus the family does not require a small incoming cap: excess incoming degree
has an explicit cost. If p_u<=3h on every u in Z_h, the penalty vanishes and

**`4h k_h <= G_h(s) <= r+4h z_h`.**                      (7)

For h=2 this gives `8k<=r+8z` whenever p<=6. It strengthens the earlier
N34 p<=4 theorem `6k<=r+6z`. The old theorem remains valid and its historical
proof is preserved. In N34's final state k=13,z=8,r=26, (7) would require
`104<=90`. The stronger statement also permits p=5, which the old cutoff did
not. Changing the cutoff, rather than simply dropping its hypothesis, is
what justifies that extension.

The coefficient 4h is the largest integer cutoff for which (4) has C=hT
with incoming cap P=3h. This is a property of this ramp and local domain,
not an optimality claim for all graph inequalities or all potentials.

## 5. Individual source capacities: exact maxima with no solver

Compatibility and distinct selected labels give

`H_u<=c_u=min(a-rho_u, #{i:h<=s_i<=rho_u})`.

We may therefore replace (4) by the exact restricted maximum

`C(h,T,P,c)=max_{0<=H<=c, 0<=p<=P} g_(h,T)(H,p)`.          (8)

This maximum has an elementary evaluation using at most five pieces. Put
m=min(h,c). For H<=h, g is nondecreasing in p, so set p=P. The three pieces
in H are

| Integer H interval, intersected with [0,m] | Cost |
|---|---|
| H<=h-P | HT+hP |
| h-P<=H<=T-P | hP+H(h+T-P-H) |
| H>=T-P | h(H+P) |

The first and third pieces increase with H. The middle is a concave quadratic;
its maximum is at the integer nearest its vertex, clipped to its interval.
For H>h, the cost is convex in p because its slopes are h-H and h, so only
p=0 and p=P need be considered. For either endpoint p,

`g=hp+H(T-p-H)_+`.

Its maximum over h+1<=H<=c is hp plus the nonnegative maximum of the same
concave quadratic over h+1<=H<=min(c,T-p), or zero if that interval is empty.
These formulas are implemented in `bounds.py` and independently checked
against direct enumeration. They apply at every a,b; there is no fixed-order
enumeration in the statement of the theorem.

## 6. Eliminate the residual profile: new tail and demand inequalities

Now assume positive surplus t, so every rho_u>=1 and
`r<=S-2t`, where S=sum_i s_i. Put delta=b-a. Suppose

`delta<=2h+1`.

Then, for u in Z_h,
`(rho_u+delta-1-3h)_+ <= rho_u-h`.
Residual activity outside Z_h gives

`sum_{Z_h}(rho_u-h) <= r-b-(h-1)z_h`.

Substitution in (6) proves

**`G_h(s) <= 2r-b+(3h+1)z_h`.**                          (9)

Consequently actual residual tails must satisfy

**`z_h >= ceil((G_h(s)-2S+b+4t)/(3h+1))`.**              (10)

This lower bound can be combined with the existing threshold-capacity lower
bound gamma_h(W_h), the trivial bound zero, and monotonicity z_h>=z_(h+1).
After closure, `r=b+sum_{h>=2}z_h<=S-2t` must still hold. This provides a
joint tail test before any residual states are enumerated.

For h>=2, residual activity also gives `z_h<=(r-b)/(h-1)`. Combining with
(9) gives the entirely demand-based inequality

**`(h-1)G_h(s)+4hb <= (5h-1)(S-2t)`**                    (11)

whenever delta<=2h+1. This bound has no residual-degree cap and no assumption
that all demands are positive. It follows from r<=S-2t, so it handles zeros
without assuming the stronger equality S=r+2t.

For N34's demand profile `(1^2,2^13)`, h=2 gives G=104,S=28,b=18,t=1.
Equation (10) requires z_2>=10, while r<=26 and b=18 allow z_2<=8.
Equivalently, (11) would require `248<=234`. The entire demand profile is
excluded without specifying or enumerating rho.

## 7. A low-demand infinite-family consequence

Suppose h>=2, positive surplus t, delta=b-a<=2h+1, and every demand belongs
to {0,1,h}. If k labels have demand h, then

`G_h=4hk`, `S<=a+(h-1)k`, and `k<=a`.

Apply (11) and rearrange:

`4hb+2(5h-1)t <= (5h-1)a+(h-1)^2 k <= h(h+3)a`.

Thus

**`(10h-2)t+4h delta <= h(h-1)a`.**                     (12)

In particular, if every demand is at most two and delta<=5,

**`9t+4delta<=a`.**                                     (13)

There is no assumption that residual degrees are also at most two. An initial
two-value residual derivation suggested this corollary; aggregating the excess
penalty in (6) removes that extra hypothesis. The statement is a candidate
infinite-family restriction on canonical graph data, not a complete theorem
for every graph in a maximum-degree band.

At the Turan edge count, `n=2a+delta+1` gives
`t=floor(n^2/4)-b(a+1)=floor((delta-1)^2/4)`.
For the next three dense degree bands, (13) gives:

| delta | Surplus at the Turan count | Necessary a for demands <=2 |
|---|---:|---:|
| 3 | 1 | a>=21 |
| 4 | 2 | a>=34 |
| 5 | 4 | a>=56 |

Graphs with higher demands are not covered by this corollary. These are exact
parameter consequences, not extrapolation from tested orders.

## 8. What the tests establish and what remains open

`check_local.py` separately enumerates the local source cost using indicator
sums, rather than the closed ramp/max formulas. It checks all h=1..12,
integer T=h..6h, P=0..5h, and H=0..T+1. The range beyond H=T is proved in
Section 3. These finite checks corroborate the hand proof; they do not prove
the unbounded parameter statement by extrapolation.

The complete preserved N34 equality and N35 two-layer domains are probed in
`probe_frontiers.py`. All h=1..max(s) are considered, first T=4h, then every
integer T=h..4a in both the uniform and individual-capacity versions.
The wider cutoffs and capacity refinements add no exclusions beyond T=4h in
this experiment. That negative result is preserved. It is not a claim that
they can never help on another domain.

The family supplies alternative hand exclusions for 595 states previously
handled by exact envelopes. The published N34/N35 ledgers remain unchanged;
this package records the new general results and their measured reach.
Many states survive the searched family. Their exact profiles, original
exclusions, search parameters and all successful witnesses are saved.

Invalid extensions are recorded too: keeping C=hT at T=4h+1 fails locally
at H=2h,p=0, and omitting the penalty when p=3h+1 fails at H=h. These are
counterexamples to proposed local inequalities, not graphs or counterexamples
to Murty–Simon. External review should focus on routing (1), endpoint-load
transport, the penalty aggregation and the distinction between these levels.
