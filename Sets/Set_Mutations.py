#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

a = input()
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation = input().split()[0]
    O = set(map(int, input().split()))
    
    if operation == "update":
        A.update(O)
    elif operation == "intersection_update":
        A.intersection_update(O)
    elif operation == "difference_update":
        A.difference_update(O)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(O)
    else:
        pass

print(sum(A))
