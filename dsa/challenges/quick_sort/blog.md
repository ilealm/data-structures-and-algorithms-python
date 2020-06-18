# QuickSort

> The idea of the quick sort, is to generate a partition, and then sub partitions, and use a order sort to order them, and then merge all together again in a
ordeder fashion.

### Here is a video of the process
[TedEd Sort algorithms](https://www.youtube.com/watch?v=WaNLJf8xzC4)

![Quick Sort](/assets/quicksort1.jpg)

## One psudocode idea

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Example of execution

![Quick Sort](/assets/quicksort2.jpg)

# References
- https://www.youtube.com/watch?v=WaNLJf8xzC4
- https://visualgo.net/en/sorting
- https://www.geeksforgeeks.org/python-program-for-quick_sort/
