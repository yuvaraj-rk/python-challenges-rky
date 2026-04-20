import functools

# Decorator factory: returns a decorator based on parameters
def prefix_decorator(prefix):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      # Use the 'prefix' argument from the factory
      print(f"{prefix} Before function call")
      result = func(*args, **kwargs)
      print(f"{prefix} After function call")
      return result
    return wrapper
  return decorator  # Return the actual decorator function

# Using the decorator with a parameter
@prefix_decorator(prefix="LOG:")
def say_hello(name):
  print(f"Hello, {name}!")

say_hello("Alice")
