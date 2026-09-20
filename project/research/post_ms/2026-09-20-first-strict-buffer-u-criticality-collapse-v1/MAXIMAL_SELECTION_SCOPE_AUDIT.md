# Scope audit for maximal outside-witness selection

Date: 2026-09-20

Status: same-session internal logical audit of the new representative normalization. This does not replace the next daily adversarial audit.

## Potential concern

The new normalization chooses, among all valid outside-U certificates of the buffer edges `b x`, a representative system maximizing the number m of distinct physical witnesses. Because the F/R label of a head depends on whether its chosen witness meets `a_0`, one must not derive an F/R classification under one representative choice, switch witnesses later, and silently retain the old labels.

## Safe order of operations

The first-strict funnel theorem is formulated after choosing one valid outside certificate for each buffer neighbour. Its raw input for a chosen pair `(x,z_x)` is only

`b z_x in E`, `x z_x notin E`, `N(x) cap N(z_x)={b}`,

plus the consequences proved from that certificate. Nothing in the funnel proof requires the representative to have been chosen by a pre-existing canonical rule.

Likewise the repaired P2 premise is explicitly **selected-representative uniqueness**, not raw-witness uniqueness. Once a representative system is fixed, P2 applies to that selected system.

Therefore the logically safe normalization is:

1. from the graph, list the valid outside-U certificates for each buffer edge;
2. choose a representative system maximizing the number of distinct physical witnesses;
3. only then define m and derive the F/R labels and downstream selected/Hall objects from that maximal system.

Under this order no previously derived F/R label is transported across a change of representative.

## Consequence for m=1

The proof `m=1 => |U_o|=1` uses only the generic reverse-fan fact that every physical outside vertex is a valid certificate for at least one buffer edge and the fact `|X'|>=2`. It occurs **before** the F/R split.

After it gives `U_o={z}`, representative ambiguity disappears completely: z is the only possible outside physical witness, so all subsequent m=1 F/R, all-R/all-F and exact-ledger arguments are representative-invariant.

Thus the new maximal-selection normalization does not require the old all-F labels to survive a re-selection. It requires only that the funnel/source-tuple machinery is valid for an arbitrary fixed valid selected system, which is exactly the semantics recorded by the repaired P2 interface.

## Remaining audit obligation

The next daily adversarial audit should still verify this scope statement against the original selected/Hall construction files, particularly any place where a deterministic tie-breaking convention rather than an arbitrary valid choice was baked into a checker or theorem statement. Until that file-level check is complete, the normalization remains internally provisional. The logical risk is now narrowed to that implementation/scope interface, not to the F/R labels themselves.
