# Range:
- The range() function is used to generate a sequence of integers.
- Syntax:
```python
range(start,stop,step)
```

- The **required** stop argument is an integer that represents the end point for the sequence of numbers being generated. 
Here is an example of using the range() function:
```python
for num in range(3):
  print(num)
```
- The following code generates a sequence of numbers between 0 and 2. The integer 3 is not included because the stop argument is non-inclusive.
- If a start argument is not specified, then the default is 0. Otherwise, we can use the optional start argument to start the sequence of integers at a integer other than 0.
- By default the sequence of integers will increment by 1. But if we want to change that default, then we can use the optional step argument.
Here is an example of generating a sequence of even integers between 2 and 10:
```python
for num in range(2,11,2):
  print(num)
```
- It is important to note that the range() function only accepts integers as arguments, not floats.
- If we want to generate a sequence of integers in decrementing order, then we can use a negative integer for the step argument, like this:
```python
for num in range(40, 0, -10):
    print(num)
# The following code prints the numbers 40, 30, 20, and 10 in that order to the console.
```

- Another thing we can do with the range() function is create a list of integers by using it with the list constructor.
like this:
```python
num = list(range(2,11,2))
print(numbers) # [2, 4, 6, 8, 10]
```
**- The range() function is a very handy way to generate a sequence of integers in Python.**
