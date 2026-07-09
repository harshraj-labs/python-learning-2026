# Linked List:
> A linked list is a linear data structure in which each node is connected to the next node in the sequence.
- These connections create a data structure that looks like a chain of nodes, where each node stores data and a reference (address of where the next node is stored) to the next node in the linked list.
- We use these references to go from the first node to the next node and so on.
- The list starts at **Head** node and ends at **Tail** node.

---

## Singly Linked List:
> A singly linked list is a type of linked list in which each node is connected to the next node in the sequence.
- This single reference per node allows you to traverse the linked list in one direction, from start to end.
- The search can only move forward, not backwards.

### Inserting Node: 
- One of the great things about linked lists is that they do not have a fixed size. They can be expanded or shrunk as needed by simply updating the connections between the nodes.
- We can insert the node at start, middle, and end of linked list.
- Inserting a node at the beginning of the linked list has a constant time complexity O(1).
- Inserting a node at the end of the linked list has a time complexity of O(n), where n is the number of nodes.

### Removing Node:
- Just as we can insert nodes, we can also remove them from the start, middle, and end of the linked list.
- To remove a node from the start, you need to update the reference to the head node, which should be the next node in the sequence.
- Its time complexity is O(1).
- To remove a node from the end of the linked list, you need to remove the connection of the previous node and make this node the new tail node. Now the linked list will end at the new tail node. This operation has a linear time complexity O(n).

---

## Doubly Linked List:
> A doubly linked list, each node stores two references: a reference to the next node and a reference to the previous node in the sequence.
- This means that doubly linked lists can be traversed in both directions.
- In this type of linked list, it's also common to keep a reference to the tail node in the linked list itself to start the traversal from the end if necessary.
- Doubly linked lists do require more memory than singly linked lists because each node stores two references instead of one.
- The insertion and deletion operations work exactly the same. The only difference is that now we will need to update two references per node and keep track of the reference to the tail node to insert elements at the end of the doubly linked list very efficiently and start the traversal process from the back, if necessary.
---

> Singly and doubly linked lists are essential data structures in computer science used for storing and manipulating elements in a sequential order. Understanding their differences is essential for choosing the right one for your specific application.
