#https://labex.io/labs/python-python-json-and-yaml-633659?course=python-cheatsheet

# anyconfig: load configuration files in various formats (JSON, YAML, TOML, etc.)
import anyconfig

# anyconfig.load() auto-detects the file format based on the extension.
#Read YAML file
conf = anyconfig.load("/home/labex/project/config.yaml")
print(conf)

#Read JSON file
json_file = anyconfig.load("/home/labex/project/data.json")
print(json_file)

'''
labex:project/ $ pip install anyconfig
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple
Collecting anyconfig
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/56/f7/72353359c7e92f4fc1c832cca68e83e8d5b08c94c738194f3ea415f050cd/anyconfig-0.15.1-py3-none-any.whl (106 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 107.0/107.0 kB 23.4 MB/s eta 0:00:00
Installing collected packages: anyconfig
Successfully installed anyconfig-0.15.1

[notice] A new release of pip is available: 24.1.2 -> 26.0.1
[notice] To update, run: python3 -m pip install --upgrade pip
labex:project/ $ python3 anyconfig_handler.py
{'user': {'name': 'Alex', 'email': 'alex@example.com'}}
{'username': 'labex', 'id': 12345}
'''