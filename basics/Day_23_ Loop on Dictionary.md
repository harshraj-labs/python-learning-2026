# Techniques for looping over Dictionary
- we can loop over a dictionary if we need to access and process its key-value pairs.
- Let's say that we have a products dictionary that associates every product with its price:
```python
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
```
- If we want to offer a 20% discount on all our products, we can loop over all the key-value pairs and modify the prices.
- The .values(), .keys(), and .items() methods are essential for these techniques.
- To print the price of all products:
  ```python
  for price in products.values():
    print(price)
  ```
- Same works for keys and items.
- for the discount we can code it like this:
  ```py
  products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
  }

  for product, price in products.items():
    products[product] = round(price * 0.8)

  print(products)
  ```
- If we Print the Dictionary we'd get the updated prices.
- We can also enumerate to counter the index for everything.
