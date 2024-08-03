class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def insert_node(self, u, v):
        if u >= 0 and u < self.V and v >= 0 and v < self.V:
            self.adj[u].append(v)
        else:
            return "Invalid node number"

    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i} : {self.adj[i]}")


# Testing the function
g = Graph(5)
g.insert_node(0, 1)
g.insert_node(0, 4)
g.insert_node(1, 2)
g.insert_node(1, 3)
g.insert_node(1, 4)
g.insert_node(2, 3)
g.insert_node(3, 4)

g.print_graph()
