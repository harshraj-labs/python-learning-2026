# Lists:
- This data type is an ordered sequence of elements that can comprise of strings,numbers,or even other lists.
- They are mutable and uses zero-based indexing.
- syntax:
  ```python
  names = ['python','c','ML']
  #can be accessed like:
  names[0] # python
  ```
- Can also use negative indexing to start from the last elements. ex: names[-1] is ML.
- Another way to create a list is to use the list() constructor. The list() constructor is used to convert an iterable into a list like this:
  ```python
  developer = "raj"
  list(developer) # ['r','a','j']
  ```
- We can use len() function to get the total number of elements in a list, so len(names) # 3
- We can update the value at a particular index just like in C
- We can use del keyword to remove an element of a list like this:
  ```python
  del names[1] # it will remove C from the list names
  ```
- We can use "in" keyword to check if an element is inside a list or not (it's plain english at this point), exmaple:
  ```python
  'python' in names # True
  ```
- Nested lists:
  ```python
  developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
  ```
- To access them is the same as accessing multi-dimensional array.
- Unpacking values from a list is a technique used to assign values from a list to new variables. Here is an example of unpacking a developer list into new variables called name, age and job.
  ```python
  developer = ['Alice', 34, 'Rust Developer']
  name, age, job = developer

  print(name) # 'Alice'
  print(age) # 34
  print(job) # 'Rust Developer'
  ```
- We can use the asterisk (*) operator like this to collect any remaining values:
  ```python
  developer = ['Alice', 34, 'Rust Developer']
  name, *rest = developer
    
  print(name) # 'Alice'
  print(rest) # [34, 'Rust Developer']
  ```
- The slice operator (:). Similar to strings, you can access portions of a list by using the slice operator like this:
  ```python
  desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
  desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
  ```
- Another thing we can do with the slice operator : is specify a step interval which determines how much to increment between the indices. like this:
  ```python
  numbers = [1, 2, 3, 4, 5, 6]
  # If we wanted to extract a list of just even numbers, you can use the slicing operator like this:
  numbers[1::2] # [2, 4, 6]
  ```
