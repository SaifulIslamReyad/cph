import heapq

adj_list = {}


def add_edge(u, v, weight):
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append((weight, v))
    adj_list[v].append((weight, u))


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
    add_edge(u, v, w)


def dijkstra(start):
    distances = {node: float("inf") for node in adj_list}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        for weight, neighbor in adj_list[node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

source = 1
shortest_paths = dijkstra(source)

for node in sorted(shortest_paths):
    print(f"Node {node}: {shortest_paths[node]}")



# **Algorithm** DijkstraShortestPaths(v, adj_list, distances)

# // distances[j] is set to the length of the shortest path from vertex v to vertex j in a digraph G. 
# // distances[v] is set to zero. G is represented by its adjacency list adj_list, where each entry 
# // consists of a neighbor vertex and the weight of the edge connecting them.

# {
#     for each node in adj_list do  
#     { // Initialize distances.  
#         distances[node] := ∞;  
#     }

#     distances[v] := 0;  
#     pq := empty priority queue;  
#     Insert (0, v) into pq;  

#     while pq is not empty do  
#     {  
#         (curr_dist, node) := Extract minimum from pq;  

#         for each (weight, neighbor) in adj_list[node] do  
#         {  
#             new_dist := curr_dist + weight;  
#             if new_dist < distances[neighbor] then  
#             {  
#                 distances[neighbor] := new_dist;  
#                 Insert (new_dist, neighbor) into pq;  
#             }  
#         }  
#     }  

#     return distances;  
# }