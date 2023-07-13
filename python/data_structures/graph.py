class Graph:
    """
    Put docstring here
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append([node2, weight])
        self.graph[node2].append([node1, weight])


class Vertex:
    pass
