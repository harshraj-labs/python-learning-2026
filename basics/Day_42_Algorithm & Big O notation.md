# <p align = "center"> What Is an Algorithm and How Does Big O Notation Work? </p>

## Algorithm:
>  An algorithm is a set of unambiguous instructions for solving a problem or carrying out a task.

- We can think of algorithms as "recipes". When you cook, recipes list all the ingredients that you'll need, and provide step by step instructions on how to prepare a dish.
- Equivalently, you can think of algorithms as "recipes" that tell computers exactly what should be done and how to do it.

### Algorithms have two key characteristics:

- They cannot continue indefinitely. They must finish in a finite number of steps.
- Each step must be precise and unambiguous.
> They may have zero, one, or more inputs, and generate one or more outputs.
> 
> The steps of an algorithm are independent from any programming language.

- Algorithm efficiency can be measured in terms of how long they take to run and how much space they require in memory to complete the task.
- This is where Big O notation becomes very important.

## Big O Notation:
> Big O notation describes the worst-case performance, or growth rate, of an algorithm as the input size increases.

- Big O notation focuses on the worst-case performance because this case is very important to understand how efficient the algorithm can be, even in the worst case scenario, regardless of the input.
- In Big O notation, we usually denote input size with the letter n.

- Here are some common ones:
    - **0(1)**: is known as "Constant Time Complexity". When an algorithm has constant time complexity, it takes the same amount of time to run, regardless of input size.
    - **O(log n)**: is known as "Logarithmic Time Complexity". This means that the time required by the algorithm increases slowly as the input size grows.
    - **O(n log n)**: is known as "Log-Linear Time Complexity". This is a common time complexity of efficient sorting algorithms, like Merge Sort and Quick Sort.
    - **O(n)**: is known as "Linear Time Complexity". The running time of algorithms with this time complexity increases proportionally to the input size.
    - **O(n²)**: s known as "Quadratic Time Complexity". The running time of these algorithms increases quadratically relative to the input size, which is generally not efficient for real-world problems.
    - Other time complexities include "Exponential Time Complexity", denoted as **O(2^n)**, and "Factorial Time Complexity", denoted as **O(n!)**. Both are inefficient for real-world scenarios.

----
> Algorithms are the building-blocks of computer programs, while Big O notation is a powerful framework for analyzing how efficient they are, based on how their time and space requirements in the worst-case scenario scale as the input size grows. Understanding their efficiency is very important for developing software that works efficiently in real-world scenarios.
