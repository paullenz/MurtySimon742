# Low-residual reservoir bound

13 September 2026. **Candidate general consequence of potential-pair capacity. External mathematical review and novelty assessment remain OPEN.**

This note turns the low-`c` / high-`q` product obstruction into an explicit upper bound for `Q` whenever selected-demand forcing guarantees a reservoir of vertices with small `c=q+rho`.

## 1. General low-c reservoir form

Let

```text
Q=sum_u q_u,
sigma=binom(b,2)-Q.
```

Fix an integer `R` and suppose at least `ell>0` vertices satisfy

```text
c_u=q_u+rho_u<=R.                                     (1)
```

By [`LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md`](LOW_C_HIGH_Q_CROSS_OBSTRUCTION.md), if

```text
U_R={u:q_u>=R+2},
u_R=|U_R|,
```

then

```text
ell*u_R<=sigma.                                       (2)
```

Residual activity gives `rho_u>=1`, hence universally

```text
q_u<=a-1.                                             (3)
```

Every vertex outside `U_R` has `q_u<=R+1`. Therefore

```text
Q
 <= (b-u_R)(R+1)+u_R(a-1)
 = b(R+1)+(a-R-2)u_R.                                 (4)
```

Assume

```text
a-R-2>=0.                                             (5)
```

Using (2):

```text
Q
 <= b(R+1)+(a-R-2)sigma/ell.                          (6)
```

Substitute `sigma=binom(b,2)-Q` and rearrange:

> **Low-c reservoir bound.** If (1) holds for at least `ell>0` vertices and `R<=a-2`, then
>
> ```text
> (ell+a-R-2)Q
> <= ell*b(R+1)+(a-R-2)binom(b,2).                    (7)
> ```

Equivalently,

```text
Q
 <= floor(
>     [ell*b(R+1)+(a-R-2)binom(b,2)]
>     /(ell+a-R-2)
>   ).                                                (8)
```

The floor is legitimate because `Q` is integral.

If `R>=a-2`, the universal source cap `q<=a-1` already makes the high-q class empty or trivial; (7) is not the useful regime.

## 2. All-positive-demand specialization

Assume every label has positive demand and define

```text
h=min_i s_i.                                          (9)
```

At every selected incidence `u-i`, the canonical bridge gives

```text
s_i<=rho_u.                                           (10)
```

Hence a source with

```text
rho_u<h                                                (11)
```

cannot carry any selected label at all. Therefore

```text
q_u=0,
c_u=rho_u<=h-1.                                      (12)
```

Let

```text
ell_h=#{u:rho_u<h}.                                   (13)
```

If `ell_h>0` and `h<=a-1`, apply (7) with `R=h-1`:

> **Low-residual reservoir bound, positive-demand form.** Every legal all-positive-demand branch satisfies
>
> ```text
> (ell_h+a-h-1)Q
> <= ell_h*b*h+(a-h-1)binom(b,2).                     (14)
> ```

or

```text
Q
 <= floor(
>     [ell_h*b*h+(a-h-1)binom(b,2)]
>     /(ell_h+a-h-1)
>   ).                                                (15)
```

This is selection-free once the scalar demand/residual multisets are fixed.

## 3. Zero-demand correction

Let

```text
z=#{i:s_i=0},
h=min{i:s_i>0}.                                       (16)
```

For a source with `rho_u<h`, no positive-demand label can be selected there. Selected labels at a source are distinct, so only the `z` zero-demand labels are available:

```text
q_u<=z.                                               (17)
```

Thus

```text
c_u=q_u+rho_u<=z+h-1.                                 (18)
```

Again let

```text
ell_h=#{u:rho_u<h}.                                   (19)
```

Apply (7) with

```text
R=z+h-1.                                              (20)
```

provided `z+h-1<=a-2`, equivalently `z+h<=a-1`. We obtain

> **Low-residual reservoir bound, zero-demand form.** If `ell_h>0` and `z+h<=a-1`, then
>
> ```text
> (ell_h+a-z-h-1)Q
> <= ell_h*b(z+h)+(a-z-h-1)binom(b,2).                (21)
> ```

This is weaker than the positive-demand form when `z>0`, as expected: low-rho sources may spend selected degree on activated zero-demand labels.

## 4. Coupling to the demand lower bound

The canonical ledger gives

```text
Q=sum_i x_i>=S=sum_i s_i>=r+2t.                       (22)
```

Therefore any upper bound `U_Q` from (15) or (21) excludes the scalar branch whenever

```text
r+2t>U_Q,                                             (23)
```

and more sharply whenever the actual known `S>U_Q`.

This provides a direct route from the potential-pair theorem back to the scalar `(a,b,t,s,rho)` catalogue without enumerating q-vectors.

## 5. Interpretation

A low-residual vertex below the minimum positive demand is unusable as a selected source (apart from the explicit zero-demand correction). It therefore remains low in the combined coordinate `c=q+rho`. Potential-pair capacity then says that every high-q source loses that vertex as a possible missing neighbour. A large reservoir of such vertices sharply limits the number of high-q sources; (7) converts that local incompatibility into an explicit bound on total selected degree.

The inequality is especially promising in regimes where demand forcing produces many small-rho vertices but `Q` must be large because `S>=r+2t`.

## 6. Trust boundary

The algebra is elementary once selected-incidence demand forcing and the low-c/high-q cross obstruction are accepted. Its Murty-Simon application inherits the trust boundary of the canonical bridge and potential-pair theorem. Passing the inequality does not imply graph feasibility or prove the unrestricted conjecture.
