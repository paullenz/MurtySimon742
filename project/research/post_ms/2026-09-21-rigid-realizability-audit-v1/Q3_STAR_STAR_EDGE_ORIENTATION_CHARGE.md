# Star-star edge orientation charge in the Q3 antipodal-transversal branch

Date: 2026-09-21

## Setup

Continue in the Q3-root antipodal-transversal branch. Let `S` denote the physical star-code vertices. For `x∈S` with centre c, write `Opp(x)` for the physical star vertices of centre `bar c`.

By `Q3_STAR_INCIDENT_A_EDGE_CERTIFICATE_CLASSIFICATION.md`, once a star-star edge `xy` is assigned a critical-pair certificate from the x side, exactly one of the following happens:

1. **direct:** y lies in `Opp(x)` and x,y have no common A-neighbour;
2. **antipode bridge:** y is the unique A-neighbour of x whose code contains `bar c`;
3. **third-star:** there is `z∈Opp(x)` with `xz` a nonedge, `yz` an edge, and y the unique common A-neighbour of x and z.

Every critical star-star edge has at least one endpoint side supplying a certificate, so choose one such side and orient the edge toward the chosen certificate source.

## Local injection

Fix a star x. Among edges oriented from x:

- at most one can use the antipode-bridge mechanism;
- every third-star oriented edge `x->y` determines an opposite-centre nonneighbour `z∈Opp(x)\N_A(x)` for which y is the unique common A-neighbour of x and z.

For fixed ordered pair `(x,z)`, there is at most one such y. Hence

`# { third-star edges oriented from x } <= |Opp(x)\N_A(x)|`.

This is a physical injection, not merely a code-type count.

## Global charge

Let

- `E_opp` = number of actual A-edges between opposite star-centre classes;
- `P_opp` = number of possible such physical pairs, i.e.

  `P_opp = sum_{ {c,bar c} } m_c m_{bar c}`;

- `M_opp=P_opp-E_opp` = number of missing opposite-centre star pairs;
- `E_nonopp` = number of star-star A-edges whose centres are not antipodal.

Direct certificates occur only inside `E_opp`. Every nonopposite edge must therefore, under the chosen orientation, use either an antipode-bridge certificate or a third-star certificate.

There are at most `|S|` antipode-bridge oriented edges globally, because each physical star supplies that mechanism at most once. Summing the local third-star injection over x gives at most

`sum_x |Opp(x)\N_A(x)| = 2 M_opp`,

since every missing opposite-centre physical pair is counted once from each endpoint.

Therefore

`E_nonopp <= |S| + 2 M_opp`.

Equivalently,

`e(G[S]) = E_opp + E_nonopp <= P_opp + M_opp + |S|`

and, in the sharper bookkeeping form,

`E_nonopp - |S| <= 2(P_opp-E_opp)`.

## Induced-P3 interpretation

The factor two above has a precise meaning. A third-star certificate is exactly an induced two-edge path

`x - y - z`

whose endpoints x,z are opposite-centre stars and are nonadjacent, with y their unique common A-neighbour. A single missing opposite pair can support at most the two edge deletions belonging to that one physical P3, and no second centre y' can use the same missing pair because common-neighbour uniqueness would fail.

Thus every nonopposite star-star edge beyond the one-per-star antipode-bridge budget must be paid for by the missing-edge geometry of an opposite-centre pair.

## Strategic consequence

This does not yet close the star branch: the inequality alone allows a large supply of missing opposite pairs to finance nonopposite edges. But it sharply identifies the only possible dense escape. Any asymptotically dense star subsystem must organize around opposite-centre pairs and induced P3 substitutions; arbitrary dense mixing of the eight star-centre classes is impossible without a commensurate opposite-pair deletion bill.

The next useful target is therefore not another local certificate list but the extremal problem for this substitution system, especially the two-antipodal-centre face. In that face every same-centre edge must sit in a unique induced P3 whose missing endpoint pair is cross-centre, making the remaining problem a concrete two-class graph inequality.
