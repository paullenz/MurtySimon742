# Exact geometry-quantified margin exclusion: N34 state 227

13 September 2026. **Candidate hand proof; external review OPEN.** This example shows that the exact-demand interval lemma can eliminate an entire selected-geometry fibre with fixed row/column margins. It is stronger than rejecting one stored selected set, but it is **not** a whole scalar-state exclusion because other `q`-vectors and `x>s` remain unquantified.

## 1. Frozen scalar data and the margin class

Take the preserved `n34-m289` state `227`:

```text
a=15, b=18, t=1,
s = 2^4, 3^11,
rho = 1^7, 2, 3^10.
```

Hence

```text
Q=sum s_i=41,
r=sum rho_u=39.
```

Consider the exact-demand margin class `x=s` with source selected degrees

```text
q = 0^7, 4, 3,3, 4,4,4,4,4,4,3,4.
```

Thus among the ten `rho=3` active sources, three have `q=3` and seven have `q=4`; the unique `rho=2` source has `q=4`.

We prove that **no choice of the selected sets `S_u` with these row and column margins can satisfy the canonical endpoint/forcing constraints.**

## 2. Incoming capacity is one unit below the sum of maxima

Because `x=s`, the exact-demand corollary gives `p_u<=rho_u-1` at every active source.

The seven inactive `rho=1` sources retain the ordinary canonical bound

```text
p_u <= rho_u+b-a-1 = 1+18-15-1 = 3.
```

The unique active `rho=2,q=4` source, call it `u_*`, has

```text
p_* <= 1.
```

Each of the ten active `rho=3` sources has

```text
p_u <= 2.
```

Therefore the sum of these individual maxima is

```text
7*3 + 1 + 10*2 = 42.
```

But the canonical ledger gives

```text
sum_u p_u = Q = 41.
```

All `p_u` are nonnegative integers. Hence **exactly one source is one unit below its displayed maximum and every other source is at its maximum.**

## 3. The four demand-two labels are forced through the rho=2 source

The selected-edge forcing `s_i<=rho_u` applies to every selected incidence. The source `u_*` has `rho=2`, so it cannot select any of the eleven demand-three labels. It has `q_*=4`, and there are exactly four demand-two labels. Therefore it selects all four of them.

Each demand-two label has selected degree `x_i=s_i=2`, so it needs exactly one further selected source.

Under exact demand the interval lemma says every label selected by `u` has

```text
q_u+p_u <= C_i <= rho_u+q_u-1,
```

where `C_i` is its raw B-cross degree.

The relevant source intervals are:

```text
rho=2,q=4:  p=0 -> C in {4,5};   p=1 -> C=5.
rho=3,q=3:  p=2 -> C=5;          p=1 -> C in {4,5}.
rho=3,q=4:  p=2 -> C=6;          p=1 -> C in {5,6}.
```

We now use the unique one-unit incoming deficit.

## 4. Three deficit locations give the same mod-three contradiction

First suppose the unique deficit occurs at one of:

1. `u_*` itself (`p_*=0`);
2. one of the seven inactive `rho=1` sources; or
3. one of the three `rho=3,q=3` sources.

In all three cases, every non-deficient `rho=3,q=4` source has the singleton interval `C=6`, whereas each demand-two label containing `u_*` must have `C<=5` (and in cases 2-3 exactly `C=5`). Therefore none of those high `q=4` sources can supply the second incidence of a demand-two label.

The second incidences of the four demand-two labels must all come from the three `rho=3,q=3` sources. Those three sources have

```text
3*3=9
```

selected incidences in total. Four are consumed by the demand-two labels, leaving exactly five incidences on demand-three labels.

Any demand-three label containing a `q=3` source has `C<=5`; it cannot also contain a non-deficient `rho=3,q=4` source, which forces `C=6`. The source `u_*` cannot select demand-three labels. Hence a demand-three label touched by the `q=3` class must receive all three of its selected incidences from that class.

The number of `q=3` incidences on demand-three labels must therefore be divisible by three. It is five. Contradiction.

This covers deficit locations 1-3.

## 5. Deficit at a rho=3,q=4 source

It remains to suppose that the unique deficient source is one of the seven `rho=3,q=4` sources. Then

```text
p_*=1,
```

so all four demand-two labels have `C=5`. Their second incidences may come from a `rho=3,q=3` source (`C=5`) or from the unique deficient `rho=3,q=4` source (`C in {5,6}`), but not from any of the other six `q=4` sources, which force `C=6`.

Let `k` of those four second incidences come from the deficient `q=4` source. Then:

- the `q=3` class has `9-(4-k)=5+k` incidences left for demand-three labels;
- the deficient `q=4` source has `4-k` incidences left for demand-three labels.

Thus at most

```text
(5+k)+(4-k)=9                         (5.1)
```

selected incidences remain from sources capable of participating in a `C=5` demand-three label.

Now use total raw B-cross degree. Since `x=s`,

```text
sum_i C_i = sum_i(R_i+x_i) = r+Q = 39+41 = 80.
```

The four demand-two labels each have `C=5`, contributing `20`. Every demand-three label has `C=5` or `6`: a `q=3` source forces 5, a non-deficient `q=4` source forces 6, and the sole deficient `q=4` source cannot fill a three-incidence label by itself.

Therefore the eleven demand-three labels have total C-degree `60`. If `h` of them have `C=6`, then

```text
5*11+h=60,
```

so `h=5`: exactly five have `C=6` and **six have `C=5`**.

Those six `C=5` demand-three labels require

```text
6*3=18
```

selected incidences from sources compatible with `C=5`, contradicting the upper bound `9` in (5.1).

## 6. Conclusion

Every possible location of the unique incoming-capacity deficit is impossible. Hence there is no selected-incidence family satisfying the stated fixed margins

```text
rho = 1^7,2,3^10,
q   = 0^7,4,3,3,4,4,4,4,4,4,3,4,
x=s = 2^4,3^11
```

together with the canonical endpoint and selected-edge forcing conditions.

This is an **all-selected-geometries exclusion for one `(q,x)` margin class**. It does not exclude state 227 itself: alternative row margins `q`, selected excess `x>s`, and ultimately graph realization remain open.
