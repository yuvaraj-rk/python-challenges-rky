#https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true

import re
from html.parser import HTMLParser

html = "\n".join([input() for _ in range(int(input()))])

html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:            
            for key, value in attrs:
                print(f"-> {key} > {value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        pass
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for key, value in attrs:
                print(f"-> {key} > {value}")

parser = MyHTMLParser()
parser.feed(html)
