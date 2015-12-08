#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, re, os, argparse
import lscolors as c
import time,lsprint,lsprocess
import lsweb #containing functions for webaccess :pingtest :geturl 

def main():
    
    url = 'http://www.livescore.com/soccer/england/premier-league/'
    pingTest = 'livescore.com'
    url_scorer = 'http://www.bbc.com/sport/football/premier-league/top-scorers'
    while True:
        try:
            if lsweb.check_ping(pingTest) == True:
                os.system('clear')
                print(' ... Fetching scores from http://www.livescore.com ... ')
                rows = lsweb.get_livescore(url,'row-gray')
                scorer_rows = lsweb.get_livescore(url_scorer,'competition-top-scorers-list')

                #prettifying array to readable form and print the array with nice view
                lsprint.scores(lsprocess.pretty_array(rows,'scores'))
                lsprint.table(lsprocess.pretty_array(rows,'table'))
                lsprint.scorers(lsprocess.pretty_array(scorer_rows,'scorers'))

            else:
                print("Check Your Internet Connection , It looks like you're out of internet.")

            time.sleep(15)
        
        except KeyboardInterrupt:
            break

        except:
            print('Unexpected Error')
            
if __name__ == '__main__':
    main()
