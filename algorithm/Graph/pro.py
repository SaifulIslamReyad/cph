import heapq

adj_list = {}

def add_edge(u, v, weight):
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append((weight, v))
    adj_list[v].append((weight, u))

def prim_mst_with_cycles(start_node):
    visited = set()
    min_heap = []
    mst = []
    cycles = []
    total_cost = 0

    visited.add(start_node)

    for weight, neighbor in adj_list[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight

            for next_weight, neighbor in adj_list[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, neighbor))
        else:
            # This edge forms a cycle (both u and v already connected)
            cycles.append((u, v, weight))

    return mst, total_cost, cycles

# Graph edges
edges = [
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

# Build graph
for u, v, w in edges:
    add_edge(u, v, w)

# Run modified Prim’s algorithm
mst, min_cost, cycles = prim_mst_with_cycles(1)

# Print MST
print(f"\n✅ Minimum Cost of MST: {min_cost}")
print("🌿 Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")

# Print cycle edges
print("\n🔁 Edges forming cycles:")
for u, v, w in cycles:
    print(f"{u} - {v} : {w}")
