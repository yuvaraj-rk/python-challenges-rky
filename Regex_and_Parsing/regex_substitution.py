#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true

import re

def operator_2_text(matched_text):
    string = matched_text.group(1)
   
    if string == "&&":
        return "and"
    else:
        return "or"

text = "\n".join([input() for _ in range(int(input()))])
regex = r'(?<= )(&&|\|\|)(?= )'

sub_text = re.sub(regex, operator_2_text, text)
print(sub_text)
