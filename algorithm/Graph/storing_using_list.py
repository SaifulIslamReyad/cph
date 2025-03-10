from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def display(self):
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for protibesi in self.adj_list[node]:
                neighbor, _ = protibesi
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                # for neighbor, _ in reversed(self.adj_list.get(node, [])):
                for protibesi in self.adj_list[node]:
                    neighbor, _ = protibesi
                    if neighbor not in visited:
                        stack.append(neighbor)
        print()


g = Graph()


g.add_edge(1, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 4, 1)
g.add_edge(2, 5, 1)
g.add_edge(3, 6, 1)
g.add_edge(3, 7, 1)


g.display()

g.bfs(1)
g.dfs(1)
