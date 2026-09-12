# Joint routing projected onto demand and residual tails

12 September 2026. Candidate general lemmas; external mathematical review,
novelty assessment and external reproduction OPEN. The finite applications
are checked separately from the graph-to-inequality implications.

## 1. The unallocated residual budget

Use the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md)
with a labels, b sources, positive surplus t, demands s_i, total demand S,
and M=S-2t. Positive surplus gives rho_u>=1 for every source, rho_u<=a,
and r=sum rho_u<=M. Set z_l=#{u:rho_u>=l}, so

`r=b+sum_{l=2}^a z_l`.

Let L_1=b and L_2>=...>=L_a>=0 be any proved integer lower bounds on these tails.
They may come from ordinary heavy capacity, the preceding load family, or
other established necessary conditions. Define

`D=M-b-sum_{l=2}^a L_l`,
`d=max({1} union {l:L_l>0})`.

If D<0, the profile is already excluded. Otherwise D is the entire residual
budget left after the lower tails have been paid for. In particular,

**`rho_u<=min(a,d+D)` for every source u.**                (1)

Fix h<=d and suppose z_h=z, where z>=L_h (at h=1 take z=b). Put

`beta_h(z)=sum_{l=2}^h max(0,z-L_l)`,
`E_h(z)=sum_{l=h+1}^a L_l+D-beta_h(z)`.

Necessarily

**`beta_h(z)<=D`,**                                      (2)
**`sum_{u:rho_u>=h}(rho_u-h)<=E_h(z)`,**                   (3)
**`rho_u<=min(a,d+D-beta_h(z))` for u with rho_u>=h.**     (4)

Thus raising one tail consumes budget both at that threshold and at lower
thresholds which must rise with it. It also tightens the largest possible
individual residual degree. These statements require no enumeration of
residual-degree distributions.

### Proof

Monotonicity gives z_l>=max(L_l,z) for 2<=l<=h. The lower tails therefore
consume at least sum_{l=2}^h L_l+beta_h(z). Subtracting them from r-b<=M-b
proves (3), and subtracting the remaining lower bounds proves (2).

For u in Z_h, at every level l>h the other sources contribute at least
max(0,L_l-1). Hence

`(rho_u-h)+sum_{l=h+1}^a max(0,L_l-1)`
`<=sum_{l=h+1}^a z_l<=E_h(z)`.

Because the positive lower tails are consecutive through d and h<=d,
`sum_{l>h} L_l-sum_{l>h}(L_l-1)_+=d-h`.
Substitution gives (4). Taking h=1 yields (1).

The lower bound rho>=1, supplied by positive surplus, is essential. These
are inequalities for canonical data, not assertions that every permitted
integer tail sequence is realized by a graph.

### Two closed consequences

If D=0, every tail is forced: z_l=L_l and r=M. The residual multiset is
therefore determined by the demands and their lower tails, with exactly
L_l-L_(l+1) sources of degree l. There is no residual search to perform.

If a constant run of m lower-tail values ends at h, with
`L_(h-m+1)=...=L_h=c` and h-m+1>=2, then

**`z_h<=c+floor(D/m)`.**

Indeed beta_h(z_h)>=m(z_h-c). This quantifies how a flat stretch of lower
bounds limits further growth of its final tail.

## 2. A demand-only joint-routing inequality

Fix h<=d with at least one demand >=h, and take T=4h. Write

`W=sum_{s_i>=h}s_i`, `G=sum_{s_i>=h}max(4h,s_i)`,
`f(L)=max(0,4h-max(h,L))`, `Rmax=min(a,d+D-beta_h(z))`.

For each candidate value z with beta_h(z)<=D, retain the local integer triples

`h<=rho<=Rmax`,
`0<=H<=min(a-rho, #{i:h<=s_i<=rho})`,
`0<=p<=min(rho+b-a-1,b-1-H)`.

These domains contain every actual heavy source. They do not prescribe a
residual distribution. Let C be their largest possible H. The number j of
sources with H>h lies in 0,...,z (only j=0 if C<=h). The old pair-capacity
condition excludes a candidate j when

`W>(z-j)min(h,C)+min(jC,K_j)`,
where `K_j=j(z-j)+j(j-1)/2`.

For arbitrary nonnegative rational lambda, mu, eta and kappa, set

`A_e = max { (h+eta)H+H f(H+p) -(lambda+mu)eH`
`             +lambda min(p,j-e)-kappa(rho-h) :`
`             (rho,H,p) in the local domain, [H>h]=e }`.

Only classes with nonzero population are needed. Then, for the actual z,j,

**`hG <= hM+kappa E_h(z)+(z-j)A_0+jA_1+mu K_j-eta W`.**  (5)

This depends only on a,b,t, the demands, the proved lower-tail bounds and
chosen scalar parameters. It contains no unknown residual-degree tuple.

### Proof

The [joint-routing lemma](../2026-09-12-joint-routing-pilot-v1/JOINT_ROUTING_LEMMA.md)
bounds hG+eta W by hr+mu K_j plus the sum of its corrected local costs.
Subtract kappa(rho-h) inside each local maximum, then restore at most
kappa E_h(z) using (3). There are exactly z-j low-heavy-degree sources and
j high-heavy-degree sources. Finally hr<=hM. All correction multipliers
are nonnegative, so each replacement is in the required upper-bound direction.

Multiplying by a common denominator makes every local maximum and final gap
an integer. A numerical optimizer may propose parameters; only strict exact
gaps are accepted.

## 3. New tail bounds and profile exclusions

For a fixed h and candidate z, exclude z only after every possible j has
been excluded. If all z=L_h,...,q-1 are excluded, then z_h>=q. If all z up
to b are excluded, the whole demand profile is impossible. Otherwise combine
the proved new lower bounds by monotone closure and require

`b+sum_{l=2}^a new_L_l<=M`.

The published experiment uses the preceding heavy-load package's proved
closed tails as L, in one pass. It does not repeatedly assume its own
unverified output as a new input. The general implication permits later
iterations once each new bound has been proved.

This is a general necessary-condition family and a way to exclude profiles
before residual enumeration. It does not establish a new maximum-degree
threshold or an unrestricted Murty–Simon proof.
