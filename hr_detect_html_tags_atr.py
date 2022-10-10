'''detect html tags, attributes and attributes values'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", Attribute2[0], ">", Attribute2[1])

