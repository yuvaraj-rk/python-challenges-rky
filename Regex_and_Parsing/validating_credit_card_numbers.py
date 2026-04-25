#https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

import re

card_regex = re.compile(r'''(
    ^([456]\d{3})-?
    ((\d{4})-?){2}
    \d{4}$
    )''', re.VERBOSE)

repeat_digits= r'(\d)\1{3,}'

def is_credit_card_number_valid(card_num):

    m=card_regex.match(card_num)
    if m:
        card_num = card_num.replace('-', '')
        rd=re.search(repeat_digits, card_num)
        if rd:
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

for _ in range(int(input())):
    card_num = input()
    print(is_credit_card_number_valid(card_num))
