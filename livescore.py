#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lib.lsweb import get_games, get_table, is_connected
from lib.lsprint import display_games, display_table, clear_screen
from lib.cli import args
from lib.urls import details, base_url
import time


def main_event(b_score, b_table):
    
    event_type = 'competition'
    prev_data = {}
    while True:
        try:
            cname = args.competition[0]
            if is_connected('www.livescores.com'):
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
            
            else:
                print(f"couldn't connect to the livescore website. check your internet connection.")
        
            time.sleep(2)
        
            if (not b_score):
                break

        except KeyboardInterrupt:
            break


def main():
    b_score = bool(args.score)
    b_table = bool(args.table)
    main_event(b_score, b_table)


if __name__ == '__main__':
    main()
