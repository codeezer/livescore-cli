from bs4 import BeautifulSoup
import requests
import os
import socket


def extractTag(tree, tag, cssClass):
    return [t.extract() for t in tree.findAll(tag, class_=cssClass)]


def parseTree(subtree):
    subtree = [t for t in subtree if t != ' ']
    for i in range(len(subtree)):
        name = getattr(subtree[i], "name", None)
        if name is not None:
            subtree[i] = parseTree(subtree[i])
    subtree = [t
               for t in subtree
               if t != ' ' and t != '' and t is not None and t != []]
    if len(subtree) == 1:
        subtree = subtree[0]
    return subtree


def create_directory(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


# function to test the internet connection if active or not
def is_connected(REMOTE_SERVER):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(REMOTE_SERVER)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
        return False


def get_content_ts(url):
    # Request html from the site using http get
    response = requests.get(url)
    # Parse the response text using html parser and BeautifulSoup library
    soup = BeautifulSoup(response.text, 'html.parser')
    # Select only the require content subtree from the website
    [content] = soup.select('body > div.wrapper > div.content')
    return content


def get_score(url):
    content = get_content_ts(url)

    # some not required tags
    extractTag(content, 'div', 'cal-wrap')
    extractTag(content, 'div', 'star')
    extractTag(content, 'div', 'row mt4 bb bt')
    extractTag(content, 'div', 'cal clear')

    score = parseTree(content)
    score[0] = score[0][1]
    score = score[:-1]
    score.pop()
    return score


def get_table(url):
    content = get_content_ts(url)

    # The extracted table is removed from the original content.
    # So the content now only contains the score
    table = extractTag(content, 'div', 'ltable')

    table = parseTree(table)
    return table




#main webscrapping code which take the url to scrap and returns the rows of data
def get_livescore(url,scrapping_class):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    _rows = soup.findAll(class_=scrapping_class)
    return _rows
