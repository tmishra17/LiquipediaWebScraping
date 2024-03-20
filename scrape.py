from bs4 import BeautifulSoup
import requests as rq
import numpy as np 
import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules 

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

# soup = BeautifulSoup(html_doc, 'lxml')

response = rq.get("https://liquipedia.net/smash/Major_Tournaments/Melee")


liqHTML = response.text

soup = BeautifulSoup(liqHTML, 'lxml')
yearCol = []
charCol = []

# print(f"HTML from Liquidpedia:\n{liqHTML}\n")
'''
for link in soup.find_all('a'):
    print(link)
'''
rowlist = soup.find_all("div", class_="divRow")
print(len(rowlist))
aRow = rowlist[11]
print(type(aRow))
winnerElem = aRow.find("div", class_="divCell Placement FirstPlace")
print(type(winnerElem))
charList = winnerElem.find_all("span", class_="heads-padding-right")
print(len(charList))
winChar = charList[0]
imgChar = winChar.find("img")
print(imgChar.get("alt"))

print("test done")
yearList = soup.find_all("span", class_="mw-headline")[1:-1]
tableList = soup.find_all("div", class_="divTable table-full-width tournament-card")[1:-1]
print(f"Year List: {len(yearList)}")
print(f"Table List: {len(tableList)}\n")

for i in range(0, len(yearList)):
    year = yearList[i].text
    table = tableList[i]
    for aRow in table.find_all("div", class_="divRow"):
        winnerElem = aRow.find("div", class_="divCell Placement FirstPlace")
        charList = winnerElem.find_all("span", class_="heads-padding-right")
        if len(charList) == 1:
            winChar = charList[0]
            imgChar = winChar.find("img")
            charText = imgChar.get("alt")
            yearCol.append(year)
            charCol.append(charText)

print(len(yearCol))
print(len(charCol))
liqDict = {"tournament year": yearCol, "winning character": charCol}
liqDf = pd.DataFrame(liqDict)
liqDf = liqDf.set_index("tournament year")
liqDf.to_csv("liqwinners.csv")
print("done")