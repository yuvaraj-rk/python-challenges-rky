#https://labex.io/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet

from pathlib import Path
import shutil

# Create a file to delete
file_to_delete = Path('/tmp/deleteme.txt')
file_to_delete.touch()
print(f"Created '{file_to_delete}'")

# Delete the file
file_to_delete.unlink()
print(f"Deleted '{file_to_delete}'")

# Create a directory to delete
dir_to_delete = Path('/tmp/temp_dir')
dir_to_delete.mkdir(exist_ok=True)
# rmdir() only works on empty directories
dir_to_delete.rmdir()
print(f"Deleted empty directory '{dir_to_delete}'")

# Use shutil.rmtree() to delete a directory and its contents
# Note: This will fail if the directory doesn't exist, which is fine for this example
if Path('/tmp/bacon_backup').exists():
    shutil.rmtree('/tmp/bacon_backup')
    print("Deleted directory '/tmp/bacon_backup' and all its contents")
else:
    print("Directory '/tmp/bacon_backup' does not exist (may have been deleted already)")

'''
labex:project/ $ python3 manage_files.py
Created '/tmp/deleteme.txt'
Deleted '/tmp/deleteme.txt'
Deleted empty directory '/tmp/temp_dir'
Deleted directory '/tmp/bacon_backup' and all its contents
'''