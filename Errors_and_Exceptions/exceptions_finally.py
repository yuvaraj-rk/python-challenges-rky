#https://labex.io/labs/python-python-exception-handling-633656?course=python-cheatsheet

# Handle multiple exceptions in one except block
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # This will raise TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Catch multiple exception types
        print(error)  # Print the error message

divide(dividend=20, divisor=5)
divide(dividend=10, divisor=5)
divide(dividend=20, divisor=0)

'''
user:project/ $ python3 multiple_handler.py
4.0
can only concatenate str (not "int") to str
division by zero
'''

# finally block: always executes regardless of exceptions
def divide_v2(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # Always executes, even if exception occurs
        print('Execution finished')

divide_v2(dividend=10, divisor=5)
divide_v2(dividend=10, divisor=0)

'''
user:project/ $ python3 finally_handler.py
2.0
Execution finished
You can not divide by 0
Execution finished
'''