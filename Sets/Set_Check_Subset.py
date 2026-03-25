#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

T = int(input())

for _ in range(T):
    count_A = int(input())
    A = set(input().split())
    _ = input()
    B = set(input().split())
    
    intersection_AB = A.intersection(B)
    
    print(len(intersection_AB) == count_A)
