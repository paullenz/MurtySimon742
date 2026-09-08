# Targeted literature comparison for v11

8 September 2026. This is a targeted search record, **not an exhaustive novelty determination**.

## Explicit maximum-degree thresholds located

1. Haynes, Henning, van der Merwe and Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12 (2014), 1882–1889, DOI 10.2478/s11533-014-0449-3. Theorem 2.1 states that the Murty–Simon bound holds if `Delta >= 0.7 n`, and also if `n>=2000` and `Delta>=0.6789 n`.

   Publisher/metadata: https://pure.uj.ac.za/en/publications/a-maximum-degree-theorem-for-diameter-2-critical-graphs/

2. A. Jabalameli, A. Behjati, M. Saghafian, M. M. Shokri, M. Ferdosi and S. Bahariyan, *Improving the Bounds On Murty_Simon Conjecture*, arXiv:1610.00360v2 (2016/2018 revision). The current v2 text states an all-order threshold approximately `Delta >= 0.6755 n` (the arXiv abstract/search metadata still displays 0.676 in places).

   https://arxiv.org/abs/1610.00360

3. Dailly, Foucaud and Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142–3159, DOI 10.1016/j.disc.2019.06.023, studies stronger non-bipartite extremal questions and dominating-edge classes. It is relevant context but the targeted search did not locate a lower general maximum-degree coefficient there.

   https://arxiv.org/abs/1812.08420

4. Kirchweger, Manrique and Szeider, *Formally Verified Graph Generation with SAT Modulo Symmetries and Lean* (2026), provides current formal/SAT verification context for finite orders. It is not a competing maximum-degree theorem.

   https://doi.org/10.1007/978-3-032-32589-1_8

## Comparison with the present candidate

V11 claims, subject to independent verification of its structural lemmas,

```text
Delta(G) >= 0.6116 n  ==>  e(G) < floor(n^2/4),  n>=4.
```

Numerically this is substantially below the explicit 0.6755 all-order preprint threshold located above. Because this project has not completed a systematic citation search across every paper, thesis, preprint and non-English source, **do not describe 0.6116 as best-known, novel, first, or a record until specialist review confirms both correctness and literature coverage.**

The most useful external-review question is therefore not the decimal comparison but whether the selected/residual construction, demand-tail pair-capacity theorem and Jensen-centred stability argument are universally valid for every diameter-two edge-critical graph in the stated scope.
