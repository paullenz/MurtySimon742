# Pair-covered interfaces and critical-edge charging

**17 September 2026. Internal candidate theorem; external review and novelty open.**
Research directed by Paul Lenz. Derivation and implementations by ChatGPT/Geeps.

## Main conclusions and precise scope

Use the actual selected-representative system of a finite simple diameter-two
edge-critical graph G. Let J be its complement, choose a minimum-degree pivot p
in J, and put A=N_J(p), B=V(J) minus N_J[p]. At each B-vertex u, selected and
residual cross-incidences partition its J-neighbours in A; rho_u is its residual
degree. At each A-label i, let R_i count residual incidences and put
s_i=max(0,deg_(G[A])(i)-R_i). Assume the **whole** levels

    T={i:s_i=d}, H={u:rho_u>=d}, |T|=|H|=d>=3.

The representative construction and its local injections are proved in the
[preceding structural treatment](PREREQUISITE_STRUCTURAL_TREATMENT.md),
pinned at commit `314f953a5ba15ca62148d52062bd0ee8568dcccb`.

Let Q=G[T], K=N_(G[A])(T) minus T, and use the full low receiver pools
V_t={v outside H:R_v=T minus {t}}. Put p_t=|V_t|, m=sum p_t,
mu=binom(d,2)-e(Q). For k in K let S_k=N_G(k) intersect T, w_k=d at zero
demand and d-1 otherwise, l_k=w_k-|S_k|, L=sum l_k. Let beta count residual
tight incidences outside the full pools, and D=L+beta+2mu. These are
nonnegative integers. The inherited scalar capacity W satisfies

    W>=d+(d-1)m+D, m>=d;
    extra high-source selections imply m>=2d.

For h>=1 define E_h(Q) as the number of tight edges whose two Q-degrees
are at least h+1. The new conclusions are:

**Pair coverage.** If D<d(d-2), every tight pair has a common K-neighbour.

**Critical-edge charge.** Whenever this pair coverage holds,

    E_h(Q)<=L+floor(L/h)+beta                         (SC)
    D>=2mu+ceil(h E_h(Q)/(h+1))                       (1)

for every integer h>=1. One K-label adjacent to all T is **not** required.

**Quadratic corollary.** Every such actual exact block, for d>=3, satisfies

    D>=ceil(d(d-1)/4).                               (2)

**Five-label corollary.** At d=5 the stronger conclusion is

    D>=8, W>=5+4m+8>=33;
    extra high-source selections imply W>=53.        (3)

These are necessary structural conditions, not graph constructions or new
catalogue exclusions. Exact-block existence is a hypothesis; unrestricted
coverage, sharpness, novelty and independent acceptance remain open.

## 1. Exact rows force pair coverage

Write K_t=N_G(t) intersect K and kappa=|K|. The inherited exact identity is

    sum_K w_k=d+(d-1)m+D.

All K-weights are at least d-1. Hence
kappa<=m+floor((d+D)/(d-1)). The exact tight rows are

    |K_t|=1+m-p_t+beta_t+nu_t,
    beta_t>=0, nu_t=d-1-deg_Q(t)>=0.

Every full pool is nonempty, so p_t+p_s<=m-(d-2). Thus
|K_t|+|K_s|>=m+d for distinct t,s. Inclusion-exclusion gives

    |K_t intersect K_s|>=d-floor((d+D)/(d-1)).          (4)

When D<d(d-2), this integer is positive. No common-label congruence or
zero-loss hypothesis has been used.

## 2. Which supports can threaten an edge?

For S subset T define

    B_Q(S)={ts in E(Q): s in S, t outside S,
                         N_Q(t) intersect S={s}}.

Edges are unordered; the displayed orientation identifies the outside endpoint.
Each t outside S contributes at most one edge, so |B_Q(S)|<=d-|S|.
Membership means that a replacement through a tight intermediate vertex is
unavailable. It does **not** imply actual criticality: other short paths may
remain.

Suppose the interface is pair-covered and delete a tight edge ts. Every affected
pair wholly inside T retains a path through a shared K-neighbour. Other
potentially destroyed paths of length at most two have endpoints t,x with x
an exclusive neighbour of s, or the reverse.

Full-pool vertices are protected. If v in V_s and k in K neighbours s, then
kv is an edge of G. It cannot be residual in J because R_v=T minus {s}; it
cannot be selected in J because k and v both miss s in J, contradicting
representative domination of every A-label. A common K-neighbour of t,s
therefore supplies t-k-v. This works without an all-tight common label.

The pivot, high vertices and A-labels outside T union K have no tight
G-neighbours. The remaining external vertices are K-labels and
O=B minus (H union V). If such an x is exclusive to s and ts is not in
B_Q(S_x), an r in N_Q(t) intersect S_x distinct from s supplies t-r-x.
Reverse the endpoints for the other direction.

Therefore **every critical tight edge must belong to the union of B_Q(S_x)
for x in K union O**. Full-pool singleton supports were protected, not charged
as arbitrary exceptions. This is a necessary cover, not a converse.

## 3. Charge the threat cover to the defect

Count only edges in E_h(Q). If k in K threatens such an edge, its outside
endpoint has at least h+1 Q-neighbours, exactly one in S_k. All the others,
and the outside endpoint itself, lie in T minus S_k. Consequently

    d-|S_k|>=h+1.

But d-|S_k|=d-w_k+l_k<=l_k+1, so l_k>=h. The label threatens at most
l_k+1 counted edges. Summing over contributing labels costs at most L plus
their number; there are at most floor(L/h) of them.

For x in O, let q_x=d-|S_x|. No low vertex selects a tight label, so q_x
counts its residual tight incidences. High vertices select T and full-pool
incidences have already been subtracted. Thus sum_(x in O)q_x=beta. The
threat counts for these vertices sum to at most beta.

A union is no larger than the sum of its constituent sizes, even if they
overlap. The necessary cover therefore proves (SC). Put q=L+beta. Then
E_h<=q+floor(q/h)=floor((h+1)q/h), and integrality gives (1).

At h=1 this is E_1<=2L+beta. At h=2 it is
E_2<=L+floor(L/2)+beta. The inequality tracks the total cost of exceptional
supports instead of applying a single worst-case hole count to every vertex.

## 4. A quadratic bound for every block size

Let C=binom(d,2). If D>=d(d-2), conclusion (2) is immediate for d>=3.
Otherwise the interface is pair-covered and the h=1 inequality applies.

Every edge outside E_1 has a degree-one endpoint. A degree-one Q-vertex
has d-2 missing neighbours, while the sum of missing degrees is 2mu.
Thus at most 2mu/(d-2) vertices have degree one, and

    E_1>=C-mu-2mu/(d-2).

Using L+beta>=E_1/2 gives

    D>=C/2+[3/2-1/(d-2)]mu>=C/2.

The bracket is positive for d>=3. Taking the integer ceiling proves (2).
This is a hand corollary for arbitrary d, not an extrapolation of the finite
tight-graph tables. The sharper h-dependent inequality (1) remains available.

## 5. Five-label boundary closure by hand

Suppose d=5 and D<=7. Pair coverage follows because D<15. The inherited
universal-core envelope is

    D>=2mu+3 max(0,4-2mu).

It rules out mu=0,1, whose lower bounds are 12 and 8. Nonnegativity excludes
mu>=4. Hence mu=2 or 3.

If mu=2, no Q-vertex has degree one: that would require three missing
incident edges. All eight edges therefore lie in E_1. But

    8<=2L+beta<=2(D-4)<=6,

which is impossible. This covers adjacent and disjoint missing edges together.

If mu=3, Q has seven edges and total missing degree six. Each degree-one
vertex consumes three of those units, so there are at most two such vertices.
At most two edges have a degree-one endpoint, hence E_1>=5. But

    E_1<=2(L+beta)=2(D-6)<=2,

again impossible. This proves (3) directly from exact rows, the universal-core
bound and the new charge; the earlier individual D=6 case split is unnecessary.

## 6. Executed checks and limitations

The Python bitset checker and C++ explicit-intermediate-vertex checker agree
on **121,549 complete records**: 87,685 local graphs and 33,864 labelled
tight-graph records. The local families include both a single common interface
label and pair-covered interfaces with **no** all-tight common label. There
are 71,241 records satisfying the sufficient deletion premises, with no lost
short pair. Five named controls test missing pair coverage, missing pool
protection, an allowed threat, the failure of the converse, and no-common-label
coverage. The first three start at diameter two and lose short pairs.

The support enumeration checks 255,632 weight/support/threshold instances,
retaining each actual threatened-edge mask. Additional exact checks cover
5,314,440 row inequalities and 244,420 floor/ceiling identities. All labelled
Q through d=6 also pass the pendant-edge inequality used in Section 4.

The numerical necessary-condition envelope has minimum 8 over the 1,024
labelled d=5 tight graphs and 13 over the 32,768 d=6 tight graphs. Respectively
40 and 60 Q-masks attain those minima. These are **auxiliary tight graphs**,
not original exact-block realizations. The d=6 minimum is retained as a
diagnostic; no d=6 sharpness or separate strengthened theorem is asserted here.

Run `python3 verify_published.py` to regenerate both implementations and check
all decision bytes and the pinned hashes. Python 3.10+ and a C++17 compiler
are sufficient. The ZIP includes full compressed input and decision streams.
Both implementations and the proof are by the same assistant; this is not
independent expert review. Older replay families were not rerun in this package.

The pre-test derivations are pinned at commits
`f047855b3d4f51f273fe1ba270284f6025134243` (special case) and
`d151af72e1fbd4a7fa2759347c045168cd868338` (pair coverage and support charge).
The quadratic corollary was extracted from the proved charge and checked
against every retained tight graph before this checked publication. Classical
background only: Tao Wang, Ping Wang and Qinglin Yu, *On Murty-Simon Conjecture
II*, arXiv:1301.0460 (2013). No literature-priority determination is made.

**Next proof obligation:** examine d=5,D=8 using the actual threat cover and
its equality conditions; a tight graph satisfying the numerical envelope is
not enough. Exact-block coverage for arbitrary original graphs remains a
separate, essential gap. Canonical counts and promotion gates are unchanged.
