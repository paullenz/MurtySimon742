# Typed cross-witness hole ledger in the all-R equality pinch

Date: 2026-09-20

Status: **internal conditional sharpening**. This note continues `CROSS_EDGE_RESERVOIR_SHARPENING.md`; all 20 September audit caveats remain binding.

## 1. Exact typed witness loads

For `y>=2`, let the at-least `R=gy` outside-certified X--Y edges be split between:

- `bar C` witnesses, with total selected X-source load `R_C` and `s_C` used physical witnesses;
- `bar d` witnesses, with total selected Y-source load `R_D` and `s_D` used physical witnesses.

Then

`R_C+R_D=R`,

`s_C<=R_C<=s_C x`,

`s_D<=R_D<=s_D y`,

and `s_C+s_D<=d-m`, where m is the disjoint internal-X witness population.

The exact type-aware slack floor is

> `P_cross >= [R_C-s_C F]_+ + R_D+s_D(p-y-1)`,          `(TYPED-PAY)`

with `F=[x-p+1]_+`.

This refines the type-relaxed `[R-(s_C+s_D)F]_+` floor. In a broad diagnostic it changes relatively few rows, which is useful evidence that the more important unexploited resource is the **location** of the cross-witness holes rather than their scalar slack alone.

## 2. X-side hole ledger

A `bar C` cross witness certifying `R_C` selected X-sources is nonadjacent to those R_C sources. A `bar d` cross witness has graph-fixed X-neighbourhood consisting of its unique X-head; by `A0-CODE` that head is not `a_0`, so it misses exactly `x-1=N` X-vertices.

Therefore the missing X--U incidence count gains

> `Z_X >= Z_X^0+NJ+e+m+R_C+s_D N`.                     `(ZX-TYPED)`

This is a physical incidence statement, not a score relaxation.

## 3. Total A--U hole ledger

The fixed-head localization also gives:

- every used `bar C` cross witness misses the other `y-1` Y-vertices;
- every used `bar d` cross witness misses `x-1` X-vertices;
- the selected source-witness nonedges contribute the total R load.

Hence

> `Z >= Z_0+NJ+e+m(y+1)+R+s_C(y-1)+s_D(x-1)`.          `(Z-TYPED)`

The extra columns are disjoint from the core, buffer, z, purified J-set and internal-X witness columns.

## 4. Typed Hall inequality

Combining `(ZX-TYPED)` with exact Hall and the type-aware U-slack floor gives

> `e >= B_d+m+P_int(e,m)+P_cross+R_C+s_D N`.            `(H-TYPED)`

This is the strongest local Hall form currently available in the literal all-R equality pinch without adding a new structural hypothesis.

## 5. Focused e(X)=0 replay

A focused diagnostic was run on the daily-audited bounded parameter box, restricting to the dominant `e(X)=0` slice and retaining exact pair-local capacity, the strengthened a0 population bill, typed cross slack, `(ZX-TYPED)`, `(Z-TYPED)`, the J independent-set q ceiling and rooted residual gate.

The number of abstract parameter rows admitting at least one typed `e(X)=0` tuple is:

> **62,800**,

split as:

- **58,193** with `y>=2`;
- **4,607** with `y=1`.

This is a slice diagnostic only. It is **not** the total survivor count after `(H-TYPED)`, because a row whose `e=0` realization is removed may still admit an `e>0` tuple. No total count is promoted here.

## 6. Failed follow-on and pivot

The natural idea “apply raw criticality again to the cross witness--head edge” does **not** automatically create a new witness obligation. If w certifies `source -> head` with `N(source) cap N(w)={head}`, then the existing source itself certifies the triangle edge `w--head` in the orientation sourced at w. Thus witness-head criticality can recycle the original certificate and is not, by itself, a new hole source.

This obstruction is worth preserving: the next attack should not count a second certificate merely by reapplying edge criticality to the witness-head edge.

The better next target is to exploit simultaneous load from **multiple** sources on one fixed-head witness, or to derive a two-witness interaction between distinct fixed heads. Any such argument must create genuinely new physical incidences rather than recycled certificates.
