#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, argparse
from lib import cli, URL
from lib import lscolors as c
from lib import lsprint, lsprocess
from lib import lsweb
import time


def main():
    bTable = bool(cli.args.table)
    bScore = bool(cli.args.score)
    bScorers = bool(cli.args.scorers)
    bNews = bool(cli.args.news)

    if not bTable and not bScore and not bScorers:
        bScore = True
    
    while True:
        try:   
            os.system('clear')
            for k in cli.args.League:
            	
                #Code to fetch data from URL[k]
                url = URL.URL[k][1] 
                pingTest = 'www.livescore.com'
                print(' ... Fetching scores from '+pingTest+' ... ')
                if lsweb.is_connected(pingTest) == True:

                    if bTable:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
                        lsprint.table(lsweb.get_table(URL.URL[k][1]),k)
                

                    if bScore:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        lsprint.scores(lsweb.get_score(URL.URL[k][1]),k)

                    if bScorers:
                        print("Displaying Top Scorers for {}".format(URL.URL[k][0]))
                        print('Working on it')
                
                else:
                    print(c.fill[2]+"Check Your Internet Connection , It looks like you're out of internet.:)"+c.END)
                
                time.sleep(3)
            
            bTable = False
            bScorers = False 
            if not bool(bScore):
                break
            time.sleep(25)
            
        except KeyboardInterrupt:
            break

        except:
            lsnews.print_news(lsnews.get_news())
    
           
if __name__ == '__main__':
    main()
