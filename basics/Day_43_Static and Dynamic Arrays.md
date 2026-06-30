## Arrays:
> Arrays are fundamental data structure in computer science.
> All arrays store ordered collections of data, but depending on their type, they may work differently behind the scenes.

# Static Arrays:
- They have a fixed size. They store memory in adjacent memory location.
- The size of a static array is determined when the array is initialized. Once that specific block of memory is allocated, it's fixed, and cannot be changed while the program is running. This is a key characteristic of static arrays.
- Storing elements in adjacent memory locations makes the data retrieval process more efficient because the program can store the location of the first element and then use indices to make simple calculations and find the other elements in memory.
- accessing the values of a static array takes constant time O(1), which is very efficient.
- We can use a static array when you know the number of elements that will be stored in advance. 
- It's also helpful when the values will be accessed very frequently, since the access operation is very efficient.
- However, this data structure cannot grow or shrink, so if the number of elements that will be stored can vary, we should use a dynamic array instead.
> Python does not include traditional static arrays as built-in data structures.
> Arrays in python are dynamic

# Dynamic Arrays:
- Dynamic arrays are more flexible because they can grow or shrink automatically while the program is running.

- They work through an automatic resizing mechanism that copies the elements into a new array when the original array is full.
- The process is done efficiently because the size of the new array is chosen in an efficient way that makes these computationally expensive operations less frequent.
- Accessing the elements of a dynamic array takes constant time O(1), so this operation is very efficient.
- Inserting an element in the middle of the array takes linear time O(n) because the elements after it need to be relocated.
> Inserting an element at the end of the array takes constant time O(1) if there is still space available in the dynamic array, but if the array is full and needs resizing, this operation has a O(n) complexity.


> The rest I know from C arrays.