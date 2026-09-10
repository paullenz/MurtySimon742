# Five exact scalar templates for the n=29, t=2 frontier

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite reduction using the primitive 16-term integer potential. A standard-library `Fraction` checker verifies the five displayed templates cover all 902 regenerated positive-demand zero-slack `n=29, Delta=16, m=210` frontier profiles. Repository CI replay is provided by `general-rx-hall-n29-t2-five-scalar-exact.yml`. This remains conditional on the candidate graph-to-RX-Hall bridge and is not an unrestricted Murty–Simon theorem.

## 1. Fixed global potential

Use the exact primitive potential already preserved in
`N29_T2_PRIMITIVE_INTEGER_POTENTIAL.md`:

```text
F(d,v) =
   11 B_{2,11} + 12 B_{2,12} + 28 B_{2,13} +  8 B_{2,14}
 + 41 B_{3,0}  +  8 B_{3,4}  +  8 B_{3,7}  +  8 B_{3,8}
 + 11 B_{3,10} +  5 B_{3,12}
 +  5 B_{4,2}  +  5 B_{4,3}  +  6 B_{4,6}  +  8 B_{4,9}
 + 15 J_2 + 14 J_0.
```

The global potential is common to every profile. The only remaining choices in the potential-certificate lemma are the nonnegative scalar coefficients `lambda,c,mu,tau_j`; the envelope values are then exact finite minima, not independent fitted data.

## 2. Five rational templates

Omitted coefficients are zero.

### Template A0

```text
lambda = 32
c      = 9
mu     = 97/3
tau_2  = 23/4
tau_3  = 17/3
tau_4  = 25/2
```

Exact coverage: 538/902 profiles. Minimum positive gap: `1/2`.

### Template A1

```text
lambda = 32
c      = 71/4
mu     = 15/2
tau_3  = 232/7
tau_5  = 17/2
tau_6  = 3
```

Exact coverage: 857/902 profiles. Minimum positive gap: `15/28`.

### Template A79

```text
lambda = 394/13
c      = 44
tau_2  = 532/13
tau_3  = 13
tau_4  = 99/7
```

Exact coverage: 823/902 profiles. Minimum positive gap: `20/91`.

### Template A82

```text
lambda = 0
c      = 209/3
tau_2  = 424/9
tau_3  = 115/4
```

Exact coverage: 759/902 profiles. Minimum positive gap: `1/3`.

### Template A94

```text
lambda = 32
c      = 263/6
tau_2  = 335/6
tau_3  = 37/4
tau_5  = 13/6
tau_7  = 14/5
```

Exact coverage: 822/902 profiles. Minimum positive gap: `11/15`.

The union of these five exact covers is all 902 profiles. Coverage is highly redundant: 467 profiles satisfy all five templates and 305 satisfy four. Only a small boundary population selects the case split.

## 3. Why this is a substantial compression

The first exact common-potential certificate still carried profile-specific scalar/envelope blocks across 902 profiles. The global Hall/slack potential has now been reduced to 16 small integers, and the remaining scalar layer has been reduced from hundreds of numerical solutions to **five fixed rational vectors**.

For each vector there is no optimization left. The checker computes

```text
L_s(lambda,c) = min_{R,x} [lambda R + c x + x F(R+s,16-R-x)]
```

and

```text
S_{rho,qmax}(c,mu,tau)
 = min_{q,p} [mu(q-p) - c q
              + sum_j tau_j T_j(rho,q,p)
              - q F(rho+q-1,16-q-p)]
```

exactly over the finite admissible state ranges, and tests

```text
sum_i L_{s_i} + sum_u S_{rho_u,qmax(u)}
    > lambda sum_u rho_u.
```

Thus the five-template verification is finite rational arithmetic applied directly to the potential-certificate lemma. There is no LP solver in the checker.

## 4. How the five cases were found

Cross-testing the exact profile-specific scalar certificates first showed that one inherited scalar ray could cover 838 profiles and two covered 896, but an exact set-cover over those inherited rays still required seven templates. That was a property of the solver-selected rays, not of the mathematics.

Re-optimising common scalar vectors over groups of profiles produced a much stronger 889-profile common case. A small-denominator rationalisation of that case retained exactly the same 889 profiles with exact minimum gap `11/15`.

The remaining compatibility geometry exposed five difficult anchors, indexed `0,1,79,82,94`. Numerical common-template tests indicate they are pairwise incompatible inside this fixed-potential scalar architecture, giving a five-template lower-bound heuristic. Rather than use the 889 case plus five exceptions, the final exact cover redesigns the anchor-1 and anchor-79 templates to absorb the three otherwise uncovered profiles `8,39,145`:

```text
A1  is constrained to cover 1,8,39;
A79 is constrained to cover 79,145.
```

The resulting five rational templates cover all 902 exactly.

**Important:** the pairwise-incompatibility/lower-bound statement is currently numerical reconnaissance, not an exact proof that five templates are minimal. The five-template *upper bound / cover* itself is exact.

## 5. Mathematical interpretation

This changes the symbolic problem materially. The n=29,t=2 endpoint is no longer “902 computational cases.” It is:

1. one fixed 16-term monotone Hall/slack potential;
2. five fixed scalar combinations of the elementary resource inequalities;
3. exact envelope minima depending only on `s` and `(rho,qmax)`;
4. a five-way finite profile case split.

The next goal is therefore to find simple profile statistics deciding which of A0, A1, A79, A82 or A94 applies, and then express those decisions in the global parameters `(a,b,t,r)` rather than in n=29 profile indices.

A particularly promising structural clue remains the geometry

```text
D = {t,t+1,t+2},
slack thresholds c = {0,t},
```

which is exact for the current t=2 potential and survives the n=29,t=3 falsification probe numerically. The correct next test is to derive parameter-based case conditions from the five exact scalar envelopes and then challenge those conditions on n=30 before using n=31 as a further falsification laboratory.
