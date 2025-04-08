class Graph:
    def __init__(self):
        self.edges = []
        self.parent = {}

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
        if u not in self.parent:
            self.parent[u] = u
        if v not in self.parent:
            self.parent[v] = v

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        self.parent[self.find(v)] = self.find(u)

    def kruskal_mst_with_cycle_detection(self):
        self.edges.sort()
        mst = []
        min_cost = 0
        cycle_edges = []

        for weight, u, v in self.edges:
            if self.find(u) != self.find(v):
                self.union(u, v)
                mst.append((u, v, weight))
                min_cost += weight
            else:
                cycle_edges.append((u, v, weight))

        return mst, min_cost, cycle_edges


g = Graph()

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

for u, v, w in edges:
    g.add_edge(u, v, w)

mst, min_cost, cycle_edges = g.kruskal_mst_with_cycle_detection()

print(f"Minimum Cost of MST: {min_cost}")
print("Edges in MST:", mst)
print("Edges forming cycles:", cycle_edges)
