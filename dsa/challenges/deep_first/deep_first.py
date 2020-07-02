from dsa.challenges.graph.graph import Graph
# I need to execute
# PYTHONPATH='.' python dsa/challenges/deep_first/deep_first.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python deep_first.py



def deep_first(graph):
    visited_vertex = set()
    DFS = []
    stack = []
    all_visited_children = False

    # print(graph._adjacency_list)
    # print("\n\n")
    # print(next(iter(graph._adjacency_list)))
    # print(next(iter(graph._adjacency_list)).value)

    # main_dict = graph.get_value_obj_dictionary()
    # print(main_dict)

    def traverse(current_vertex):
        if not current_vertex : return

        # if current_vertex is an Edge, I need to get the reference of the Vortex OBJ, and
        # reassign it as that new reference as the current vertex
        if "Edge" in str(type(current_vertex)) :
            current_vertex = current_vertex.vertex
            # print("\nis a edge")
            # current_vertex_value = current_vertex.vertex
            # print(current_vertex.vertex.value)
            # print(current_vertex.vertex)

        # <class 'dsa.challenges.graph.graph.Vertex'>
        # <class 'dsa.challenges.graph.graph.Edge'>


        # print("type", type(current_vertex))
        # print("traverse", current_vertex)

        visited_vertex.add(current_vertex)
        DFS.append(current_vertex)
        edges = graph.get_neighbors(current_vertex)

        # print(edges)
        for i in range(0,len(edges)):
            if not edges[i] in visited_vertex:
                traverse(edges[i])

    # 1 push the root into the stack
    root = next(iter(graph._adjacency_list))
    traverse(root)
    # stack.append(root)
    # send the 1srt vertex in the graph to traverse
    # traverse(root)
    # 2 starr a loop while the stack is not empty
    # while len(stack) > 0:
    # 3 peek at the top of the stack
    # top = stack[-1]
    # 4.0 get top's edges
    # edges = graph.get_neighbors(top)
    # 4.4 if the top has invisited children, if so, mask top as visited
    # all_visited_children = True
    # for i in range(0,len(edges)):
    #     # print(edges[i])
    #     if not edges[i] in visited_vertex :
    #         # 4.5 add any uvisited children in the stack
    #         print("addig to stack ", edges[i].vertex.value)
    #         stack.append(edges[i])
    #         all_visited_children = False
    # # 4.6 if so, mask top as visited
    # if not all_visited_children :
    #     visited_vertex.add(top)
    # print (top.value)
    # print (edges)
    # print (edges[0].vertex.value)
    # print (edges[1].vertex.value)

    print("\n\nElements in stack: ", len(stack))
    for ele in stack:
        print(ele)

if __name__ == "__main__":
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

    graph.add_edge(b,a)
    graph.add_edge(b,d)
    graph.add_edge(b,c)

    graph.add_edge(c,b)
    graph.add_edge(c,g)

    graph.add_edge(d,a)
    graph.add_edge(d,b)
    graph.add_edge(d,f)
    graph.add_edge(d,h)
    graph.add_edge(d,e)

    graph.add_edge(e,d)

    graph.add_edge(f,d)
    graph.add_edge(f,h)

    graph.add_edge(g,c)

    graph.add_edge(h,f)
    graph.add_edge(h,d)


# A, B, C, G, D, E, H, F
    deep_first(graph)

print ("\n ALL GOOD")
