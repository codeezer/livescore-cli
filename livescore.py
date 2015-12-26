#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, re, os, argparse
import lscolors as c
import time,lsprint,lsprocess
import lsweb #containing functions for webaccess :pingtest :geturl 
import URL #Contains the urls to fetch data
import cli #Contains our command line interface code

def main():
    while True:
        try:   
            os.system('clear')
            print(' ... Fetching scores from http://www.livescore.com ... ')
 
            for k in cli.args.League:
            	
                #Code to fetch data from URL[k]
                url = URL.URL[k][1] 
                pingTest = 'livescore.com'
                url_scorer = URL.URL[k][2]
                if lsweb.check_ping(pingTest) == True:
                    rows = lsweb.get_livescore(url,'row-gray')
    
                    if cli.args.table:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
                        lsprint.table(lsprocess.pretty_array(rows,'table'),k)
                
#                   if cli.args.fixtures:
#                       print("Displaying Fixtures for {}".format(URL.URL[k][0]))
                
                    if cli.args.score:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        lsprint.scores(lsprocess.pretty_array(rows,'scores'),k)
    
                    if cli.args.scorers:
                        print("Displaying Top Scorers for {}".format(URL.URL[k][0]))
                        scorer_rows = lsweb.get_livescore(url_scorer,'competition-top-scorers-list')
                        lsprint.scorers(lsprocess.pretty_array(scorer_rows,'scorers'),k)
    
                else:
                    print("Check Your Internet Connection , It looks like you're out of internet.")
                time.sleep(3)
        
            time.sleep(25)
            
        except KeyboardInterrupt:
            break
    
    #except :
     #   print('Unexpected Error')
     
    

           
if __name__ == '__main__':
    main()
