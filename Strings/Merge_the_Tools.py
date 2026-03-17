#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    u=""
    ucount=0
    for s in string:     
        if s not in u:
            u=f"{u}{s}"
        ucount+=1
        if ucount == k:
            print(u)
            ucount=0
            u=""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
