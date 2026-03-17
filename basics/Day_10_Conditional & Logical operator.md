Its the same as in C, the conditional operators are also the same.
- And as always it returns the value in boolean True or False
  Syntax :-

```python
if condition:
    pass # Code to execute if condition is True
-----------------------
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
```
- Indentation are realy important
- for multiple if statements
  syntax:-
```python
if condition1:
   pass # Code to execute if condition1 is True
elif condition2:
   pass # Code to execute if condition1 is False and condition2 is True
else:
   pass # Code to execute if all conditions are False
-------------------
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```
-We can use as many elif statements as we want.
- Nested if conditions also work the same as in C just with corrent Indentaiton

## Truthy & Falsy
-  Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False.
- some Falsy are:
  - None
  - False
  - Integer 0
  - Float 0.0
  - Empty strings ""

## Boolean Operators:
There are three boolean operators:
**- AND** : The and operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.
**- OR** : This operator returns the first operand if it is truthy, otherwise, it returns the second operand.
**- NOT** : It takes a single operand and inverts its boolean value.

# Workshop for the same:
- **Build a Movie Ticket Booking Calculator**
```python
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    
    print('Service charges:', service_charges)

    final_price = base_price+extra_charges+service_charges-discount
    print("Final price of ticket:",final_price)
else:
    print('Ticket booking failed due to restrictions')

```

  
