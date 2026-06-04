# What are Getters and Setters?

- Getters and Setters are methods that let us control how the attributes of a class are accessed and modified.
- With getters we retreive a value and with setters we set a value.
- These actions are done through what's knowns as properties. They are what connects getters and setters, and allow acess to data.
  ## Properties:
  - Properties act like attributes but behave like methods. Therefore, they can accessed with dot notations instead of using brackets.
  - The main thing properties do is run extra logic behind the scene when we get,set or delete values wiht them.
  - This makes them perfect for when we want to access or manipulate data within objects.
  - To create a property we define a method and place **"@property"** decorator above it.
  - Example code:
    ```py
    class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
  
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

    my_circle = Circle(3)

    print(my_circle.radius) # 3
    print(my_circle.area) # 28.26
    ```

- A deleter runs custom logic when we use the del statement on a property, to create one, we use **"@<property_name>.deleter"**
  - example code with setter logic too:
    ```py
    class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
    ```
  - Deleter in use:
    ```py
    # Create circle object with a radius
    my_circle = Circle(33)
    print("Initial radius:", my_circle.radius)  # 33

    # Delete the radius
    # This calls the deleter
    del my_circle.radius # Deleting radius...
    print("Radius deleted!") # Radius deleted!

    # Trying to access radius after deletion
    try:
      print(my_circle.radius)
    except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'
    ```
---

### Summary:
- Getters let you retrieve a value or even compute a value on the fly.
- Setters let you modify the values safely by running checks before assignment.
- Properties are what tie these getters and setters together so you can write logic while still using dot notation.
- Deleters let you define what happens when an attribute is deleted.
