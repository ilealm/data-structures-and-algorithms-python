import pytest
from dsa.challenges.graph.graph import Graph, Vertex, Edge
from dsa.challenges.deep_first.deep_first import deep_first


def test_one_letters(dummy_letters_graph):
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']

    actual = deep_first(dummy_letters_graph)

    assert actual == expected, 'Error obtaining the deep first of one graph.'


def test_one_city(dummy_city_graph):
    expected = ['Pandora', 'Metroville', 'Narnia', 'Naboo', 'Monstropolis', 'Arendale']

    actual = deep_first(dummy_city_graph)

    assert actual == expected, 'Error obtaining the deep first of one graph with cities.'


def test_real_cities(dummy_real_graph):
    expected = ['Seattle', 'Mexico', 'Londres', 'Miami', 'LA']

    actual = deep_first(dummy_real_graph)

    assert actual == expected, 'Error obtaining the deep first of one graph with real cities.'



@pytest.fixture
def dummy_letters_graph():
    graph = Graph()
    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")
    f = graph.add_vertex("F")
    g = graph.add_vertex("G")
    h = graph.add_vertex("H")

    graph.add_edge(a,b)
    graph.add_edge(a,d)

    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(b,a)

    graph.add_edge(c,b)
    graph.add_edge(c,g)

    graph.add_edge(d,e)
    graph.add_edge(d,a)
    graph.add_edge(d,b)
    graph.add_edge(d,h)
    graph.add_edge(d,f)

    graph.add_edge(e,d)

    graph.add_edge(f,d)
    graph.add_edge(f,h)

    graph.add_edge(g,c)

    graph.add_edge(h,f)
    graph.add_edge(h,d)

    return graph

@pytest.fixture
def dummy_city_graph():
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendale = g.add_vertex('Arendale')
    metroville = g.add_vertex('Metroville')
    monstropolis = g.add_vertex('Monstropolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')

    g.add_edge(pandora,metroville,82)
    g.add_edge(pandora,arendale,150)

    g.add_edge(arendale, pandora,150)
    g.add_edge(arendale, metroville,99)
    g.add_edge(arendale, monstropolis,42)

    g.add_edge(metroville,narnia,37)
    g.add_edge(metroville,pandora, 82)
    g.add_edge(metroville,arendale, 99)
    g.add_edge(metroville,monstropolis,105)
    g.add_edge(metroville,naboo, 26)

    g.add_edge(monstropolis,arendale,42)
    g.add_edge(monstropolis,metroville,105)
    g.add_edge(monstropolis,naboo,73)

    g.add_edge(narnia,metroville,37)
    g.add_edge(narnia,naboo,250)

    g.add_edge(naboo,monstropolis,73)
    g.add_edge(naboo,metroville,26)
    g.add_edge(naboo,narnia,250)

    return g


@pytest.fixture
def dummy_real_graph():
    g = Graph()
    seattle = g.add_vertex('Seattle')
    la = g.add_vertex('LA')
    miami = g.add_vertex('Miami')
    denver = g.add_vertex('Denver')
    mexico = g.add_vertex('Mexico')
    londres = g.add_vertex('Londres')

    g.add_edge(seattle,mexico,82)
    g.add_edge(seattle,la,150)
    g.add_edge(seattle, londres,99)


    g.add_edge(la, mexico,150)
    g.add_edge(la,seattle,105)
    g.add_edge(la,londres,73)


    g.add_edge(londres, miami,42)
    g.add_edge(londres,la,105)
    g.add_edge(londres,seattle,250)

    g.add_edge(mexico,seattle,37)
    g.add_edge(mexico,londres,42)

    g.add_edge(miami,la, 82)
    g.add_edge(miami,mexico, 82)

    return g
