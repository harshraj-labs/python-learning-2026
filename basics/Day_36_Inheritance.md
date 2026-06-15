# Inheritance
> With inheritance, a subclass (or child class) can use the attributes and methods of a base class (or parent class). This allows us to reuse code, create clear class hierarchies, and customize behavior without rewriting everything. We can customize by extending existing methods or overriding them in the child class.
```py
#syntax
class Parent:
    # Parent attributes and methods

class Child(Parent):
    # Child inherits, extends, and/or overrides where necessary
```
- We need to pass Parent class as an argument to the child class, for the child to inherit from parent
- This style is called ``` Single Inheritance ``` , since a child class inherits from exactly one parent class.
- There's also multiple inheritance, where a child class can inherit from more than one parent class.
```py
class Parent:
    # Attributes and methods for Parent

class Child:
    # Attributes and methods for Child

class GrandChild(Parent, Child):
    # GrandChild inherits from both Parent and Child
    # GrandChild can combine or override behavior from each
```


