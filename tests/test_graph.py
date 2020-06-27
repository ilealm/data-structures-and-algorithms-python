import pytest
from dsa.challenges.graph.graph import Graph, Vertex, Edge

def test_add_vertex():
    g = Graph()
    expected = 'one'

    vertex = g.add_vertex('one')
    actual = vertex.value

    assert actual == expected, 'Error adding one vertex to the graph'

def test_add_edge():
    g = Graph()
    one = g.add_vertex('one')
    two = g.add_vertex('two')

    g.add_edge(one, two)

    assert True, 'Will be fully exercised in get_neighbors tests'


def test_add_edge_interloper():
    g = Graph()
    insider = g.add_vertex('insider')

    outsider = Vertex('outsider')

    with pytest.raises(KeyError):
        g.add_edge(outsider, insider)


def test_get_vertices():
    g = Graph()
    one = g.add_vertex('one')

    two = g.add_vertex('two')

    actual = g.get_vertices()

    assert len(actual) == 2


def test_get_neighbors():
    g = Graph()
    one = g.add_vertex('one')
    two = g.add_vertex('two')

    g.add_edge(one, two)

    neighbors = g.get_neighbors(one)

    assert len(neighbors) == 1

    neighbor = neighbors[0]

    assert neighbor.vertex.value == 'two'

    assert neighbor.weight == 0


def test_get_size():

    g = Graph()

    one = g.add_vertex('one')

    two = g.add_vertex('two')

    assert len(g) == 2
