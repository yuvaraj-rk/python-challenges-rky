#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3

def fibonacci(n):
    fib = []
    for i in range(n):
        if i <= 1:
            fib.append(i)
        else:
            fib.append(fib[i-2]+fib[i-1])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
