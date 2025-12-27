from collections import defaultdict


edges = [
        (1, 2, 1),
        (1, 3, 1),
        (1, 4, 1),
        # --------
        (5, 6, 1),
        (5, 7, 1),
        (5, 8, 1),
        # --------
        (9, 10, 1),
        (9, 11, 1),
        (9, 12, 1),
        # --------
        (10, 21, 1),
        # --------
        (50, 60, 1),
        # --------
        (90, 112, 1),
        # --------
    ]


g= defaultdict(list)
v=set()
global_visited=set()

def create_graph(L):
    for i,j,k in L:
        g[i].append((j,k))
        v.add(i)
        v.add(j)

def dfs(a):
    visited = set()
    stack = [a]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            for i,j in reversed (g[n]):
                if i not in visited:
                    stack.append(i)

    for i in visited:
        global_visited.add(i)

if __name__=="__main__":
    create_graph(edges)
    c=0
    for i in v:
        if i not in global_visited:
            c+=1
            dfs(i)
    print(c)
