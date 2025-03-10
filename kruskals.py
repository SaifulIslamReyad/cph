# Disjoint Set Union (DSU) (also known as Union-Find). Let’s break it down step by step.

# 1. Class: DisjointSet (Union-Find Data Structure)
# This class helps efficiently check if two nodes belong to the same connected component and merge them if needed.

# Attributes:
# python
# Copy
# Edit
# def __init__(self, n):
#     self.parent = list(range(n))  
#     self.rank = [0] * n 
# parent: Keeps track of the leader (representative) of each set. Initially, each node is its own parent.
# 📌 Example: If n = 5, then parent = [0, 1, 2, 3, 4] (each node is its own leader).
# rank: Helps in union by rank, which optimizes merging. Initially, all nodes have rank 0.
# Find Operation with Path Compression
# python
# Copy
# Edit
# def find(self, u):
#     if self.parent[u] != u:
#         self.parent[u] = self.find(self.parent[u])  
#     return self.parent[u]
# Finds the root (leader) of a set.
# Path Compression: Flattens the tree by making all nodes point to the root, improving efficiency.
# 📌 Example:
# If parent = [0, 1, 2, 1, 3], then find(4) calls find(3), then find(1), and updates parent[4] = 1.
# Union Operation (Merging Two Sets)
# python
# Copy
# Edit
# def union(self, u, v):
#     root_u = self.find(u)
#     root_v = self.find(v)

#     if root_u != root_v:
#         if self.rank[root_u] > self.rank[root_v]:
#             self.parent[root_v] = root_u
#         elif self.rank[root_u] < self.rank[root_v]:
#             self.parent[root_u] = root_v
#         else:
#             self.parent[root_v] = root_u
#             self.rank[root_u] += 1
# Find the root of u and v.
# Union by Rank:
# Attach the smaller tree under the larger tree to keep the tree shallow.
# If ranks are the same, pick one root arbitrarily and increase its rank.
# 2. Kruskal’s Algorithm (kruskal(n, edges))
# python
# Copy
# Edit
# def kruskal(n, edges):
#     edges.sort(key=lambda edge: edge[2])
# Sort edges in ascending order of weight to ensure we always pick the smallest edge first.
# python
# Copy
# Edit
#     disjoint_set = DisjointSet(n)
#     mst = []
#     total_cost = 0
# Initialize Disjoint Set to track connected components.
# mst stores the edges of the Minimum Spanning Tree.
# total_cost keeps track of the total weight.
# python
# Copy
# Edit
#     for u, v, weight in edges:
#         if disjoint_set.find(u) != disjoint_set.find(v):
#             mst.append((u, v, weight))
#             total_cost += weight
#             disjoint_set.union(u, v)
# Iterate through sorted edges.
# If two nodes belong to different sets (find(u) != find(v)), add the edge to MST and merge the sets (union(u, v)).
# This ensures we don't form cycles.
# python
# Copy
# Edit
#     return mst, total_cost
# Returns the MST and its total weight.
# 3. Input Graph & Running Kruskal
# python
# Copy
# Edit
# n = 9  
# edges = [
#     (1, 2, 11),
#     (1, 3, 13),
#     (1, 5, 2),
#     (2, 3, 15),
#     (2, 4, 8),
#     (2, 5, 12),
#     (2, 7, 6),
#     (4, 5, 14),
#     (4, 8, 17),
#     (4, 7, 10),
#     (5, 8, 5),
#     (6, 7, 21),
#     (6, 8, 7),
#     (7, 8, 11)
# ]

# mst, total_cost = kruskal(n, edges)
# print(f"\nTotal Minimum Cost: {total_cost}")
# Runs Kruskal’s Algorithm on n=9 vertices.
# Prints the total cost of the MST.
# Time Complexity Analysis
# Sorting edges: 
# 𝑂
# (
# 𝐸
# log
# ⁡
# 𝐸
# )
# O(ElogE)
# Find & Union operations (using path compression & rank): 
# 𝑂
# (
# 𝛼
# (
# 𝑛
# )
# )
# ≈
# 𝑂
# (
# 1
# )
# O(α(n))≈O(1)
# Total complexity: 
# 𝑂
# (
# 𝐸
# log
# ⁡
# 𝐸
# )
# O(ElogE) (dominant term is sorting edges)
# **Final Output