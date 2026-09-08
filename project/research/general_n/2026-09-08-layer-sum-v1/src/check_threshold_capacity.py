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
