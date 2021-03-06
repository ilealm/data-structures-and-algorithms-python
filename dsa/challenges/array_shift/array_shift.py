import math

# Challenge 02: array_shift. Going to use approach 3
# Function that receives an array and a value, and return a new array with all the same elements and the value inserted in the middle of the array.
def insert_shift_array(array, value):
    """Function that receives an array and a value, and return a new array with all the same elements and the value inserted in the middle of the array."""
    middle = (math.ceil(len(array) / 2)) - 1
    return_array = []
    for i in range(len(array)):
        return_array.append(array[i])
        if i == middle : return_array.append(value)

    return return_array

# # Challenge 02: streach goal.
def delete_shift_array(array):
    """Function that receives an array and return a new array with all the same elements except the one in the middle of the array."""
    if len(array) % 2 :
        middle = len(array) // 2
    else:
        middle = (math.ceil(len(array) / 2)) #- 1
    return_array = []
    for i in range(len(array)):
        if i != middle : return_array.append(array[i])

    return return_array



