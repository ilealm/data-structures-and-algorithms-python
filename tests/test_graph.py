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


def test_breadth_first_arendale(dummy_graph_six_nodes):
    g = dummy_graph_six_nodes[0]
    arendale = dummy_graph_six_nodes[1]

    expected = ['Arendale', 'Pandora', 'Metroville', 'Monstropolis', 'Naboo', 'Narnia']

    actual = g.breadth_first(arendale)

    assert actual == expected, 'Error generating the graph of Arendale.'


def test_breadth_first_monstropolis(dummy_graph_six_nodes):
    g = dummy_graph_six_nodes[0]
    monstropolis = dummy_graph_six_nodes[2]

    expected = ['Monstropolis', 'Arendale', 'Metroville', 'Naboo', 'Pandora', 'Narnia']

    actual = g.breadth_first(monstropolis)

    assert actual == expected, 'Error generating the graph of Monstropolis.'


def test_breadth_first_naboo(dummy_graph_six_nodes):
    g = dummy_graph_six_nodes[0]
    naboo = dummy_graph_six_nodes[3]

    expected = ['Naboo', 'Monstropolis', 'Metroville', 'Narnia', 'Arendale', 'Pandora']

    actual = g.breadth_first(naboo)

    assert actual == expected, 'Error generating the graph of Naboo.'



def test_breadth_first_no_edges():
    g = Graph()
    pandora = g.add_vertex('Pandora')

    expected = ['Pandora']

    actual = g.breadth_first(pandora)

    assert actual == expected, 'Error generating the graph of a vertex without edges.'



@pytest.fixture
def dummy_graph_six_nodes():
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

    return [g, arendale, monstropolis, naboo]
