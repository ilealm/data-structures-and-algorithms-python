'''
code references:
https://www.youtube.com/watch?v=WaNLJf8xzC4
https://visualgo.net/en/sorting
https://www.geeksforgeeks.org/python-program-for-quick_sort/
'''


def quick_sort(arr, start_index, end_index):
    if start_index < end_index:
        pivot = partition(arr,start_index, end_index)
        print('pivot', pivot, start_index, end_index)

        quick_sort(arr, start_index, pivot-1) # taking all from the pivot to the left
        quick_sort(arr, pivot+1, end_index) # taking all from the pivot to the right

    return arr


# returns the next position of the lowest founded value
def partition(arr,start_index, end_index):
    pointer_left = ( start_index-1 )    # index of smaller element, that I already visited
    pivot = arr[end_index]
    for pointer_right in range(start_index , end_index):
            # swap values
        if arr[pointer_right] <= pivot:
            pointer_left = pointer_left + 1
            arr[pointer_left],arr[pointer_right] = arr[pointer_right],arr[pointer_left]

    arr[pointer_left+1],arr[end_index] = arr[end_index],arr[pointer_left+1]
    # print(i+1)
    return ( pointer_left + 1 )


def quick_sort_craking(arr, left, right):
    index = partition_craking(arr, left, right)

    #  sort left half
    if left < index-1:
        quick_sort_craking(arr, left, index-1)
    #  sort right half
    if index < right:
        quick_sort_craking(arr, index, right)


def partition_craking(arr, left, right):
    pivot = arr[(left + right) // 2] # pivot
    while left <= right:
        # find the element on left that should be on the right (greater than pivot)
        # aka find the possition of the first element that is GRATER than the pivot, from the LEFT
        while (arr[left] < pivot):
            left += 1

        # find the element on the right that should be on the left (lower than pivot)
        # aka find the possition of the first element that is LESS than the pivot, from the RIGHT
        while (arr[right] > pivot):
            right -= 1

        #swap elements
        arr[left],arr[right] = arr[right],arr[left]
        # Move right indices
        left += 1
        right -= 1

    # how do I know I need to return left?.
    # left is the middle always
    return left



if __name__ == "__main__":
    # print(quick_sort([10, 5, -3, 12, 1, 30, 7],0, 6) )
    array =[10, 15, -3, 12, 1, 30, 7]
    quick_sort_craking(array,0, len(array)-1)
    print(array)
