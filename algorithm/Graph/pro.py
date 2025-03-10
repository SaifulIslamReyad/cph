import heapq as hq


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, w):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((w, v))
        self.adj_list[v].append((w, u))

    def prims(self, start):
        L = []
        weight = 0
        ans = []
        visit = set()
        visit.add(start)
        for w, x in self.adj_list[start]:
            hq.heappush(L, (w, x, start))

        while L:
            ww, xx, yy = hq.heappop(L)
            if xx not in visit:
                weight += ww
                ans.append((xx, yy, ww))
                visit.add(xx)
                for www, xxx in self.adj_list[xx]:
                    hq.heappush(L, (www, xxx, xx))

        return ans, weight


g = Graph()

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

for u,v,w in ed:
    g.add_edge(u,v,w)

ans , weight =  g.prims(1)

print(ans, weight)
