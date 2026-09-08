# A sharper one-threshold stability consequence

**Status:** candidate hand proof for independent review. Project direction: Paul Lenz. Derivation and drafting: ChatGPT/Geeps. 8 September 2026.

## 1. Imported structural facts

Use the selected/residual construction and notation of the v9 threshold-capacity continuation. Put

- a=n-1-b, where b=Delta(G),
- t=m-b(n-b),
- s_i=max(0,d_i-R_i), S=sum_i s_i,
- rho_u for residual source degrees and r=sum_u rho_u,
- alpha=1-1/sqrt(2), c=(3-2sqrt(2))/2.

The argument imports the following already-written candidate lemmas, and no finite-order computation:

1. every selected incidence ui has s_i<=rho_u;
2. for selected ui->w, w neighbours every other selected label at u;
3. for h>=1, with T_h={u:rho_u>=h}, z_h=|T_h| and W_h=sum_{s_i>=h}s_i,

   W_h <= (z_h^2+h^2)/2;

4. the charging-defect identity

   c a^2-t = sum_i (s_i-alpha a)^2/(a-s_i) + (Gamma+tau)/2,

   where Gamma,tau>=0;
5. consequently, with delta=c a^2-t, epsilon=delta/a^2 and y=S/a^2,

   (y-alpha)^2 <= epsilon(1-y),

   and r/a^2 <= y-2c+2epsilon.

The proof of the demand-tail theorem is in the preceding continuation and does not require positive surplus.

## 2. Fixed quadratic loss for a>=25

**Candidate theorem.** If a>=25, then

    t < (c-1/750)a^2.                                      (2.1)

Suppose instead epsilon<=1/750.

We use the rational brackets

    0.2928 < alpha < 0.2929,
    2c > 0.1715.

They follow from

    1.41421 < sqrt(2) < 1.41422.

The stability inequality forces

    0.2614 < y < 0.323.                                    (2.2)

Indeed, at y=0.2614,

    (0.2928-y)^2 > (1/750)(1-y),

and at y=0.323,

    (y-0.2929)^2 > (1/750)(1-y).

The relevant functions are monotone away from alpha, so values outside this interval also fail.

Set

    theta=0.227,    h=ceil(theta a).

Call a label low when s_i<h. Since h-1<theta a, every low label has x=s_i/a<theta<alpha. The function

    f(x)=(alpha-x)^2/(1-x)

is decreasing on [0,alpha]. At theta, using alpha>0.2928,

    f(theta) > (0.2928-0.227)^2/(1-0.227)
             = 108241/19325000
             > 1/180.

The dispersion term in the charging-defect identity is at most epsilon a^2. Hence, if L is the number of low labels,

    L/a < 180/750 = 0.24.                                  (2.3)

The low labels contribute less than theta*0.24 to S/a^2. Therefore

    W_h/a^2 > y-theta*0.24.                                (2.4)

On the source side, z_h h<=r and h>=theta a, so

    z_h/a <= (r/a^2)/theta
            <= (y-2c+2epsilon)/theta
            < (y-K)/theta,                                 (2.5)

where

    K=0.1715-2/750 = 0.168833333... .

Also a>=25 gives

    h/a <= theta+1/a <= 0.267.                              (2.6)

The demand-tail capacity theorem, (2.4)--(2.6), would therefore require

    y-theta*0.24
      < 1/2 [ ((y-K)/theta)^2 + 0.267^2 ].                  (2.7)

But define

    Q(y)=y-theta*0.24
         -1/2 [ ((y-K)/theta)^2 + 0.267^2 ].

This is a concave quadratic. Its minimum on the interval [0.2614,0.323] occurs at an endpoint. Exact rational arithmetic gives

    Q(0.2614) = 81744504311/927522000000 > 0,
    Q(0.323)  =  2090899511/927522000000 > 0.

Thus Q(y)>0 throughout the interval, contradicting (2.7). This proves (2.1).

The proof deliberately uses one threshold only. No numerical optimiser is a proof dependency.

## 3. All-order maximum-degree consequence

**Candidate theorem.** For every n>=4, if

    Delta(G) >= 0.6126 n,

then

    m < floor(n^2/4).                                      (3.1)

A universal vertex gives a star and is immediate. Otherwise a=n-1-b>=1. Assume for contradiction m>=floor(n^2/4).

Put beta=0.6126=3063/5000. Since n-b=a+1,

    b-n/2 >= ((beta-1/2)/(1-beta))(a+1)
            = (563/1937)(a+1).

Hence, allowing the worst odd-order rounding,

    t >= (563/1937)^2 (a+1)^2 - 1/4.                      (3.2)

Exact rational comparisons give

    (563/1937)^2 > 0.08448,
    c-1/750 < 0.08448.

Moreover 0.08448(a+1)^2-1/4>0.08448a^2 for every a>=1. Thus if a>=25, (3.2) contradicts (2.1).

For 1<=a<=24 use the original charging bound t<=ca^2. The rational estimates

    (563/1937)^2 > 0.08448,
    c < 0.086

reduce the required contradiction to

    0.08448(a+1)^2 - 1/4 - 0.086a^2 > 0.

The left side is a concave quadratic in a. At a=1 it equals 6/3125>0, and at a=24 it equals 1507/500>0. Hence it is positive throughout 1<=a<=24.

This proves the candidate implication (3.1).

## 4. Scope and review priorities

This result depends on the graph-to-selected-system construction, the selected-incidence residual-demand inequality, supplement forcing, the demand-tail pair-capacity theorem, and the charging-defect identity. Those are the places for specialist scrutiny.

It does not use the n=28 finite computation, Fan's numerical bound, the weak-core route, residual activity, or deletion-preserves-criticality.

The 0.6126 constant is intentionally conservative. A discretised multi-threshold relaxation suggests additional room, but no stronger theorem is claimed without a reviewable exact argument.
