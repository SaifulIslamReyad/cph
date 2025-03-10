class Graph:
    def __init__(self):
        self.edges = []
        self.parent = {}
        self.rank = {}

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
        if u not in self.parent:
            self.parent[u] = u
            self.rank[u] = 0
        if v not in self.parent:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

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

    def kruskal_mst(self):
        self.edges.sort() 
        mst = []
        min_cost = 0

        for weight, u, v in self.edges:
            if self.find(u) != self.find(v):
                self.union(u, v)
                mst.append((u, v, weight))
                min_cost += weight

        return mst, min_cost


g = Graph()

edges = [(1, 2, 1), (1, 3, 10), (2, 4, 1), (2, 5, 1), (3, 6, 1), (3, 7, 1) , (7,5,2) , (6, 4 ,1)]

for u, v, w in edges:
    g.add_edge(u, v, w)

mst, min_cost = g.kruskal_mst()


ans = []
for u, v, w in mst:
    ans.append((u, v, w))

print(f"Minimum Cost of MST: {min_cost}")
print(f"edges areans {ans}")
