# String Slicing
- It lets you extract a specific portion of string or work with only a specific part of it.
Syntax:
```
string[start:stop] 

my_str = 'Hello world'
print(my_str[1:4]) # ell
```
Note: this is non inclusive index, so [1:4] just extracted the characters from index 1, and up to 4, but not including, the character at index 4.

-We can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively.
```
my_str = 'Hello world'
print(my_str[:7])  # Hello w

my_str = 'Hello world'
print(my_str[8:])  # rld
```
- Note that slicing a string does not modify the original string:
- You can also omit both the start and stop indices, which will extract the whole string.

-Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.
```
string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

#the slicing starts at index 0, stops before 11, and extracts every second character
```
-A helpful trick we can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank
```
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

# Some common String Methods ---
- Python provides a number of built-in methods that make working with strings a piece of cake.
  - upper(): Returns a new string with all characters converted to uppercase.
```
my_str = 'hello world'
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```
  - lower(): Returns a new string with all characters converted to lowercase.
```
uppercase_my_str = my_str.upper()
```
  - strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
  - replace(old, new): Returns a new string with all occurrences of old replaced by new.
  - split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.
  - join(iterable): Joins elements of an iterable into a string with a separator.

And many more...

That's it for today, completed 2 modules today!
