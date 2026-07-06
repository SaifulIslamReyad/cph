from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, w=1, directed=False):
        """Add edge to graph. Works for weighted/unweighted, directed/undirected"""
        self.adj_list[u].append((v, w))
        self.vertices.add(u)
        self.vertices.add(v)

        if not directed:
            self.adj_list[v].append((u, w))


# ==================== DFS FUNCTIONS ====================


def dfs_recursive(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor, weight in graph.adj_list[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path)

    return path


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)

            for neighbor, weight in reversed(graph.adj_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return path


def dfs_detect_cycle_undirected(graph):
    visited = set()

    def dfs_util(node, parent):
        visited.add(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                if dfs_util(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph.vertices:
        if vertex not in visited:
            if dfs_util(vertex, -1):
                return True
    return False


def dfs_detect_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)

    def dfs_util(node):
        color[node] = GRAY

        for neighbor, weight in graph.adj_list[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs_util(neighbor):
                return True

        color[node] = BLACK
        return False

    for vertex in graph.vertices:
        if color[vertex] == WHITE:
            if dfs_util(vertex):
                return True
    return False


def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs_util(node):
        visited.add(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                dfs_util(neighbor)

        stack.append(node)

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs_util(vertex)

    return stack[::-1]


# ==================== BFS FUNCTIONS ====================


def bfs_basic(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        path.append(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return path


def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start], 0

    visited = set()
    queue = deque([(start, [start], 0)])
    visited.add(start)

    while queue:
        node, path, dist = queue.popleft()

        for neighbor, weight in graph.adj_list[node]:
            if neighbor == end:
                return path + [neighbor], dist + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], dist + 1))

    return None, -1


def bfs_level_order(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    levels = defaultdict(list)

    visited.add(start)

    while queue:
        node, level = queue.popleft()
        levels[level].append(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return dict(levels)


def bfs_bipartite_check(graph):
    color = {}

    def bfs_util(start):
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor, weight in graph.adj_list[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for vertex in graph.vertices:
        if vertex not in color:
            if not bfs_util(vertex):
                return False, {}

    return True, color


# ==================== UTILITY FUNCTIONS ====================


def find_all_paths_dfs(graph, start, end, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    path = path + [start]

    if start == end:
        all_paths.append(path)
        return all_paths

    for neighbor, weight in graph.adj_list[start]:
        if neighbor not in path:
            find_all_paths_dfs(graph, neighbor, end, path, all_paths)

    return all_paths


def connected_components_dfs(graph):
    visited = set()
    components = []

    def dfs_component(node, component):
        visited.add(node)
        component.append(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                dfs_component(neighbor, component)

    for vertex in graph.vertices:
        if vertex not in visited:
            component = []
            dfs_component(vertex, component)
            components.append(component)

    return components


def get_node_level(graph, start, target):
    """
    Returns the level of a target node from the start node using BFS.
    If the target node is not reachable, returns -1.
    """
    visited = set()
    queue = deque([(start, 0)])  # (node, level)

    visited.add(start)

    while queue:
        node, level = queue.popleft()

        if node == target:
            return level

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return -1  # Target node not reachable


def count_provinces(graph):
    """
    Count the number of provinces (connected components) in the graph.
    A province is a group of directly or indirectly connected nodes.

    Time: O(V+E), Space: O(V)
    """
    visited = set()
    provinces = 0

    def dfs(node):
        visited.add(node)
        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs(vertex)
            provinces += 1

    return provinces


# ==================== EXAMPLE USAGE ====================

if __name__ == "__main__":
    g = Graph()

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
        g.add_edge(u,v,w)

    print("DFS Recursive:", dfs_recursive(g, 1))
    print("BFS Level Order:", bfs_level_order(g, 1))
    print("Cycle Detection (Undirected):", dfs_detect_cycle_undirected(g))
    print("Connected Components:", connected_components_dfs(g))
    print("Number of Provinces:", count_provinces(g))

    # Example with multiple disconnected components
    g2 = Graph()
    # Province 1: nodes 1-3
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    # Province 2: nodes 4-5
    g2.add_edge(4, 5)
    # Province 3: node 6 (isolated)
    g2.vertices.add(6)

    print("\nGraph with 3 provinces:", count_provinces(g2))  # Output: 3

    # Example usage of get_node_level
    g3 = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)]
    g3.add_edges_from_list(edges)

    print("Level of node 6 from node 1:", get_node_level(g3, 1, 6))  # Example output: 3
