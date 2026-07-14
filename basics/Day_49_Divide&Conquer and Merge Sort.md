# Divide & Conquer:
> The divide and conquer paradigm in computer science is a technique for recursively breaking down problems into smaller sub-problems.
> One of the key aspects of this technique is recursion, which happens when a function calls itself repeatedly until a base case is reached.

- We'll see merge sort algorithm to better understand how the divide and conquer technique works.
- Let's say we had this list of numbers:
``` 69 37 88 22 ```
- The goal is to sort that list from smallest to largest using the merge sort algorithm.
- So basically, we'll first divide the list into half, assigning it to left and right.
- Then we'll divide each sides individually into halves and assigning them left and right until we are left with only 1 number both sides.
- A list with only one item in it is sorted by default. Next we need to merge each of those one element sub lists into a sorted list.
  ``` py
  # right side of original list
  88 22

  # divide the list in half
  88 | 22

  # merge the lists in sorted order
  22 88
  ```
- Same for left side now.
- Now that both halves of the original list are sorted, we merge those two halves together and sort the elements"
  ```
  22 37 69 88
  ```

Example code of the algorithm:
```py
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
```

>The time complexity for merge sort would be O(n log n) because the list is continuously divided in half (log n) and then merged together (O(n)). Unlike other sorting algorithms like bubble sort, merge sort is not sorted in place and has a space complexity of O(n).
