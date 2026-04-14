# Sets:
- Sets are one of Python's built-in data structures. One of the core characteristics of sets is that they don't store duplicate values. If we try to add a duplicate value to a set, only one of them will be stored.

- Sets are mutable and unordered, which means that their elements are not stored in any specific order, so we cannot use indices or keys to access them. They can only contain values of immutable data types like numbers, strings, and tuples. And they support mathematical set operations, including union, intersection, difference, and symmetric difference.
- set:
```py
my_set = {1, 2, 3, 4, 5}
```
- .add() to add and .remove() to remove, python functions are all self understood.
- .clear() to clear the whole set.
- The .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.
- The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common.
- There are operators for union and intersection of sets (its easy to understand if we have studied SETS in mathematics.) There operators are | and &, respectively.
- The difference operator - returns a new set with the elements of the first set that are not in the other sets.
- The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both.
- Each one of these operators also has its corresponding compound assignment operator if we add the equal sign next to it. These operators automatically assign the resulting set to the first set in the expression.
- we can check if an element is in a set or not with the in operator.

 
