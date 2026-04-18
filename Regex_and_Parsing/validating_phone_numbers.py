#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import re

regex = r"^[789]{1,1}[0-9]{9,9}$"

def isValidMobileNumber(mobile_number):
    m = re.match(regex, mobile_number)
    if m:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    m_num = input()
    print(isValidMobileNumber(m_num))
