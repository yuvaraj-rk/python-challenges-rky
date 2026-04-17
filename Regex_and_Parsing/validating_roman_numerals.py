#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

#thousand = 'M{0,3}'
#hundred = '(C[MD]|D?C{0,3})'
#ten = '(X[CL]|L?X{0,3})'
#digit = '(I[VX]|V?I{0,3})'

regex_pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))
