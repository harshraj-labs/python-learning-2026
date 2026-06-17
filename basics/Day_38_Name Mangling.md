> Prefixing an attribute with a double underscore triggers Python's name mangling process, in which Python internally renames the attribute by adding an underscore and the class name as a prefix, turning __attribute into _ClassName__attribute.
- why does Python do name mangling?
 > The main purpose of name mangling is to prevent accidental attribute and method overriding when we use inheritance. Here's an example:

```py
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
```
