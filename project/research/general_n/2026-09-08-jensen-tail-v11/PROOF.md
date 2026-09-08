# Jensen-centred demand-tail stability

**Status:** candidate hand/computer-assisted algebraic proof for independent review. Project direction: Paul Lenz. Derivation and drafting: ChatGPT/Geeps. 8 September 2026.

## 1. Setup and imported structural facts

Use the selected/residual construction of v9/v10. Put

    a=n-1-b,  b=Delta(G),  t=m-b(n-b),
    x_i=s_i/a,  y=(1/a)sum_i x_i=S/a^2,
    R=r/a^2,
    alpha=1-1/sqrt(2),  c=(3-2sqrt(2))/2.

We import the written candidate facts

    R >= (1/a) sum_i x_i^2/(1-x_i),
    R <= y-2c+2epsilon,
    (y-alpha)^2 <= epsilon(1-y),

where epsilon=(c a^2-t)/a^2, and the demand-tail capacity theorem

    W_h/a^2 <= 1/2 [ (z_h/a)^2 + (h/a)^2 ],

with z_h h<=r. These statements ultimately depend on the selected-incidence demand bound and supplement forcing. No finite-order computation is imported.

## 2. Exact Jensen-defect identity

Let

    g(x)=x^2/(1-x).

For every x,y<1,

    g(x)-g(y)-g'(y)(x-y)
      = (x-y)^2 / ((1-x)(1-y)^2).                         (2.1)

Averaging over the a labels kills the linear term because y is their mean. Therefore

    (1/a)sum_i g(x_i)-g(y)
      = 1/[a(1-y)^2] sum_i (x_i-y)^2/(1-x_i).             (2.2)

Since the left average is at most R, (2.2) and the upper residual budget give

    V := (1/a)sum_i (x_i-y)^2/(1-x_i)
      <= (1-y)^2 [ y-2c+2epsilon - y^2/(1-y) ].           (2.3)

If the bracket is negative, the assumed configuration is already impossible. This is a second stability estimate centred at the actual demand mean y rather than at alpha.

## 3. Fixed loss 1/300 for a>=50

**Candidate theorem.** If a>=50, then

    t < (c-1/300)a^2.                                     (3.1)

Suppose instead epsilon<=1/300. The alpha-centred stability inequality and

    0.2928<alpha<0.2929

force

    0.242 < y < 0.341.                                    (3.2)

The endpoint exclusions are exact:

    (0.2928-0.242)^2-(1/300)(1-0.242)
      = 253/4687500 > 0,

    (0.341-0.2929)^2-(1/300)(1-0.341)
      = 35083/300000000 > 0.

Also 2c>0.1715. Hence throughout the proof we may use the permissive residual upper bound

    R < y-K,   K=0.1715-2/300=989/6000.                  (3.3)

Set d=0.09 and theta=y-d. By (3.2), theta>0. Choose

    h=ceil(theta a).

A low label has s_i<h, hence x_i<theta=y-d. The function

    (y-x)^2/(1-x)

is decreasing for x<y, so each low label contributes more than

    d^2/(1-theta)=d^2/(1-y+d)

to the summand in V. If p is the fraction of low labels, (2.3) therefore gives

    p <= V(1-y+d)/d^2.                                    (3.4)

Low labels contribute less than theta p to the normalised demand y. Thus

    W_h/a^2 > y-theta p.                                  (3.5)

On the source side,

    z_h/a <= R/(h/a) < (y-K)/theta,

while a>=50 gives

    h/a <= theta+1/a <= theta+0.02.                       (3.6)

Substituting the permissive upper bound from (2.3) into (3.4), then (3.5), and comparing with the demand-tail capacity theorem shows that a configuration would require Q(y)<=0, where

    Q(y)= y-theta*pbar(y)
          - 1/2 [ ((y-K)/theta)^2 + (theta+0.02)^2 ],

    theta=y-0.09,
    pbar(y)= (1-y)^2 [ y-K-y^2/(1-y) ]
             * (1-y+0.09)/(0.09)^2.                       (3.7)

If the square bracket in pbar is negative, impossibility was already established; otherwise (3.7) is a valid upper bound for p.

After exact simplification,

    Q(y)=P(y) / [2430000(100y-9)^2],                      (3.8)

where

    P(y)=6000000000000 y^7
        -17654500000000 y^6
        +18813120000000 y^5
        - 9119933700000 y^4
        + 2234773372000 y^3
        -  290644878645 y^2
        +   20854785690 y
        -      723532716.

The denominator in (3.8) is positive on [0.242,0.341]. An exact Sturm sequence gives four sign variations at each endpoint, so P has zero real roots in that interval. Finally

    P(0.3)=4661739/20>0.

Therefore P, and hence Q, is positive throughout the entire permitted y interval. This contradicts the demand-tail capacity theorem and proves (3.1).

The Sturm calculation uses rational polynomial arithmetic only. `check_v11.py` implements it with Python's standard library `fractions`; SymPy or a numerical optimiser is not a proof dependency.

## 4. All-order degree consequence

**Candidate theorem.** For every n>=4,

    Delta(G)>=0.6116 n

implies

    m<floor(n^2/4).                                       (4.1)

Let beta=0.6116=1529/2500. If a=1, then every demand s_i is zero because 0<=s_i<=a-1. Hence S=0 and S>=r+2t gives t<=0. Under b=n-2>=beta n we have n>=6, and therefore

    m=b(n-b)+t <=2n-4 < floor(n^2/4).

Now suppose a>=2 and, for contradiction, m>=floor(n^2/4). Since n-b=a+1,

    b-n/2 >= ((beta-1/2)/(1-beta))(a+1)
            = (279/971)(a+1).

Thus

    t >= (279/971)^2(a+1)^2-1/4.                         (4.2)

Exact arithmetic gives

    (279/971)^2 = 77841/942841 > 0.08256,
    c-1/300 < 0.08256.

For a>=50, (4.2) is therefore strictly larger than (c-1/300)a^2, contradicting (3.1).

For 2<=a<=49 use the original t<=ca^2. The rational estimate c<0.08579 reduces the contradiction to

    0.08256(a+1)^2-1/4-0.08579a^2>0.

This is a concave quadratic. Its values at the interval endpoints are

    a=2:  3747/25000>0,
    a=49: 16821/100000>0.

Hence it is positive throughout 2<=a<=49. This proves (4.1).

## 5. Review scope

The genuinely new mechanism in this checkpoint is (2.2)--(2.3): near saturation of the residual charging budget forces the demand values to concentrate around their own mean. A threshold placed a fixed distance below that mean then forces most demand into a tail whose supplements compete for too few source pairs.

The degree-seven polynomial is only the final algebraic verification of this hand reduction. Correctness still depends on the graph-to-selected-system construction, selected-incidence demand inequality, supplement forcing and demand-tail pair-capacity theorem. Those remain the highest-value specialist review targets.

No best-known, novelty or priority claim is made here. The finite-order proofs and theorem ledger are unchanged.
