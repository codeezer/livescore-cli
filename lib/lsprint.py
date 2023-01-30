#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import defaultdict
from . import lscolors as c
import os, sys


def send_notification(text, title=''):
    icon = '~/.livescore-cli/assets/logo.png'
    if sys.platform.startswith('linux'):
        shell_cmd = f'notify-send -i {icon} "{title}" "{text}"'
    elif sys.platform == 'darwin':
        shell_cmd = f"""osascript -e 'display notification "{text}" with title "{title}"'"""
    else:
        raise OSError('OS Not Supported.')
    os.system(shell_cmd + ' > /dev/null 2>&1')
    return


def clear_screen():
    os.system('clear') # if unix


def print_pattern(c2p, n, color):
    for _ in range(n):
        print(color + c2p, end="")
    print(c.RESET)


def get_lmaxd(ld: list) -> dict:
    res = defaultdict(int)
    for d in ld:
        for k, v in d.items():
            l = len(str(v))
            if l > res[k]:
                res[k] = l
    res.pop('match_details_url')
    return res


def get_lmaxl(ld):
    res = [0] * len(ld[0])
    i = 0
    for e1 in ld:
        for i, e2 in enumerate(e1):
            res[i] = max(res[i], len(e2))
    return res


def get_match_line(match, lmaxd, c):
    match_line = ['{c.STATUS}', 'date', '', 'match_status', 
    '{c.HOME}', 'home_team', '{c.SCORE}', 'home_score', '-', 'away_score', '{c.AWAY}', 'away_team', '{c.RESET}']
    
    line = ''
    
    if match.get('home_score') > match.get('away_score'):
        c.HOME = c.WIN
        c.AWAY = c.LOSE
    
    elif match.get('home_score') < match.get('away_score'):
        c.HOME = c.LOSE
        c.AWAY = c.WIN
    else:
        c.HOME = c.AWAY = c.DRAW
    
    for element in match_line:
        temp = str(match.get(element) if element in match.keys() else element)
        temp = ''.join(temp.ljust(lmaxd.get(element))) if lmaxd.get(element) else temp
        line += temp
        line += ' '
    line.strip()
    line = eval(f'f"{line}"')
    return line


def send_alert(prev, curr):
    if prev:
        pms = prev.get('match_status')
        phts, pats = prev.get('home_score'), prev.get('away_score')
        cms = curr.get("match_status") 
        cht, chts = curr.get("home_team"), curr.get("home_score")
        cat, cats = curr.get("away_team"), curr.get("away_score")

        mtext = f'{cms}  {cht} {chts} - {cats} {cat}'

        if (phts != chts or pats != cats):
            send_notification(mtext, "GOAL!")
        
        if (pms != "1'" and cms == "1'"):
            send_notification(mtext, "Match Started!")
        
        if (pms != "FT" and cms == "FT"):
            send_notification(mtext, "Match Ended!")


def display_games(games, title='No Title', prev_data=None):
    title = f'{title} SCORES'
    matches = [match for match_day in games.values() for match in match_day]
    lmax_dict = get_lmaxd(matches)
    lmax_dict['date'] = max([len(k) for k in games.keys()])
    lmax = sum(lmax_dict.values())
    
    print_pattern('-', lmax+14, c.RESET)
    print(title.center(lmax+14))
    print_pattern('-', lmax+14, c.RESET)

    for i, (day, match_day) in enumerate(games.items()):
        prev_matchday = prev_data.get(day) if prev_data else None
        
        for j, match in enumerate(match_day):
            prev_match = prev_matchday[j] if prev_matchday else None
            send_alert(prev_match, match)
            match['date'] = day
            c.STATUS = c.STATS[i%len(c.STATS)]
            line = get_match_line(match, lmax_dict, c)
            match.pop('date')
            print(line)
    
    print_pattern('-', lmax+14, c.RESET)
    print_pattern('-', lmax+14, c.RESET)


def display_table(table, title='No Title'):
    title = f'{title} TABLE'
    lmax_list = get_lmaxl(table)
    lmax_list.pop(1)
    lmax = sum(lmax_list) + (len(lmax_list)-1) * 3 + 2

    head_map = {
        'LP': 'League Position',
        'GP': 'Games Played',
        'W': 'Win',
        'D': 'Draw',
        'L': 'Lose',
        'GF': 'Goals For',
        'GA': 'Goals Against',
        'GD': 'Goal Difference',
        'Pts': 'Points'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    }

    prom = {p for p in [e[1] for e in table] if p}
    prom_map = {}
    k = 0
    for p in prom:
        if p == 'Champions League':
            prom_map[p] = c.GREEN
        elif p == 'Relegation':
            prom_map[p] = c.RED
        else:
            prom_map[p] = c.STATS[k]
            k += 1

    print_pattern('+', lmax, c.BLUE)
    print(title.center(lmax))
    print_pattern('+', lmax, c.BLUE)

    line = ''
    for i, row in enumerate(table):
        if i == 1:
            print_pattern('-', lmax, c.RESET)
        prom = row.pop(1)
        color = prom_map.get(prom) if prom else c.RESET
        line = f' {"   ".join([e.ljust(lmax_list[j]) for j, e in enumerate(row)])}'
        print(color + line)

    print_pattern('+', lmax, c.BLUE)

    tlen = 0
    text = ''
    for k, v in head_map.items():
        temp = f' {k} = {v}   '
        if tlen + len(temp) > lmax:
            text += '\n'
            tlen = 0
        text += temp
        tlen += len(temp)
    print(text)

    print_pattern('-', lmax, c.RESET)

    tlen = 0
    text = ''
    for k, v in prom_map.items():
        temp = f' {v}{k}' + c.RESET
        if tlen + len(temp) > lmax:
            text += '\n'
            tlen = 0
        text += f'{temp}\t'
        tlen += len(temp)
    print(text)
    print_pattern('+', lmax, c.BLUE)
