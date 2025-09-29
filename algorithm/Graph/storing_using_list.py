from collections import defaultdict

adj_list = defaultdict(list)

def add_edge(u,v,w):
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

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

for u,v,w in edges:
    add_edge(u,v,w)