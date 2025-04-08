edges=[]
parent={}
def add_edge(u,v,w):
    edges.append((w,u,v))
    if u not in parent:
        parent[u]=u
    if v not in parent:
        parent[v]=v


def find(node):
    if parent[node]!=node:
        parent[node]= find(parent[node])
    return parent[node]

def union(u,v):
    parent[find(u)]= find(v)



def kruskal():
    edges.sort()
    mst=[]
    cycle=[]
    cost=0
    for w , u , v in edges:
        if find(u)!=find(v):
            union(u,v)
            mst.append((u,v,w))
            cost+=w
        else: 
            cycle.append((u,v,w))
    

    return mst,cycle, cost

graph_edges = [
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

for u,v,w in graph_edges:
    add_edge(u,v,w)

print(kruskal())