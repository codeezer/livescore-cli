#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lib.lsweb import get_games, get_table, is_connected, get_scorers
from lib.lsprint import display_games, display_table, clear_screen
from lib.cli import args
from lib.urls import details, base_url
import time


def main():
    b_score = bool(args.score)
    b_table = bool(args.table)
    b_scorers = bool(args.scorers)

    prev_data = {}
    while True:
        try:
            for cname in args.competition:
                if is_connected('www.livescores.com') and is_connected('www.livescore.com'):
                    event_type = 'competition'
                    title = details.get(event_type).get(cname).get('title')
                    
                    if b_score:
                        games = get_games(cname, event_type)
                        if (games != prev_data):
                            print(f'displaying scores for {title}')
                            clear_screen()
                            display_games(games, title, prev_data)
                        prev_data = games
                    
                    if b_table:
                        table = get_table(cname, event_type)
                        print(f'displaying table for {title}')
                        clear_screen()
                        display_table(table, title)
                    if b_scorers:
                        scorers = get_scorers(cname, event_type)
                
                else:
                    print(f"couldn't connect to the livescore website. check your internet connection.")
            
            time.sleep(2)
        
            if (not b_score):
                break

        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
