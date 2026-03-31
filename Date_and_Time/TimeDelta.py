#https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true

#!/bin/python3
import os
import datetime as dt

def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = dt.datetime.strptime(t1, date_format)
    dt2 = dt.datetime.strptime(t2, date_format)
    
    t_delta = abs(dt1-dt2)
    t_delta_sec = int(t_delta.total_seconds())
    return str(t_delta_sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
