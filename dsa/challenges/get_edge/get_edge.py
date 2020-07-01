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

    city_objs = graph.get_value_obj_dictionary()

    # loop for all the rest of the cities in the intineraty
    for current_city in range(0,len(itinerary)):
        city_object_neighbors = graph.get_neighbors(city_objs[itinerary[current_city]])
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
