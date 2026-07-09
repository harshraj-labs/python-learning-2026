# Map:
> A map is an ADT that manages collections of key-value pairs and their operations in a very specific and efficient way.
- ADT -> Abstract Data Type: Basically a blueprint that describe what operations can be performed, not how they are performed.
- In a map, every value is associated with a specific key.
- One of the key characteristics of maps is that every key must be unique. This uniqueness allows for direct lookups, which makes the process of retrieving information much more efficient.
- Only keys must be unique, values can be repeated.

# Hash Map:
> A hash map, also known as a hash table, is a concrete implementation of the map Abstract Data Type.
- Hash maps use a technique called "hashing" to perform common operations very efficiently.
- Hash maps use a technique called "hashing" to perform common operations very efficiently.
- The hash value is generated based on the key of the key-value pair and it's used to calculate an index in an underlying array, the actual data structure where the key-value pairs are stored.
- Python's dictionaries are implemented as hash maps behind the scenes.

# Sets:
> Sets are unordered collections of unique elements.
- They are analogous to sets in mathematics and they implement the same set operations, like intersection, union, and difference.
- They are also dynamic. They can adjust to the number of elements that are currently stored. This makes them quite powerful.
- Python has a built-in set data structure that we use to work with sets in your programs.
- To define a set in Python, we just need to surround the elements with curly brackets and separate them with commas.
- To create an empty set, you can call set()
- We can add an element to a set with the .add() method
- We can also remove an element from set with .remove() method.
