from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.vertices= set()

    def add_edge(self,u,v,w, directed= False):
        self.adj_list[u].append((v,w))
        if not directed: self.adj_list[v].append((u,w))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def dfs(self,start):
        stack = [start]
        path = []
        visited= set()

        while stack:
            node = stack.pop()
            for neighbour, w in self.adj_list[node]: 
                if neighbour not in visited: pass
        

def main():
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
    g= Graph()
    for u,v,w in edges:
        g.add_edge(u,v,w)

if __name__ =="__main__":
    main()