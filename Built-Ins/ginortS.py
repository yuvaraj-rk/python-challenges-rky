#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

string = input()

def sort_by_custom_rules(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        if int(c) % 2 != 0:
            return (2, c)
        else:
            return (3, c)

# Sort using the custom key and join the result back into a string
print("".join(sorted(string, key=sort_by_custom_rules)))
