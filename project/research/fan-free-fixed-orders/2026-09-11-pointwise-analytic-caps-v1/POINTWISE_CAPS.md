# Pointwise charging caps that remove upper-range computation

11 September 2026. Research directed by Paul Lenz. Triggered by a blind external-assistant red-team of the n=29 proof; algebra and cross-order propagation independently rechecked by ChatGPT/Geeps.

**Status:** candidate hand mathematics. These are direct consequences of the already-used charging inequality and therefore reduce computational dependencies; they do not introduce a new graph-theoretic hypothesis.

## 1. Common charging inequality

In the standard complement/residual setup, with `a=|A|`, `b=|B|` and surplus

```text
t = m-b(n-b),
```

the bridge gives

```text
sum_i s_i(a+1-2s_i)/(a-s_i) >= b+2t,       (1)
```

for integer demands `0<=s_i<=a-1`.

A pointwise upper bound on the summand therefore gives an immediate analytic cap on `t`.

## 2. The a=12 bound

For every integer `0<=s<=11`,

```text
s(13-2s)/(12-s) <= 5/2.                    (2)
```

Indeed

```text
5/2 - s(13-2s)/(12-s)
  = (s-4)(4s-15)/(2(12-s)).                (3)
```

The denominator is positive. For integers `s=0,1,2,3`, both numerator factors are negative; at `s=4` the expression is zero; for integers `s>=5` both factors are positive. Hence (2) holds, with equality only at `s=4`.

With twelve labels, the right side of (1) is therefore at most `30`.

### 2.1 n=29, Delta=16

Here

```text
a=12, b=16,
m=208+t.
```

Equation (1) and (2) give

```text
16+2t <= 30,
```

so

```text
t<=7,
m<=215.                                      (4)
```

Thus **every n=29, Delta=16 scope with m>=216 is excluded by hand**. The former generic zero-survivor scan over `m=216..232` is no longer a logical dependency.

At the boundary `t=7` (`m=215`), (1) requires equality in all twelve pointwise bounds. Equality in (2) is possible only for `s=4`, so

```text
s_1=...=s_12=4,
S=48.
```

The charging lower bound before elimination is

```text
r-b >= sum_i s_i(s_i-1)/(a-s_i)
     = 12*(4*3/8)
     = 18,
```

hence `r>=34`. But `S>=r+2t` gives `48>=r+14`, so `r<=34`. Therefore

```text
r=34.                                          (5)
```

Let `z_4` be the number of residual sources with degree at least four. Residual activity gives every one of the sixteen sources a baseline degree one, hence

```text
r >= 16+3z_4.
```

By (5),

```text
z_4 <= floor((34-16)/3)=6.                    (6)
```

Threshold capacity at `h=4` gives

```text
2W_4 <= z_4^2-z_4+4*5.
```

Here `W_4=48`, so the left side is `96`, while (6) makes the right side at most

```text
6^2-6+20 = 50.
```

Contradiction. Hence **m=215 is also excluded entirely by hand**.

Consequently the only n=29, Delta=16 upper-range scopes requiring finite computation are now

```text
m=212,213,214,
```

while `m=215` and every `m>=216` are analytic hand cases.

### 2.2 n=30, Delta=17

Here again `a=12`, now `b=17`, and

```text
m=221+t.
```

The same pointwise cap gives

```text
17+2t <= 30,
```

so `t<=6`, hence

```text
m<=227.                                      (7)
```

Thus every `n=30, Delta=17` scope with `m>=228` is excluded analytically. The former explicit zero-domain scan over `m=228..255` is no longer needed logically. The boundary `m=227` (`t=6`) remains the small 15-profile threshold calculation already preserved in the repository.

### 2.3 n=28, Delta=15

Here `a=12`, `b=15`, and

```text
m=195+t.
```

The same cap gives

```text
15+2t <= 30,
```

so `t<=7`, hence

```text
m<=202.                                      (8)
```

Thus every `n=28, Delta=15` scope with `m>=203` is excluded analytically. The former report that the charging domain is empty at `m=203..210` is correct but no longer needed as a computational proof event. The `m=202` boundary still has 15 charging-feasible demand profiles and remains covered by the existing exact threshold computation.

## 3. The a=13 bound

For every integer `0<=s<=12`,

```text
s(14-2s)/(13-s) <= 8/3.                    (9)
```

Indeed

```text
8/3 - s(14-2s)/(13-s)
  = 2(s-4)(3s-13)/(3(13-s)).              (10)
```

The denominator is positive. For integer `s<=4`, the two numerator factors have the same sign or one is zero; for integer `s>=5` both are positive. Equality occurs only at `s=4`.

With thirteen labels the total is at most

```text
13*(8/3)=104/3.
```

### 3.1 n=30, Delta=16

Here `a=13`, `b=16`, and

```text
m=224+t.
```

Equation (1) and (9) give

```text
16+2t <= 104/3,
```

so integer `t<=9`, hence

```text
m<=233.                                      (11)
```

Thus every `n=30, Delta=16` scope with `m>=234` is excluded analytically. The former generic statement that the charging domain is empty for `m=234..240` is correct but no longer a computational dependency. The `m=233` boundary remains the nine-profile threshold calculation already preserved.

## 4. Exact charging-domain census at n=29, Delta=16

As an independent front-end cross-check, the complete nondecreasing integer demand domains for `a=12,b=16` are

```text
t=2: 9251
t=3: 4867
t=4: 2032
t=5:  586
t=6:   79
t=7:    1
t=8:    0
```

These counts agree with the repository's earlier generators. The unique `t=7` profile is `(4,4,...,4)`, exactly as forced analytically above.

## 5. Effect on proof architecture

These pointwise caps should be preferred wherever they apply because they remove whole edge ranges from the finite search:

- `n=28, Delta=15`: computation is unnecessary for `m>=203`;
- `n=29, Delta=16`: computation is unnecessary for `m>=215` (with `m=215` handled by the threshold hand contradiction above and `m>=216` by the 5/2 cap);
- `n=30, Delta=17`: computation is unnecessary for `m>=228`;
- `n=30, Delta=16`: computation is unnecessary for `m>=234`.

Historical workflows and checkpoints should remain preserved for auditability, but current reviewer-facing proofs should not cite them as logical dependencies when a shorter exact hand argument is available.
