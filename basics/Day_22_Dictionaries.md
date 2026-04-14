# What Are Dictionaries, and How Do They Work?
- In Python, dictionaries are built-in data structures that store collections of key-value pairs. They work very similarly to real dictionaries, where you search for a word to find its corresponding meaning.
- With Python dictionaries, you use a key to find its corresponding value. You should use dictionaries when you need to associate values to unique keys. This is helpful when you need to find a value fast based on the key, and when you need to represent structured data.

- This is the general syntax of a Python dictionary:
```python
dictionary = {
    key1: value1,
    key2: value2
}
```
```python
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
```
- Another alternative would be using the dict() constructor, which builds the dictionary from a sequence of key-value pairs.

- This would be the equivalent syntax for our pizza example. We pass a list of tuples as argument to the dict() constructor. These tuples contain the key as the first element and the value as the second element.
```python
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
```
- To access a value we use: **dictionary[key1]**
- To update a value, you just need to add the assignment operator, followed by the new value.
- If the key doesn't exist in the dictionary, a new key-value pair will be created.
- The **.get()** method retrieves the value associated with a key. It's similar to the bracket notation that we just used, but its advantage is that you can set a default value, so you won't get an error if the key doesn't exist.
- The **.keys()** and **.values()** methods return a view object with all the keys and values in the dictionary, respectively.
- The **.items()** method returns a view object with all the key-value pairs in the dictionary, including both the keys and the values.
- The **.clear()** method removes all the key-value pairs from the dictionary.
- The **.pop()** method removes the key-value pair with the key that you specify as the first argument and returns its value.
- And **.popitem()** is used to remove the last inserted value.
- The **.update()** method updates the key-value pairs with the key-value pairs of another dictionary. It will create a new pair if doesn't exists or overwrite the existing one.
