def floyd_warshall(n, edges):
    # Step 1: Initialize distance matrix
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    next_node = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0
        next_node[i][i] = i

    for u, v, w in edges:
        dist[u][v] = w
        next_node[u][v] = v

    # Step 2: Floyd-Warshall DP
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Step 3: Check for negative cycles
    for i in range(1, n + 1):
        if dist[i][i] < 0:
            print("⚠️ Negative weight cycle detected!")
            return None, None
    return dist, next_node

def print_apsp(dist, n):
    print("\n📌 All-Pairs Shortest Distances:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

def reconstruct_path(u, v, next_node):
    if next_node[u][v] == -1:
        return []

    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

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

n = 8

dist_matrix, next_matrix = floyd_warshall(n, edges)

if dist_matrix:
    print_apsp(dist_matrix, n)

    # Print a specific path example (from node 1 to node 6)
    u, v = 1, 6
    path = reconstruct_path(u, v, next_matrix)
    print(f"\n📍 Shortest path from {u} to {v}: {' -> '.join(map(str, path))}")
