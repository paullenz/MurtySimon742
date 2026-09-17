# Direct certification of the published 12-vertex exception against the X3 reconstruction

18 September 2026. Research directed by Paul Lenz; figure reconstruction and graph check by ChatGPT/Geeps.

**Status: direct figure-based internal certification. The graph drawn in Figure 1 of Radosavljevic--Stanic--Zivkovic (2024) is isomorphic to the project's independently constructed `X_3`. The comparison is from the authoritative published vector figure itself; there is still no author-supplied adjacency-list file.**

The active target is the eventual / sufficiently-large second-extremal D2C problem around

\[
M(n)=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor+1.
\]

This note closes a long-standing audit gap in the project. The published paper states that its Figure 1 is a D2C graph of order 12 and size 32, exceeding `M(12)=31`, and highlights a dominating edge. Earlier project notes reconstructed an independent twelve-vertex graph `X_3` with the same invariants but deliberately stopped short of identifying the drawing without an authoritative adjacency representation. The published vector drawing is sufficiently clear to reconstruct its complete adjacency directly.

---

## 1. Label the published Figure 1

Use the geometry of the authoritative 2024 Figure 1. Label the twelve drawn vertices as follows:

- `A`: leftmost vertex;
- `B,C`: upper-left and lower-left vertices;
- `D,E`: upper- and lower-mid-left vertices;
- `r`: central vertex, the upper endpoint of the dashed edge;
- `G,H`: upper- and lower-mid-right vertices, with `H` the lower endpoint of the dashed edge;
- `I,J`: upper-right and lower-right vertices;
- `K`: rightmost vertex;
- `L`: bottom vertex.

The dashed highlighted edge is therefore `rH`.

The eight vertices

\[
\{B,C,D,E,G,H,I,J\}
\]

form the visibly drawn cube. Its twelve edges are

\[
BC,\ DE,\ GH,\ IJ,
\]
\[
BD,\ CE,\ GI,\ HJ,
\]
\[
BG,\ DI,\ CH,\ EJ.
\]

The first two rows are the four vertical and four horizontal straight edges in the drawing; the last row consists of the two upper and two lower curved connector edges.

The central vertex `r` is joined to all eight cube vertices and to none of `A,K,L`.

The remaining outer vertices have neighbourhoods

\[
N(A)=\{B,C,G,H\},
\]
\[
N(K)=\{G,H,I,J\},
\]
\[
N(L)=\{C,E,H,J\}.
\]

There are no edges among `A,K,L`.

This accounts for

\[
12+8+4+4+4=32
\]

edges, so there is no room for an omitted or extra drawn edge relative to the paper's stated size.

---

## 2. Read the cube as binary coordinates

Assign coordinates to the eight cube vertices by

\[
H=000,\quad G=001,\quad C=010,\quad J=100,
\]
\[
B=011,\quad I=101,\quad E=110,\quad D=111.
\]

Every one of the twelve edges listed above now joins strings at Hamming distance one, and every Hamming-distance-one pair appears. Hence the inner graph is exactly `Q_3`.

Moreover the three outer neighbourhoods become the three coordinate zero-faces:

- `A` is adjacent precisely to the cube vertices whose first coordinate is zero;
- `K` is adjacent precisely to those whose second coordinate is zero;
- `L` is adjacent precisely to those whose third coordinate is zero.

Finally `r` is adjacent to every cube vertex and to none of the three face vertices.

This is exactly the definition of the independently reconstructed graph `X_3` in `HYPERCUBE_FACE_EXCEPTION.md`.

Thus the explicit isomorphism is

\[
r\mapsto r,
\]
\[
A\mapsto a_1,\quad K\mapsto a_2,\quad L\mapsto a_3,
\]

and the eight remaining vertices map to the cube strings displayed above.

In particular, the dashed edge is

\[
rH=r\,000,
\]

which is the unique dominating edge in the independent `X_3` reconstruction.

---

## 3. Independent graph checks

The companion checker `check_published_12_vertex_exception_figure.py` encodes only the adjacency reconstructed above and independently verifies:

1. the graph has 12 vertices and 32 edges;
2. the inner eight vertices induce `Q_3` under the stated binary map;
3. the three outer vertices are exactly the three coordinate-zero face vertices;
4. the resulting adjacency is exactly the programmatic `X_3` construction;
5. the degree multiset is
   \[
   \{8,7,6,6,6,5,5,5,4,4,4,4\};
   \]
6. `rH` is the unique dominating edge;
7. the graph has diameter 2;
8. deleting any edge raises the diameter above 2, so the reconstructed figure is D2C.

The check does not infer adjacency from pixels. The mathematical reconstruction is the explicit edge tracing in Sections 1--2; the script checks that this tracing has exactly the claimed structural consequences.

---

## 4. Consequence for the project's negative control

The previous trust boundary can now be sharpened:

> **PUBLISHED-EXCEPTION IDENTIFICATION -- internal certification.** The graph drawn in Figure 1 of Radosavljevic--Stanic--Zivkovic (2024) is isomorphic to the project's independently reconstructed Boolean/cube graph `X_3`.

Therefore the mandatory hostile control is not merely an invariant match. It is the same explicit mechanism:

\[
k=4,\quad b=8,\quad a=3,\quad r=0,\quad F=\varnothing,
\]

with `G[B]=Q_3`, three coordinate-face A-vertices, and a universal root on the cube.

This materially strengthens the interpretation of the residual-zero classification: the unique nontrivial `k=4` normal form obtained there is directly the published 12/32 counterexample.

---

## 5. Source and trust boundary

The adjacency above is reconstructed from Figure 1 on page 23 of:

Jovan Radosavljevic, Zoran Stanic, and Miodrag Zivkovic, *Primitive diameter 2-critical graphs*, Publications de l'Institut Mathematique 115(129) (2024), 21--32, DOI `10.2298/PIM2429021R`.

The paper itself states immediately below the figure that the graph has order 12, size 32, and a dominating edge highlighted in the figure. The same drawing appeared earlier as Figure 5 in Radosavljevic (2023), where the highlighted edge is coloured red.

The remaining caveat is documentary rather than mathematical: no machine-readable adjacency list supplied by the authors has been located. The identification here is a direct reconstruction from the authoritative published vector figure, followed by an exact graph check. It should be described that way rather than as an author-supplied adjacency certification.

No claim about an all-order second-extremal theorem follows; this graph remains the mandatory finite counterexample to the false 2019 strengthening.