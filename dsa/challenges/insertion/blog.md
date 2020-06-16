# Insertion

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

- Simple implementation: Jon Bentley shows a three-line C version, and a five-line optimized version[1]
- Efficient for (quite) small data sets, much like other quadratic sorting algorithms
- More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort
- Adaptive, i.e., efficient for data sets that are already substantially sorted: the time complexity is O(kn) when each element in the input is no more than k places away from its sorted position
- Stable; i.e., does not change the relative order of elements with equal keys
- In-place; i.e., only requires a constant amount O(1) of additional memory space
- Online; i.e., can sort a list as it receives it

[Source](https://en.wikipedia.org/wiki/Insertion_sort)


## Implementation

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

### This can be described as follows...

![My solution](/assets/insertion_psudo.jpg)

### And this is an example of the execution
![Example](/assets/insertion_example.jpg)

## This is the code in Python

```
def insertion(list_to_review):
    for index in range(1, len(list_to_review)):
        position = index
        temp_value = list_to_review[index]

        print( f'Value of {index}, position {position} the array is {list_to_review}')

        while position > 0 and list_to_review[position - 1] > temp_value:
            list_to_review[position] = list_to_review[position-1]
            position = position -1

        list_to_review[position] = temp_value

    return list_to_review
```
### An example of this code is:

```
test1 =[8,4,23,42,16,15]
print(insertion (test1))


Value of 1, position 1 the array is [8, 4, 23, 42, 16, 15]
Value of 2, position 2 the array is [4, 8, 23, 42, 16, 15]
Value of 3, position 3 the array is [4, 8, 23, 42, 16, 15]
Value of 4, position 4 the array is [4, 8, 23, 42, 16, 15]
Value of 5, position 5 the array is [4, 8, 16, 23, 42, 15]
[4, 8, 15, 16, 23, 42]
```
