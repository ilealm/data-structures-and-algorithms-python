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

    print(arr_return)
    #duplicates in the same tree?


if __name__ == "__main__":
    tree_one = BinarySearchTree()
    tree_one.add(150)
    tree_one.add(100)
    tree_one.add(250)
    tree_one.add(75)
    tree_one.add(160)
    tree_one.add(200)
    tree_one.add(350)
    tree_one.add(125)
    tree_one.add(175)
    tree_one.add(300)
    tree_one.add(500)

    tree_two = BinarySearchTree()
    tree_two.add(42)
    tree_two.add(100)
    tree_two.add(600)
    tree_two.add(15)
    tree_two.add(160)
    tree_two.add(200)
    tree_two.add(350)
    tree_two.add(125)
    tree_two.add(175)
    tree_two.add(4)
    tree_two.add(500)



    print(tree_one.BreadthFirst(tree_one))
    print(tree_one.BreadthFirst(tree_two))

    tree_intersection(tree_one,tree_two)

    print('here')
