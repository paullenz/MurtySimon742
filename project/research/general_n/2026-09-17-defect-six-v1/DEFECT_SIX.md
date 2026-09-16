# The five-label defect-six boundary

17 September 2026. Research directed by Paul Lenz; derivation by ChatGPT/Geeps.

**WIP_UNVERIFIED: complete hand argument preserved before new finite tests.** The inherited exact-block construction and internally checked D>=6 bound are pinned at commit 314f953a5ba15ca62148d52062bd0ee8568dcccb, project/research/general_n/2026-09-17-structural-consolidation-v1/STRUCTURAL_TREATMENT.md. External review, novelty, sharpness and promotion remain open.

## Claim and notation

Under that treatment's whole-level exact-block hypothesis, with d=5, D>=7. Consequently W>=5+4m+7, hence W>=32; extra high-source selections require W>=52. This is conditional on the actual exact block, not an unrestricted conjecture proof or a finite catalogue exclusion.

Use Q=G[T], mu=10-e(Q), L>=0, beta>=0, D=L+beta+2mu, and full receiver pools V_t. Every K-label has weight 5 at zero demand and 4 at positive demand. Let a0 count zero-demand K-labels, kappa=|K|. The exact weight identity and universal-core inequality are

    4*kappa+a0=5+4m+D,
    L+beta>=3 max(0,g-1),
    D>=2mu+3 max(0,4-2mu),

where g is the number of universal vertices of Q. Every common K-label (one adjacent in G to all T) is adjacent to every full-pool vertex. This follows from the inherited domination/residual argument and does not require L=beta=0.

## 1. Exhaustive parameter split

Suppose D=6. The numerical inequality rules out mu=0 and mu=1; nonnegativity rules out mu>=4. Thus either mu=3,L=beta=0, or mu=2,L+beta=2. Also a0 is 3 modulo 4, hence a0>=3. Each zero-demand label that is not common costs at least one unit of L, so there is a common label c0 in either case.

If mu=3, the inherited zero-loss star-forest lemma applies. It gives e(Q)<=4, whereas e(Q)=7, contradiction.

If mu=2, the universal-core inequality forces g<=1. Two missing edges sharing an endpoint would leave two universal vertices. The missing edges must therefore be disjoint, so Q is K5 minus a two-edge matching. Its minimum degree is three.

## 2. All nonexceptional loss distributions

A K-label k has ell_k=|N_G(k) intersect T|=w_k-l_k with l_k>=0 and sum l_k=L. Unless there is a positive-demand label with l_k=2, every K-label has at least three tight neighbours: zero-demand labels have at least 5-2=3, and positive-demand labels with l_k<=1 have at least 4-1=3.

Every B-vertex outside H and the full pools has no selected tight incidence, and each missing tight G-neighbour is a residual incidence counted in beta. It therefore misses at most beta<=2 tight vertices. Pool vertices have one tight neighbour and are adjacent to c0; high vertices, the pivot and A-labels outside T union K have none.

Thus all external vertices satisfy the inherited bounded-hole lemma with h=2. Every edge of Q has endpoint degrees at least three and would be noncritical, contradiction.

## 3. The unique exceptional two-neighbour label

The only remaining possibility is one positive-demand label x with l_x=2 and exactly two tight neighbours S. It uses the whole loss budget: L=2, beta=0, and all other K-labels have zero loss, hence full or one-hole tight support. All residual tight incidences are in the full pools; remaining low B-vertices have full tight support.

There is an edge ts in Q[T minus S]. Indeed T minus S has three vertices and Q has only two missing edges, so its three potential internal edges cannot all be missing. The exceptional x is adjacent to neither t nor s. It therefore cannot be an endpoint of a destroyed path of length at most two using ts.

For every other external vertex, use the inherited h=1 path replacement: common c0 handles tight endpoints and protected singleton pools; a one-hole label missing t still neighbours an alternative r in N_Q(t) minus {s}. Such an r exists because deg_Q(t)>=3, and similarly at s. Vertices adjacent to both endpoints or neither are not exclusive neighbours. Thus every pair previously within distance two remains so after deleting ts. This contradicts edge-criticality.

All possibilities at D=6 are excluded. Integrality and the predecessor's D>=6 theorem yield D>=7. The W consequences follow from W>=5+4m+D, m>=5, and m>=10 when extras exist.

## General local observation extracted

The bounded-hole lemma permits arbitrary additional external vertices which have equal adjacency to the two endpoints of the edge being deleted: both adjacent or both nonadjacent. They are not exclusive neighbours and hence cannot create a new affected pair. Their other adjacencies are unrestricted. An exceptional tight support therefore threatens only edges crossing its support cut, not every tight edge.

This observation is the reusable content of the new boundary proof. It suggests charging potentially critical tight edges to exceptional supports rather than repeatedly increasing a uniform worst-case hole budget. No such global charging inequality is claimed proved by this checkpoint.

## Checks and next action

No new finite execution is claimed yet. Test the equal-adjacency exception lemma using two external probes, full per-pair reachability before/after deletion, and a separately structured explicit-path checker. Include controls where the exception crosses the deleted edge, the common label is absent, or singleton protection fails. Check the complete mu/loss split independently. Preserve results before attempting a further mathematical extension.
