## Stacks & Queues:
- Stacks and queues are data structures commonly used in computer science.
- They're linear data structures that follow specific rules for adding and removing elements.

# Stacks:
> A stack is a Last-in, First-out (LIFO) data structure.This means that the last element that was added to the stack is the first one to be removed.
- Stack has 1 end which is known as Top.
- Elements are added and removed from the top.
- Example: A pile of plate/dishes, where we can only place dishes at the top of the pile and take dishes from the top of the pile.
- These operations of adding and removing elements have special names in this context.
  - **PUSH:** Adding an element to a stack is known as a "push" operation. We say that we "push" an element onto the stack when we add it to the top of the stack.
  - **POP:** Removing an element from a stack is known as a "pop" operation. We say that we "pop" an element from the stack when we remove it from the top of the stack.
- The time complexity for PUSH and POP are O(1), constant. Regardless the size of Stack.

# Queues:
> A queue is a First-in First-out (FIFO) linear data structure. This means that the first element added to the queue is the first one to be removed.
- Queues have 2 end, ```Top and Bottom```.
- Elements are added to the back of the queue and they are removed from the front of the queue.
- An example of this would be a real queue of people in line.
- The operations of adding and removing elements have special names in the context of a queue.
  - **Enqueue:** Adding an element to the back of a queue is known as an "enqueue" operation.
  - **Dequeue:** Removing an element from the front of the queue is known as a "dequeue" operation.

- The time complexity of the enqueue and dequeue operations is O(1), constant time. The time it takes to perform these operations remains constant, regardless of the size of the queue.
