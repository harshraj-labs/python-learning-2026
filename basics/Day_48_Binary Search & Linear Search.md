# What Is Binary Search and How Does It Differ From Linear Search?
- There are two key algorithms when it comes to searching: 
  - Linear search
  - Binary search

## Linear Search: 
> Linear search starts at the beginning of a list and iterates through each item until it finds the target value it is looking for.
- If the target value is found, the index where it's located in the list is returned. If the target value isn't found, -1 is returned.
Example code:
```py
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```
- While this is a relatively straightforward algorithm, it is not the most efficient. If you have a large list of items, linear search can take a long time to find the target value.
- The time complexity of linear search is **O(n)** because the time it takes to search through the list grows linearly with the size of the list.
- The space complexity of linear search is **O(1)** because it doesn't require any additional space to search through the list.

## Binary Search:
- Binary search is a more efficient algorithm for searching through a large list of items. The condition here is that the list must be sorted in ascending order.
> Binary search works by dividing the list in half and checking if the target value is in the middle of the list. If the target value is in the middle of the list, the index of the target value is returned. Otherwise, the algorithm checks if the target value is in the left or right half of the list.
- It continues to divide the remaining parts of the list into halves until the target value is found. If the target value is not in the list, it returns -1.
Example code:
```py
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
- The time complexity of binary search is O(log n) because the time it takes to search through the list grows logarithmically with the size of the list.
- The space complexity of binary search is O(1) because it doesn't require any additional space to search through the list.

---

> Binary search and linear search can be used for a variety of problems we will encounter in computer science. It is important to understand the differences between the two algorithms and when to use each one.
