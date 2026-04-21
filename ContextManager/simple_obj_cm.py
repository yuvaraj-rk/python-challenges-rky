#https://labex.io/labs/python-python-context-manager-633650?course=python-cheatsheet

# We will create a file to demonstrate the 'with' statement.
# First, let's write some content to a file.
with open('my_file.txt', 'w') as f:
    f.write('This is a test file.')

# Now, let's read it back using a context manager.
# The file is automatically closed when exiting the 'with' block.
with open('my_file.txt') as f:
    file_contents = f.read()
    print(file_contents)

# The file is automatically closed here, even if an error occurred.
print("\nFile has been read and closed.")
