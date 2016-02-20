from bs4 import BeautifulSoup
import requests, re, os
import socket
#function which returns boolean true if the ping test results positive false if negative test
def check_ping(hostname):
    response = os.system("echo off>ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False

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
    _rows = soup.find_all(class_=scrapping_class)
    return _rows

def get_dates(url,date_class):
    raw = get_livescore(url,date_class)
    dates = '\n'.join(map(lambda r: r.text, raw))
    array_dates = re.split('\n',dates)
    return array_dates

