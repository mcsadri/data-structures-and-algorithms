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
            node1_obj.edges.append((node2_obj, weight))
            node2_obj.edges.append((node1_obj, weight))
        # else:
        #     raise ValueError("Doodah")

    def size(self):
        return len(self.graph)

    def get_neighbors(self, node):
        pass


class Vertex:
    def __init__(self, value):
        self.value = value
