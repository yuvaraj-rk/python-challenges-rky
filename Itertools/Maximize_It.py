#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

k, m = map(int, input().split())

# Read each list, skipping the first element (which is the size Ni)
lists = []
for _ in range(k):
    # We take the elements from index 1 onwards
    row = list(map(int, input().split()))[1:]
    lists.append(row)

max_s = 0

# itertools.product generates all possible tuples (x1, x2, ..., xk)
# where xi is from the i-th list
for combination in product(*lists):
    # Calculate S = (x1^2 + x2^2 + ... + xk^2) % M
    current_sum = sum(x**2 for x in combination) % m
    
    # Keep track of the maximum value found
    if current_sum > max_s:
        max_s = current_sum
        
print(max_s)
