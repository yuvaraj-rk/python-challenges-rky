#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true

import re

def fun(s):
    regex_email_rules="^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    isEmailValid = re.search(regex_email_rules, s)
    return isEmailValid is not None
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
