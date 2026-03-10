# What Are Strings and What Is String Immutability?

- String is a sequence of characters surrounded by either single or double quotation marks.
- In python both single and double quotation are treated equally unlike other programming languages.

  ```
  my_str_1 = 'Hello'
  my_str_2 = "World"
  ```

- We can add multiline strings using triple single or double quotes:

  ```
  my_str_3 = """Multiline
  string"""
  my_str_4 = '''Another
  multiline
  string'''
  ```

- If your string contains either single or double quotation marks, then you have two options:
  Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:

  ```
  msg = "It's a sunny day"
  quote = 'She said, "Hello World!"'
  ```
- Or use backslash (\) to escape the quotes:
  ```
  msg = 'It\'s a sunny day'
  quote = "She said, \"Hello!\""
  ```
- To check if a character(s) is in a string or not, python provides an operator (in).
  ```
  my_str = 'Hello world'
  print('Hello' in my_str)  # True
  print('hey' in my_str)    # False
  print('hi' in my_str)    # False
  print('e' in my_str)  # True
  ```
- To get the legnth of a string we can use (len) operator, it also counts spaces.
  ```
  my_str = 'Hello world'
  print(len(my_str))  # 11
  ```

-Each character in a string has a position called an index. The index starts with a 0,  meaning that the index of the first character of a string is 0, the index of the second character is 1, and so on.
To access a character by its index, we use square brackets ([]) with the index of the character. (Similar to array in C)
```
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w
```
- Negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on:
```
my_str = 'Hello world
print(my_str[-1])  # d
print(my_str[-2]) # l
```

# Immutable and Mutable:

- As per my understanding its basically like pointers and refernce in C.
- Strings are immutable data types in Python. This means that we can reassign a different string to a variable:
```
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```
- But direct modification of a string isn't allowed:
```
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```
- Examples of other immutable data types in Python are integer, float, boolean, tuple, and range. You'll get to know each of these types in upcoming lessons.
