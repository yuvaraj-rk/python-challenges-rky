#https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true

import operator

def to_int(func):
    return lambda x: int(func(x))

def person_lister(f):
    def inner(people):
        #1. Using operation.itemgetter method
        people.sort(key=to_int(operator.itemgetter(2)))
        
        #2. Using plain lambda function (not accepted for this problem's solution)
        #people.sort(lambda x: int(x[2]))
        
        for person in people:
            yield f(person)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
