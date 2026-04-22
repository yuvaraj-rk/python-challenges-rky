#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

import re

html = '\n'.join(input() for _ in range(int(input())))

#remove comments
html=re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

regex_tags_attrs = r'<\s*(\w+)\s*([^>]*)>'
regex_attrs = r'([\w-]+)="([^"]*)"'

for tag, attribs in re.findall(regex_tags_attrs, html, re.DOTALL):
    print(tag)  
    for key, value in re.findall(regex_attrs, attribs, re.DOTALL):
        print(f"-> {key} > {value}")
