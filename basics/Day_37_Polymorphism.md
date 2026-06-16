# POLYMORPHISM
> Polymorphism allows methods in different classes to share the same name but perform different tasks. We call the same method name on different objects, and each responds in its own way.
- Example:
```py
class Cat:
   def speak(self):
       return "A cat meow"

class Bird:
   def speak(self):
       return "A bird tweet"
  
class Monkey:
   def speak(self):
       return "A monkey ooh ooh aah aah ooh ooh aah aah"

def animal_sound(animal):
   print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())
```
- There's also a kind of polymorphism called inheritance-based polymorphism.
  > In inheritance-based polymorphism, a parent class defines a method, and multiple child classes override that method in their own way. We can then call the same method on any child object, and it behaves differently depending on which child class it is.
  ```py
  class Animal:
   def speak(self):
       return 'Some generic sound'

  class Cat(Animal):
     def speak(self):
         return 'A cat meow'

  class Dog(Animal):
     def speak(self):
         return 'A dog barks woof woof'

  class Monkey(Animal):
     def speak(self):
         return 'A monkey ooh ooh aah aah ooh ooh aah aah'
  
  print(Cat().speak()) # A cat meow
  print(Dog().speak()) # A dog barks woof woof
  print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
  print(Animal().speak()) # Some generic sound
  ```
