#https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

'''
(.*[A-Z]){2,}
.* matches any character (except for a newline).
[A-Z] matches a single character present in the range between A and Z (case sensitive).

(.*[0-9]){3,}
.* matches any character (except for a newline).
[0-9] matches a single character present in the range between 0 and 9 (case sensitive)

.*(.).*\1+.*
.* matches any character (except for a newline).
\1+ matches the same text as the most recently matched by the 1st capturing group.
'''

from collections import Counter
import re

regex=r"^[a-z0-9]{10}$"

def is_valid_uid(uid):
    is_valid = "Invalid"
    m=re.match(regex, uid, re.I)

    if m:
        count=Counter(uid)
        upper=re.search(r"(.*[A-Z]){2,}", uid)
        digits=re.search(r"(.*[0-9]){3,}", uid)

        if upper and digits and len(count.items()) == 10:
            is_valid = "Valid"
    return is_valid

for _ in range(int(input())):
    uid = input()
    print(is_valid_uid(uid))
