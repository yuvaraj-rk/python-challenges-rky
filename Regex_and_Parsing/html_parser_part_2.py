#https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        comments = data.split("\n")
        if data == "\n" or data is None:
            return
        if len(comments) > 1:
            print(">>> Multi-line Comment")
            print(*comments, sep="\n")
        else:
            print(">>> Single-line Comment")
            print(*comments)

    def handle_data(self, data):
        if data != "\n":
            print(f">>> Data\n{data}")  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
