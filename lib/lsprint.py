#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    modules containing all the layout configuration of printable data
    scores : function containing layout info of scores
    table : function containing layout info of table
"""

from . import lscolors as c
import os
from . import tt
from .URL import URL
from . import lsprocess
import sys


def send_alert(message, title=''):
    # path to icon png file
    if sys.platform.startswith('linux'):
        icon_path = '/usr/share/icons/logo.png'
        bash_command = 'notify-send -i {} "{} "{}"'.format(icon_path, title, message)
    elif sys.platform == 'darwin':
        icon_path = '~/.livescore-cli/logo.png'
        bash_command = """osascript -e 'display notification "{}" with title "{}"'""".format(message, title)
    else:
        raise OSError('OS Not Supported.')
    os.system(bash_command + ' > /dev/null 2>&1')
    return

# global variable to temporarily store the score of home and away team to compare for notification
score_h = [0]*50
score_a = [0]*50

def scores(scores, key):
    if not scores:
        print("Somethig went wrong. Couldn't print scores. :(")
        return
    global score_h, score_a
    try:
        lmax = lsprocess.get_longest_list(scores)
    except Exception as e:
        print("Something went wrong. Unexpected data.")
        print(e)
        return

    total_width = sum(lmax) + 12
    test = 3

    print_pattern('-', total_width, c.BLUE)
    print(c.TITLE + '{} SCORES'.format(URL[key][0]).center(total_width, ' ') + c.END)
    print_pattern('-', total_width, c.BLUE)

    for position, each_row in enumerate(scores):
        if isinstance(each_row, list) is False:
            # extract date if 1D array
            date = each_row.strip()
            date_color = c.dateArray[test % 3]
            test += 1
        else:
            # time conversion to local time
            val = each_row[0]
            if isinstance(each_row[0], list) is True:
                val = each_row[0][0]
            time = tt._convert(val.strip())

            home_team = each_row[1][0].strip()
            home_team_color = c.GREEN
            away_team = each_row[1][2].strip()
            away_team_color = c.GREEN

            try:
                home_team_score = int(each_row[1][1][0])
                away_team_score = int(each_row[1][1][2])

                middle_live = str(home_team_score) + ' - ' + str(away_team_score)
                if home_team_score > away_team_score:
                    away_team_color = c.RED
                    home_team_color = c.ORANGE
                elif home_team_score < away_team_score:
                    away_team_color = c.ORANGE
                    home_team_color = c.RED
                else:
                    away_team_color = c.CYAN
                    home_team_color = c.CYAN
                # if previous score is not equal to present score send notification to user
                if home_team_score != score_h[position] or away_team_score != score_a[position]:
                    send_alert('{}   {}  {}  {}'.format(time, home_team, middle_live, away_team).replace("'", ""), key)
                    score_h[position] = home_team_score
                    score_a[position] = away_team_score

            except:
                middle_live = ' '.join(each_row[1][1])
            print(' ' + date_color + ''.join(date.ljust(lmax[0])) + ' ' + ''.join(time.ljust(lmax[1] + 2))\
                  + c.END + home_team_color + ''.join(home_team.ljust(lmax[2]+2)) + c.END\
                  + ''.join(middle_live.ljust(lmax[3]+2)) + '  ' +  away_team_color \
                  + ''.join(away_team.ljust(lmax[4])) + c.END)

    print_pattern('-', total_width, c.BLUE)
    print_pattern('-', total_width, c.BLUE)


def table(tables, key):
    if not tables:
        print("Somethig went wrong. Couldn't print tables. :(")
        return
    table = URL[key][0] + ' TABLE'
    lmax_list = lsprocess.get_longest_list_table(tables)
    lmax = max(90, sum(lmax_list) + 55)
    ucl = 'Champions League';   ucl_color = c.ORANGE
    ucl_qual = 'Champions League qualification'
    ucq_color = c.BLUE
    europa = 'Europa League';   eup_color = c.PURPLE
    europa_qual = 'Europa League qualification'
    euq_color = c.CYAN
    rel = 'Relegation'; rel_color = c.RED

    print_pattern('+', lmax, c.BLUE)
    print('\t\t\t\t' + c.GREEN + table)
    print_pattern('+', lmax, c.BLUE)

    print(' LP' + '\t' + ''.join('Team Name'.ljust(lmax_list[1]))\
          + '\t'+'GP' + '\t' + 'W' + '\t' + 'D' + '\t' + 'L' + '\t' + 'GF'\
          + '\t' + 'GA' + '\t' + 'GD' + '\t' + 'Pts')

    print_pattern('-', lmax, c.BLUE)

    for each_row in tables[0][1]:
        league_position = each_row[0][0]
        team_name = each_row[1]
        games_played = each_row[2]
        total_wins = each_row[3]
        total_draws = each_row[4]
        total_loses = each_row[5]
        goals_for = each_row[6]
        goals_against = each_row[7]
        goal_difference = each_row[8]
        total_points = each_row[9]

        row_color = c.GREEN
        if isinstance(each_row[0], list) is True:
            if each_row[0][1] == ucl:
                row_color = ucl_color
            elif each_row[0][1] == ucl_qual:
                row_color = ucq_color
            elif each_row[0][1] == europa:
                row_color = eup_color
            elif each_row[0][1] == europa_qual:
                row_color = euq_color
            elif each_row[0][1] == rel:
                row_color = rel_color
        
        print(row_color + ' ' + str(league_position) + '\t' + ''.join(team_name.ljust(lmax_list[1]))\
              + '\t' + games_played + '\t' + total_wins + '\t' + total_draws + '\t' + total_loses\
              + '\t' + goals_for + '\t' + goals_against + '\t' + goal_difference + '\t' + total_points + c.END)

    print_pattern('+', lmax, c.BLUE)
    print(c.GRAY + ' LP = League Position \tGP = Games Played\tW = Wins \tD = Draws \tL = Lose \n GF = Goals For\t\tGA = Goal Against \tGD = Goal Differences')
    print_pattern('-', lmax, c.GREEN)
    print(' ' + ucl_color + ucl + '\t' + ucq_color + ucl_qual + '\t'\
        + eup_color + europa + '\n ' + euq_color + europa_qual + '\t' + rel_color + rel + c.END)
    print_pattern('+', lmax, c.BLUE)
    print(c.CYAN + '\n'.join([' {}'.format(t) for t in tables[-1]])) if isinstance(tables[-1], list) else print(c.CYAN + ' {}'.format(tables[-1]))
    print_pattern('-', lmax, c.END)


# character_to_print
# no of character to print
def print_pattern(c2p, n, color):
    for _ in range(n):
        print(color + c2p, end="")
    print(c.END)


