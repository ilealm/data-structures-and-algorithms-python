# from dsa.challenges.linked_list.linked_list import LinkedList
# I need to execute
# PYTHONPATH='.' python dsa/challenges/left_join/left_join.py
# to I can execute the code
# OR in this directory: PYTHONPATH="../../../" python left_join.py

from dsa.challenges.hashtable.hashtable import Hashtable


def left_join(left_hashtable, right_hastable):
    list_return = []

    # get the values of each hasttable. They will be inside a dictionary
    # # The order is based on how was the key saved on the hashtable
    dict_left = (left_hashtable.return_hashtable_values())
    dict_right = (right_hastable.return_hashtable_values())

    # Taking the left table as a base, search if the current key exists in dict_right
    # if so, append the value of the dict_right.key. Else, append "none"
    for key in dict_left:
        left_join = ""
        if key in dict_right :
            left_join = key + ', ' + dict_left[key] + ', ' + dict_right[key]
        else:
            left_join = key + ', ' + dict_left[key] + ', ' + 'None'
        list_return.append(left_join)

    return list_return

