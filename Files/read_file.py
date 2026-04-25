#https://labex.io/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet

# Read file using 'with' statement: automatically closes file when done
with open('/home/labex/project/hi.txt') as hello_file:
    hello_content = hello_file.read()  # Read entire file content

print(hello_content)

# readlines() method: returns list of strings, one per line
with open('/home/labex/project/sonnet29.txt') as sonnet_file:
    lines = sonnet_file.readlines()  # Returns list with each line as a string

print(lines)


# Iterate through file line by line (memory efficient for large files)
with open('/home/labex/project/sonnet29.txt') as sonnet_file:
    for line in sonnet_file:  # File object is iterable
        print(line, end='')  # Print without extra newline

'''
labex:project/ $ python3 read_file.py
Hello World!

["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,\n']
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,
'''
