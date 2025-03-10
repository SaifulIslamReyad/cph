class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:

            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges):
    edges.sort(key=lambda edge: edge[2])
    disjoint_set = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            total_cost += weight
            disjoint_set.union(u, v)

    return mst, total_cost



n = 9  
edges = [
    (1, 2, 11),
    (1, 3, 13),
    (1, 5, 2),
    (2, 3, 15),
    (2, 4, 8),
    (2, 5, 12),
    (2, 7, 6),
    (4, 5, 14),
    (4, 8, 17),
    (4, 7, 10),
    (5, 8, 5),
    (6, 7, 21),
    (6, 8, 7),
    (7, 8, 11)
]

mst, total_cost = kruskal(n, edges)

print(f"\nTotal Minimum Cost: {total_cost}")
