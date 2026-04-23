#https://labex.io/labs/python-python-json-and-yaml-633659?course=python-cheatsheet

# Read YAML file using ruamel.yaml library
from ruamel.yaml import YAML

with open("config.yaml") as f:
    yaml=YAML()  # Create YAML parser instance
    data = yaml.load(f)  # Parse YAML and return Python dict/list
    print(data)

'''
labex:project/ $ pip install ruamel.yaml
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple
Collecting ruamel.yaml
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/b8/0c/51f6841f1d84f404f92463fc2b1ba0da357ca1e3db6b7fbda26956c3b82a/ruamel_yaml-0.19.1-py3-none-any.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.1/118.1 kB 48.2 MB/s eta 0:00:00
Installing collected packages: ruamel.yaml
Successfully installed ruamel.yaml-0.19.1

[notice] A new release of pip is available: 24.1.2 -> 26.0.1
[notice] To update, run: python3 -m pip install --upgrade pip
labex:project/ $ python3 yaml_handler.py
{'user': {'name': 'Alex', 'email': 'alex@example.com'}}
labex:project/ $ cat config.yaml 
user:
  name: Alex
  email: alex@example.com
'''