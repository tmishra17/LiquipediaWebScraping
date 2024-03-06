from bs4 import BeautifulSoup
import requests as rq

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie<p id="nested tag"></p></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')

response = rq.get("https://liquipedia.net/smash/Major_Tournaments/Melee")


HTML = response.text

print(f"HTML from Liquidpedia:\n{HTML}\n")

for link in soup.find_all('a'):
    print(link)

