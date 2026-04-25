#https://labex.io/labs/python-python-reading-and-writing-files-633663?course=python-cheatsheet

# Write to file: 'w' mode overwrites existing file
with open('/home/labex/project/bacon.txt', 'w') as bacon_file:  # 'w' = write mode
    chars_written = bacon_file.write('Hello world!\n')  # Returns number of characters written

print(chars_written)

# Append to file: 'a' mode appends to existing file
with open('/home/labex/project/bacon.txt', 'a') as bacon_file:  # 'a' = append mode
    chars_written = bacon_file.write('Bacon is not a vegetable.')

print(chars_written)

with open('/home/labex/project/bacon.txt') as bacon_file:
    content = bacon_file.read()

print(content)

'''
labex:project/ $ python3 write_file.py
13
25
Hello world!
Bacon is not a vegetable.
'''
