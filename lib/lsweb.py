from bs4 import BeautifulSoup
import requests
import socket
import re


# function to test the internet connection if active or not
def is_connected(remote_server='www.google.com'):
    try:
        host = socket.gethostbyname(remote_server)
        socket.create_connection((host, 80), 2)
        return True
    except:
        return False

def extract_tag(tree, tag, css_class=None, css_id=None):
    if css_class:
        return [t.extract() for t in tree.findAll(tag, class_=css_class)]
    else:
        return [t.extract() for t in tree.findAll(tag, id=css_id)]

def extract_tag_without_class_or_id(tree, tag):
    return [t.extract() for t in tree.find_all() if (t.name == tag and not(t.has_attr('class') or t.has_attr('id')))]

def parse_tree(subtree):
    subtree = [t for t in subtree if t != ' ']
    for i in range(len(subtree)):
        name = getattr(subtree[i], "name", None)
        if name is not None:
            subtree[i] = parse_tree(subtree[i])
    subtree = [t
               for t in subtree
               if t != ' ' and t != '' and t is not None and t != []]
    if len(subtree) == 1:
        subtree = subtree[0]
    return subtree

def get_content_ts(url):
    response = requests.get(url)
    if not response.ok:
        return False
    # Parse the response text using html parser and BeautifulSoup library
    soup = BeautifulSoup(response.text, 'html.parser')    
    # Select only the require content subtree from the website
    ts = soup.find('div', id='match-rows__root')
    # extract unnecessary tags
    extract_tag(ts, 'div', css_class='FilterBar_filterBarWrapper__20Mg4')
    extract_tag_without_class_or_id(ts, 'span')
    return ts

def get_score(url):
    content = get_content_ts(url)
    if not content:
        return False
    # some not required tags
    extract_tag(content, 'div', css_id='league-table')
    score = parse_tree(content)
    return score

def get_table(url):
    content = get_content_ts(url)
    if not content:
        return False
    # The extracted table is removed from the original content.
    # So the content now only contains the score
    extract_tag(content, 'div', css_id=re.compile('.*league-header'))
    extract_tag(content, 'div', css_class=re.compile('.*tabs.*'))
    table = extract_tag(content, 'div', css_id='league-table')
    table = parse_tree(table)
    return table

# main webscrapping code which take the url to scrap and returns the rows of data
def get_livescore(url, scrapping_class):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    _rows = soup.findAll(class_=scrapping_class)
    return _rows
