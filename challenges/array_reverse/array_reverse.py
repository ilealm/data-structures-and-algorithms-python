# Challenge 01: array_reverse
# Function that receives an array and return a new array with all the same elements in reverse order.
def reverseArray(array):
    returnArray = []
    print(len(array))
    for i in range(0,len(array)):
        returnArray.insert(0, array[i])

    return(returnArray)


# if __name__ == "__main__":
#         print(reverseArray(input()))
