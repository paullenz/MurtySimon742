# Parameter-only corollaries of the cross-grid witness structure

Date: 2026-09-20

Status: internal conditional synthesis; follows directly from `CROSS_GRID_COVER_DICHOTOMY.md` and `CROSS_WITNESS_INDEPENDENCE.md`.

For `y>=2`, the residual cross-certificate grid forces either `s_D>=g` or `s_C>=y`. Hence in every case

> `s:=s_C+s_D >= min{g,y}`.                              `(GRID-s)`

The internal-X witness population m is physically disjoint from the cross population and all these witnesses lie among the d z-nonneighbours, so

> `d >= m+min{g,y}`.                                     `(GRID-d)`

Every one of the m+s used witnesses is unavailable as an extra U-neighbour of `a_0`. With `epsilon_z=p+k-1+d`, this yields the orientation-free conservation law

> `epsilon_z+epsilon_{a_0}`
> ` >= 2p+k+u-y+m+min{g,y}-2`.                          `(GRID-ZA0)`

The same-type independence theorem gives either at least `binom(g,2)` D--D holes or at least `binom(y,2)` C--C holes. Therefore the rooted triangle ceiling has the parameter-only strengthening

> `q <= binom(u,2)-binom(k+1,2)-k-d-binom(J,2)`
> `     -min{binom(g,2),binom(y,2)}`.                   `(GRID-Q)`

These bounds deliberately discard the stronger typed information in order to expose a compact structural bill suitable for later asymptotic synthesis. They are necessary conditions only and inherit the rigid-cut realizability caveat.
