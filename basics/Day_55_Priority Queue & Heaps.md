## Priority Queue:
> A priority queue is an abstract data type (ADT) that works similarly to a queue or stack, but with one key difference.
- Queues and stacks only consider the order of insertion of the elements.
- However, priority queues take the "priority" of the elements into account. The priority is used to determine which element should be removed next.
- Usually, the element with the highest priority is removed first, but some implementations may also choose to remove the element with the lowest priority first. This will depend on the requirements of our program.
- Priority queues are very helpful for practical applications like finding the shortest path between two locations, scheduling tasks in operating systems, simulating traffic, compressing data, and managing networks.

## Heap:
> A heap is a tree data structure with a very specific property called the heap property. This property determines the relationship between each node and its children, based on the type of heap.
- There are 2 types of heaps:  
  ### Max heap:
  > The value of each node is greater than or equal to the value of its children.

  ### Min Heap:
  > The value of each node is less than or equal to the value of its children.
  - Python has a heapq built-in module that can be used to work with an implementation of a min-heap.
