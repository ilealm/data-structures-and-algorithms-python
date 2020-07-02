from dsa.challenges.graph.graph import Graph
# I need to execute
# PYTHONPATH='.' python dsa/challenges/deep_first/deep_first.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python deep_first.py


def deep_first(graph):
    visited_vertex = set()
    DFS = []
    # all_visited_children = False
    if not graph : return

    def traverse(current_vertex):
        if not current_vertex : return
        # if current_vertex is an Edge, I need to get the reference of the Vortex OBJ, and
        # reassign it as that new reference as the current vertex
        # if "Edge" in str(type(current_vertex)) :
        #     current_vertex = current_vertex.vertex

        visited_vertex.add(current_vertex)
        DFS.append(current_vertex.value)
        edges = graph.get_neighbors(current_vertex)

        for i in range(0,len(edges)):
            if not edges[i].vertex in visited_vertex:
                traverse(edges[i].vertex)





    # This gets the first element of the _adjacency_list
    root = next(iter(graph._adjacency_list))
    traverse(root)

    return DFS
