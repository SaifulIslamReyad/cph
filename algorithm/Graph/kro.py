class Graph :
    def __init__(self):
        self.edges = []
        self.parent = {}
    
    def add_edge(self,u,v,w):
        self.edges.append((w,u,v))
        if u not in self.parent:
            self.parent[u]=u
        if v not in self.parent:
            self.parent[v]=v

    def find(self, x):
        if self.parent[x]!=x :
            self.parent[x]= self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        self.parent[self.find(u)]= self.find(v)
    
    def kru(self):
        ans = []
        weight= 0
        self.edges.sort()
        for w,u,v in self.edges:
            if self.find(u) != self.find(v):
                self.union(u,v)
                ans.append((u,v,w))
                weight+=w
        return ans , weight
    

g= Graph()
ed = [
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

for i,j,k in ed:
    g.add_edge(i,j,k)

ans , weight =g.kru()
print(ans, weight)