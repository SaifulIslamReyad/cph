class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight  # For undirected graph

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0  # For undirected graph

    def visualize(self):
        for row in self.adj_matrix:
            print(row)
    def display(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] != 0:
                    print(i, "-->", j, ":", self.adj_matrix[i][j])

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)


    g.display()