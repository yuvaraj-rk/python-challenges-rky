#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

import re

def isValid(string):
    invalid_patterns = "[\*\+\?\)\(\{\}]{2,}"
    re_search_obj = re.compile(invalid_patterns)
    result = re_search_obj.search(string)
    return result is None

for _ in range(int(input())):
    str_regex = input()
    try:        
        print(isValid(str_regex))
    except:
        print(False)
