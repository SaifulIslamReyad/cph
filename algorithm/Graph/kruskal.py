edges = []
parent = {}


def add_edge(u, v, weight):
    edges.append((weight, u, v))
    if u not in parent:
        parent[u] = u
    if v not in parent:
        parent[v] = v


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(u, v):
    parent[find(v)] = find(u)


def kruskal_mst_with_cycle_detection():
    edges.sort()
    mst = []
    min_cost = 0
    cycle_edges = []

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            min_cost += weight
        else:
            cycle_edges.append((u, v, weight))

    return mst, min_cost, cycle_edges


graph_edges = [
    (1, 2, 11),
    (1, 3, 13),
    (1, 5, 2),
    (2, 3, 15),
    (2, 5, 12),
    (5, 4, 14),
    (5, 8, 5),
    (4, 2, 8),
    (2, 7, 6),
    (4, 7, 10),
    (4, 8, 17),
    (7, 8, 11),
    (7, 6, 21),
    (8, 6, 7),
]

for u, v, w in graph_edges:
    add_edge(u, v, w)

mst, min_cost, cycle_edges = kruskal_mst_with_cycle_detection()

print(f"Minimum Cost of MST: {min_cost}")
print("Edges in MST:", mst)
print("Edges forming cycles:", cycle_edges)



# **Algorithm** KruskalMSTWithCycleDetection(edges, parent)

# // Computes the Minimum Spanning Tree (MST) of a connected, undirected graph using Kruskal's algorithm,
# // while detecting and collecting edges that form cycles when rejected.
# // Uses Union-Find (Disjoint Set Union) data structure for efficient cycle detection.
# // Returns:
# //   - mst: List of edges in the MST as tuples (u, v, weight)
# //   - min_cost: Total weight of the MST
# //   - cycle_edges: List of edges that form cycles when rejected

# {
#     // Helper function to find root parent of a node with path compression
#     function Find(node):
#         if parent[node] ≠ node then
#             parent[node] := Find(parent[node]);  // Path compression
#         return parent[node];

#     // Helper function to merge sets of two nodes
#     function Union(u, v):
#         root_u := Find(u);
#         root_v := Find(v);
#         parent[root_v] := root_u;  // Union by attaching to root

#     // Initialize
#     Sort edges in non-decreasing order of weight;
#     mst := empty list;
#     min_cost := 0;
#     cycle_edges := empty list;

#     // Process each edge in sorted order
#     for each (weight, u, v) in edges do:
#         if Find(u) ≠ Find(v) then:
#             Union(u, v);
#             Append (u, v, weight) to mst;
#             min_cost := min_cost + weight;
#         else:
#             Append (u, v, weight) to cycle_edges;  // Edge forms a cycle

#     return (mst, min_cost, cycle_edges);
# }

# **Subroutine** AddEdge(u, v, weight, edges, parent)

# // Adds an edge to the graph and initializes parent pointers if nodes are new
# {
#     Append (weight, u, v) to edges;
#     if u not in parent then:
#         parent[u] := u;  // Initialize as self-parent
#     if v not in parent then:
#         parent[v] := v;
# }