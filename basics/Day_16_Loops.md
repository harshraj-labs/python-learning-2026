# For Loop:
-  Here is an example of using a for loop to iterate through a list and print each item to the console:
  ```python
  programming_languages = ['Rust', 'Java', 'Python', 'C++']

  for language in programming_languages:
    print(language)
  #output:-
  #Rust
  #Java
  #Python
  #C++
  ```
- Notice that the print(language) is indented inside of the loop. Without that indentation, we would get an IndentationError
- We  can also use a for loop to iterate through other iterables like a string. Here is an example of using a for loop to loop through the string code and print out each character:
  ```python
  for char in 'code':
    print(char)
  # output:
  #c
  #o
  #d
  #e
  ```
- We can also nest loops.

# While Loop:
- This type of loop will repeat a block of code until the condition is False. Here is an example of using a while loop for a guessing game:
  ```python
  secret_number = 3
  guess = 0

  while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

  print('You got it!')
  ```
- Just like in C. Python supports break and conitnue statements.
- The break statement is used to stop the execution of loop. here is an example:
  ```python
  developer_names = ['Jess', 'Naomi', 'Tom']

  for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)
  ```
- The continue statement is used to skip the current iteration of a loop and move onto the next iteration.
