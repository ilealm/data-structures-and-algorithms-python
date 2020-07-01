from dsa.challenges.graph.graph import Graph
# I need to execute
# PYTHONPATH='.' python dsa/challenges/get_edge/get_edge.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python get_edge.py


def get_edge(graph, itinerary):
    possible_travel = True
    travel_cost = 0
    city_objs = {}

    if len(itinerary) == 0 :
        raise Exception('The itineray is empty.')
        return is_possible

    city_objs = g.get_value_obj_dictionary()
#
    # print('departure_city: ', itinerary[0], ', Destination:', itinerary[1])

    #  get the city object of the departure city
    # departure_city_object = city_objs[itinerary[0]]

    # loop for all the rest of the cities in the intineraty
    for current_city in range(0,len(itinerary)):
        print("**** current city", itinerary[current_city])
        city_object_neighbors = g.get_neighbors(city_objs[itinerary[current_city]])

        # get the next city to visit and review if is un my neighbors list
        if not (current_city+1 == len(itinerary)):
            next_city = itinerary[current_city + 1]
            print('next_city', next_city)
            for i in range(0, len(city_object_neighbors)):
                if next_city == city_object_neighbors[i].vertex.value:
                    print ("you can travel")
                    travel_cost += city_object_neighbors[i].weight
                # print(city_object_neighbors[i].vertex.value)
                # print(city_object_neighbors[i].weight)
        # print(city_object_neighbors)
    print(travel_cost)

    # get city neighbors
    # departure_city_object_neighbors = g.get_neighbors(departure_city_object)
    # print(departure_city_object_neighbors[0].vertex.value)
    # print(departure_city_object_neighbors[0].weight)


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

