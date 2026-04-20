# Decorator: a function that takes another function and returns a wrapper
def your_decorator(func):
  def wrapper():
    # Do stuff before func...
    print("Before func!")
    func()  # Call the original function
    # Do stuff after func...
    print("After func!")
  return wrapper  # Return the wrapper function

# @your_decorator is syntactic sugar for: foo = your_decorator(foo)
@your_decorator
def foo():
  print("Hello World!")

foo()  # Calls wrapper, which calls foo with extra behavior
