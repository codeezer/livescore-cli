#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from lib import lscolors as c
from lib import cli
from lib.URL import URL
from lib import lsprint
from lib import lsweb


def main():
    b_table = cli.args.table
    b_score = cli.args.score
    b_scorers = cli.args.scorers

    # by default display match scores
    if not b_table and not b_score and not b_scorers:
        b_score = True

    leagues = [lsprint.League(k) for k in cli.args.League]

    while True:
        try:
            os.system('clear')
            for league in leagues:
                # Code to fetch data from URL[k]
                ping_test = 'www.google.com'
                print(' ... Fetching information from www.livescore.com ... ')
                if lsweb.is_connected(ping_test):
                    if b_table:
                        print("Displaying Table for {}".format(URL[league.key][1]))
                        league.display_table(lsweb.get_table(URL[league.key][1]))

                    if b_score:
                        print("Displaying Scores for {}".format(URL[league.key][1]))
                        league.display_scores(lsweb.get_score(URL[league.key][1]))

                    if b_scorers:
                        print("Displaying Top Scorers for"
                              " {}".format(URL[league.key][1]))
                        print('Working on it')

                else:
                    print(c.fill[3] + "Check Your Internet Connection ,"
                          " It looks like you're out of internet." + c.END)

                time.sleep(3)

            b_table = False
            b_scorers = False
            if not b_score:
                break
            time.sleep(7)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
