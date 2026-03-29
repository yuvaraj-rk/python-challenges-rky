#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

T = int(input())

for _ in range(T):
    values = input().split()
    
    try:
        print(int(values[0])//int(values[1]))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
