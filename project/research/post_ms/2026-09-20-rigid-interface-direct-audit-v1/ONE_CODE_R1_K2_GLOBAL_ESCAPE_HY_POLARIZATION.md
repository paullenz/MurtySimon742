# Residual-one k=2 global escape H/Y polarization

Date: 2026-09-20

Status: **same-session conditional strengthening**, under residual dimension one, `k=2`, `J2=empty`, `p>=3`. No finite scan is used. This note strengthens the immediately preceding F0-only polarization: the source escape vertex need not be F0, W_s-free, nonhub, or proper-support.

## 1. Theorem

Let

`E=U\W_s`

be the outside escape reservoir in the residual-one `k=2` branch. Then every `t in E` satisfies

> **`d_H(t)>0  =>  d_Y(t)<=1`.**                         `(GHY-POL)`

Hence for every subset `S subseteq E`,

> **`Z_{H,S}+Z_{Y,S} >= |S| min{|H|,y-1}`.**            `(GHY-BILL)`

On the exact low-k ray `|E|=|H|=y=p-1`,

> **`Z_{H,E}+Z_{Y,E} >= (p-1)(p-2)`.**                  `(GHY-RAY)`

Thus the whole escape reservoir carries an exact located A--U hole block of leading coefficient one, independently of the old five-class partition.

## 2. Why the source class is irrelevant

Fix `t in E` with an H-neighbour `h_i` and suppose `t` has two distinct Y-neighbours `y0,y1`.

The edge `ty0` lies in the triangle `t-h_i-y0`, since Y is complete to H. Apply raw triangle-edge criticality.

### t-sourced orientation

Any witness in the rooted B-neighbourhood shares the root with t, so it cannot have singleton common neighbourhood `{y0}`. A witness in X sees both Y-neighbours `y0,y1`; a witness in Y sees the H-neighbour `h_i`. Thus no t-sourced singleton certificate exists.

This uses only `t in U`, `d_Y(t)>=2`, and `d_H(t)>0`. It does not use the escape class of t.

### y0-sourced orientation

Let w satisfy

`w in N(t)\N[y0]`,

`N(y0) cap N(w)={t}`.                                    `(GHY-R)`

Exactly as in the F0-only proof:

1. the root and matched endpoints are impossible witness locations because they create fixed extra common neighbours with y0;
2. the singleton condition across all tight fibres forces `c(w)=bar d`;
3. at `J2=empty`, `A_{bar d}=empty`, so `w in U_{bar d}`;
4. Y is complete to X, hence `N_X(w)=empty`.

The selected witnesses W_s cannot be w because their selected K-head is another common neighbour with y0. Therefore w is an outside `U_{bar d}` vertex.

Now `c(w)=bar d` means w sees every private endpoint `q_l`, `l in I`.

For the private-spoke edge `wq_l`, the orientation sourced at `q_l` would require an A-witness adjacent to w. But w is X-anticomplete; a Y-witness has `h_l` as an extra common neighbour; and K is also excluded by X-anticompleteness. A B-layer witness shares the root. Thus the reverse private-spoke orientation is impossible.

Consequently every private spoke is forced forward through `h_l`:

> `N(w) cap N(h_l)={q_l}` for every `l in I`.             `(GHY-PRIV)`

Take the original H-neighbour `h_i of t`. Since `(GHY-R)` requires `wt in E` and by assumption `th_i in E`, the vertex t is a common neighbour of w and h_i distinct from q_i, contradicting `(GHY-PRIV)`.

Thus the y0-sourced orientation is also impossible. The edge ty0 would not be critical, contradiction.

This proves `(GHY-POL)` for **every** outside escape t.

## 3. Exact located-hole bill

For each `t in S`:

- if `d_H(t)=0`, all `|H|` H--t pairs are absent;
- if `d_H(t)>0`, `(GHY-POL)` gives at least `y-1` missing Y--t pairs.

These physical pairs are disjoint across t. Summation gives `(GHY-BILL)`.

On the exact stress ray

`y=p-1`, `|H|=p-1`, `|E|=p-1`,

the cheaper arm costs `p-2` per escape, giving `(GHY-RAY)` exactly.

## 4. Strategic consequence

This supersedes the F0-only interpretation of the new polarization. The entire outside reservoir is now forced into an H-anticomplete / Y-sparse dichotomy.

In particular:

- the compressed pure-F0 endpoint is impossible;
- the pure-D1 endpoint cannot evade by changing the K-neighbour count;
- K-heavy, F1, W-heavy and mixed escapes also pay the same located A-hole floor before their class-specific bills;
- the old class partition is still useful for *additional* disjoint costs, but no class can remove `(GHY-RAY)`.

The immediate next calculation should therefore restart the exact weighted rooted ledger with the global located block `(GHY-RAY)` inserted as a compulsory baseline, and then add only currencies provably disjoint from it (notably missing U--U pairs, U-slack and selected A-side slack). This is preferable to another unweighted class coefficient.

## 5. Trust boundary

The theorem is conditional on the same rigid one-code / residual-one / `J2=empty` interface as the surrounding package. It does not establish that the rigid complete Hall cut is realizable. Bounded actual-D2C regression still has zero positive complete-cut fixtures with `x>=3`, and `X_3` remains the mandatory hostile control.