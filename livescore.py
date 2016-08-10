#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, time
from lib import lscolors as c
from lib import cli
from lib import URL
from lib import lsprint
from lib import lsweb
from lib import lsnews


def main():
    bTable = bool(cli.args.table)
    bScore = bool(cli.args.score)
    bScorers = bool(cli.args.scorers)

    if not bTable and not bScore and not bScorers and not bNews:
        bScore = True

    while True:
        try:
            os.system('clear')
            for k in cli.args.League:
                # Code to fetch data from URL[k]
                pingTest = 'www.google.com'
                print(' ... Fetching information from www.livescore.com'+' ... ')
                if lsweb.is_connected(pingTest) is True:

                    if bTable:
                        print("Displaying Table for {}".format(URL.URL[k][0]))
                        lsprint.table(lsweb.get_table(URL.URL[k][1]), k)

                    if bScore:
                        print("Displaying Scores for {}".format(URL.URL[k][0]))
                        lsprint.scores(lsweb.get_score(URL.URL[k][1]), k)


                    if bScorers:
                        print("Displaying Top Scorers for"
                              " {}".format(URL.URL[k][0]))
                        print('Working on it')

                else:
                    print(c.fill[3]+"Check Your Internet Connection ,"
                          " It looks like you're out of internet."+c.END)


                time.sleep(3)

            bTable = False
            bScorers = False
            if not bool(bScore):
                break
            time.sleep(7)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
