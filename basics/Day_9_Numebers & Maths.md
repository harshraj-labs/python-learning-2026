# Integers & Floats
- Basically everything i already know about integers (whole numbers, positive and negative) & float(numbers with decimal).
- Operations with them and also theres no need to convert a number to another data type to perform an operation.
- function to convert to either data type, int() & float()
- rounding nunmbers with round() function
- finding absolute values with abs()
- raising a number to power of another or modular exponentation with pow()

# Augmented Assignments
- Same as in C, so I know em all.
- it can also be used with strings
- urinary operators doesn't work in python

# Workshop for the same:

**BillSplitter**

```
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays= round(final_bill,2)
print('Each person pays:',each_pays)
```
