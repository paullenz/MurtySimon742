# Exact primitive integer potential for the n=29, t=2 frontier

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite common-potential result, independently replayed in integer arithmetic over all 902 regenerated positive-demand zero-slack `n=29, Delta=16, m=210` frontier profiles. Conditional on the candidate graph-to-RX-Hall bridge. This is not an unrestricted Murty–Simon theorem.

## 1. Result

Let

```text
B_{D,V}(d,v) = 1[d>=D and v>=V],
J_c(d,v)     = 1[d+v>=16-c].
```

Then the following single coordinatewise nondecreasing integer-valued potential works for every one of the 902 frontier profiles:

```text
F(d,v) =
   11 B_{2,11} + 12 B_{2,12} + 28 B_{2,13} +  8 B_{2,14}
 + 41 B_{3,0}  +  8 B_{3,4}  +  8 B_{3,7}  +  8 B_{3,8}
 + 11 B_{3,10} +  5 B_{3,12}
 +  5 B_{4,2}  +  5 B_{4,3}  +  6 B_{4,6}  +  8 B_{4,9}
 + 15 J_2 + 14 J_0.
```

No floating-point arithmetic is needed to interpret this potential. The exactifier fixed these primitive integer weights up to one common positive factor, found profile-specific scalar/envelope coefficients numerically only as proposals, then accepted the complete certificate only after direct Python-integer checking. A separately written standard-library verifier rebuilt all finite inequalities without importing the LP builder or exactifier and replayed the same integer certificate.

Preserved checkpoint:

`checkpoints/N29_T2_SUPPORT16_FIXED_INTEGER_EXACT_RUN_34464748811.json`

Workflow artifact SHA-256:

`3f19c45e3483cd5cef27939a1d335b93018836c5bea951c809bc2f197f0ea1d8`

The exact run checked 334,159 inequalities in 20,551 variables. There were zero row violations and zero bound violations. With denominator `10^6`, the worst profile margin numerator was `-1,999,912`, versus the required `-1,000,000` before dividing out the common factor 2. Hence after dividing every certificate coefficient by 2, the primitive potential displayed above still leaves strict negative margin (`-0.999956` or better) on every profile.

## 2. Step-function form

Write

```text
F(d,v) = A2(v) 1[d>=2] + A3(v) 1[d>=3] + A4(v) 1[d>=4]
       + 15 J_2(d,v) + 14 J_0(d,v).
```

The three monotone step functions are

```text
A2(v):
  0                 v<=10
  11                v=11
  23                v=12
  51                v=13
  59                v>=14

A3(v):
  41                0<=v<=3
  49                4<=v<=6
  57                v=7
  65                8<=v<=9
  76                10<=v<=11
  81                v>=12

A4(v):
  0                 v<=1
  5                 v=2
  10                3<=v<=5
  16                6<=v<=8
  24                v>=9.
```

Thus the common Hall geometry is only three horizontal `d` layers, plus two one-dimensional slack-majorization thresholds.

## 3. Original-variable interpretation

For a label state,

```text
d = R+s,
v = 16-(R+x).
```

Therefore a rectangle `B_{D,V}` is exactly

```text
1[R+s>=D and R+x<=16-V].
```

For a source state,

```text
d = rho+q-1,
v = 16-(q+p),
```

so the same rectangle is

```text
1[rho+q-1>=D and q+p<=16-V].
```

The diagonal terms lose the internal transport variables entirely:

```text
J_2(label) = 1[x-s<=2],
J_2(source)= 1[p-rho+1<=2],

J_0(label) = 1[x=s],
J_0(source)= 1[p-rho+1<=0].
```

Consequently the last two terms are exactly the cumulative slack-transport inequalities `DST_2` and `DST_0`, not fitted LP artefacts.

## 4. What remains computational

The global potential `F` is now fixed, exact, small-integer, and common to all 902 profiles. The only profile-specific objects remaining are the scalar/envelope coefficients in the potential-certificate lemma (`lambda`, `c`, `mu`, selected threshold weights `tau_j`, and the envelope values `ell_s`, `sigma_rho`).

This is a substantial reduction in the symbolic target. Since `F` is fixed, there is **no cross-profile coupling left**. Each frontier profile can now be viewed as a small independent scalar-envelope inequality. The next task is to classify those scalar coefficients, identify a bounded set of recurring patterns, and replace them by explicit formulas or a small parameter-derived case split.

## 5. Immediate symbolic target

Use the potential-certificate lemma to prove, for every admissible profile in the target parameter band, a strict gap

```text
sum_i ell_{s_i} + sum_u sigma_{rho_u} > lambda sum_u rho_u
```

with the displayed primitive `F` (or its parameterized analogue), without solving an LP.

The first diagnostic is to mine the exact 902 profile certificates for:

1. which `tau_j` are actually nonzero;
2. how many distinct normalized `(lambda,c,mu,tau)` rays occur;
3. whether those rays are determined by simple statistics of the demand and residual-degree profiles;
4. whether the apparent `D={t,t+1,t+2}`, `DST_0`, `DST_t` geometry survives the n=30 falsification laboratory.
