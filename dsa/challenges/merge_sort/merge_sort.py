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


