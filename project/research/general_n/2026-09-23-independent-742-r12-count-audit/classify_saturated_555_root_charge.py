"""Exact finite classification for the saturated n=18 (5,5,5) profile.

This is a necessary-condition screen, not a D2C realization search.  It
enumerates the upward-closed membership counts, all one-use Boolean-step
assigned-source skeletons, and the minimum root-certificate deficit charge
visible from the forced B-skeleton.
"""
from itertools import product
import json


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def membership_vectors():
    for c in compositions(10, 8):
        if any(sum(c[K] for K in range(8) if (K >> i) & 1) != 5
               for i in range(3)):
            continue
        if all(not c[K] or all((K >> i) & 1 or c[K | (1 << i)]
                               for i in range(3))
               for K in range(8)):
            yield c


def evaluate(counts):
    vertices = []
    for K, count in enumerate(counts):
        vertices.extend((K, j) for j in range(count))
    index = {vertex: j for j, vertex in enumerate(vertices)}
    incidences = []
    for t, (K, _) in enumerate(vertices):
        for i in range(3):
            if not ((K >> i) & 1):
                choices = [index[u] for u in vertices
                           if u[0] == K | (1 << i)]
                incidences.append((t, i, choices))

    valid = 0
    optimum = None
    for picks in product(*(incidence[2] for incidence in incidences)):
        forced, forbidden = set(), set()
        okay = True
        for (t, i, _), u in zip(incidences, picks):
            edge = tuple(sorted((t, u)))
            if edge in forced:  # a physical edge is assigned only once
                okay = False
                break
            forced.add(edge)
            for w, (Kw, _) in enumerate(vertices):
                if ((Kw >> i) & 1) and w != u:
                    forbidden.add(tuple(sorted((t, w))))
        if not okay or forced & forbidden:
            continue
        valid += 1
        neighbours = [set() for _ in vertices]
        for u, w in forced:
            neighbours[u].add(w)
            neighbours[w].add(u)

        root_vertices = [t for t in range(10) if neighbours[t]]
        choices = []
        for t in root_vertices:
            candidates = []
            K = vertices[t][0]
            for b, (L, _) in enumerate(vertices):
                if b == t or b in neighbours[t] or K & L:
                    continue
                if neighbours[t].isdisjoint(neighbours[b]):
                    candidates.append(b)
            candidates.append(-1)  # singleton A-witness
            choices.append(candidates)

        best_for_skeleton = None

        def search(j, witness_classes, singleton_costs):
            nonlocal best_for_skeleton
            if len(singleton_costs) > 4:  # only four inactive A-vertices
                return
            if j == len(root_vertices):
                b_cost = 0
                for endpoint_list in witness_classes.values():
                    missed = set(endpoint_list)
                    for t in endpoint_list:
                        missed.update(neighbours[t])
                    b_cost += max(0, len(missed) - 7)
                s_cost = sum(singleton_costs)
                value = (b_cost + s_cost, len(singleton_costs), b_cost, s_cost)
                if best_for_skeleton is None or value < best_for_skeleton:
                    best_for_skeleton = value
                return
            t = root_vertices[j]
            for b in choices[j]:
                if b == -1:
                    r_t = 3 - vertices[t][0].bit_count()
                    search(j + 1, witness_classes,
                           singleton_costs + [3 + r_t])
                else:
                    new_classes = {key: list(value)
                                   for key, value in witness_classes.items()}
                    new_classes.setdefault(b, []).append(t)
                    search(j + 1, new_classes, singleton_costs)

        search(0, {}, [])
        if optimum is None or best_for_skeleton < optimum:
            optimum = best_for_skeleton

    return {
        "membership_counts": list(counts),
        "valid_assigned_source_skeletons": valid,
        "minimum_visible_root_charge": optimum[0],
        "minimum_singleton_count": optimum[1],
        "minimum_B_witness_charge": optimum[2],
        "minimum_singleton_charge": optimum[3],
    }


def main():
    rows = [evaluate(counts) for counts in membership_vectors()]
    print(json.dumps({"profile": "n18-Delta10-saturated-555",
                      "membership_vector_count": len(rows),
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
