# Tree:
- A tree is a specific type of graph, which satisfies these conditions:
  - Have no loops or cycles (paths where the start and end nodes are the same).
  - Be connected (every node can be reached from every other node).
- Trees are non-linear data structures that organize nodes in a hierarchy, where nodes may have children, siblings, and parent nodes.
- The **root node** is the very top of a tree. It's the only node in the tree without a parent node.
- This is the node where you will start traversing the entire data structure, usually with algorithms like breadth-first search (BFS) or depth-first search (DFS).
- A **parent node** is a node that is immediately connected to other nodes below it.
- A **child node** is a node that is immediately connected to a node above it. 
- A **leaf** is a node that has no child nodes. Think of them as the end of the "branches" of the tree.

**Depth:** the length of the path from the root to that node. 
**Height:** the length of the path from that node down to a leaf.
**Degree:** the number of child nodes each node has.
Trees also have a **height**. The height of a tree is the height of its root node.

# Binary Trees and Binary Search Trees:
> A binary tree is a type of tree in which each node can have at most two child nodes, a left child node and a right child node.
> A binary search tree is a more specific version of a binary tree, with a very particular ordering property.
  - The ordering property of binary search trees (BST) establishes that for every node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value.
  - The left and right subtrees must also be binary search trees themselves.
  - This ordering makes search, insertion, and deletion operations very efficient if the tree is balanced.
  - A balanced tree is a tree in which the heights of the left and right subtrees of any node are very similar to make sure that operations remain efficient.

## Tries:
> Tries are tree data structures used to store a set of strings.
- Tries are also known as prefix trees because they are very efficient for operations that require finding strings based on their prefixes.
