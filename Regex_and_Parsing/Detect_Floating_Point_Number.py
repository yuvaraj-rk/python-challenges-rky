#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re

float_match_expr = "^[+-]{0,1}[0-9]*.[0-9]+$"

def isFloatingPointNumber(string):
    matched_string = re.search(float_match_expr, string)
    try:
        _ = float(string)
        return matched_string is not None

    except Exception:
        return False

for _ in range(int(input())):
    print(isFloatingPointNumber(input()))
