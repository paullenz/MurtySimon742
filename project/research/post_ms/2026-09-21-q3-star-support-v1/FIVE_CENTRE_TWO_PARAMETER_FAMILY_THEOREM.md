# Uniform five-centre two-parameter D2C family

21 September 2026.  Q3 antipodal-transversal scope.  Internally proved and
machine-replayed; external review remains open.

## The construction

Let `E={0,3,5,6}` and `O={1,2,4,7}` be the even and odd parts of Q3.  Start
with the root joined to Q3.  Add one vertex of each of the six coordinate
halfcube codes, five star vertices with centres `{0,1,2,4,7}`, `r>=1` copies
of `P0=E`, and `q>=1` copies of `P1=O`.  Make the `P0--P1` block complete.
Choose one P1 vertex `h`, join it to all six coordinate vertices, and add the
three star edges

    S0--S7, S1--S4, S2--S4.

Call the resulting graph `G(r,q)`.

## Theorem

For every `r,q>=1`, `G(r,q)` is diameter-two-critical.  Moreover

    n = 20+r+q,
    m = rq+4(r+q)+73.

Writing `u=r+q` and `d=|r-q|`, its exact gap below
`M(n)=floor((n-1)^2/4)+1` is

    M(n)-m = 11u/2+18+d^2/4                 if u is even,
    M(n)-m = (11u+37)/2+(d^2-1)/4           if u is odd.

Equivalently, the balanced baseline is `11u/2+18` for even `u` and
`(11u+37)/2` for odd `u`, plus `floor(d^2/4)`.  In particular the gap is
positive and grows linearly even in the densest balanced subfamily.

## Proof by two safe twin extensions

The graph `G(1,1)` is directly D2C.  The companion certificate file checks
all 82 of its edges and, for each deleted edge, records a pair whose distance
exceeds two and which is safe under both extensions below.

Add a new P0 vertex `x`.  Its neighbourhood is exactly

    N(x) = E union P1.

It is within distance two of every old vertex: it is adjacent to E and every
P1 vertex, reaches O through cube edges, reaches the root through E, and
shares an even cube neighbour with every coordinate or star vertex.  Thus
diameter two is preserved.  The only new length-two paths between old
vertices have both ends in `E union P1`.  Hence any old deletion witness not
contained in that set survives.  Each new spoke `xb`, `b in E`, is critical
with witness `(x,b)`, and every new edge `xy`, `y in P1`, is critical with
witness `(x,y)`: after deleting the edge, those endpoint pairs have no common
neighbour.

Similarly, add a nonhub P1 vertex `y`.  Its neighbourhood is

    N(y) = O union P0.

The parity-reversed diameter argument applies.  New length-two paths between
old vertices have both ends in `O union P0`; the stored old witnesses avoid
that set.  Every new odd spoke and every new P0--P1 edge is critical with its
own endpoints as witness.

The witnesses of newly added edges are themselves safe under every later
extension: a P0-spoke pair has one end outside each future hazard set, as does
a P1-spoke pair, while a P0--P1 pair is never contained in either same-side
hazard set.  Induction therefore permits the two extensions in any order and
proves the theorem for all `r,q>=1`.

Finally, Q3 plus its root contributes 20 edges; the `11+r+q` outside vertices
contribute four spokes each; and the A-graph has `rq+6+3` edges.  This gives
the formula for `m`.  Substitution in `M(n)`, using
`floor(u^2/4)-rq=floor(d^2/4)`, gives the displayed exact gap.

## Audit boundary

This is an actual graph-level theorem, not a scalar or type-relation scan.
It establishes a dense positive-control family but does not prove optimality
within five-centre support, address the other two support orbits at arbitrary
multiplicity, or settle the eventual second-extremal problem.
