
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



    def get_vertices(self):
        return self._adjacency_list.keys()


    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])


    def __len__(self):
        return len(self._adjacency_list)



    # def breadth_first(self, vertex):
    #     visited_vertex = set()
    #     visited_vertex_names = []
    #     breadth = Queue()

    #     breadth.enqueue(vertex)
    #     visited_vertex_names.append(vertex.value)

    #     while not breadth.is_empty():
    #         front = breadth.dequeue()
    #         visited_vertex.add(front)

    #         #  get the edges of the current vector
    #         neighbors = self.get_neighbors(front)
    #         for edge in neighbors:
    #             # print(edge.vertex.value)
    #             if not edge.vertex in visited_vertex:
    #                 visited_vertex.add(edge.vertex)
    #                 visited_vertex_names.append(edge.vertex.value)
    #                 breadth.enqueue(edge)

    #         # working
    #         # print(edge)
    #         # print(edge.vertex.value)



    #     print(visited_vertex)
    #     print(visited_vertex_names)


    def breadth_first(self, vertex):
        visited_vertex = set()
        visited_vertex_names = []
        breadth = Queue()

        breadth.enqueue(vertex)
        visited_vertex_names.append(vertex.value)

        while not breadth.is_empty():
            front = breadth.dequeue()
            # visited_vertex_names.append("1")
            visited_vertex.add(front)

            #  get the edges of the current vector
            neighbors = self.get_neighbors(front)
            for edge in neighbors:
                # print(edge.vertex.value)
                if not edge.vertex in visited_vertex:
                    visited_vertex.add(edge.vertex)
                    visited_vertex_names.append(edge.vertex.value)
                    breadth.enqueue(edge.vertex)

            # working
            # print(edge)
            # print(edge.vertex.value)



        print(visited_vertex)
        print(visited_vertex_names)


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


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



if __name__ == "__main__":
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendale = g.add_vertex('Arendale')
    metroville = g.add_vertex('Metroville')
    monstropolis = g.add_vertex('Monstropolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')



    g.add_edge(pandora,arendale)

    g.add_edge(arendale, pandora)
    g.add_edge(arendale, metroville)
    g.add_edge(arendale, monstropolis)

    g.add_edge(metroville,arendale)
    g.add_edge(metroville,monstropolis)
    g.add_edge(metroville,naboo)
    g.add_edge(metroville,narnia)

    g.add_edge(monstropolis,arendale)
    g.add_edge(monstropolis,metroville)
    g.add_edge(monstropolis,naboo)

    g.add_edge(narnia,metroville)
    g.add_edge(narnia,naboo)

    g.add_edge(naboo,monstropolis)
    g.add_edge(naboo,metroville)
    g.add_edge(naboo,narnia)

    # print(g._adjacency_list)
    # print(g.get_neighbors('Pandora'))
    g.breadth_first(pandora)
    # g.breadth_first(arendale)
    # g.breadth_first(monstropolis)

    print("\nall good")
