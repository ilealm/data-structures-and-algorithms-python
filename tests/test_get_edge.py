import pytest
from dsa.challenges.graph.graph import Graph
from dsa.challenges.get_edge.get_edge import get_edge


def test_one_city(dummy_city_graph):
    expected = [False,0]

    actual = get_edge(dummy_city_graph, ['Metroville'])

    assert actual == expected, 'Error obtaining the route price for one city.'


def test_all_cities(dummy_city_graph):
    expected = [True, 677]

    actual = get_edge(dummy_city_graph, ['Pandora', 'Arendale','Metroville','Monstropolis','Naboo','Narnia'])

    assert actual == expected, 'Error obtaining the route price for visiting all the cities.'


def test_metroville_pandora(dummy_city_graph):
    expected = [True, 82]

    actual = get_edge(dummy_city_graph, ['Metroville', 'Pandora'])

    assert actual == expected, 'Error obtaining the route price for two cities.'


def test_metroville_pandora_naboo(dummy_city_graph):
    expected = [True, 115]

    actual = get_edge(dummy_city_graph, ['Arendale', 'Monstropolis', 'Naboo'])

    assert actual == expected, 'Error obtaining the route price for three cities.'


def test_naboo_pandora(dummy_city_graph):
    expected = [False, 0]

    actual = get_edge(dummy_city_graph, ['Naboo', 'Pandora'])

    assert actual == expected, 'Error obtaining the route price for two cities.'


def test_narnia_arendale_naboo(dummy_city_graph):
    expected = [False, 0]

    actual = get_edge(dummy_city_graph, ['Narnia', 'Arendale','Naboo'])

    assert actual == expected, 'Error obtaining the route price for three cities.'




@pytest.fixture
def dummy_city_graph():
    g = Graph()
    pandora = g.add_vertex('Pandora')
    arendale = g.add_vertex('Arendale')
    metroville = g.add_vertex('Metroville')
    monstropolis = g.add_vertex('Monstropolis')
    narnia = g.add_vertex('Narnia')
    naboo = g.add_vertex('Naboo')

    g.add_edge(pandora,arendale,150)
    g.add_edge(pandora,metroville,82)

    g.add_edge(arendale, pandora,150)
    g.add_edge(arendale, metroville,99)
    g.add_edge(arendale, monstropolis,42)

    g.add_edge(metroville,pandora, 82)
    g.add_edge(metroville,arendale, 99)
    g.add_edge(metroville,monstropolis,105)
    g.add_edge(metroville,naboo, 26)
    g.add_edge(metroville,narnia,37)

    g.add_edge(monstropolis,arendale,42)
    g.add_edge(monstropolis,metroville,105)
    g.add_edge(monstropolis,naboo,73)

    g.add_edge(narnia,metroville,37)
    g.add_edge(narnia,naboo,250)

    g.add_edge(naboo,monstropolis,73)
    g.add_edge(naboo,metroville,26)
    g.add_edge(naboo,narnia,250)

    return g

 