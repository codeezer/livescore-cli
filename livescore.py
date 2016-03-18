#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, re, os, argparse
from lib import lscolors as c
from lib import cli
from lib import URL
from lib import lsprocess
from lib import lsprint
from lib import lsweb
from lib import lsnews

import time,json

def main():
    bTable = bool(cli.args.table)
    bScore = bool(cli.args.score)
    bScorers = bool(cli.args.scorers)
    bNews = bool(cli.args.news)

    if not bTable and not bScore and not bScorers and not bNews:
        bScore = True
    
    while True:
        try:   
            os.system('clear')
            print(' ... Fetching scores from http://www.livescore.com ... ')
            for k in cli.args.League:
            	
                #Code to fetch data from URL[k]
                url = URL.URL[k][1] 
                pingTest = 'www.livescore.com'
                url_scorer = URL.URL[k][2]
                if lsweb.is_connected(pingTest) == True:
                    #rows = lsweb.get_livescore(url,'row-gray')
    
                    if bTable:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
                        #print(lsprocess.pretty_array(rows,'table'))
                        lsprint.table(lsweb.get_table(URL.URL[k][1]),k)

                
                    if bNews:
                        #print("Displaying Few News from Goal.com")
                        lsnews.print_news(lsnews.get_news())

                    if bScore:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        #lsprint.scores(lsprocess.pretty_array(rows,'scores'),k)
                        lsprint.scores1(lsweb.get_score(URL.URL[k][1]),k)

                    if bScorers:
                        print("Displaying Top Scorers for {}".format(URL.URL[k][0]))
                        scorer_rows = lsweb.get_livescore(url_scorer,'competition-top-scorers-list')
                        lsprint.scorers(lsprocess.pretty_array(scorer_rows,'scorers'),k)
#            bTable = False
#            bScorers = False
#                else:
#                    print(c.RED+"Check Your Internet Connection , It looks like you're out of internet."+c.END)
#                time.sleep(3)
            bTable = False
            bScorers = False 
            bNews = False
            if not bool(bScore):
                break
            time.sleep(25)
            
        except KeyboardInterrupt:
            break
    
#        except:
 #           print('Unexpected Error')
  #          time.sleep(4)
     
    

           
if __name__ == '__main__':
    main()
