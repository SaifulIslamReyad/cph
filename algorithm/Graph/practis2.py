import heapq
L={}
def add_edge(u,v,w):
    if u not in L: L[u]=[]
    if v not in L: L[v]=[]
    L[u].append((w,v))
    L[v].append((w,u))
def prims():
    cost=0
    heap=[]
    mst=[]
    visited=set()
    cycle=[]
    start= 1
    visited.add(start)
    for w,n in L[start]:
        heapq.heappush(heap,(w,start,n))

    while heap:
        w,u,v= heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            mst.append((u,v,w))
            cost+=w
            for w,n in L[v]:
                if n not in visited:heapq.heappush(heap,(w,v,n))
        else:
            cycle.append((u,v,w))
    return mst, cycle, cost

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
print(prims())