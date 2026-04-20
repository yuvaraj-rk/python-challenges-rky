#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re

regex = r'(#[A-Fa-f0-9]{3}|#[A-Fa-f0-9]{6})[;,)]'

for _ in range(int(input())):
    string = input()
    m = re.findall(regex, string)
    if m:
        print(*m, sep="\n")
