# Merge Sort

Merge sort (also commonly spelled mergesort) is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output. Merge sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.A detailed description and analysis of bottom-up mergesort appeared in a report by Goldstine and von Neumann as early as 1948.

[Source](https://en.wikipedia.org/wiki/Merge_sort)

## The idea is divide and divide, then merge again
![My solution](/assets/merge_sort.jpg)

## This is the psudo code to achive Merge Sort

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## And this is the code in Python

```
def merge_sort(list_to_review):
    if len(list_to_review) >1:
        mid = len(list_to_review) // 2
        left = list_to_review[:mid]
        right = list_to_review[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
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
    ```
