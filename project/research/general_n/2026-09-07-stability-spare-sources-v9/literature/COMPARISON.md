# Literature comparison and priority limits

Checked 7 September 2026. This is a targeted comparison, not an exhaustive novelty determination or an audit of every cited proof.

## Maximum-degree precedents

1. Teresa W. Haynes, Michael A. Henning, Lucas C. van der Merwe and Anders Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12(12), 1882–1889 (2014), DOI 10.2478/s11533-014-0449-3. The author-institution abstract states Delta >= 0.7n, or n >= 2000 and Delta >= 0.6789n. Sources: https://dc.etsu.edu/etsu-works/15862/ and https://doi.org/10.2478/s11533-014-0449-3 . No new full audit of its original proof is claimed.

2. Afrouz Jabalameli, Amin Behjati, Morteza Saghafian, MohammadMahdi Shokri, Mohsen Ferdosi and Sorush Bahariyan, *Improving the Bounds On Murty_Simon Conjecture*, arXiv:1610.00360. Canonical metadata: submitted 2 October 2016, v2 10 October 2016. The canonical abstract states Delta >= 0.676n for every n: https://arxiv.org/abs/1610.00360 .

The associated author-uploaded full text at https://www.researchgate.net/publication/308807548_Improving_the_Bounds_On_Murty_Simon_Conjecture was uploaded by Morteza Saghafian in October 2020. It carries the arXiv v2 identifier but a September 2018 title-page date. Its title and author order differ from the arXiv abstract. Its PDF-text abstract says 0.6755n, while the introduction and Theorem 3.5 state 0.6756n. Accordingly, this checkpoint distinguishes the canonical 0.676 abstract from the related full-text 0.6756 theorem and does not silently reconcile the 0.6755/date discrepancies. The body contains a recursive common-neighbourhood/quasi-clique estimate, with Lemma 3.2 and Theorems 3.4–3.5 furnishing the bound. The apparent c-notation in Lemma 3.2 and Theorem 3.4 also differs in the parsed text. None of these observations is being presented as a disproof of that paper. Direct retrieval of the canonical arXiv PDF was unsuccessful, so a byte-identical canonical-full-text comparison was not possible.

**Correction to the preceding strategic discussion:** a comparison with only the 2014 thresholds omitted this later preprint. Any review of our candidate coefficient should consider both, not call 0.6789 the established last word.

## Relationship to this checkpoint

Complement quasi-edges, unique supplements and rooted neighbourhood partitions are established tools. We claim no ownership of those definitions. The project's v2 residual-demand charge is rederived directly from diameter-two edge-criticality; the proof does not invoke the numerical conclusions or classification theorems of the papers above. This version adds an exact demand-deficit identity, a shared-pair inequality, the fixed quadratic loss 1/5000 for a>=25, and a compensated h+k spare-source bound.

The new coefficient 0.6131682474535585... is below the identified 2014 and 2016/related-body thresholds. That numerical comparison is exact; a claim of best known, priority or novelty would require additional literature and specialist review. Our prior project coefficient is (10-sqrt(2))/14=0.613270459830... . The improvement over our own coefficient is modest, not a dramatic new numerical jump.

Searches included the exact titles, 0.6756, 0.676, maximum-degree Murty–Simon, 2n/3, and later work through the current date. Search results are not a completeness proof. Existing sufficiently-large-order results also mean that merely giving an asymptotic statement is not by itself a new contribution. The present all-n high-degree implication has explicit constants and a different proof objective.

## Formal verification precedent

Markus Kirchweger, Pablo Manrique and Stefan Szeider, *Formally Verified Graph Generation with SAT Modulo Symmetries and Lean*, IJCAR 2026, LNCS 16688, 117–135, published 24 July 2026, https://doi.org/10.1007/978-3-032-32589-1_8 . The primary paper describes an end-to-end Lean/SAT pipeline for graph specifications, encodings and symmetry breaking, including Murty–Simon instances. Public implementation: https://github.com/leansolving/leansms .

Our five Lean lemmas are only a local logical slice and are not the first formal treatment of the subject, a complete graph encoding, or a formally verified general theorem. No claim of those kinds is made.

## Review handoff

Paul will seek specialist external review. No invitation or email was sent in this continuation. The two most useful questions are whether the new residual-demand/pair argument overlaps an existing theorem, and whether its graph-to-data injections and compensated spare-source proof are universally sound. Published precedent, exact arithmetic, formal scope and mathematical review must remain distinct.
