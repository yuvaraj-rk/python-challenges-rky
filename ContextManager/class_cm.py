#https://labex.io/labs/python-python-context-manager-633650?course=python-cheatsheet

# Class-based context manager: implement __enter__ and __exit__ methods
class ContextManager:
    def __enter__(self, *args, **kwargs):  # Called when entering 'with' block
        print("--enter--")
        return self  # Can return object to use as 'as' variable

    def __exit__(self, *args):  # Called when exiting 'with' block
        print("--exit--")

with ContextManager():  # Calls __enter__, then __exit__ when done
    print("test")
