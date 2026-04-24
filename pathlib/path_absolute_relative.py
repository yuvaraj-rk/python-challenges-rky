#https://labex.io/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet

from pathlib import Path

# Check if paths are absolute
print(f"Path('/') is absolute: {Path('/').is_absolute()}")
print(f"Path('..') is absolute: {Path('..').is_absolute()}")

# Resolve a relative path to its absolute form
# '..' refers to the parent directory of the current working directory
resolved_path = Path('..').resolve()

print(f"Current working directory: {Path.cwd()}")
print(f"Resolved path of '..': {resolved_path}")

# Get a relative path from a starting point
# This shows the path to 'passwd' relative to the root directory '/'
relative_path = Path('/etc/passwd').relative_to('/')
print(f"Path to '/etc/passwd' relative to '/': {relative_path}")

'''
labex:project/ $ python3 main.py
Path('/') is absolute: True
Path('..') is absolute: False
Current working directory: /home/labex/project
Resolved path of '..': /home/labex
Path to '/etc/passwd' relative to '/': etc/passwd
'''