# Threshold source–supplement capacity: explicit continuation

8 September 2026. Project direction: Paul Lenz. Derivation and drafting: ChatGPT/Geeps.

**Status: candidate hand arguments for independent review.** This note supplies an explicit derivation from the established selected/residual construction. It does not claim external acceptance, a completed all-order Murty–Simon proof, an exhaustive novelty assessment, or formal verification of its counting arguments. The regression program at the end is supplied for execution; no new execution report is asserted here. The unfinished earlier v9 storage upload and the frozen finite-order editions are not modified by this note.

## 1. Setup and the two structural properties needed

Let G be a finite simple diameter-two edge-critical graph with n vertices, m edges and maximum degree b. Distances between disconnected vertices are infinite. A universal vertex forces G to be a star: an edge between other vertices would be redundant. Handle that case separately.

Put H=complement(G). Choose v of minimum H-degree a=n-1-b, let A=N_H(v), B=V(H) minus N_H[v], C=H[A], and F=complement(C) on A. Thus |A|=a and |B|=b. The case considered below has a>=1.

For each missing unordered B-pair uw, select exactly one cross quasi-edge ui->w (or the opposite orientation), with i in A. Its endpoints totally dominate H except for the unique vertex w, and both uw and iw are absent in H. This exists directly: G-uw has a pair at distance greater than two, so H+uw has an adjacent total dominating pair. H has none. That pair cannot be {u,w}, since it misses v; it uses an existing edge incident with u or w. Its auxiliary belongs to A to dominate v. The only newly dominated vertex is the opposite endpoint of uw.

Distinct missing B-pairs select distinct cross edges. At a source, selected labels and their supplements are distinct. Every unordered B-pair supports at most one oriented selected arc; opposite orientations are not independent resources. All other existing A–B edges are residual.

Write rho_u and R_i for residual degrees at B and A, r for their common total, q_u for actual selected outdegree, x_i for actual selected label degree, d_i=d_F(i), and

    t=m-b(n-b), s_i=max(0,d_i-R_i), S=sum_i s_i.

Then

    e(F)=r+t, sum_i d_i=2(r+t), sum_i R_i=sum_u rho_u=r,
    x_i>=s_i, S>=r+2t, q_u+rho_u<=a.

Minimum H-degree proves x_i>=s_i. Actual x_i need not equal s_i.

The two structural properties used below are:

(A) Every selected incidence ui satisfies s_i<=rho_u.

(B) For selected ui->w, the supplement w neighbours every other selected label at u.

For (A), every F-neighbour j of i neighbours u. At most rho_u of the edges uj are residual. Each remaining uj is selected, with a distinct supplement w_j different from w. The edge ui forces iw_j. This edge is residual, because i and w_j both miss j in A, whereas every selected edge has its sole exception in B. Therefore d_i<=rho_u+R_i, proving (A).

For (B), selected uj has an exception different from w and must dominate w. Since uw is absent, jw exists. No positive-surplus or residual-activity assumption is used in either argument.

## 2. A demand-tail capacity theorem

Fix an integer h>=1. Call label i heavy when s_i>=h. Define

    T_h={u in B:rho_u>=h}, z_h=|T_h|,
    W_h=sum_{i:s_i>=h} s_i.

All actual selections of heavy labels originate in T_h, by (A). Let ell_u count actual heavy-label selections at source u, and let X_h=sum_{u in T_h} ell_u. Thus W_h<=X_h.

A vertex outside T_h cannot select any heavy label. Consequently every one of its neighbours among heavy labels is residual, and it has at most h-1 such neighbours.

If ell_u>h, the supplement of each heavy selection at u must belong to T_h: property (B) requires it to neighbour the other ell_u-1>=h heavy labels, impossible outside T_h. The outgoing heavy arcs of such a source are all internal to T_h.

Let j be the number of sources in T_h with ell_u>h. The other z_h-j sources contribute at most (z_h-j)h heavy arcs. Arcs from the j high-load sources use distinct unordered pairs of T_h with at least one high-load endpoint. There are at most

    j(z_h-j)+binom(j,2)=j*z_h-j(j+1)/2

such pairs. Hence

    W_h <= X_h <= z_h*h+j(z_h-h)-j(j+1)/2.                 (2.1)

If z_h<h, there is no heavy label: any such label needs at least h distinct sources in T_h. Therefore W_h=0.

If z_h>=h, put k=z_h-h. Maximising the integer quadratic in (2.1) over 0<=j<=z_h gives its maximum at j=k or k-1 (at j=0 when k=0). Thus

    W_h <= h*z_h+binom(z_h-h,2).                          (2.2)

A convenient weaker bound, valid in all cases, is

    W_h <= (z_h^2+h^2)/2.                                (2.3)

Indeed the right side of (2.1) equals

    (z_h^2+h^2)/2 - (j-(z_h-h))^2/2 - j/2.

This proves the theorem. The proof uses actual heavy selections, not an assumption that all selected degrees equal their minimum demands. It allows arbitrary non-heavy labels, arbitrary extra selected incidences, and zero residual degrees outside T_h.

## 3. Arbitrarily many spare sources

Suppose h=max_u rho_u>=1 and exactly h+k sources have residual degree h, where k>=0. All demands are at most h. If M labels have demand h, then W_h=Mh and z_h=h+k. Equation (2.2) gives

    M <= h+k+floor(k(k-1)/(2h)).                          (3.1)

There is no upper restriction on k in this statement.

In particular:

- k=0 gives M<=h.
- k=1 gives M<=h+1, stronger than the earlier candidate upper bound 2h.
- k=2 gives M<=h+2 for h>=2; when h=1 it gives M<=4.

For example, h=3 and five maximum-residual sources permit at most five demand-three labels: six would require 18 heavy selections, whereas (2.2) permits at most 3*5+1=16.

These are necessary-condition bounds, not classifications of actual extremal critical graphs. Sharpness for actual graphs is not asserted. No positive-surplus assumption is needed.

## 4. Exact charging-defect identity

For a>=1, every demand satisfies 0<=s_i<=a-1. Choose exactly s_i actual selected incidences at each label i. If q'_u is the chosen count at source u, then q'_u<=a-rho_u, and each incidence has rho_u>=s_i.

The increasing weight x/(a-x), distributed along those chosen incidences, gives

    r >= D := sum_i s_i^2/(a-s_i).

Rows with rho_u=a have no selected incidences and need not distribute their residual cost. Let

    alpha=1-1/sqrt(2), c=(3-2sqrt(2))/2,
    Gamma=S-r-2t=sum_i max(0,R_i-d_i)>=0,
    tau=r-D>=0.

The elementary identity

    (3-2sqrt(2))*a - s(a-2s)/(a-s)
      = 2(s-alpha*a)^2/(a-s)

gives the exact decomposition

    c*a^2-t = sum_i (s_i-alpha*a)^2/(a-s_i) + (Gamma+tau)/2.   (4.1)

In particular t<=c*a^2. Write delta=c*a^2-t, e=delta/a^2, and y=S/a^2. Weighted Cauchy–Schwarz applied to (4.1) yields

    (y-alpha)^2 <= e(1-y).                               (4.2)

This identity quantifies demand dispersion and the unused charging budget separately. It does not assume t>0.

## 5. An explicit fixed quadratic improvement

**Candidate theorem.** If a>=100, then

    t < (c-1/1250)*a^2.                                  (5.1)

Proof. Suppose instead e<=1/1250. We use only exact rational comparisons and 0.2928<alpha<0.2929.

Equation (4.2) implies

    0.2686 < y < 0.3164.                                 (5.2)

For the upper endpoint, (0.3164-0.2929)^2>(1/1250)(1-0.3164). For the lower endpoint, the function (0.2928-y)^2/(1-y) is decreasing for y<0.2928, and at y=0.2686 its numerator is 14641/25000000, while (1/1250)(1-0.2686)=14628/25000000. Both endpoints therefore violate (4.2), as do values beyond them.

Since 2c>0.1715 and Gamma>=0, (5.2) gives

    r/a^2 <= y-2c+2e < 0.3164-0.1715+0.0016=0.1465.

Set h=ceil(0.23a), and let L count labels with s_i<h. For each such label, s_i/a<0.23. The function (alpha-x)^2/(1-x) is decreasing on 0<=x<alpha. Its value at 0.23 is

    kappa=10929/7700-sqrt(2)>1/195.

Thus each low label contributes more than a/195 to the nonnegative sum in (4.1), and

    L/a < 195/1250=0.156.

The threshold source count satisfies

    z_h/a <= (r/a^2)/0.23 < 293/460 < 0.637.

Heavy demands consequently require

    W_h/a^2 > 0.2686-0.23*0.156=0.23272.                 (5.3)

But a>=100 implies h/a<=0.24, so (2.3) gives

    W_h/a^2 <= (0.637^2+0.24^2)/2=0.2316845,             (5.4)

contradicting (5.3). The strict gap is 2071/2000000. This proves (5.1).

All irrational estimates can be checked by squaring rationals. For example sqrt(2)<70711/50000, whose square exceeds 2, implies kappa>1/195. The argument is deliberately conservative; no optimality claim is made for 1/1250.

## 6. A conservative all-order maximum-degree consequence

**Candidate theorem.** For every n>=4, a diameter-two edge-critical graph satisfying

    Delta(G)>=0.6129*n

has

    m<floor(n^2/4).                                      (6.1)

This is an improvement to the project's earlier 0.6132704598 coefficient, not a claimed best-known literature result without completed novelty review.

Proof. A universal vertex gives a star, with n-1<floor(n^2/4) for n>=4. Otherwise a=n-1-b>=1. Suppose m>=floor(n^2/4), and put

    d=(1129/3871)^2.

From b>=0.6129n one obtains b-n/2>0 and

    b-n/2 >= (1129/3871)(a+1).

Thus, accounting for odd n by the worst-case subtraction 1/4,

    t >= (b-n/2)^2-1/4 >= d(a+1)^2-1/4.                 (6.2)

Exact rational arithmetic gives d>17/200=0.085. Also

    c-1/1250=937/625-sqrt(2)<0.085,
    c-1/1250>1/12.

If a>=100, (6.2) is strictly larger than (c-1/1250)a^2, contradicting (5.1).

For 1<=a<=99, use the original t<=ca^2 and c<43/500=0.086. The lower bound (6.2) exceeds 0.086a^2 because

    (17/200)(a+1)^2-1/4-(43/500)a^2
       =(-a^2+170a-165)/1000>0.

The numerator is concave and positive at both endpoints 1 and 99 (values 4 and 6864). This covers all remaining a. No finite graph enumeration, Fan estimate, total-domination classification, weak-core transfer or residual-activity lemma is needed.

## 7. Review scope and next work

The main new mechanism is that low-residual vertices cannot supply sufficiently many neighbours among heavy labels. This forces the selected arcs of a heavy-loaded source back into the same limited source set. An unordered pair cannot be spent twice. Equations (2.1)–(2.2) express the resulting competition exactly.

The numerical coefficient change is modest. The qualitative advance is an explicit fixed quadratic loss, not merely exclusion of equality or a finite list of profiles. Improving the conservative estimates in Section 5, using several thresholds jointly, and studying equality/sharpness of the spare-source bound are natural further targets.

The previously recorded Lean 4.19.0 run 34166620020 checked five local quasi-edge logical lemmas from commit 93a7cdc5ff2a3677d9985941a5df0c4ad08bd1f6. It did not formalise the existence/selection construction, finite injections, this threshold theorem, the stability identity or the 0.6129 consequence. No such larger formalisation is claimed here.

Independent mathematical review, an executed fresh regression record for this continuation, a complete literature/priority assessment and verification of this note's GitHub publication remain separate obligations. The note must not be silently treated as a certified replacement for frozen proof inputs.

## 8. Standalone exact regression program (execution not asserted)

Save the following as check_threshold_capacity.py. It checks the displayed rational margins, the integer maximisation and the abstract oriented-pair counting lemma on all labelled oriented graphs of order at most five. These tests do not establish the universal graph-to-selected-system implication; that is the hand proof above.

```python
#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations, product
import json

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def constants():
    sqrt_lo, sqrt_hi = F(141421, 100000), F(70711, 50000)
    require(sqrt_lo**2 < 2 < sqrt_hi**2, 'sqrt brackets')
    al, au = F(183,625), F(2929,10000)
    require(2*(1-al)**2 > 1 > 2*(1-au)**2, 'alpha brackets')
    eps, low, high = F(1,1250), F(1343,5000), F(791,2500)
    require((al-low)**2 > eps*(1-low), 'lower y margin')
    require((high-au)**2 > eps*(1-high), 'upper y margin')
    require(3-2*sqrt_hi > F(343,2000), 'charging lower bound')
    require(F(10929,7700)-sqrt_hi > F(1,195), 'low label cost')
    rcap = high-F(343,2000)+2*eps
    require(rcap == F(293,2000), 'residual cap')
    require(rcap/F(23,100) < F(637,1000), 'source cap')
    needed = low-F(23,100)*195*eps
    allowed = (F(637,1000)**2+F(6,25)**2)/2
    require(needed-allowed == F(2071,2000000), 'quadratic contradiction')
    d=F(1129,3871)**2
    require(d>F(17,200), 'degree threshold')
    require(F(937,625)-sqrt_lo < F(17,200), 'improved coefficient upper bound')
    require(F(937,625)-sqrt_hi > F(1,12), 'rounding allowance')
    require(F(3,2)-sqrt_lo < F(43,500), 'old coefficient upper bound')
    for a in range(1,100):
        require(-a*a+170*a-165>0, 'small-a rounding')
    return {'quadratic_margin':str(needed-allowed), 'small_a_cases':99}

def spare_maximisation():
    cases=0
    for h in range(1,51):
        for k in range(51):
            z=h+k
            actual=max((z-j)*h+j*z-j*(j+1)//2 for j in range(z+1))
            require(actual==z*h+k*(k-1)//2, 'integer maximum')
            cases+=1
    return cases

def oriented_pair_test():
    graphs=checks=0
    for n in range(1,6):
        pairs=list(combinations(range(n),2))
        for choices in product(range(3),repeat=len(pairs)):
            out=[0]*n
            for (u,v),choice in zip(pairs,choices):
                if choice==1:
                    out[u] |= 1<<v
                elif choice==2:
                    out[v] |= 1<<u
            degrees=[mask.bit_count() for mask in out]
            graphs+=1
            for z in range(n+1):
                inside=(1<<z)-1
                for limit in range(n+1):
                    if any(degrees[u]>limit and out[u]&~inside for u in range(z)):
                        continue
                    q=sum(degrees[:z])
                    bound=max((z-j)*limit+j*z-j*(j+1)//2 for j in range(z+1))
                    require(q<=bound, 'oriented pair bound')
                    require(2*q<=z*z+limit*limit, 'square relaxation')
                    checks+=1
    # Opposite arcs invalidate the unordered-pair premise: do not admit them.
    require(2*12>4*4+1, 'negative control must violate the relaxed bound')
    return {'labelled_oriented_graphs':graphs,'admitted_checks':checks,
            'opposite_orientation_negative_control':'violates bound as expected'}

if __name__=='__main__':
    print(json.dumps({'constants':constants(),
                      'spare_maximisation_cases':spare_maximisation(),
                      'abstract_orientation':oriented_pair_test(),
                      'actual_critical_graph_enumeration':False,
                      'universal_graph_lemmas_formally_verified':False},indent=2))
```
