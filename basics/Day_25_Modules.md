# What Is the Python Standard Library, and How Do You Import a Module?
- In Software Development, Library is a toolbox for developers.
- A library gives us a pre-written reusable code.
- Python has an extensive standard library with many different built-in modules. They're all standardized, well-vetted solutions for many of the problems and tasks you'll face daily as a programmer, such as:
  - Interacting with the operating system.
  - Working with files.
  - Networking.
  - Working with date and time.
  - Performing mathematical operations.
  - Using regular expressions.
  - Testing and debugging your code.
  - And much more!

- You use an import statement. These statements let you import modules into your Python script. Import statements are generally written at the top of the file. Also, you can customize them based on your needs.
```py 
import module_name
```
```py
import math
```
- This is the most basic version of an import statement, but there are other alternatives.
- If you need to import the module with a different name (also known as an "alias"), you can use this syntax, with as followed by the alias at the end of the import statement:
```py
import math as m 
```
- But sometimes you don't need to import everything from a module. Perhaps you only need one or two specific functions or classes. Python has exactly what you need in that case.
```py 
from math import radian, sin as s,cos
```
- Now the import statement starts with from, followed by the name of the module, and then the import keyword followed by the name of the elements that you want to import

```py
from math import *
```
- The asterisk is telling Python that you want to import everything in that module, but you want to import it so that you don't need to use the name of the module as a prefix

---
```py
if __name__ == '__main__': 
    # Code
```
__name__ is a special built-in variable in Python.

- When a Python file is executed directly, Python sets the value of this variable to the string "__main__".
But if the Python file is imported as a module into another Python script, the value of the __name__ variable is set to the name of that module (usually the filename without the .py extension).
- This is why you'll often find this conditional in Python scripts. It contains the code that you want to run only if the Python script is running as the main program.
