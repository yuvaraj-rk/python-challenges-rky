# Decorator that works with functions that have parameters
def your_decorator(func):
  def wrapper(*args,**kwargs):  # Accept any arguments
    # Do stuff before func...
    print("Before func!")
    func(*args,**kwargs)  # Pass arguments to original function
    # Do stuff after func...
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")  # Arguments are passed through wrapper
