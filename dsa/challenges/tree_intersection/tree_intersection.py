# from dsa.challenges.linked_list.linked_list import LinkedList
# I need to execute
# PYTHONPATH='.' python dsa/challenges/tree_intersection/tree_intersection.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python tree_intersection.py

from dsa.challenges.tree.tree import BinarySearchTree


#for every node, send the value o a function which if exist in the
def tree_intersection(tree_one, tree_two):
    arr_return = []
    values_dic = {}

    if not tree_one or not tree_two : return arr_return

    # obtain the nodes of each tree in a list
    list_tree_one = tree_one.BreadthFirst(tree_one)
    list_tree_two = tree_two.BreadthFirst(tree_two)

    # loop list one, and if the element not exist in the dictionary, add there with value=0
    for i in range(0, len(list_tree_one)):
        if not list_tree_one[i] in values_dic:
            values_dic[list_tree_one[i]] = 0

    # loop each element of list two, if is in the dictionary, add value1
    for i in range(0, len(list_tree_two)):
        if  list_tree_two[i] in values_dic:
            values_dic[list_tree_two[i]] = 1

    # print(values_dic)

    # return los keys where value =1
    for key, value in values_dic.items():
        if value == 1:
            arr_return.append(key)

    return arr_return

