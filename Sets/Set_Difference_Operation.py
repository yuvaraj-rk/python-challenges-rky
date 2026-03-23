#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

a = input()
english = set(map(int, input().split()))

b = input()
french = set(map(int, input().split()))

print(len(english.difference(french)))
