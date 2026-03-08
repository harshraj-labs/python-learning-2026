# Print
- introduced to the print function, to call it you don't need to call in any library, you just write print and the things inside it with     (' ') to show the output.
for example:
```
print('Hello World!')

#output: Hello World!
```
you can use commas to seprate words and it will show as a space in the output
example:

```
print('Hello', 'World', '!')
#output: Hello World !
```
Another noticing thing is" no need of semicolons to end the lines.

Then,

# Datatypes
- A data type describes the kind of value a variable holds. For example, a number, a piece of text, or a list of items. Programming languages use data types so they know how to store and work with different kinds of information.
- Python is a dynamically-typed language, meaning we don't need to explicitly declare types for variables like we used to do in C. The language knows what data type a variable is based on what we assign to it.
examples:

```
name = 'jhon' #python knows its a string
age = 20 #python knows its an integer.
```

- This dynamic nature of python makes coding really fast but also prone to many unexpected errors and bugs in bigger programs.
- Also python determines datatype while the programm is running, so the mistakes are only shown when the compiler reaches that line.
- Unlike C and other similar languages which compile the programm before running, which shows the error even before running the program.

Here are the most common datatypes: (with examples)
1. Integer = 10;
2. Float = 0.04;
3. String = 'Hello World!';
4. Boolen = True / False;
5. Set = {4,5,6};
6. Dictionary = {'name': 'Raj', 'age':'19'};
7. Tuple = (1,2,4);
8. Range = range(5) ==> 0 to 5;
9. list = ['raj','19','True'];
10. None

- To know the datatype of a variable we can use the "type()" function
- There is also a built in function to check if the variable matches a specific datatype, the function is  "isinstance()"

example:

```
age = 19
print(type(age)) # <class'int'>

isinstance(age, int) # True
```

That's it for today!