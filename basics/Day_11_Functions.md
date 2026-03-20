# Function
- It's a piece of reusable code that runs when we call them. Its the same as in C.
- Built in functions:
    - print()
    - input() {used to take input from user}
    ```python
    name = input("What's your name?")
    print("Hello",name)
    ```
    - int()
    - and more predefined functions we can use

- We can also define our own custom function using the keyword ==def== 
example:
```python
def hello():
    print("Hello World!")
hello() # Hello World!

def sum(a,b):
    print(a+b)

sum(2,4) #6
```
- Calling a function without the correct arguements would give type error
- And just like in C we can use ==return== keyword to return a value instead of getting it printed or anything else.

# Scope
- In Python, scope determines the point at which we can access a variable. It's what controls the lifetime of a variable and how it is resolved in different parts of the code.

- To correctly determine scope, Python follows the LEGB rule, which stands for the following:
    - Local scope(L): Variables defined inside a function or class
    - Enclosing scope(E): variables defined in enclosing or nested functions
    - Global scope(G): Variables defined at the top level of the module or file
    - Built-in Scope(B): Reserved names in python for predefined functions,module,keywords and objects.
    