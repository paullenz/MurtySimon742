# Residual charging stability and spare sources in diameter-two edge-critical graphs

**Paul Lenz — research direction. Mathematical development, software, drafting and internal checking: ChatGPT (Geeps).** 7 September 2026. Reviewer draft v9.

**Status.** Candidate mathematical theorems with explicit proofs and internal regression checks. Independent mathematical review and novelty assessment are OPEN. Five local logical implications have been checked in Lean; the graph-to-data construction, cardinality arguments and theorems below are not yet formally verified. This work changes neither the frozen finite-order papers nor their theorem ledger.

## Abstract

We isolate a residual charging argument for diameter-two edge-critical graphs and quantify its loss using the common source–supplement pair budget. For $a=n-1-\Delta$ and $t=m-\Delta(n-\Delta)$, the inherited charging argument gives $t\le(3/2-\sqrt2)a^2$. An exact deficit identity forces concentration of the label demands near its scalar optimum. A joint pair-capacity inequality then excludes that concentration at every $a\ge25$, giving $t<(3/2-\sqrt2-1/5000)a^2$. With 24 elementary rounding cases this yields a candidate maximum-degree threshold $\beta_1=0.61316824745\ldots$ for all $n\ge4$, improving the project's previous $0.61327045983\ldots$ coefficient. A separate weighted theorem bounds the number of maximum-demand labels supported by $h+k$ maximum-residual sources, for $0\le k\le h^2$. In particular, two spare sources permit at most $2h+2$ such labels for $h\ge2$. Neither theorem uses positive-surplus residual activity, finite-order certificate enumerations, Fan's density estimate, or a weak-core reduction. Numerical tests support, but do not replace, the proofs.

## 1. Scope, main statements and prior work

A graph is simple and finite. Disconnected pairs have infinite distance. A graph $G$ is diameter-two edge-critical if its diameter is two and deleting any edge increases the diameter. Let $n=|V(G)|$, $m=e(G)$ and $b=\Delta(G)$. The Murty–Simon conjecture asks whether $m\le\lfloor n^2/4\rfloor$, with equality only for the balanced complete bipartite graph.

**Theorem A (quantitative charging loss).** In the minimum-complement-degree construction below, let $a=n-1-b\ge25$ and $t=m-b(n-b)$. Put

$$c=\frac32-\sqrt2,\qquad c_1=c-\frac1{5000}.$$

Then

$$\boxed{t<c_1a^2.} \tag{1}$$

**Corollary A (maximum degree).** For $n\ge4$, define

$$\beta_1=\frac{1/2+\sqrt{c_1}}{1+\sqrt{c_1}}=0.6131682474535585\ldots.$$

Then

$$\boxed{\Delta(G)\ge\beta_1n\quad\Longrightarrow\quad e(G)<\lfloor n^2/4\rfloor.} \tag{2}$$

The decimal is explanatory; the radical is the exact coefficient. The improvement from the earlier project coefficient $\beta_0=(10-\sqrt2)/14=0.613270459830\ldots$ is small numerically. The new ingredient is a loss proportional to $a^2$, rather than strictness only at the exact scalar optimum.

**Theorem B (spare sources).** Let $h\ge1$ be the largest residual degree on $B$, and let exactly $z$ sources have residual degree $h$. If $h\le z\le h^2+h$, and $\ell$ labels have minimum demand $h$, then

$$\boxed{h\ell\le(2h-1)z.} \tag{3}$$

Consequently, with $z=h+2$ and $h\ge2$, one has $\ell\le2h+2$. With $z=h+1$ one recovers $\ell\le2h$. No positive-surplus assumption is made. The bound is attained by reduced incidence systems described below; sharpness for actual critical graphs is not claimed.

**Literature positioning.** Haynes, Henning, van der Merwe and Yeo [1] prove the conjecture for $\Delta\ge0.7n$, and for $n\ge2000$ with $\Delta\ge0.6789n$. The canonical abstract of the 2016 preprint [2] advertises $0.676n$ for every $n$. An author-posted full text associated with that record states $0.6756n$ in Theorem 3.5, with other metadata differences detailed in `literature/COMPARISON.md`. The earlier project comparison mentioning only [1] was incomplete. Complement quasi-edges and supplements are established tools, not introduced here. The present argument charges residual degrees against selected label demands, then uses simultaneous pair capacity; [2] uses an inductive quasi-clique estimate. We do not claim a completed audit of [1] or [2], a best-known threshold, priority, or novelty. Those results are comparisons, not proof inputs to (1)–(3).

The inherited charging argument and one-spare-source lemma are preserved in project checkpoints [4–5]. We reproduce their needed ingredients below, eliminating any dependency on classification of total-domination-critical complements. The full n=25, n=27 and n=28 numerical proofs are not dependencies.

## 2. A direct quasi-edge construction

Put $H=\overline G$. An adjacent pair totally dominates a graph when every vertex has a neighbour in the pair. For any graph $J$, its complement has a pair at distance greater than two exactly when $J$ has an adjacent total dominating pair: the two endpoints are nonadjacent in the complement and have no common neighbour there. This remains valid for disconnected pairs. Thus $H$ has no such pair, while $H+uw$ has one whenever $uw$ is a nonedge of $H$.

**Lemma 2.1 (unique exception).** Suppose $uw$ is a nonedge of $H$ and both endpoints miss a third vertex. There is an existing edge $ui$, or symmetrically $wi$, whose open-neighbourhood union is $V(H)\setminus\{w\}$ in the former orientation. Write $ui\to w$.

*Proof.* An adjacent total dominating pair in $H+uw$ cannot be $\{u,w\}$, because that pair still misses the third vertex. A pair disjoint from $\{u,w\}$ has unchanged domination, also impossible. Its edge therefore already existed and it uses exactly one endpoint of $uw$. The only newly dominated vertex is the other endpoint. It is the unique exception of that existing edge in $H$. In particular $u$ and $i$ both miss $w$. $\square$

Choose $v$ of minimum degree in $H$, and set

$$A=N_H(v),\quad B=V(H)\setminus N_H[v],\quad a=|A|=n-1-b,\quad |B|=b.$$

Put $C=H[A]$ and $F=\overline C$ on $A$. Write $d_i=d_F(i)$. Each missing unordered pair in $H[B]$ misses $v$; its quasi-edge auxiliary lies in $A$, to dominate $v$. Choose exactly one such quasi-edge for each missing pair. Call the chosen cross-edges *selected*, and all other $H[A,B]$ edges *residual*. Orient the missing pair from its selected source $u$ to its supplement $w$.

Distinct missing pairs select distinct cross-edges: the $B$-endpoint and unique exception recover the pair. At one source the labels and supplements are separately distinct. The selected arcs on $B$ form an oriented simple graph: an unordered pair supports at most one arc, not one in each direction.

Let $\rho_u$ and $R_i$ be residual degrees at $u\in B$ and $i\in A$, with common sum $r$. Let $q_u,p_u$ be selected outdegree and indegree, $x_i$ the actual selected degree of label $i$, and $Q=\sum q_u=\sum x_i$. Define

$$t=m-b(n-b),\qquad s_i=\max(0,d_i-R_i),\qquad S=\sum_i s_i.$$

**Ledger.** Selected cross-edges and existing $H[B]$ edges together number $\binom b2$. Counting the remaining edges gives

$$e(F)=r+t,\quad \sum_i d_i=2(r+t),\quad \sum_iR_i=\sum_u\rho_u=r. \tag{4}$$

Minimum degree in $H$ gives $d_H(i)=a-d_i+R_i+x_i\ge a$. Therefore

$$x_i\ge s_i,\qquad S\ge r+2t,\qquad q_u+\rho_u\le a. \tag{5}$$

The actual degree $x_i$ need not equal its minimum $s_i$. No argument below makes that substitution.

## 3. The structural inequalities needed here

**Lemma 3.1.** For every selected $ui\to w$,

$$d_i\le\rho_u+R_i,\qquad d_i\le\rho_u+\rho_w, \tag{6}$$

$$\rho_w+q_w\ge q_u-1,\qquad R_i+x_i\ge q_u+p_u. \tag{7}$$

*Proof.* Every $F$-neighbour $j$ of $i$ neighbours $u$, because $ui$ must dominate $j$. At most $\rho_u$ of these $uj$ edges are residual. Every other $uj$ is selected, with a distinct supplement $w_j\ne w$. Since $ui$ dominates $w_j$ and $u$ misses $w_j$, the edge $iw_j$ exists. It is residual: $i,w_j$ both miss $j\in A$, whereas every selected edge has its unique exception in $B$. The distinct $w_j$ inject these incidences into residual edges at $i$, proving the first inequality of (6).

For the second inequality, $uj$ must dominate $w$, so $jw$ exists. Both $j,w$ miss $i\in A$, hence $jw$ is residual. Distinct $j$ give $d_i-\rho_u\le\rho_w$.

Every other selected label at $u$ neighbours $w$, because its quasi-edge must dominate $w$ and the supplements at $u$ are distinct. This proves the first inequality of (7). Finally, $i$ neighbours $u$ and every missing-$B$-pair neighbour of $u$ except $w$. There are $q_u+p_u$ distinct vertices in that list. Hence $d_H(i,B)=R_i+x_i\ge q_u+p_u$. $\square$

In particular, every selected incidence of label $i$ requires $\rho_u\ge s_i$. These proofs allow zero residual degrees and do not invoke the residual-activity lemma. The unique-exception argument needs no restriction on the diameter of $H$ and no classification theorem for its total domination number.

## 4. Charging and an exact deficit identity

**Lemma 4.1 (inherited charging, rederived).** If $a\ge1$, then

$$0\le s_i<a,\qquad r\ge\sum_i\frac{s_i^2}{a-s_i},\qquad t\le ca^2. \tag{8}$$

*Proof.* The demand is at most $d_i\le a-1$. For each label choose exactly $s_i$ of its actual selected incidences. Let $q'_u$ count chosen incidences at $u$. Then $q'_u\le a-\rho_u$, and each chosen incidence requires $\rho_u\ge s_i$. At a source with $q'_u>0$, assign charge $\rho_u/(a-\rho_u)$ to each chosen incidence. Its total charge is at most $\rho_u$. Since $x/(a-x)$ is increasing on $[0,a)$, each of the $s_i$ chosen incidences of label $i$ receives at least $s_i/(a-s_i)$. Summing proves the residual bound. A source with $\rho_u=a$ has no chosen incidence and is not divided by zero; its cost is simply unused. Zero-residual sources cause no problem.

Using (5),

$$2t\le S-r\le\sum_i\frac{s_i(a-2s_i)}{a-s_i}.$$

For $k=a-s>0$ the summand equals $3a-2k-a^2/k\le(3-2\sqrt2)a$, by $2k+a^2/k\ge2\sqrt2a$. There are $a$ labels, giving $t\le ca^2$. $\square$

Put $\lambda=1-1/\sqrt2$ and $\mathcal D=ca^2-t$. Direct algebra yields

$$\boxed{\mathcal D=\sum_i\frac{(s_i-\lambda a)^2}{a-s_i}+\frac{S-r-2t}{2}+\frac{r-\sum_i s_i^2/(a-s_i)}2.} \tag{9}$$

All three terms are nonnegative. For clarity, the pointwise identity is

$$2ca-\frac{s(a-2s)}{a-s}=\frac{2(s-\lambda a)^2}{a-s}.$$

If $t\ge(c-\eta)a^2$, then (9), $a-s_i\le a$, and Cauchy–Schwarz imply

$$\sum_i(s_i-\lambda a)^2\le\eta a^3,\quad S\le(\lambda+\sqrt\eta)a^2,\quad r\le(\lambda+\sqrt\eta-2c+2\eta)a^2. \tag{10}$$

This is stability of the **demand distribution**, not a graph edit-distance or near-bipartiteness theorem.

## 5. Shared pair capacity and a quadratic loss

**Lemma 5.1 (good-label pair capacity).** Let $I\subseteq A$ have $s_i\ge La$ for $i\in I$, where $L>0$, and assume $|A\setminus I|\le\theta a$. Set

$$Z=\{u\in B:\rho_u\ge La\},\quad z=|Z|,\quad T=(L+\theta)a+1,\quad P=\sum_{i\in I}x_i.$$

If $k$ sources in $Z$ have $q_u>T$, then

$$P\le(z-k)T+kz-\frac{k(k+1)}2\le\frac{z^2+T^2}{2}. \tag{11}$$

*Proof.* All selected incidences with labels in $I$ have sources in $Z$. Outside $Z$, a vertex has $\rho_u<La$ and can select only labels outside $I$, so $q_u\le\theta a$ and $d_H(u,A)<(L+\theta)a$. A source with $q_u>T$ therefore cannot use a supplement outside $Z$, by (7).

Let $U\subseteq Z$ be the $k$ busy sources. The other $z-k$ sources supply at most $(z-k)T$ incidences in $I$. All outgoing arcs of $U$ lie inside $Z$ and occupy distinct unordered pairs incident with $U$. Their number is at most

$$\binom z2-\binom{z-k}2=kz-\frac{k(k+1)}2.$$

This bounds all their outgoing arcs, and hence their incidences in $I$. We have used one common pair budget, not a separate favourable capacity for each source. Finally,

$$(z-k)T+kz-\frac{k(k+1)}2=\frac{z^2+T^2}{2}-\frac{(z-T-k)^2}{2}-\frac k2,$$

proving (11). It holds even when $T$ is not integral or exceeds $z$. $\square$

**Proof of Theorem A.** Suppose $a\ge25$ and $t\ge c_1a^2$. Use

$$\eta=\frac1{5000},\quad L=\frac6{25},\quad \theta=\frac9{125}.$$

Since $\lambda-L>0$ and $(\lambda-L)^2>1/360$, (10) implies that fewer than $\theta a$ labels have $s_i<La$. Take $I$ to be the remaining labels. Thus

$$P\ge La|I|\ge\frac{696}{3125}a^2. \tag{12}$$

Here $\sqrt\eta=\sqrt2/100$. The residual bound (10) becomes

$$r\le\left(-\frac{4999}{2500}+\frac{151}{100}\sqrt2\right)a^2<\frac{17}{125}a^2.$$

Each source in $Z$ costs at least $La$, giving $z\le17a/30$. Also $a\ge25$ implies

$$T=(L+\theta)a+1\le\frac{44}{125}a.$$

Apply (11):

$$P\le\frac12\left[\left(\frac{17}{30}\right)^2+\left(\frac{44}{125}\right)^2\right]a^2=\frac{250321}{1125000}a^2<\frac{696}{3125}a^2,$$

contradicting (12). The exact gap is $239a^2/1125000$. This proves (1). $\square$

All irrational comparisons above are elementary rational-square comparisons. Two separately written checkers verify the constants, one in $\mathbb Q(\sqrt2)$ and one using rational enclosures for $\sqrt2$; neither numerical optimisation nor finite graph enumeration is needed by the proof.

## 6. The all-order maximum-degree consequence

**Proof of Corollary A.** A universal vertex forces an edge-critical graph to be a star: an edge between other vertices would be redundant. For $n\ge4$ that star has fewer than $\lfloor n^2/4\rfloor$ edges. Hence take $a\ge1$.

Suppose $b\ge\beta_1n$ and $m\ge\lfloor n^2/4\rfloor$. Put $\varepsilon=0$ for even $n$ and $1$ for odd $n$. Then

$$t\ge(b-n/2)^2-\varepsilon/4.$$

The function $((x-1/2)/(1-x))^2$ is increasing on $[1/2,1)$ and equals $c_1$ at $x=\beta_1$. Consequently

$$t\ge c_1(n-b)^2-\varepsilon/4=c_1a^2+c_1(2a+1)-\varepsilon/4>c_1a^2,$$

where $c_1>1/12$ gives the final strictness. This contradicts Theorem A for $a\ge25$.

For $1\le a\le24$, the exact lower bound $\beta_1>613168/10^6$ implies

$$b\ge b_0(a)=\left\lceil\frac{613168(a+1)}{386832}\right\rceil>a+1.$$

Since $n=a+b+1$,

$$t\ge\left\lfloor\frac{(b-a-1)^2}{4}\right\rfloor\ge t_0(a)=\left\lfloor\frac{(b_0(a)-a-1)^2}{4}\right\rfloor.$$

The following 24 hand-checkable cases have $t_0(a)>ca^2$, contradicting (8):

| $a$ | $b_0$ | $t_0$ | $a$ | $b_0$ | $t_0$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 1 | 13 | 23 | 20 |
| 2 | 5 | 1 | 14 | 24 | 20 |
| 3 | 7 | 2 | 15 | 26 | 25 |
| 4 | 8 | 2 | 16 | 27 | 25 |
| 5 | 10 | 4 | 17 | 29 | 30 |
| 6 | 12 | 6 | 18 | 31 | 36 |
| 7 | 13 | 6 | 19 | 32 | 36 |
| 8 | 15 | 9 | 20 | 34 | 42 |
| 9 | 16 | 9 | 21 | 35 | 42 |
| 10 | 18 | 12 | 22 | 37 | 49 |
| 11 | 20 | 16 | 23 | 39 | 56 |
| 12 | 21 | 16 | 24 | 40 | 56 |

For each fixed $a$ the lower bound is increasing in $b\ge b_0(a)$, so this covers all orders, not just the 24 minimum orders in the table. A rational upper enclosure $c<3/2-1414213562373095/10^{15}$ suffices to check every entry. $\square$

**Audit of the older coefficient.** The same argument with $c$ and $\beta_0$ proves the inherited theorem directly for all $a\ge1$, because $3c>1/4$. This confirms its floor/odd-order strictness without the residual-activity lemma. No blocking error was found in that rederivation. It is still a candidate pending independent review.

**A scalar comparison only.** At $a=7000,b=11200,h=2000,z=2800$, take $z$ residual rows of degree $h$, the other rows of degree one, and every label demand $h$. Then $r=5608400$, $S=14000000$, $t=(S-r)/2=4195800$. These numbers satisfy both basic charging and the active scalar charging equality $r-b=\sum s_i(s_i-1)/(a-s_i)$, and have $c_1a^2<t<ca^2$. This witnesses a genuine strengthening of the scalar inequality. It is not a graph, and is not asserted to pass the older source–supplement tests.

## 7. A general spare-source theorem

Let $h\ge1$ be the maximum residual degree and $Z=\{u:\rho_u=h\}$ with $|Z|=z$. Let $I=\{i:s_i=h\}$ have size $\ell$. If $z<h$ then $I$ is empty by (6), so assume $h\le z\le h^2+h$.

Every selected incidence of a label in $I$ has its source in $Z$, and $h\le x_i\le z$. At such an incidence (6) gives $d_i\le2h$. Since $R_i=d_i-h$, call $i$ *exceptional* if $d_i=2h$, and *ordinary* otherwise. An exceptional selected incidence must have its supplement in $Z$, by the second inequality of (6). That supplement misses the label and cannot be one of its selected sources. Thus $x_i\le z-1$ for an exceptional label.

Writing $D_i=R_i+x_i$, we have

$$D_i\le h+x_i-1\text{ for ordinary }i,\qquad D_i=h+x_i\text{ for exceptional }i,$$

and in either case $D_i\le h+z-1$.

For $u\in Z$, let $y_u$ count outgoing incidences in $I$, $e_u$ count the exceptional ones, and $p^E_u$ count incoming exceptional arcs. Let $\sigma_u=q_u+p_u$ be its actual pair degree. Define the weighted label load

$$L_u=\sum_{i\in I:\,ui\text{ selected}}\frac h{x_i}.$$

Each label contributes $h$ in total. Also

$$y_u\le q_u\le\sigma_u-p^E_u,\quad p^E_u\le z-1,\quad \sum_{u\in Z}e_u=\sum_{u\in Z}p^E_u. \tag{13}$$

The last equality holds because every exceptional arc is wholly inside $Z$.

**Weighted local bound.** We claim

$$L_u\le2h-1+\frac{e_u-p^E_u}{h+1}. \tag{14}$$

If $y_u=0$, then $L_u=e_u=0$, while $p^E_u\le z-1\le h^2+h-1$ makes the right side nonnegative. If $y_u>0$ and $\sigma_u\le2h-1$, each weight is at most one, so

$$L_u\le y_u\le2h-1-p^E_u\le2h-1+\frac{e_u-p^E_u}{h+1}.$$

It remains to take $\sigma_u=2h+j$. The endpoint inequality (7) bounds the actual degree by $h+z-1$, hence $0\le j\le h^2-1$. Every ordinary label selected at $u$ has $x_i\ge h+j+1$, and every exceptional label has $x_i\ge h+j$. Thus

$$L_u\le\frac{h(2h+j-p^E_u)}{h+j+1}+\frac{he_u}{(h+j)(h+j+1)}. \tag{15}$$

Subtract (15) from the right side of (14). The result is

$$\frac{(h-1)(j+1)}{h+j+1}+p^E_u\left(\frac h{h+j+1}-\frac1{h+1}\right)+e_u\left(\frac1{h+1}-\frac h{(h+j)(h+j+1)}\right).$$

Every term is nonnegative: the middle coefficient is $(h^2-j-1)/[(h+j+1)(h+1)]$, and the final numerator after taking a common denominator is $j(2h+j+1)$. This proves (14) for every source, including those with no selected label in $I$.

Sum (14) over $Z$. The exceptional incoming and outgoing charges cancel by (13), leaving $h\ell\le(2h-1)z$. This proves Theorem B. $\square$

**Corollaries.** For $z=h+k$ with $0\le k\le h^2$,

$$\ell\le\left\lfloor\frac{(2h-1)(h+k)}h\right\rfloor.$$

For $1\le k\le h$ this is $\ell\le2h+2k-2$. In particular $k=1$ gives the older one-spare-source bound, and $k=2$ gives $2h+2$ for $h\ge2$. The case $h=1,k=2$ lies outside this theorem; no conclusion for it is silently asserted. For $k=0$ the bound is $2h-1$.

**Sharpness of reduced premises.** Set $\ell=\lfloor(2h-1)z/h\rfloor$. Number sources modulo $z$ and give label $i$ the distinct sources $ih,ih+1,\ldots,ih+h-1$ modulo $z$. All labels are ordinary with $x_i=h,R_i=h-1,d_i=2h-1$. Each source appears at most $2h-1$ times, so the endpoint inequalities hold with no exceptional arcs. These data attain the integer label bound for the reduced ordinary incidence model. They do not specify the remaining residual graph, missing-pair structure, or graph $G$, so this is not an extremal-graph construction.

The cancellation is essential. An exceptional source can locally exceed $2h-1$ in weighted load; suppressing the compensation term would be an invalid proof. The abstract tests include such systems rather than testing only the ordinary case.

## 8. Validation, formalisation and remaining obligations

The code and data in this checkpoint make the checks repeatable. `src/exact_checks.py` verifies the quadratic-field constants, 24 small-$a$ cases, 25,755 pair identities, 5,050 deficit identities, and 338,350 spare-coefficient triples. `src/interval_check.py` independently verifies the constants and rounding with rational enclosures and rejects three corrupted parameter choices. Neither is a formal proof for all graph orders.

Actual-graph regression reconstructs 4,694 selected systems from 781 distinct labelled critical graphs. It includes all 21 critical graphs found in NetworkX's atlas, 120 generated larger critical graphs, four cycle expansions, and inherited examples. The atlas criticality decisions were cross-checked using a separate distance-based implementation. Some roots' quasi-edge choices were sampled; details and seeds are saved. There are 191 nonempty-demand systems and 194 nonempty good-label pair tests, but **no positive-surplus example and no nonempty maximum-demand spare class in the theorem's range**. Those limitations prevent claiming a nonvacuous actual-graph test of the new dense contradiction or spare theorem.

To exercise the latter's premises directly, the abstract tests accept 7,435 reduced incidence systems, of which 3,555 have exceptional arcs. They also exhaust 59,809 oriented simple graphs through five vertices, making 358,058 pair-capacity threshold checks. These are not critical graphs; they test the counting mechanisms only. All recorded tests pass. Omitted, duplicate and self-supplement graph selections are rejected.

**Formal scope.** `formal/QuasiCore.lean` has been checked using official Lean 4.19.0 in GitHub run 34166620020, at source commit `93a7cdc5ff2a3677d9985941a5df0c4ad08bd1f6`. The five checked propositions concern uniqueness of an exception, forcing a neighbour when the source misses a vertex, and the common-miss obstruction to selecting a forced cross-edge. The file assumes explicit quasi-edge predicates; it does not prove they exist for every critical graph. It contains no `sorry`, new axiom declaration or `native_decide`. The printed axiom dependencies are either empty or the standard `propext`, `Classical.choice`, `Quot.sound`. **No claim of a formally verified charging theorem, spare-source theorem, maximum-degree bound or n=28 proof follows.**

The general formalisation literature already includes an end-to-end Lean/SAT graph-generation framework [3]. This small local slice is not claimed as the first formal treatment of Murty–Simon. The next useful formal targets are quasi-edge existence and the finite injections behind (6), then the charging sum.

The important independent-review questions are: whether the selected-edge injections are genuinely injective and residual; whether all actual selected incidences of good labels are confined to $Z$; whether the shared unordered-pair count in (11) covers every orientation; and whether exceptional arcs in Theorem B have both endpoints in $Z$, enabling exact cancellation. Paul is undertaking specialist outreach. No external endorsement, whole-order extension or resolution of the general conjecture is claimed.

## References

[1] T. W. Haynes, M. A. Henning, L. C. van der Merwe and A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12 (2014), 1882–1889. DOI: 10.2478/s11533-014-0449-3. Author-institution record: <https://dc.etsu.edu/etsu-works/15862/>.

[2] A. Jabalameli, A. Behjati, M. Saghafian, M. M. Shokri, M. Ferdosi and S. Bahariyan, *Improving the Bounds On Murty_Simon Conjecture*, arXiv:1610.00360, canonical v2 dated 10 October 2016. <https://arxiv.org/abs/1610.00360>. Related author-posted full text is identified and distinguished in `literature/COMPARISON.md`.

[3] M. Kirchweger, P. Manrique and S. Szeider, *Formally Verified Graph Generation with SAT Modulo Symmetries and Lean*, IJCAR 2026, LNCS 16688, 117–135. Published 24 July 2026. DOI: 10.1007/978-3-032-32589-1_8. <https://doi.org/10.1007/978-3-032-32589-1_8>.

[4] Paul Lenz project, ChatGPT development, *General-order residual charging and coupled source–supplement cuts*, 7 September 2026, `2026-09-07-coupled-resource-v2/PROOF.md`, Git blob `3d3b4ab5b2da8207f17a3a2afcce49e7119d78e2`. Candidate project source, not an independently published theorem.

[5] Paul Lenz project, ChatGPT development, *LocalIncidence v7*, 7 September 2026, original `MurtySimon_GeneralN_LocalIncidence_v7.zip`, Section 7; its archive hash is recorded in `PROVENANCE.json`. Candidate one-spare-source antecedent.
