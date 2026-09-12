# Rigidity at equality in the heavy-load bound

12 September 2026. Candidate all-parameter hand lemma. External mathematical
review and novelty assessment OPEN. Use the canonical bridge and the notation
of the [heavy-load family](../2026-09-12-heavy-load-family-v1/HEAVY_LOAD_FAMILY.md):
h>=1, Z={u:rho_u>=h}, z=|Z|, W=sum_{s_i>=h}s_i,
G=sum_{s_i>=h}max(4h,s_i), and r=sum rho_u.

Suppose every source in Z has supplement indegree p<=P, where P is an
integer and 0<=P<=3h. Put

`Jmax=max(0,min(z-2h, floor(Pz/(P+2h))))`,
`B_h(z,P)=h(z+Jmax)`.

Then the general load inequality has the following strictness criterion:

**`W>B_h(z,P) => G<=r+4hz-1`.**                          (1)

Equivalently, equality G=r+4hz forces W<=B_h(z,P). This is an explicit
integer inequality with no maximization over local types, no multiplier
search, and no residual-degree enumeration.

## Proof

The earlier source cost at T=4h is

`g(H,p)=hH+hp+H max(0,4h-max(h,H+p))-hH[H>h]`.

For 0<=p<=3h, g<=4h^2. Equality occurs only in the following two cases:

- H=h, with any 0<=p<=3h;
- H=2h and p=0.

For H<h and h<=H+p<=4h, the deficit is
`4h^2-g=(h-H)(4h-H-p)>0`, since p<=3h. Below that interval, p<h-H and g=4hH+hp<h^2+3hH<4h^2.
Above it, H+p<=H+3h<4h prevents equality.
For H=h, direct substitution gives equality throughout 0<=p<=3h.
For H>h in the active ramp,
`g=4h^2-(H-2h)^2-(H-h)p`; outside the active ramp,
`g=hp<=3h^2<4h^2`. This proves the classification.

If G=r+4hz, every inequality in the preceding load proof is tight. In
particular every source in Z attains its local maximum. Thus every H is
h or 2h, and every source in J={u:H=2h} has p=0. Write j=|J|.

All 2hj heavy arcs from J end in Z. None can end in J, since those vertices
have incoming degree zero. Each high sender therefore needs 2h distinct
destinations in Z minus J. If j>0,

`z-j>=2h`, and `2hj<=P(z-j)`.

The first inequality uses distinct selected unordered pairs; the second is
the total incoming capacity of the remaining destinations. Hence j<=Jmax.
For j=0 the same upper bound is harmless because Jmax>=0. In fact, if heavy
labels are present, full equality rules this case out: max(4h,s)<=4s for
s>=h, so G<=4W<=4h(z+j). Therefore r<=4hj, while r>=hz>0. Thus
j>=ceil(r/(4h))>=1 at nontrivial equality. This uses global label information
which is absent from the local maximum classification alone. Finally

`W<=sum_Z H=h(z+j)<=h(z+Jmax)=B_h(z,P)`.

This proves the equality restriction. Since the quantities in the original
bound G<=r+4hz are integers, its contrapositive gives the one-unit improvement
(1). No assumption that heavy degree H equals total selected degree q is used.

## Demand-only use

In the [tail projection](TAIL_PROJECTION.md), positive surplus gives r<=M.
For a candidate tail z_h=z, beta_h(z)<=D and

`rho<=Rmax=min(a,d+D-beta_h(z))` on Z.

Thus one may take P=Rmax+b-a-1. When 0<=P<=3h:

- G>M+4hz already excludes z by the preceding load bound;
- G=M+4hz and W>B_h(z,P) excludes z by the new equality restriction.

In the second case any possible graph would have to have r=M and equality
in the load bound, exactly the situation just ruled out. Excluding initial
z values yields a new lower tail; monotone closure can then exclude the whole
profile when its total residual cost exceeds M.

## A concrete new lower tail

At a=15,b=18,t=1, take the demand profile

`s=(0,1,2,2,3^11)`.

Here S=38, M=36. The preceding lower tails are L_2=9,L_3=8, with all higher
L zero. Thus D=1,d=3. At h=3,z=8, beta=0 and Rmax=4, so P=6<=9.
Also G=132=M+4hz, W=33, and

`Jmax=max(0,min(8-6,floor(6*8/12)))=2`,
`B_3(8,6)=3*(8+2)=30<33`.

Therefore z_3>=9. The full projected inequality separately gives z_2>=10;
together these demand 18+10+9=37 residual incidences, exceeding M=36.
This is one of the two profile exclusions requiring the combination of new
tails in the finite application. The scalar equality lemma supplies the
z_3 step directly; the z_2 step still uses a recorded projected certificate.

The indegree hypothesis is essential. An initial draft overstated the role
of the j=0 case; the global argument above corrects that explanation without
changing the stated bound. The draft record and exhaustive local checks are
preserved in the audit evidence.
These results do not improve the 7/12 maximum-degree theorem by themselves.
