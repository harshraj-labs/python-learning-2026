# What Are Methods and Attributes, and How Do They Work?

- **Attributes:** These are variables that belong to an object, so they hold data. There are two kinds of attributes: instance attributes and class attributes.
  - Instance Attribute: are unique to each object created from a class, and you usually set them with the __init__ method.
  - Class attributes: belong to the class itself and are shared by all instances of that class.
    ```py
    class Dog:
    species = "French Bulldog" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute
    
    ```
* Note that you can access class attributes directly from the class itself, but you need to create an object and pass it data first before you can access instance attributes.

---

- **Methods:** are functions defined inside a class.With them, any object defined from a class can perform actions that operate on or modify its own data. You also access a method with dot notation.
- For example, dogs can bark. So we can have a bark method in the Dog class like we saw previously.
  ```py
  class Dog:
   species = "French Bulldog"

   def __init__(self, name):
     self.name = name

   def bark(self): #method
       return f"{self.name} says woof woof!"

  jack = Dog("Jack")
  jill = Dog("Jill")

  print(jack.bark()) # Jack says woof woof!
  print(jill.bark()) # Jill says woof woof!
  ```
  

