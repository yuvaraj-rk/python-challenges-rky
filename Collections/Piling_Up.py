#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

from collections import deque

def is_cube_stacking_possible(n, blocks):
    possible = True
    last_picked = float('inf')
    current = 0
    
    while blocks:        
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()
        
        if current > last_picked:
            possible = False
            break
        last_picked = current

    return "Yes" if possible else "No"

T=int(input())
for i in range(T):
    n = int(input())
    blocks = deque(list(map(int, input().split())))
    print(is_cube_stacking_possible(n, blocks))
