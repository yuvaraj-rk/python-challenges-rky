#https://labex.io/labs/python-python-json-and-yaml-633659?course=python-cheatsheet

# Write JSON file: json.dump() writes Python object as JSON
import json

content = {"name": "Joe", "age": 20}
with open("output.json", "w") as f:  # Open file in write mode
    json.dump(content, f, indent=2)  # Write JSON with 2-space indentation

# Read JSON file: json.load() parses JSON from file object
with open("data.json", "r") as f:  # Open file in read mode
    content = json.load(f)  # Parse JSON and return Python dict/list
    print(content)

'''
labex:project/ $ python3 json_handler.py 
labex:project/ $ cat output.json 
{
  "name": "Joe",
  "age": 20
}                                                                                                                                                                                                                                                                                                                                                                                               
labex:project/ $ python3 json_handler.py
{'username': 'labex', 'id': 12345}
''' 