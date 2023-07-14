class Graph:
    """
    Put docstring here
    graph solution with assistance from ChatGPT
    """

    def __init__(self):
        self.graph = {}

    def add_node(self, value):
        if value not in self.graph:
            self.graph[value] = Vertex(value)
        return self.graph[value]

    def add_edge(self, node1, node2, weight=None):
        if node1 in self.graph and node2 in self.graph:
            node1_obj = self.graph[node1]
            node2_obj = self.graph[node2]
            node1_obj.edges.append(Edge(node2_obj, weight))

    def size(self):
        return len(self.graph)

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
