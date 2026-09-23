# Subset-union Hall envelope: second fresh batch

The proved graph-level envelope H was tested on a disjoint range: seeds 550--749, n=17--42.

Every one of the 5,200 greedy-deletion outputs was independently checked to have diameter two and to cease having diameter at most two after deletion of each edge.

Results:
- certified graphs: 5,200 / 5,200;
- live-strip maximum-root states: 350;
- scalar E>=15 roots: 1;
- maximum E: 17;
- H>=15 roots: 0;
- maximum H: 10.

The sole scalar false positive is n=22, seed 729, root 17, with E=17 but H=6. An independent exact certificate-edge assignment DP enumerated 227 reachable eligible-label count vectors and found exact maximum S=6. Thus H is sharp on this hostile root and the scalar envelope overcounts it by eleven.

Combined with the immediately preceding disjoint batch, the new H screen covers 7,800 fully certified graphs and 519 live-strip maximum roots, with three scalar E>=15 roots and no H>=15 root. This remains finite internal evidence and authorizes no universal H<15 claim.
