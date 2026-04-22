# f-string: recommended way to format strings (Python 3.6+)
name = 'Elizabeth'
print(f'Hello {name}!')  # f prefix allows expressions in {}

# f-strings support expressions: can include calculations inside {}
a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')

name = 'Robert'
messages = 12
multiline_string = (
    f'Hi, {name}. '
    f'You have {messages} unread messages'
)
print(multiline_string)

# = specifier: prints both variable name and value (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
print(f'date and time: {now=}')

'''
Hello Elizabeth!
Five plus ten is 15 and not 30.
Hi, Robert. You have 12 unread messages
date and time: now='Apr/23/2026 - 01:27:39'
'''

########## String Formatting ############

# Adding thousands separator
a = 10000000
print(f"Number with separators: {a:,}")

# Rounding a float to 2 decimal places
b = 3.1415926
print(f"Rounded number: {b:.2f}")

# Showing a number as a percentage with 2 decimal places
c = 0.816562
print(f"As a percentage: {c:.2%}")

'''
Number with separators: 10,000,000
Rounded number: 3.14
As a percentage: 81.66%
'''