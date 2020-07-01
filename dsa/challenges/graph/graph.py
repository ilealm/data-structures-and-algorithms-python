
from collections import deque


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def __str__(self):
        return self._adjacency_list.keys()

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        # add the new vertex to the graph dictionary (vertex is the key),
        # and asing an enpty list as value of the key
        self._adjacency_list[new_vertex] = []

        return new_vertex


    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self._adjacency_list:
            raise KeyError('The vertex from must be in the graph')

        if to_vertex not in self._adjacency_list:
            raise KeyError('The vertex to must be in the graph')

        new_edge = Edge(to_vertex, weight)

        self._adjacency_list[from_vertex].append(new_edge) # list of neighbors


    def get_value_obj_dictionary(self):
        # retuns a dictionaty with obj.value = obj ?eg Arendale : <obj>
        value_obj_objs = {}
        objs = self.__str__()
        for obj in objs:
            # store city = <city object>
            value_obj_objs[obj.value] = obj

        return value_obj_objs


    def get_vertices(self):
        return self._adjacency_list.keys()


    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])


    def __len__(self):
        return len(self._adjacency_list)



    def breadth_first(self, vertex):
        visited_vertex = set()
        visited_vertex_names = []
        breadth = Queue()

        breadth.enqueue(vertex)
        visited_vertex_names.append(vertex.value)

        while not breadth.is_empty():
            front = breadth.dequeue()
            visited_vertex.add(front)

            #  get the edges of the current vector
            neighbors = self.get_neighbors(front)
            for edge in neighbors:
                if not edge.vertex in visited_vertex:
                    visited_vertex.add(edge.vertex)
                    visited_vertex_names.append(edge.vertex.value)
                    breadth.enqueue(edge.vertex)

        return visited_vertex_names


class Vertex:
    def __init__(self, value):
        self.value = value

    # def __str__(self):
    #     return self.value


class Edge:
    def __init__(self, to_vertex, weight=0):
        self.vertex = to_vertex
        self.weight = weight


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

