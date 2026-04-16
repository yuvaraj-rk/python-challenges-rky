#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

S = input()
k = input()

match_sets = set()
match_found = False

for i in range(len(S)):
    m = re.search(k, S[i:])
    if m:
        match_index = f"({m.start()+i}, {m.end()+i-1})"
        match_found = True
        if match_index not in match_sets:
            match_sets.add(match_index)
            print(match_index)

if match_found is False:
    print("(-1, -1)")
