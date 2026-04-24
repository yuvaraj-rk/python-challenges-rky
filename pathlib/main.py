from pathlib import Path

# Join path components using the / operator
my_path = Path('usr') / 'bin' / 'spam'
print(my_path)

# Get the current working directory
cwd = Path.cwd()
print(cwd)

# Define the path for the new nested directories
new_dirs = cwd / 'delicious' / 'walnut' / 'waffles'

# Create the directories, including any missing parents
new_dirs.mkdir(parents=True, exist_ok=True)

print(f"Successfully created: {new_dirs}")

'''
labex:project/ $ python3 main.py
usr/bin/spam
/home/labex/project
Successfully created: /home/labex/project/delicious/walnut/waffles
labex:project/ $ tree
.
├── delicious
│   └── walnut
│       └── waffles
├── main.py
├── manage_files.py
└── setup.py

3 directories, 3 files
labex:project/ $ ls -R delicious 
delicious:
walnut

delicious/walnut:
waffles

delicious/walnut/waffles:
'''