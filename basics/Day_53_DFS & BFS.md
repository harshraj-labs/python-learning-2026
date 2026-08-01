### Traversing: The process of visiting each node.
- Traversals are used to do something with every single node in the data structure, like printing their values, finding a specific value, or performing certain operations on the nodes.

# Breadth First Search (BFS):
- It's an algorithm that visits all neighboring nodes before moving to the next level in the graph.
- It can be used to find the shortest path between two nodes in an unweighted graph because it analyzes all the nodes at each level, so it finds the path with fewest edges first.
- This algorithm is commonly implemented using a queue data structure to keep track of the nodes that have been visited. Queues follow the FIFO (first in, first out) method, where the first node that was added to the queue is the first one to be removed.
- The algorithm works like this:
  - It starts at a specific node.
  - That node is marked as visited and added to the queue.
  - While the queue is not empty, the current node is removed from the queue (dequeued). Then, for each one of its neighbors, if the neighbor has not been visited, it is marked as visited and added to the queue.

- One important consideration is that, since breadth-first search (BFS) requires storing a queue in memory, and this queue may have a large number of nodes, the space requirements of this algorithm can be considerable. This is especially true for graphs with a large number of nodes on the same level.

# Depth First Search (DFS):
- While breadth-first search (BFS) first visits all the neighboring nodes at the same level, depth-first search (DFS) follows each branch as deep as possible before it backtracks.
- Depth-first search (DFS) is commonly used to solve puzzles with a single solution, detecting cycles in a graph, and finding connected graph components.
- This algorithm can be implemented using recursion or a stack data structure to keep track of the visited nodes.
- The algorithm works like this:
  - Start at a specific node.
  - That node is marked as visited and added to the stack.
  - While the stack is not empty, the current node is popped (removed). This is when we "visit" or process it (for example, by printing its value). Then, all of its unvisited neighbors are marked as visited and added to the stack.
