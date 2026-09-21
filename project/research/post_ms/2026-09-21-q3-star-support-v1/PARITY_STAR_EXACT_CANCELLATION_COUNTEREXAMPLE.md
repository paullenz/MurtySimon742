# Exact parity-star cancellation is false

21 September 2026. Actual D2C counterexample plus exact fixed-multiset optimization.

Let `B=e(G[R union T union S])`, with `r=|R|`, `q=|T|`, and `s=|S|`. The hoped-for universal inequality

    B <= rq+s

is false, even in the exactly-four-centre Q3 parity-plane branch.

## Actual counterexample

The `n=33,m=143` RTS-bow-tie control in `RTS_BOWTIE_REALIZABILITY_RESULTS.json` has

    r=4, q=2, s=12,
    e(R,T)=2, I=e(R)+e(T)=2,
    e(R,S)=4, e(T,S)=12, e(S)=1.

Therefore

    B=2+2+4+12+1=21,
    rq+s=8+12=20.

It is a literal D2C graph and passes direct deletion replay, so the unit excess is not a scalar artefact. In missing-pair notation `M=6`, `U=M-I=4`.

## Exactness on the fixed multiset

`maxsat_rts_bowtie_block.py` maximizes only the parity/star-block edges subject to full diameter-two-criticality, the fixed multiset of six coordinate vertices, three copies of every even star code, `r=4,q=2`, and the RTS bow-tie constraints. Exact RC2 optimization proves

    max B = 21 = rq+s+1.

The returned optimum is independently rebuilt and checked as D2C. Thus the counterexample is block-optimal on this constrained multiset.

## What survives

The unconditional ledger

    B <= rq+s+U

survives, as does the exact identity through matching deficiency and unused capacity. More importantly, `FOUR_CENTRE_BUDGETED_CANCELLATION_GATE.md` was designed precisely for this situation: the full graph still satisfies `m<=M(n)` whenever the block excess

    epsilon=max(0,B-rq-s)

obeys `epsilon<=D(u,s)`. Here `epsilon=1`, while `D(12,12)=93`, so the graph lies very far inside the safe region.

The correct theorem target is therefore not exact cancellation. It is a quantitative upper bound on `epsilon` strong enough to fit the large budget `D`, preferably using raw star-fan replication and coordinate capacity. Any document treating `B<=rq+s` as an unconditional destination is superseded by this control.

## Trust boundary

This invalidates one proposed intermediate inequality, not the four-centre budgeted closure, triangle-free closure, support classification, or general eventual target. The example is sparse and does not challenge `M(n)`.
