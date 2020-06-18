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
    i = ( start_index-1 )    # index of smaller element, that I already visited
    pivot = arr[end_index]
    for j in range(start_index , end_index):
            # swap values
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end_index] = arr[end_index],arr[i+1]
    # print(i+1)
    return ( i+1 )
