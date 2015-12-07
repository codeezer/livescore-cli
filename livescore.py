#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests, re, os, argparse
import lscolors as c
import time,lsprint,lsprocess


#function which returns boolean true if the ping test results positive false if negative test
def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False

#main webscrapping code which take the url to scrap and returns the rows of data
def get_livescore(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    _rows = soup.find_all(class_='row-gray')
    return _rows


def main():
    
    url = 'http://www.livescore.com/soccer/england/premier-league/'
    pingTest = 'livescore.com'
    
    while True:
        try:
            if check_ping(pingTest) == True:
                os.system('clear')
                print(' ... Fetching scores from http://www.livescore.com ... ')
                rows = get_livescore(url)
                
                #prettifying array to readable form and print the array with nice view
                lsprint.scores(lsprocess.pretty_array(rows,'scores'))
                lsprint.table(lsprocess.pretty_array(rows,'table'))

            else:
                print("Check Your Internet Connection , It looks like you're out of internet.")

            time.sleep(15)
        
        except KeyboardInterrupt:
            break

        except:
            print('Unexpected Error')
            
if __name__ == '__main__':
    main()
