# Tight total-demand threshold obstruction

12 September 2026. Research direction: Paul Lenz. Development and internal
audit: ChatGPT/Geeps. **Candidate universal graph lemma; external review OPEN.**

This lemma uses the [canonical bridge](../2026-09-11-canonical-bridge-v1/CANONICAL_BRIDGE.md)
and no numerical solver. It isolates a reusable equality obstruction already
visible in some fixed-order arguments.

## Statement

Use the bridge variables with positive surplus `t>0`. Let

`S=sum_i s_i`, `r=sum_u rho_u`, and `b=|B|`.

Suppose an integer `h>=2` satisfies:

1. every label has demand `s_i>=h`;
2. with `Z={u:rho_u>=h}` and `z=|Z|`, the threshold is exactly tight:

   `S=C_h(z)=[z(z-1)+h(h+1)]/2`.

Then necessarily

`b+2t <= h(h+1)`.

Consequently these conditions are impossible whenever `b+2t>h(h+1)`.
No fixed order, uniform source degree, or demand equality profile is assumed.

## Proof

Every selected label has demand at least h. Selected-incidence forcing sends
every selected source into Z. Put `X=sum_i x_i=sum_{u in Z} q_u`.
Let `J={u in Z:q_u>h}` and `j=|J|`. The bridge's threshold-capacity proof gives

`S <= X <= (z-j)h + jz - j(j+1)/2 <= C_h(z)=S`.

All inequalities are equalities. In particular, `X=S`; since `x_i>=s_i`
pointwise, `x_i=s_i` for every label. As every demand is positive,
`d_i=R_i+s_i=R_i+x_i`.

The last inequality has exact slack

`[(z-h-j)(z-h-j-1)]/2`.

Therefore `j=z-h` or `j=z-h-1` (only nonnegative feasible values are allowed).
Every source in `Z\J` must contribute exactly h selected incidences; those
in J contribute more than h. Thus **every source in Z is active**.

For each `u in Z`, choose a selected incidence with label i. Endpoint load
and source-degree forcing give

`q_u+p_u <= R_i+x_i=d_i <= rho_u+q_u-1`,

hence `p_u<=rho_u-1`. Residual activity on all b sources implies

`sum_{u in Z} p_u <= sum_{u in Z}(rho_u-1) <= r-b`.                 (1)

Every selected arc from J has its exception in Z, by the same heavy-label
supplement argument used in threshold capacity. Such arcs contribute to
the incoming count on Z, so

`sum_{u in Z} p_u >= sum_{u in J}q_u`

`= S-(z-j)h >= S-h(h+1)`.                                      (2)

Combining (1), (2), and the bridge demand inequality `S>=r+2t` gives

`r+2t-h(h+1) <= r-b`,

which is exactly the claimed bound. QED.

## Application at n=34, m=291

The one state left by the fixed nine-rectangle envelope has

`s=(5^9,6^6)`, `rho=(1^5,4,5^6,6^6)`, `b=18`, `t=3`.

Here `S=81`, `r=75`, `h=2`, `z=13`, and `C_2(13)=81`. The lemma requires
`24=b+2t<=6`, impossible. Equivalently, incoming selected exceptions into Z
number at least `81-6=75`, whereas endpoint forcing permits at most
`75-18=57`.

## Audit boundary

The equality step must establish that all selected incidences are heavy and
that every source in Z is active. Both follow explicitly above; neither is
assumed for a generic threshold subset. In particular, this lemma must not
be applied unchanged to profiles containing demands below h or zero demands.
The retained numerical envelope failure is a failure to find that particular
certificate, not a feasible graph and not evidence against this hand proof.
