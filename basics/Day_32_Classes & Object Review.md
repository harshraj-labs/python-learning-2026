### Class Definition: A class is a blueprint for creating objects. It defines the behavior an object will have through its attributes and methods. Here is a basic example of a class definition in Python:
- Example Code:
```py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof woof!')
```
### Creating Objects: Objects are instances of a class. They are created by calling the class with the necessary arguments.
- Example Code:
```y
dog1 = Dog('Jack', 3)
dog2 = Dog('Thatcher', 5)

dog1.bark()  # JACK says woof woof!
dog2.bark()  # THATCHER says woof woof!
```
### Calling Methods on Objects: You can call methods on objects to perform actions or retrieve information.

## Difference Between Class and Object: A class is a reusable template, while an object is a specific instance of that class with actual data.

### Attributes
- **Instance Attributes:** Defined in __init__() using self, and unique to each object.
- **Class Attributes:** Defined directly inside the class and shared by all instances.

### Methods
- **Methods:** Functions defined inside a class that operate on the object's attributes.

### Dunder (Magic) Methods
- **Definition:** Special methods that start and end with a double underscore (e.g., __init__, __len__, __str__, __eq__). Python uses them internally for built-in operations.
