#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

N, nums = input(), input().split()
print(all(int(num) > 0 for num in nums) and any(num == num[::-1] for num in nums))
