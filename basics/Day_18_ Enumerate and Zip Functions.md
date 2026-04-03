# Enumerate:
- The enumerate() function keeps track of the index for an iterable and returns an enumerate object.
- If we pass the languages list to the enumerate() function and convert its returned value into a list with the list() function, it looks like this:
```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
```

Now:
```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
```
- So far we've only been iterating over one list. But what if you need to iterate over multiple iterables in parallel? Well, you can use the zip() function for that, which combines lists into pairs of elements and returns an iterator of tuples.
- If we pass a list of developers and ids to the zip() function and convert its returned value into a list with the list() function, here's what it looks like:
```python
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
```




