from bs4 import BeautifulSoup
import requests, re, os
import socket
import scrap

import errno    
import os


def create_directory(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

#function which returns boolean true if the ping test results positive false if negative test
def check_ping(hostname):
    response = os.system("echo off>ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False

#function to test the internet connection if active or not
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


#main webscrapping code which take the url to scrap and returns the rows of data
def get_livescore(url,scrapping_class):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    _rows = soup.findAll(class_=scrapping_class)
    return _rows


def get_content_ts(url):
    #Request html from the site using http get
    response = requests.get(url)
    #Parse the response text using html parser and BeautifulSoup library
    soup = BeautifulSoup(response.text, 'html.parser')
    #Select only the require content subtree from the website
    [content] = soup.select('body > div.wrapper > div.content')
    return content

def get_score(url):
    content = get_content_ts(url)
    
    #some not required tags
    scrap.extractTag(content, 'div', 'cal-wrap')
    scrap.extractTag(content, 'div', 'star')
    scrap.extractTag(content, 'div', 'row mt4 bb bt')
    scrap.extractTag(content, 'div', 'cal clear')
    
    score = scrap.parseTree(content)
    score[0] = score[0][1]
    score = score[:-1]
    return score

def get_table(url):
    content = get_content_ts(url)
    
    #Extract the table part into table variable
    #The extracted part is removed from the original content.
    #So the content now only contains the score
    table = scrap.extractTag(content, 'div','ltable')

    table = scrap.parseTree(table)
    return table


