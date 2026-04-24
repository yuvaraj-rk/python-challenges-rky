#https://labex.io/labs/python-python-file-and-directory-path-manipulation-633657?course=python-cheatsheet

from pathlib import Path

# List contents of a directory
print("Contents of '/usr/bin':")
count = 0
for f in Path('/usr/bin').iterdir():
    if count < 5: # Print first 5 items to keep output short
        print(f)
        count += 1
    else:
        break

total_size = 0
directory = Path('/usr/bin')

for sub_path in directory.iterdir():
    if sub_path.is_file(): # Ensure we only add size of files
        total_size += sub_path.stat().st_size

print(f"Total size of files in '{directory}': {total_size} bytes")

p = Path('/tmp/delicious')
print(f"Walking directory tree for: {p}")

for i in p.rglob('*'):
    print(i)


'''
labex:project/ $ mkdir -p /tmp/delicious/cats /tmp/delicious/walnut/waffles
touch /tmp/delicious/spam.txt /tmp/delicious/cats/catnames.txt /tmp/delicious/walnut/waffles/butter.txt
labex:project/ $ python3 main.py                                           
Contents of '/usr/bin':
/usr/bin/[
/usr/bin/addpart
/usr/bin/apt
/usr/bin/apt-cache
/usr/bin/apt-cdrom
Total size of files in '/usr/bin': 909252383 bytes
Walking directory tree for: /tmp/delicious
/tmp/delicious/spam.txt
/tmp/delicious/eggs2.txt
/tmp/delicious/cats
/tmp/delicious/walnut
/tmp/delicious/cats/catnames.txt
/tmp/delicious/walnut/waffles
/tmp/delicious/walnut/waffles/butter.txt
'''