# Hostile replay of the minimal two-star-class exact M(n) bound

Date: 2026-09-21

Target: `Q3_MINIMAL_TWO_STAR_CLASS_FACE_EXACT_M_BOUND.md`.

## Verdict

No flaw was found in the exact closure at its stated, deliberately narrow scope:

- only two opposite star-centre classes occur;
- exactly one physical vertex occurs in each of the six coordinate-halfcube codes;
- no parity halfcubes, no third star centre and no extra coordinate multiplicity occur;
- every A-to-B code is an antipodal transversal.

The theorem remains a face closure, not a closure of the full Q3 branch.

## 1. Independent 16-code replay

A fresh bit-level enumeration of Q3's four antipodal pairs generated all `2^4=16` transversals and independently confirmed that they are exactly:

- the six coordinate halfcubes;
- the two parity halfcubes;
- the eight closed-neighbourhood stars.

The same replay checked the two disjointness facts used in the proof:

1. for every star `S_c`, the unique antipodal transversal disjoint from it is `S_{bar c}`;
2. for every coordinate halfcube `C_i^epsilon`, the unique antipodal transversal disjoint from it is the complementary halfcube `C_i^{1-epsilon}`.

These are exact finite identities, not assumptions from the earlier notes.

## 2. Independent B-target replay

For every coordinate halfcube H, the replay checked every cube vertex outside H and found a cube neighbour in H; equivalently H dominates all of Q3. Hence an A-edge incident to a coordinate-halfcube source cannot be certified on that source side by a B-target: every candidate outside B-vertex retains a B-mediated two-path, while vertices of H are already adjacent to the source.

For every star `S_c`, the replay independently recovered exactly one undominated cube vertex, `bar c`. This matches the star-side incident-edge classification and confirms that the antipode-B mechanism has capacity one per physical star.

## 3. Star-core injection replay

Take a same-centre star edge `xy` in X. Direct certification is impossible because the two B-codes coincide; antipode-B certification is impossible because y's code does not contain `bar c`. Thus any certificate from either endpoint must use a third A-vertex of the unique disjoint code `S_{bar c}`.

The resulting missing cross pair has the other edge endpoint as its unique common A-neighbour. One missing X-Z pair cannot support two distinct same-centre edges, because that would give it two common A-neighbours. The same missing pair cannot simultaneously support one X-X and one Z-Z edge: its unique common A-neighbour lies on only one side. Therefore

`e(X)+e(Z) <= pq-e(X,Z)`

and hence `e(S)<=pq` survives replay.

## 4. Six-witness mixed-edge replay

For each `x∈X`, each of the three star leaves has no available adjacent-star certificate inside the two-centre star population: the required centre is `bar c⊕e_i`, distinct from c and `bar c`. Therefore the unique physical vertex in the relevant coordinate-halfcube code must be the halfcube-side certificate for every x. It is consequently nonadjacent to every x.

The three X-side coordinate witnesses are therefore anticomplete to X; the three Z-side witnesses are anticomplete to Z. These are six distinct code types, giving exactly the robust ceiling

`e(W,S)<=3s`.

No shared-certificate assumption is being smuggled in: uniqueness of the physical vertex in each coordinate code is an explicit hypothesis of this minimal face.

## 5. Internal W-edge replay

For a W-edge joining noncomplementary coordinate codes, endpoint-direct certification fails because the codes intersect. There is no B-target certificate by the domination check above. A third-A certificate must use the unique disjoint complementary coordinate code.

Thus every noncomplementary W-edge is a side of an induced P3 whose endpoints are a missing complementary coordinate pair. With exactly three physical complementary pairs, each missing pair has at most one common A-neighbour and hence supports at most the two sides of one P3. If `E_comp` complementary pairs are present,

`e(W)<=E_comp+2(3-E_comp)=6-E_comp<=6`.

This count remains valid even in the presence of star vertices, because the required common-neighbour uniqueness is global across A, not merely internal to W.

## 6. Arithmetic replay

With `s=p+q`, `a=s+6`:

`e(A)<=floor(s^2/4)+3s+6`.

Since

`floor((s+6)^2/4)-3 = floor(s^2/4)+3s+6`,

we obtain

`e(A)<=floor(a^2/4)-3`.

For the Q3-root skeleton,

`e(G)=20+4a+e(A)`

and

`M(n)=floor(a^2/4)+4a+17`, `n=a+9`.

Therefore `e(G)<=M(n)` exactly.

## 7. Remaining escape routes

The hostile replay reinforces rather than broadens the theorem. The still-open escapes are precisely:

1. a third star-centre class;
2. extra multiplicity in a coordinate-halfcube code;
3. at least one parity-halfcube vertex;
4. a non-antipodal-transversal A-to-B neighbourhood.

The next attack should preserve this separation. In particular, the most economical extension is extra coordinate multiplicity, because it weakens the forced anticompleteness step by allowing different physical leaf certificates for different star sources; that is the exact point at which the present proof ceases to apply.
