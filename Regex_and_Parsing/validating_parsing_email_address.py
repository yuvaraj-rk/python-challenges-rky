#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import re
import email.utils

regex = r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,100}@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

def is_valid_email_address(email_addr):
    m = re.match(regex, email_addr)    
    if m:
        return True
    else:
        return False

for _ in range(int(input())):
    e_addr = email.utils.parseaddr(input())
    if is_valid_email_address(e_addr[1]):
        print(email.utils.formataddr(e_addr))
