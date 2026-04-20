# Pattern 1: Decorating a method within a class
class DecorateMyMethod:

  # Static method decorator for methods with only 'self' parameter
  def decorator_for_class_method_with_no_args(method):
    def wrapper_for_class_method(self):  # Only takes self
      try:
        return method(self)  # Call original method
      except Exception as e:
        print(f"\nWARNING: An exception occurred: {e}\n")
    return wrapper_for_class_method

  def __init__(self,succeed:bool):
    self.succeed = succeed

  @decorator_for_class_method_with_no_args
  def class_action(self):
    if self.succeed:
      print("You succeeded by choice.")
    else:
      raise Exception("Epic fail of your own creation.")

print("--- Testing Pattern 1 ---")
test_succeed = DecorateMyMethod(True)
test_succeed.class_action()

test_fail = DecorateMyMethod(False)
test_fail.class_action()
print("-" * 25)

# Pattern 2: Class-based decorator for maintaining state
class CountCallNumber:

  def __init__(self, func):
    self.func = func  # Store the function to decorate
    self.call_number = 0  # Initialize call counter

  def __call__(self, *args, **kwargs):  # Makes instance callable
    self.call_number += 1  # Increment counter
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)  # Call original function

@CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

print("\n--- Testing Pattern 2 ---")
say_hi("Jack")
say_hi("James")
