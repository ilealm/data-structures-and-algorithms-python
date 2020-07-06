def merge_sort(list_to_review):
    if len(list_to_review) >1:
        mid = len(list_to_review) // 2
        left = list_to_review[:mid]
        right = list_to_review[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            print(left, right)
            if left[i] < right[j]:
                list_to_review[k] = left[i]
                i+= 1
            else:
                list_to_review[k] = right[j]
                j+= 1
            k+= 1

        # Checking if any element was left
        while i < len(left):
            list_to_review[k] = left[i]
            i+= 1
            k+= 1

        while j < len(right):
            list_to_review[k] = right[j]
            j+= 1
            k+= 1

    return list_to_review


def merge_sort_craking_code(array, helper, left_start, right_end ):
    if left_start>= right_end:
        return

    middle = (left_start + right_end) // 2

    merge_sort_craking_code(array, helper, left_start, middle)
    merge_sort_craking_code(array, helper, middle +1 , right_end)
    merge_helves(array, helper, left_start, right_end)

    # print(array)
    # print(helper)

def merge_helves(array, helper, left_start, right_end):
    left_end = (left_start + right_end) // 2
    right_start = left_end + 1
    size = right_end - left_start + 1

    left_index = left_start
    right_index = right_start
    helper_index = left_start

    while left_index <= left_end and right_index <= right_end:
        if array[left_index] <= array[right_index]:
            helper[helper_index] = array[left_index]
            left_index += 1
        else:
            helper[helper_index] = array[right_index]
            right_index += 1
        helper_index += 1

    #  get the rest the unbalanced size of elements (eg one halve is 2 and other 1)
    while left_index <= left_end:
        helper[helper_index] = array[left_index]
        left_index += 1
        helper_index += 1

    while right_index <= right_end:
        helper[helper_index] = array[right_index]
        right_index += 1
        helper_index += 1

    for i in range(left_start, left_start + size):
        array[i] = helper[i]





if __name__ == "__main__":
    array = [10,5,13,21,3,7]
    print(array)
    helper = [None] * len(array)
    merge_sort_craking_code(array, helper, 0, len(array) -1)
    print(array)
# [None] * self.size
