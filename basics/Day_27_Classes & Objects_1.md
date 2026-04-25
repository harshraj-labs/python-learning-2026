# What are classes & Objects:
- In Python, classes and objects are the core components of Object-Oriented Programming (OOP), used to bundle data and behavior into single, manageable units.
- **Classes:** A class is a user-defined blueprint or template for creating objects. It defines the structure and behavior that all its objects will share but does not represent a specific entity itself.
- **Objects:** An object (also called an instance) is a concrete, usable version of a class created at runtime. It occupies memory and holds actual data.

#example code:

```py
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Call the bark method
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!
```
