# Tuples
- A tuple is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types like this:
    ```python
    developer = ('Alice', 34, 'Rust Developer')
    ```
- Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created.

- All the operations are similar to as in List, except for the mutable onces. Like changing the value, deleting and adding a new element.

- When to use tuple over lists?
    - When we need a dynamic collection of elements where we can add, remove and update elements, then we should use a list. If we know that we are working with a fixed and immutable collection of data, then we should use a tuple.


# Common methods with Tuple:

- Count(): Used to determine how many times an item is repeated in a tuple.
```python
names = ('trix','raj','kromp','raj')
names.count("raj") #2
```

- Index(): used to determine the index number of the particular item.
```python
tup = ('34','ear','nose','12','python',"12")
tup.index("nose")#2
#Another thing we can do with the index() method is to pass in optional start and stop index arguments. Here is an example of passing in an optional start index:
tup.index("12",4)#6
```
    - we are specifying to start searching at index 4. Since 12 appears twice in the tuple, the index() function will return index 6 instead of index 3 because of the use of the optional start index argument.
    - We can also give a stopping index value.

- Sorted(): The sorted() function will always create a new list of the sorted values. This differs from the sort() method which sorts the elements of a list in place and does not return a new list.
