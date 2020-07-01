from dsa.challenges.graph.graph import Graph
# I need to execute
# PYTHONPATH='.' python dsa/challenges/get_edge/get_edge.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python get_edge.py


def get_edge(graph, itinerary):
    travel_cost = 0
    city_objs = {}

    if len(itinerary) == 0 :
        raise Exception('The itineray is empty.')
        return is_possible

    if len(itinerary) == 1 :  return [False,0]

    city_objs = g.get_value_obj_dictionary()

    # loop for all the rest of the cities in the intineraty
    for current_city in range(0,len(itinerary)):
        city_object_neighbors = g.get_neighbors(city_objs[itinerary[current_city]])
        # get the next city to visit and review if is un my neighbors list
        if not (current_city+1 == len(itinerary)):
            next_city = itinerary[current_city + 1]
            can_move_next_city = False
            for i in range(0, len(city_object_neighbors)):
                if next_city == city_object_neighbors[i].vertex.value:
                    can_move_next_city = True
                    travel_cost += city_object_neighbors[i].weight


        if not can_move_next_city :  return [False,0]

    return [True, travel_cost]


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

    print(get_edge(g, ['Metroville', 'Pandora']))  # [True, 82]
    print(get_edge(g, ['Arendale', 'Monstropolis', 'Naboo']))  # [True, 115]
    print(get_edge(g, ['Naboo', 'Pandora']))  # [False, 0]
    print(get_edge(g, ['Narnia', 'Arendale','Naboo']))  # [False, 0]
    print(get_edge(g, ['Metroville']))  # [False, 0]
    print(get_edge(g, ['Pandora', 'Arendale','Metroville','Monstropolis','Naboo','Narnia']))  # [False, 0]



