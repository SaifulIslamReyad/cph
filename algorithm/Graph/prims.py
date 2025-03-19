import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((weight, v))
        self.adj_list[v].append((weight, u))


    def prim_mst(self, start_node):
        visited = set()
        min_heap = []
        mst = []
        w= 0

        visited.add(start_node)
        
        for edge_weight, neighbor in self.adj_list[start_node]:
            heapq.heappush(min_heap, (edge_weight, start_node, neighbor))  

        while min_heap:
            edge_weight, u, v = heapq.heappop(min_heap)

            if v not in visited:  
                visited.add(v)
                mst.append((u, v, edge_weight)) 
                w += edge_weight
                for next_weight, neighbor in self.adj_list[v]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (next_weight, v, neighbor))
        return mst , w


g = Graph()

# edges = [(1, 2, 1), (1, 3, 10), (2, 4, 1), (2, 5, 1), (3, 6, 1), (3, 7, 1), (7, 5, 2), (6, 4, 1)]
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

mst, min_cost = g.prim_mst(1) 

print(f"Minimum Cost of MST: {min_cost}")
print("Edges in MST:", mst)
