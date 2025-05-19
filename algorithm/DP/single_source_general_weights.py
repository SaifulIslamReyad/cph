def bellman_ford(n, edges, source):
    # Step 1: Initialize distances and parent pointers
    dist = [float('inf')] * (n + 1)
    dist[source] = 0
    parent = [None] * (n + 1)

    # Step 2: Relax all edges n-1 times
    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Step 3: Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("⚠️ Negative weight cycle detected!")
            return None, None

    return dist, parent

def print_paths(dist, parent, source, n):
    print(f"\n📌 Shortest distances from node {source}:")
    for node in range(1, n + 1):
        print(f"Node {node}: {dist[node]}")

    print("\n📍 Shortest paths from source to each node:")
    for node in range(1, n + 1):
        if node == source:
            continue
        path = []
        curr = node
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        print(f"Path to {node}: {' -> '.join(map(str, path))}")

# -------------------------------
# Example usage

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

n = 8           # Number of nodes
source = 1      # Source node

# Run Bellman-Ford algorithm
distances, parents = bellman_ford(n, edges, source)

# Output results
if distances:
    print_paths(distances, parents, source, n)
