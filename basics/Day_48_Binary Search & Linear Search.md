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
