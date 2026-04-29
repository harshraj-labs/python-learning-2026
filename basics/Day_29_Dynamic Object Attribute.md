### What are attributes?
- Attributes are variable that holds data that describe the state or behaviour of an object.
- For example: a car would normally have a brand and model. The brand and model could make attributes for a Car class:
  ```py
  class Car: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 

  my_car = Car('Lamborghini', 'Gallardo') 
  print(my_car.brand) # Lamborghini 
  print(my_car.model) # Gallardo 
  ```

- But sometimes, we might not know which attributes we need until ourr program is running. Imagine we're writing a script that receives attribute names from a user or a configuration file.
- Those are not attributes we can hardcode ahead of time.
- That's where handling attributes dynamically comes in. This way, we can access, modify, check, or even delete attributes using their names as variables, and not as fixed names in our code. This gives our program the flexibility to respond to different data or user input on the fly.
- Python gives up four handy built-in functions to dynamically work with object attributes.
    - They are:
        - getattr()
        - setattr()
        - hasattr()
        - delattr()
    - They let us access, create, check, and remove attributes using variable names. Let's take a look at each one in action.

  - getattr() makes us read the attribute from an object when we don't know its name until runtime.
      - syntax: ```getattr(object,attribute_name,default_value) ```
      - example:
        ```py
        class Person: 
        def __init__(self, name, age): 
        self.name = name 
        self.age = age 

        person = Person('John Doe', 30)

        attr_name = input('Enter the attribute you want to see: ')
        print(getattr(person, attr_name, 'Attribute not found'))
        ```
  - setattr() function lets us create a new attribute or update an existing one dynamically.
    - The syntax looks like this: ```setattr(object, attribute_name, value) ```
      ```py
      class Configuration:
        pass

        # Data loaded at runtime (like from a config or env file)
        settings_data = {
            'server_url': 'https://api.example.com',
            'timeout_sec': 30,
            'max_retries': 5
        }

      config_obj = Configuration()

      # Dynamically set attributes using dictionary keys and values
      for attr_name, attr_value in settings_data.items():
        setattr(config_obj, attr_name, attr_value)

      print(config_obj.server_url) # https://api.example.com
      print(config_obj.timeout_sec) # 30
      ```
  - hasattr() to check if a particular attribute exists or not.
    - syntax: ```hasattr(object, attribute_name)  ```
  - delattrr() is ofc used to delete an attribute.
    - syntax: ```delattr(object, attribute_name)```
