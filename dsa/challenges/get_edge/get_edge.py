from dsa.challenges.graph.graph import Graph
# I need to execute
# PYTHONPATH='.' python dsa/challenges/get_edge/get_edge.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python get_edge.py


def get_edge(graph, itinerary):
    is_possible = False
    travel_cost = 0
    city_objs = {}

    if len(itinerary) == 0 :
        raise Exception('The itineray is empty.')
        return is_possible

    departure_city = itinerary[0]
    destination_city = itinerary[1]
    print('departure_city: ', departure_city, ', Destination:', destination_city)

    # give the list of cities, with their obj values

    # gives the list of objct cities
    # city_obj = g.__str__()
    # print(city_obj)
    # for obj in city_obj:
    #     city_objs[obj.value] = obj
    city_objs = g.get_value_obj_dictionary()

    print(city_objs)

    # get city edges
    # print(g._adjacency_list[departure_city])
    # loop throug each of the rest of the cities
    # check if departure_city has an edge with destination_city
    # if so, add the sum of the weight
    # else retun false and cost




if __name__ == "__main__":
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

    # get_edge(['Metroville', 'Pandora'])
    get_edge(g, ['Arendale', 'Monstropolis', 'Naboo'])

    print('All good')

