#https://labex.io/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet

import shutil
from pathlib import Path

# Create the destination directory if it doesn't exist
Path('/tmp/eggs').mkdir(parents=True, exist_ok=True)

# Move a file to a directory (only if source exists)
bacon_source = Path('/tmp/bacon.txt')
if bacon_source.exists():
    shutil.move('/tmp/bacon.txt', '/tmp/eggs')
    print("Moved '/tmp/bacon.txt' to '/tmp/eggs'")
else:
    print("'/tmp/bacon.txt' not found (may have been moved already)")

# Move and rename a file
# First, let's recreate the file to move
Path('/tmp/bacon.txt').touch()
shutil.move('/tmp/bacon.txt', '/tmp/eggs/new_bacon.txt')
print("Moved and renamed '/tmp/bacon.txt' to '/tmp/eggs/new_bacon.txt'")


'''
labex:project/ $ python3 manage_files.py
Moved '/tmp/bacon.txt' to '/tmp/eggs'
Moved and renamed '/tmp/bacon.txt' to '/tmp/eggs/new_bacon.txt'
labex:project/ $ ls /tmp/eggs
bacon.txt  new_bacon.txt
'''
