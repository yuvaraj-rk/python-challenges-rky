#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

#For A to be strict superset of all other N sets:
#Logic using Sets Module: 
#1. Count of elements in Ni after Intersection operation between (Ni and A) should be same (i.e., All elements in Ni should be present in A)
#and
#2. Count(A)> Count(Ni)

is_A_SuperSet = True
A=set(input().split())

for _ in range(int(input())):
    Ni = set(input().split())
    count_Ni = len(Ni)
    count_intersection_Ni = len(Ni.intersection(A))
    if not(count_Ni == count_intersection_Ni and len(A) > count_Ni):
        is_A_SuperSet = False

print(is_A_SuperSet)
