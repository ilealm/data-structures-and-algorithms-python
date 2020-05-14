import math


# cases: check if the seached number is in the middle
# if key < array[middle]:. send array to the left, else to the right
# if len(array) == 1, check if = key, if not, return -1
# if is only one value: done
# is not working
def binary_search_recursive(list_to_seach, key,search_begin, search_end):
    print("array to review", list_to_seach[search_begin:search_end])
    print("len del array", len(list_to_seach[search_begin:search_end]))
    # search_begin = 7
    # search_end = 10
    print("len del array de 5 a  10", len(list_to_seach[search_begin:search_end]))
    # print("array is odd", not(len(list_to_seach[search_begin:search_end]) % 2) )

    if len(list_to_seach[search_begin:search_end]) % 2 :
        print("is odd")
        middle = (math.ceil(len(list_to_seach[search_begin:search_end]) / 2)) -1
    else:
        print("is even")
        middle = len(list_to_seach[search_begin:search_end]) // 2


    print('search_begin:', search_begin, 'search_end',search_end,'middle:', middle)


    if len(list_to_seach) == 1:
        if list_to_seach[0] == key :
            print("Value founded")
            return search_begin
        else:
            print('The value is not in the array')
            return -1


    if list_to_seach[middle] == key:
        print('the value is in the middle')
        return middle
    else:
        if list_to_seach[middle] < key: # take the values to the right
            print("we need to split the array to the right")
            print(list_to_seach[search_begin + middle:], "with the values:", search_begin + middle, len(list_to_seach))
            binary_search(list_to_seach, key, search_begin + middle, len(list_to_seach))
        else: # take the values to the left
            print("we need to split the array to the left")
            print(list_to_seach[:arch_begin - middle], "with the values:", 0, middle)
            binary_search(list_to_seach, key, 0, search_begin - middle)
    #     print(list_to_seach[middle:])




def binary_search(list_to_seach, key):
    if len(list_to_seach) == 1:
        if list_to_seach[0] == key :
            print("Value founded")
            return 0
        else:
            return -1

    middle = (math.ceil(len(list_to_seach) / 2))

    # print('middle', middle)

    if list_to_seach[middle] == key:
        # print('the value is in the middle')
        return middle
    else:
        # we need to split list to seach on it
        postion = -1
        search_begin = 0
        search_end =len(list_to_seach) -1

        index_found = False
        while (search_begin <= search_end and not index_found):
            middle = (search_begin + search_end) // 2
            if list_to_seach[middle] == key:
                index_found = True
                return middle
            else:
                if key < list_to_seach[middle]:
                    # print("we need to split the array to the left")
                    search_end = middle - 1
                else:
                    # print("we need to split the array to the right")
                    search_begin = middle + 1

        if index_found == False : return -1





# if __name__ == "__main__":
    # array = [10,20,30,40,50,60,70,80,90,100] #middle: 5
    # array = [10,20,30,40, 50,60,70,80,90] #middle: 5
    # array = [10,20,30,40] #middle: 2
    # array = [10,20,30] #middle: 2
    # array = [10,20] #middle: 1
    # array = [10] #middle: 1
    # key = 10
    # print("original array:", array)
    # print('returned index:',binary_search(array,key))
