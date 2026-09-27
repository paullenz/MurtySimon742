# Chen comparison boundary and all-order prefix separation

27 September 2026. Internal hand proofs and exact checks, not a novelty determination.

## 1. What was and was not accessed

The requested comparison was to William Y. C. Chen, *Integral matrices with given row and column sums*, Journal of Combinatorial Theory A 61 (1992), 153–172, DOI 10.1016/0097-3165(92)90015-M. The official abstract identifies a main condition and characterizations but does not state that condition. This continuation did NOT obtain its full statement. Direct publisher access ultimately returned HTTP 403; PDF/API/author-site attempts did not yield the full text. No access control was bypassed and no paper was purchased.

Jeffrey W. Miller's *Reduced Criteria for Degree Sequences*, arXiv:1205.2686v2 (2013), is available as parsed full text. Section 3.5 explicitly discusses an upper-left 2-by-2 structural-zero example in Chen's monotone class satisfying Chen's main condition. That prevents identifying Chen's class with Anstee's one-forbidden-position class. Miller discusses generalized conjugates, but the inspected text does not supply a complete usable transcription of Chen's main condition. The PDF screenshot attempts failed; the matrix has not been visually certified from a rendered page in this session.

A separate Yunsun Nam paper with the same title, Ars Combinatoria 52 (1999), 141–151, was located. Its image-only PDF supplied no parsed text and screenshot attempts failed. It was not inspected and is NOT a substitute for Chen's paper.

Accordingly this checkpoint does not claim that the six-vertex example fails any specifically named Chen premise. It proves a direct obstruction to a precisely defined single-reference prefix-dominance characterization, and classifies all column orders of the frozen example. This is useful separation evidence, not resolution of every possible Chen-based reduction.

Primary-source identifiers:

- Chen: https://www.sciencedirect.com/science/article/pii/009731659290015M ; DOI above. Abstract only.
- Miller: https://arxiv.org/pdf/1205.2686 ; DOI 10.1016/j.disc.2012.11.027. Parsed Sections 3 and 3.5; rendering failed.
- Nam metadata: https://combinatorialpress.com/ars-articles/volume-052-ars-articles/integral-matrices-with-given-row-and-column-sums/ . No theorem from this paper used.

## 2. Frozen support and generalized family

Fix integers p>=2 and k>=p+2. Let the base be a bidirected star with centre c and k leaves L, and add a universal bidirected hub h. All original sources have demand one. Receiver capacities are one on c and the leaves and p at h. All vertices form one block. There are n=k+2 original vertices.

For the balanced full-demand matrix construction, add p-1 universal dummy rows. The binary support B has

    N = k+p+1 rows and k+2 columns.

Every row has prescribed sum one. Column demands are p at h and one elsewhere, summing to N. The original rows are supported by the digraph; each dummy row can use every column.

The k leaf columns can only use the centre row, the hub row, and p-1 dummy rows: k units of column demand have only p+1 units of available row supply. Since k>=p+2, no required matrix exists. This proves infeasibility independently of a prefix criterion or of the stratified closure theorem.

For a column set J, the exact supply upper bound is

    K_B(J) = sum_i min(r_i, number of supported entries in row i and columns J).

Prefix testing means comparing the demand of each initial segment in one fixed column order with K_B of that segment. It is necessary for feasibility but is not generally sufficient.

## 3. Every nonincreasing-demand order fails in the original orientation

The hub column must come first because p>1; the k+1 columns of demand one can follow in any order. The first column has support in all rows except the hub row, hence supply N-1=k+p>=p. Once any second column is included, the hub row also has a supported entry, so the prefix supply is N. Every later prefix demand is at most the total N.

Therefore ALL (k+1)! nonincreasing-demand column orders pass every prefix inequality, despite infeasibility. In the frozen case k=4,p=2, this is all 120 possible tie orders. It is not an accident of the previously chosen centre-before-leaves order.

## 4. No fixed single reference vector can repair this orientation

For any of those orders, the nonincreasing vector

    g = (N-1,1,0,...,0)

is feasible for the same support and same row margins: every row except the hub chooses column h, and the hub chooses the second column. Meanwhile the required infeasible target is

    c = (p,1,...,1).

They have equal total N and c is dominated by g in every prefix. Both obey the individual support-size bounds on columns.

Suppose there were ONE fixed vector b* such that, among all nonnegative nonincreasing integer column-margin vectors of total N for this ordered support and these fixed row margins,

    realizable(a) iff every prefix sum of a is <= the corresponding prefix of b*.

Since g is realizable, every prefix of g must lie below b*. Transitivity then places every prefix of c below b*, wrongly declaring c realizable. Contradiction.

This excludes not only the particular greedy vector but ANY fixed reference vector with the displayed characterization. It does not rule out a condition depending on the candidate margins, testing more than one reference, changing the ordering, checking arbitrary subsets, or using a different matrix construction. Nor is it an identification of Chen's uninspected main condition. The distinction between an explicit impossible conclusion and an uninspected premise is essential.

## 5. All transposed orders: exact detection fraction

Transpose B. Its N column demands are all one, so every ordering is nonincreasing. Its row capacities are the original receiver capacities P. For a subset S of these columns, K_(B^T)(S) is the capped receiver count from the corresponding original and dummy source rows.

If S consists of r leaves and nothing else, its supply is zero for r=0 and

    1+min(p,r)

for r>0. Such a set is deficient exactly when r>=p+2.

Every other S is nondeficient. Here are the cases, without an appeal to numerical testing.

1. S contains a dummy row. Let t>=1 be the number of dummies and s the number of selected non-hub original rows; let e indicate whether h is selected. Every ordinary receiver is saturated, so

       K(S)-|S| = k+1+min(p,s+t)-(s+t)-e >= 0,

   because t<=p-1, s<=k+1 and e<=1.

2. S contains h but no dummy. All ordinary receivers are saturated. With s other original rows selected,

       K(S)-|S| = k+min(p,s)-s >= 0,

   since s<=k+1 and p>=2.

3. S contains c but neither h nor a dummy. Write S={c} plus r leaves. Its margin is

       k+1_(r>0)+min(p,r+1)-(r+1) >= 0

   for 0<=r<=k.

Thus a transposed permutation detects the obstruction iff its first p+2 entries are all leaves. Once any non-leaf column appears, every later prefix is nondeficient. The fraction of detecting permutations is exactly

    binom(k,p+2) / binom(k+p+1,p+2).

For k=4,p=2, exactly 4!*3!=144 of 7!=5,040 orders detect it; the other 4,896 pass. The checker enumerates every order, stores aggregate results and hashes of the ordered payoff records, and checks the detecting-prefix equivalence on every permutation.

## 6. Interpretation and remaining comparison obligation

The original orientation has an order-robust obstruction to a single-reference prefix-dominance description. The transposed orientation is different: a suitable ordering DOES expose the infeasibility. Therefore an overbroad claim that no transposition or reordering can reveal the obstruction would be false.

These statements refine the earlier direct-Anstee separation. They do not exclude all indirect reductions to Chen, general fixed-support flow theorems, or other matrix characterizations. General all-subset Hall feasibility remains exact; the issue here is which reductions to a fixed prefix chain are justified.

The Chen question remains: inspect the ACTUAL full main condition and map it variable by variable, keeping the matrix orientation, fixed support, ordering and row/column margins explicit. Until that text is available, do not spend another continuation treating the abstract or the one-position Anstee premise as its substitute. The separate actionable mathematical continuation is the residual-implication certificate rule specified in PROOF.md Section 10.
