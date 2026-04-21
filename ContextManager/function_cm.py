#https://labex.io/labs/python-python-context-manager-633650?course=python-cheatsheet

# Function-based context manager using contextlib decorator
import contextlib

@contextlib.contextmanager
def context_manager(num):
    print('Enter')  # Code before yield runs on __enter__
    yield num + 1   # Value yielded becomes 'cm' variable
    print('Exit')    # Code after yield runs on __exit__

with context_manager(2) as cm:  # cm receives the yielded value (3)
    print('Right in the middle with cm = {}'.format(cm))
