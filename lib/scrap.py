import requests
from bs4 import BeautifulSoup
import URL
import pprint

def extractTag(tree, tag, cssClass):
    return [t.extract() for t in tree.findAll(tag, class_=cssClass)]



def parseTree(subtree):
    subtree = [t for t in subtree if t!=' ']
    for i in range(len(subtree)):
        name = getattr(subtree[i], "name", None)
        if name is not None:
            subtree[i] = parseTree(subtree[i])
    subtree = [t for t in subtree if t!=' ' and t!='' and t!=None and t!=[]]
    if len(subtree)==1: subtree = subtree[0]
    return subtree
'''
#Request html from the site using http get
response = requests.get(URL.URL['bpl'][1])

#Parse the response text using html parser and BeautifulSoup library
soup = BeautifulSoup(response.text, 'html.parser')

#Select only the require content subtree from the website
[content] = soup.select('body > div.wrapper > div.content')
#Extract the table part into table variable
#The extracted part is removed from the original content.
#So the content now only contains the score
table = extractTag(content, 'div','ltable')
#Remove the some not required tags
extractTag(content, 'div', 'cal-wrap')
extractTag(content, 'div', 'star')
extractTag(content, 'div', 'row mt4 bb bt')
extractTag(content, 'div', 'cal clear')

table = parseTree(table)
print(table)
print("\n\n\n")
score = parseTree(content)
score[0] = score[0][1]
score = score[:-1]
print(score)
'''
