#https://labex.io/labs/python-python-exception-handling-633656?course=python-cheatsheet

#Custom Exceptions
class MyCustomException(Exception):
    pass

try:
    raise MyCustomException('A custom message for my custom exception')
except MyCustomException:
    print('My custom exception was raised')

'''
user:project/ $ python3 custom_exception.py
My custom exception was raised
'''
