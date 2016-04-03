#!/usr/bin/env python3
# -*- coding:utf-8 -*-

<<<<<<< HEAD
import os, argparse
from lib import cli, URL
=======
import os
>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984
from lib import lscolors as c
from lib import lsprint, lsprocess
from lib import lsweb
import time

<<<<<<< HEAD
=======
import time

>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984

def main():
    bTable = bool(cli.args.table)
    bScore = bool(cli.args.score)
    bScorers = bool(cli.args.scorers)

    if not bTable and not bScore and not bScorers:
        bScore = True

    while True:
        try:
            os.system('clear')
            for k in cli.args.League:
                # Code to fetch data from URL[k]
                pingTest = 'www.livescore.com'
                print(' ... Fetching scores from '+pingTest+' ... ')
                if lsweb.is_connected(pingTest) is True:

                    if bTable:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
<<<<<<< HEAD
                        lsprint.table(lsweb.get_table(URL.URL[k][1]),k)
                
=======
                        lsprint.table(lsweb.get_table(URL.URL[k][1]), k)

                    if bNews:
                        lsnews.print_news(lsnews.get_news())

>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984
                    if bScore:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        lsprint.scores(lsweb.get_score(URL.URL[k][1]), k)

                    if bScorers:
                        print("Displaying Top Scorers for"
                              " {}".format(URL.URL[k][0]))
                        print('Working on it')

                else:
<<<<<<< HEAD
                    print(c.fill[2]+"Check Your Internet Connection , It looks like you're out of internet.:)"+c.END)
                
=======
                    print(c.RED+"Check Your Internet Connection ,"
                          " It looks like you're out of internet."+c.END)

>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984
                time.sleep(3)

            bTable = False
<<<<<<< HEAD
            bScorers = False 
=======
            bScorers = False
            bNews = False
>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984
            if not bool(bScore):
                break
            time.sleep(25)

        except KeyboardInterrupt:
            break

<<<<<<< HEAD
        except:
            lsnews.print_news(lsnews.get_news())
    
           
=======
>>>>>>> f4bb32101262b34d240ba4106e3ed54fa21b6984
if __name__ == '__main__':
    main()
