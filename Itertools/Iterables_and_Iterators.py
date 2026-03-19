#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

N = input()
chars = input().split()
string = "".join(chars)
K = int(input())

letters_combintation = list(combinations(string, K))
total_combinations = len(letters_combintation)

count_of_a = 0
for t in letters_combintation:
    if 'a' in t:
        count_of_a += 1

print(count_of_a/total_combinations)
