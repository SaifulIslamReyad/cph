from icecream import ic
class ds:
    def __init__(self , n):
        self.p = list(range(n))
        self.r = [0]*n

    def  find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find[self.p[u]]
        return self.p[u]
    
    def union (self , u , v):
        ru = self.find(u)
        rv = self.find(v)
        
        if ru != rv :
            if self.r[ru] > self.r[rv]:
                self.p[rv] = ru
            elif self.r[ru] < self.r[rv]:
                self.p[ru] = rv
            else: self.p[rv] = ru ; self.r[ru] +=1
        return rv




def kruskal (n, edges):
    edges.sort(key= lambda edge : edge[2])
    set = ds(n)
    total = 0
    for u,v, wight in edges:
        if set.find(u) != set.find(v): 
            total += wight
            set.union(u,v)


    return total

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
    (7, 8, 11),
]


total= kruskal(n,edges)
print(total)