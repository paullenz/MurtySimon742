# Audit summary — Hall density / cut stability

Date: 2026-09-18

Status: independent algebraic audit support only. These computations do not replace the hand proofs.

## Scope

The checker `check_hall_cut_stability.py` generates arbitrary finite A-graphs, partitions the A-vertices into pair classes, designates an arbitrary subset of same-class edges as direct, chooses one source endpoint for every non-direct edge, and constructs nonnegative `L_P,Z_P` and direct-credit variables satisfying the exact local degree identities.

It then checks every family of pair classes for:

1. the exact degree/cut identity;
2. the exact Hall decomposition
   `w_X-a_X(a_X-T0)=2E_X+M_X+J_X`;
3. the capacity lift with independent nonnegative capacity excess `kappa_X`;
4. the dual Hall sandwich;
5. complementary-cut conservation.

The generated objects are intentionally more general than actual D2C configurations. The purpose is to independently stress the algebra and sign conventions.

## Frozen run

Command-equivalent parameters:

- seed: `74218`;
- trials: `50,000`;
- A-order range: `2..14`;
- pair-class count: up to `6`;
- every subset of pair classes checked.

Results:

- random graph/partition trials: **50,000**;
- pair-class instances: **156,014**;
- family/subset checks: **834,948**;
- failures: **0**.

A separate development stress run used seed `742` and completed **200,000** random trials with zero failures of the same exact identities.

## What this audit does not establish

It does not verify:

- existence of a corresponding D2C graph for an abstract generated tuple;
- any eventual second-extremal conclusion;
- the beta/source structural input;
- the aligned-code capacity theorem itself.

Those remain mathematical statements whose support comes from the preserved hand proofs and their own audits.