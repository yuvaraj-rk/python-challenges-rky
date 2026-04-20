import functools

'''
import functools: Imports the necessary module.
@functools.wraps(func): This is a decorator applied to the wrapper function. 
It copies the metadata from the original func (like __name__ and __doc__) to the wrapper function.
'''

# Best practice decorator template: preserves function metadata and return value
def your_decorator(func):
  @functools.wraps(func)  # Preserves function name, docstring, etc.
  def wrapper(*args,**kwargs):
    print("Before function execution...")
    result = func(*args,**kwargs)  # Call function and capture return value
    print("After function execution...")
    return result  # Return the original function's return value
  return wrapper

@your_decorator
def add(a, b):
  """This function adds two numbers."""
  return a + b

sum_result = add(5, 3)
print(f"Function name: {add.__name__}")
print(f"Docstring: {add.__doc__}")
print(f"Result: {sum_result}")
