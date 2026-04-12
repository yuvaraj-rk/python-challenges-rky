#https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

#def print_from_stream(n, stream=EvenStream()):
#    for _ in range(n):
#        print(stream.get_next())

#Debug and Fixed Method
#Mutable Default Arguments:
#In Python, default arguments are evaluated only once when the function is defined, not every time it is called.
#This means the EvenStream() object is created at definition time and shared across every subsequent call to print_from_stream(n)
def print_from_stream(n, stream=None):
    if stream is None:
        stream=EvenStream()

    for _ in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
