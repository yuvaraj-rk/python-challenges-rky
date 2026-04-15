#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
#https://www.dataquest.io/cheat-sheet/regular-expressions-cheat-sheet/

import re

m=re.findall(r'(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])', input(), re.I)

if m:
    print(*m, sep="\n")
else:
    print(-1)
