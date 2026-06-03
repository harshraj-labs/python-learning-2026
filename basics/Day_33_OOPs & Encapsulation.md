- Object-oriented programming, also known as OOP, is a programming style in which developers treat everything in their code like a real-world object.
- OOP has 4 key principles that helps us manage and organize code effectively, They are:
  - Encapsulation
  - inheritance
  - polymorphism
  - extraction

# Encapsulation:
- Encapsulation is the bundling of attributes and methods of an object into a single unit, the class.
- With encapsulation, we can hide the internal state of the object behind a simple set of public methods and attributes that act like doors. Behind those doors are private attributes and methods that control how the data changes and who can see it.
- By convention, prefixing attribute and methods with a single underscore means they are meant for internal use. No one should directly access them from outside the class since it defies the principles of encapsulation, which can lead to bugs.
- While a single underscore prefix is just a convention, prefixing attributes and methods with a double underscore effectively prevents them to be accessed from the outside of their class, making those attributes and methods private.

- **In summary, encapsulation locks down internal data behind clear public methods. That's how we keep our classes safe from tampering and centralize validation in one place. We can update or extend your code freely, knowing that outside code only touches the interfaces we expose.**
