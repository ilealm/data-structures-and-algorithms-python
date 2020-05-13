# Challenge 01: array_reverse
# Function that receives an array and return a new array with all the same elements in reverse order.
def reverseArray(array):
    returnArray = []
    # print(len(array))
    for i in range(0,len(array)):
        returnArray.insert(0, array[i])

    return returnArray


# if __name__ == "__main__":
        # this works:
        # original_Array=[1,2,3,4,5]
        # print(original_Array)
        # print(reverseArray(original_Array))
        # print(reverseArray(input()))

        # original_Array = list(input().split(','))

        # original_Array = input()
        # input_array = input()

        # original_Array = list(input_array)
        # print(original_Array)

        # input_array=[int(elem) for elem in input().split()] 

        # print(original_Array[0])
        # print(original_Array[len(original_Array)]

        # print(reverseArray(original_Array))

