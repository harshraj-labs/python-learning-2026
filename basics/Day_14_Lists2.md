# Append:
- This is used to add an item to the end of the list.
- ex:
  ```python
  numbers = [1, 2, 3, 4, 5]
  numbers.append(6)
  print(numbers) # [1, 2, 3, 4, 5, 6]
  ```
- If we want to add one list at the end of another, we can also use the append() method.
  ```python
  numbers = [1, 2, 3, 4, 5]
  even_numbers = [6, 8, 10]

  numbers.append(even_numbers)
  print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
  ```
- But if we want to add all of the individual numbers from the even_numbers list at the end of the numbers list, then we can use the extend() method.Like this:
  ```python
  numbers = [1, 2, 3, 4, 5]
  even_numbers = [6, 8, 10]

  numbers.extend(even_numbers)
  print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]
  ```

# Insert:
- To insert an element at a specific index in a list, we can use the insert() method. This method accepts two arguments: the index where we wish to insert the new item and the item we want to insert.

# Remove:
- If we want to remove an element from a list, we can use the remove() method. The remove() method takes the value of the element to remove as an argument.
- But it only removes the first occurence of an item.

# Pop:
- To remove an element at a specific index in the list, we can use the ==pop()== method like this:
  ```python
  numbers = [1, 2, 3, 4, 5]
  numbers.pop(1) # The number 2 is returned
  ```
- If we don't specify an element for the pop method, then the last element is removed.
- If we need to empty the list, then we can use the clear() method.

# Sort:
- This method is used to sort the elements in place. Here is an example of sorting a random list of numbers in place:
  ```python
  numbers = [19, 2, 35, 1, 67, 41]
  numbers.sort()

  print(numbers) # [1, 2, 19, 35, 41, 67]
  ```
- In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list.

# Reverse:
- This method, will reverse a list of elements in place like this:
  ```python
  numbers = [6, 5, 4, 3, 2, 1]
  numbers.reverse()

  print(numbers) # [1, 2, 3, 4, 5, 6]
  ```

# Index:
- This is used to find the first index where an element can be found in a list. Here is an example of using the index method to find the language 'Java' in a programming_languages list:
  ```python
  programming_languages = ['Rust', 'Java', 'Python', 'C++']
  programming_languages.index('Java') # 1
  ```
- If the element cannot be found, then Python throws a ValueError
