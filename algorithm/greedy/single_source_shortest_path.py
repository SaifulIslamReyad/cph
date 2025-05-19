import heapq

# Graph as an adjacency list
adj_list = {}

def add_edge(u, v, weight):
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append((v, weight))
    # adj_list[v].append((u, weight))  

def dijkstra(start_node):
    # Min-heap priority queue
    min_heap = [(0, start_node)]  # (distance, node)
    distances = {node: float('inf') for node in adj_list}
    distances[start_node] = 0
    visited = set()
    parent = {start_node: None}

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        if u in visited:
            continue
        visited.add(u)

        for neighbor, weight in adj_list[u]:
            if neighbor not in visited:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = u
                    heapq.heappush(min_heap, (new_dist, neighbor))

    return distances, parent

# Sample adj_list
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

# Build the adj_list
for u, v, w in edges:
    add_edge(u, v, w)

# Run Dijkstra from source node 1
source = 1
distances, parents = dijkstra(source)

# Print results
print(f"\n📌 Shortest distances from node {source}:")
for node in sorted(distances):
    print(f"Node {node}: {distances[node]}")

print("\n📍 Paths from source to each node:")
for node in sorted(parents):
    if node == source:
        continue
    path = []
    curr = node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    print(f"Path to {node}: {' -> '.join(map(str, path[::-1]))}")
