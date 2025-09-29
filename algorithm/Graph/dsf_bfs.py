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

    def add_edges_from_list(self, edges, directed=False):
        """Add multiple edges from list of tuples"""
        for edge in edges:
            if len(edge) == 2:  # unweighted
                u, v = edge
                self.add_edge(u, v, 1, directed)
            else:  # weighted
                u, v, w = edge
                self.add_edge(u, v, w, directed)


# ==================== DFS IMPLEMENTATIONS ====================


def dfs_recursive(graph, start, visited=None, path=None):
    """
    SIMPLE: Basic recursive DFS traversal
    Time: O(V+E), Space: O(V)
    """
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
    """
    SIMPLE-MODERATE: Iterative DFS using stack
    Time: O(V+E), Space: O(V)
    Better for deep graphs (no recursion limit)
    """
    visited = set()
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)

            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor, weight in reversed(graph.adj_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return path


def dfs_with_parent_tracking(graph, start):
    """
    MODERATE: DFS with parent tracking for path reconstruction
    Useful for finding paths, detecting cycles
    """
    visited = set()
    parent = {}
    stack = [(start, None)]  # (node, parent)
    path = []

    while stack:
        node, par = stack.pop()
        if node not in visited:
            visited.add(node)
            parent[node] = par
            path.append(node)

            for neighbor, weight in reversed(graph.adj_list[node]):
                if neighbor not in visited:
                    stack.append((neighbor, node))

    return path, parent


def dfs_detect_cycle_undirected(graph):
    """
    MODERATE: Detect cycle in undirected graph using DFS
    Returns True if cycle exists, False otherwise
    """
    visited = set()

    def dfs_util(node, parent):
        visited.add(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                if dfs_util(neighbor, node):
                    return True
            elif neighbor != parent:  # Back edge found
                return True
        return False

    # Check all components
    for vertex in graph.vertices:
        if vertex not in visited:
            if dfs_util(vertex, -1):
                return True
    return False


def dfs_detect_cycle_directed(graph):
    """
    COMPLEX: Detect cycle in directed graph using DFS
    Uses white-gray-black coloring technique
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)

    def dfs_util(node):
        color[node] = GRAY

        for neighbor, weight in graph.adj_list[node]:
            if color[neighbor] == GRAY:  # Back edge (cycle)
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
    """
    COMPLEX: Topological sorting using DFS
    Only works for DAG (Directed Acyclic Graph)
    """
    visited = set()
    stack = []

    def dfs_util(node):
        visited.add(node)

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                dfs_util(neighbor)

        stack.append(node)  # Add to stack after visiting all descendants

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs_util(vertex)

    return stack[::-1]  # Reverse to get topological order


# ==================== BFS IMPLEMENTATIONS ====================


def bfs_basic(graph, start):
    """
    SIMPLE: Basic BFS traversal
    Time: O(V+E), Space: O(V)
    """
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
    """
    MODERATE: Find shortest path using BFS (unweighted graph)
    Returns path and distance
    """
    if start == end:
        return [start], 0

    visited = set()
    queue = deque([(start, [start], 0)])  # (node, path, distance)
    visited.add(start)

    while queue:
        node, path, dist = queue.popleft()

        for neighbor, weight in graph.adj_list[node]:
            if neighbor == end:
                return path + [neighbor], dist + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], dist + 1))

    return None, -1  # No path found


def bfs_level_order(graph, start):
    """
    MODERATE: BFS with level tracking
    Returns nodes grouped by levels/distances from start
    """
    visited = set()
    queue = deque([(start, 0)])  # (node, level)
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


def bfs_multi_source(graph, sources):
    """
    COMPLEX: Multi-source BFS
    Useful for finding nearest source for each node
    """
    visited = set()
    queue = deque()
    distance = {}
    nearest_source = {}

    # Initialize with all sources
    for source in sources:
        queue.append((source, 0, source))
        visited.add(source)
        distance[source] = 0
        nearest_source[source] = source

    while queue:
        node, dist, source = queue.popleft()

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = dist + 1
                nearest_source[neighbor] = source
                queue.append((neighbor, dist + 1, source))

    return distance, nearest_source


def bfs_bipartite_check(graph):
    """
    COMPLEX: Check if graph is bipartite using BFS
    Returns True if bipartite, False otherwise
    Also returns the coloring if bipartite
    """
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

    # Check all components
    for vertex in graph.vertices:
        if vertex not in color:
            if not bfs_util(vertex):
                return False, {}

    return True, color


# ==================== UTILITY FUNCTIONS ====================


def find_all_paths_dfs(graph, start, end, path=None, all_paths=None):
    """
    MODERATE-COMPLEX: Find all paths between two nodes using DFS
    """
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    path = path + [start]

    if start == end:
        all_paths.append(path)
        return all_paths

    for neighbor, weight in graph.adj_list[start]:
        if neighbor not in path:  # Avoid cycles
            find_all_paths_dfs(graph, neighbor, end, path, all_paths)

    return all_paths


def connected_components_dfs(graph):
    """
    MODERATE: Find all connected components using DFS
    """
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

    g.add_edges_from_list(edges)

    print("=== GRAPH TRAVERSAL EXAMPLES ===")
    print(f"DFS Recursive from 1: {dfs_recursive(g, 1)}")
    print(f"DFS Iterative from 1: {dfs_iterative(g, 1)}")
    print(f"BFS from 1: {bfs_basic(g, 1)}")

    print(f"\n=== PATH FINDING ===")
    path, dist = bfs_shortest_path(g, 1, 6)
    print(f"Shortest path 1->6: {path}, Distance: {dist}")

    print(f"\n=== ADVANCED ALGORITHMS ===")
    print(f"Has cycle (undirected): {dfs_detect_cycle_undirected(g)}")
    print(f"Connected components: {connected_components_dfs(g)}")

    levels = bfs_level_order(g, 1)
    print(f"BFS levels from 1: {levels}")

    is_bipartite, coloring = bfs_bipartite_check(g)
    print(f"Is bipartite: {is_bipartite}")
