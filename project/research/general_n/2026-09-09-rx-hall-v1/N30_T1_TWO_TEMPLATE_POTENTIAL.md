# n=30, t=1: exact 13-term 3D potential with two rational scalar templates

10 September 2026. Research direction: Paul Lenz. Mathematical development and internal checking: ChatGPT/Geeps.

**Status:** exact finite RX-Hall certificate across the seven preserved hard `(a,b,t,dmax)=(13,16,1,11)` profiles, conditional on the graph-to-profile bridge and `POTENTIAL_CERTIFICATE_LEMMA_3D.md`. This is a falsification/compression result for the general-N research programme. It is **not** a new dependency of the existing fixed-order n=30 candidate proof and is not an unrestricted Murty-Simon theorem.

## 1. Why n=30 was used

The n=29,t=2 work produced a compact BC-rectangle + diagonal-slack potential. Rather than generalising from one order, n=30,t=1 was deliberately used as a falsification laboratory.

The seven hard profiles were recovered from the original non-expired GitHub Actions artifact from run `34348486247`:

```text
artifact id:   10102703529
artifact name: n30-bc-upper-set-cut-generation
SHA-256:       399397f3bad85e6de6b6ae4c8b14342d538c03fd80ffe5e1289063c0ee0c57e6
```

That historical exact BC upper-set run records seven hard rows, six exact BC rejections and one survivor. The survivor is zero-based hard position 0.

## 2. Falsification result

The first parameter-derived test used

```text
BC d-layers D = {1,2,3},
diagonal slack thresholds c = {0,1},
no SH term.
```

Floating reconnaissance found certificates for hard positions `1,...,6` individually but not position `0`. A deliberately over-generous follow-up gave position 0 all BC rectangle layers `D=1,...,11` and all diagonal thresholds; it still produced no certificate numerically.

This was useful failure rather than a reason to add arbitrary terms. The missing coordinate was then tested directly.

Among the simple SH rectangles scanned on the natural source range, the single term

```text
1[s>=2]
```

was sufficient to restore a certificate for the exceptional profile. These negative/minimality scans used floating LP/MIP reconnaissance and are **not proof events**. Only the positive rational certificate below is promoted as exact evidence.

## 3. Exact primitive global potential

Write

```text
d = R+s,
h = R+x,
v = 16-h.
```

For sources use

```text
alpha = rho+q-1,
beta = q+p,
w = 16-beta.
```

The exact common potential is the coordinatewise nondecreasing 3D function

```text
Phi(s,d,v)
 =  7  1[d>=1,v>=7]
 + 11  1[d>=1,v>=10]
 +  5  1[d>=1,v>=12]
 + 21  1[d>=1,v>=13]
 + 29  1[d>=1,v>=14]
 + 39  1[d>=1,v>=15]
 +  6  1[d>=2,v>=12]
 +  5  1[d>=3,v>=8]
 +  8  1[d>=3,v>=9]
 + 11  1[d>=3,v>=11]
 + 17  1[d+v>=15]
 +  8  1[d+v>=16]
 + 39  1[s>=2].
```

There are 13 nonnegative generators. The weights are primitive (`gcd=1`) and sum to 206.

The last term is the only SH correction. Since every admissible state has `v>=0`, it is exactly the SH rectangle `(S,V)=(2,0)`.

The validity of this mixed BC/SH/slack potential is covered by `POTENTIAL_CERTIFICATE_LEMMA_3D.md`: on every selected incidence

```text
(s,d,v) <= (rho,alpha,w)
```

coordinatewise, so the incidence transport inequality holds for every nondecreasing `Phi`.

## 4. Two exact scalar templates

With this single common `Phi`, all seven profiles are covered by just two fixed rational scalar templates.

### Template A — hard positions 0 and 1

```text
lambda = 33
c      = 91/6
mu     = 143/3

tau_2 = 1
tau_3 = 27/4
tau_6 = 1/10
tau_9 = 11/5
all other tau_j = 0
```

The exact strict gaps after taking the finite envelope minima are

```text
position 0: 27/5
position 1: 1/2
```

### Template B — hard positions 2 through 6

```text
lambda = 33
c      = 76/5
mu     = 89/2

tau_2 = 17/8
tau_3 = 41/5
tau_6 = 1/10
tau_8 = 9/10
tau_9 = 3/2
all other tau_j = 0
```

The exact gaps are

```text
position 2: 333/20
position 3: 7/10
position 4: 1369/20
position 5: 674/5
position 6: 11/20
```

Thus the minimum strict gap over all seven profiles is `1/2`.

## 5. Solver-free exact replay

Run

```sh
python3 -I -B project/research/general_n/2026-09-09-rx-hall-v1/n30_t1_two_rational_templates_exact.py
```

The checker uses only Python's standard library and `fractions.Fraction`. It hard-codes the seven frozen profile vectors, the 13 primitive potential weights and the two displayed templates. For every demand value and residual source degree it exhaustively reconstructs the finite label/source state ranges, computes the envelope minima exactly, and verifies the displayed positive gap.

No LP solver, MIP solver, floating point or saved dual vector is used in acceptance.

## 6. Discovery/minimisation provenance

For transparency, the displayed potential was found in stages:

1. three-layer + `c={0,1}` BC/slack test: one exceptional profile remained numerically;
2. single SH scan: `(S,V)=(2,0)` restored that profile;
3. one common potential then covered all seven with profile-specific scalar bookkeeping;
4. greedy support deletion reduced to 13 active generators;
5. a bounded support MIP with global generator upper bound 100 also returned optimum support size 13 with zero reported MIP gap;
6. fixing that support and requiring integer global weights gave the displayed weight vector, with reported objective sum 206 and zero MIP gap;
7. the seven scalar vectors were compressed to two common templates and then manually rationalised to the simple fractions above;
8. final acceptance was rerun from scratch in exact `Fraction` arithmetic.

Steps 1-6 are discovery/reconnaissance. Solver optimality and infeasibility statuses are not promoted as exact mathematical claims. Step 8 is the proof-relevant finite check.

## 7. Interpretation

The n=30 falsification lab did **not** confirm the naive idea that three BC layers plus the two `t=1` slack levels would suffice unchanged. It identified a precise missing feature: the first monotone-coupling coordinate `s<=rho`.

The encouraging part is how small the repair is. The older pairwise-staircase exploration used several SH staircase corrections for the exceptional n=30 state. In the present 3D-potential language, the required SH information collapses to the elementary threshold

```text
sum_i x_i 1[s_i>=2] <= sum_u q_u 1[rho_u>=2],
```

which is simply the incidence transport inequality for `1[s>=2]`.

This suggests a more promising general-N architecture:

```text
few t-derived BC layers
+ few diagonal slack thresholds
+ one or a small number of demand/residual-degree thresholds.
```

The next appropriate test is not theorem promotion. It is to derive a parameter rule for the location of the SH threshold and test that rule against a fresh frontier (n=31 if a complete comparable frontier can be generated), while keeping the graph-to-RX-Hall bridge as the principal external-review trust boundary.