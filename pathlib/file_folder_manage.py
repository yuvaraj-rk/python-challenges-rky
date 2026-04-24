import shutil
from pathlib import Path

# Define source and destination
source_file = Path('/tmp/spam.txt')
destination_dir = Path('/tmp/delicious')

# Copy the file
shutil.copy(source_file, destination_dir)

print(f"Copied '{source_file}' to '{destination_dir}'")

# You can also rename the file while copying
shutil.copy('/tmp/eggs.txt', '/tmp/delicious/eggs2.txt')
print("Copied and renamed 'eggs.txt' to 'eggs2.txt'")

# Copy an entire directory tree
shutil.copytree('/tmp/bacon', '/tmp/bacon_backup')
print("Copied directory '/tmp/bacon' to '/tmp/bacon_backup'")

'''
labex:project/ $ python3 manage_files.py
Copied '/tmp/spam.txt' to '/tmp/delicious'
Copied and renamed 'eggs.txt' to 'eggs2.txt'
Copied directory '/tmp/bacon' to '/tmp/bacon_backup'
labex:project/ $ 
'''
