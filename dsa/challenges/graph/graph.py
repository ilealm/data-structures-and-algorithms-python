
class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self._adjacency_list[new_vertex] = []

        return new_vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self._adjacency_list:
            raise KeyError('The vertex from must be in the graph')

        if to_vertex not in self._adjacency_list:
            raise KeyError('The vertex to must be in the graph')

        new_edge = Edge(to_vertex, weight)

        self._adjacency_list[from_vertex].append(new_edge) # list of neighbors



    def get_vertices(self):
        return self._adjacency_list.keys()


    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])

    def __len__(self):
        return len(self._adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, to_vertex, weight=0):
        self.vertex = to_vertex
        self.weight = weight
