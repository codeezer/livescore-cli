#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time
from lib import lscolors as c
from lib import cli
from lib.URL import URL
from lib import lsprint
from lib import lsprocess
from lib import lsweb
from datetime import datetime


def main():
    b_table = bool(cli.args.table)
    b_score = bool(cli.args.score)
    b_scorers = bool(cli.args.scorers)

    if not b_table and not b_score and not b_scorers:
        b_score = True

    while True:
        try:
            lsprocess.clear_screen()
            for k in cli.args.League:
                # Code to fetch data from URL[k]
                print('...Fetching information from www.livescores.com' + '...')
                
                if lsweb.is_connected() is True:
                    if b_table:
                        print("Displaying Table for {}".format(URL[k][0]))
                        lsprint.table(lsweb.get_table(URL[k][1]), k)

                    if b_score:
                        print("Displaying Scores for {}".format(URL[k][0]))
                        lsprint.scores(lsweb.get_score(URL[k][1]), k)

                    if b_scorers:
                        print("Displaying Top Scorers for"
                              " {}".format(URL[k][0]))
                        print('Working on it')

                else:
                    print(c.fill[3] + "Check Your Internet Connection ,"
                          " It looks like you're out of internet." + c.END)

                time.sleep(3)

            b_table = False
            b_scorers = False
            if not bool(b_score):
                break
            time.sleep(7)

        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    main()
