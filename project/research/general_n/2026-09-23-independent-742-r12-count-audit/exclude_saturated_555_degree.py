"""Exact degree-budget exclusion for the saturated n=18 (5,5,5) tuple.

The proof enumerates only eight Boolean membership counts and the forced
one-step physical-source choices.  It does not encode diameter or full D2C.
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
        if not all(not c[K] or all((K >> i) & 1 or c[K | (1 << i)]
                                   for i in range(3))
                   for K in range(8)):
            continue
        # Budget rigidity forces a right endpoint incident with all labels,
        # equivalently an empty membership type.
        if c[0] >= 1:
            yield c


def source_skeletons(counts):
    vertices = []
    for K, count in enumerate(counts):
        vertices.extend((K, j) for j in range(count))
    index = {vertex: j for j, vertex in enumerate(vertices)}
    incidences = []
    for t, (K, _) in enumerate(vertices):
        for i in range(3):
            if not ((K >> i) & 1):
                incidences.append((t, i, [index[u] for u in vertices
                                          if u[0] == K | (1 << i)]))
    for picks in product(*(row[2] for row in incidences)):
        forced, forbidden = set(), set()
        valid = True
        for (t, i, _), u in zip(incidences, picks):
            edge = tuple(sorted((t, u)))
            if edge in forced:
                valid = False  # physical edge assigned more than once
                break
            forced.add(edge)
            for w, (Kw, _) in enumerate(vertices):
                if ((Kw >> i) & 1) and w != u:
                    forbidden.add(tuple(sorted((t, w))))
        if valid and not forced & forbidden:
            yield vertices, forced, forbidden


def inspect(counts):
    rows = []
    for vertices, forced, forbidden in source_skeletons(counts):
        allowed_degree = []
        for u, (K, _) in enumerate(vertices):
            allowed_degree.append(sum(
                tuple(sorted((u, w))) not in forbidden
                for w in range(10) if w != u))
        empty_allowed = [allowed_degree[u] for u, (K, _) in enumerate(vertices)
                         if K == 0]
        rows.append({
            "forced_edges": len(forced),
            "forbidden_edges": len(forbidden),
            "allowed_B_edges": 45 - len(forbidden),
            "empty_type_allowed_B_degrees": empty_allowed,
        })
    unique = sorted({(r["forced_edges"], r["forbidden_edges"],
                      r["allowed_B_edges"],
                      tuple(r["empty_type_allowed_B_degrees"])) for r in rows})
    # Degree budget: e(B)>=17.  Every row has exactly 17 allowed B-edges,
    # hence all must occur, U is independent, and U--B is complete.  An empty
    # B-vertex then requires B-degree 4 at deficit one and 5 at deficit zero.
    excluded = all(
        allowed == 17 and (
            (len(empty_degrees) == 1 and empty_degrees[0] < 4) or
            (len(empty_degrees) == 2 and sorted(empty_degrees) < [4, 5])
        )
        for _, _, allowed, empty_degrees in unique)
    return {
        "membership_counts": list(counts),
        "valid_source_skeletons": len(rows),
        "unique_edge_budget_rows": [
            {"forced_edges": row[0], "forbidden_edges": row[1],
             "allowed_B_edges": row[2],
             "empty_type_allowed_B_degrees": list(row[3])}
            for row in unique],
        "degree_budget_excluded": excluded,
    }


def main():
    rows = [inspect(c) for c in membership_vectors()]
    print(json.dumps({
        "profile": "n18-Delta10-saturated-555-one-use",
        "budget_rigid_membership_vectors": len(rows),
        "all_degree_budget_excluded": all(r["degree_budget_excluded"]
                                          for r in rows),
        "rows": rows,
    }, indent=2))


if __name__ == "__main__":
    main()
