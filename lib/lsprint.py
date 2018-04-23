#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Module containing all the layout configuration of printable data"""

import lscolors as c
import sys
import os
import tt
from URL import URL
import lsprocess


def send_alert(message, title=''):
    if sys.platform == 'darwin':
        icon_path = '~/.livescore-cli/logo.png'
        bash_command = """osascript -e 'display notification "{}" with title "{}"'""".format(message, title)
    elif sys.platform.startswith('linux'):
        icon_path = '/usr/share/icons/logo.png'
        bash_command = 'notify-send -i {} "{}" "{}"'.format(icon_path, title, message)
    else:
        raise OSError(
            'OS not supported. '
            'Currently livescore-cli is supported on Linux and Mac OS X')
    # send notification
    os.system(bash_command + ' > /dev/null 2>&1')


class League():

    def __init__(self, key):
        self.key = key
        # variables to temporarily store the scores to compare for notification
        self.score_h = [-1]*50
        self.score_a = [-1]*50

    def display_scores(self, scores):
        """Display the scores of the league"""
        lmax = lsprocess.get_longest_list(scores)
        total_width = sum(lmax) + 8
        test = 3

        self.__print_pattern('-', total_width, c.BLUE)
        print(c.TITLE + '\t\t ' + URL[self.key][0] + ' SCORES ' + c.END)
        self.__print_pattern('-', total_width, c.BLUE)

        for position, each_row in enumerate(scores):
            if not isinstance(each_row, list):
                # extract date if 1D array
                date = each_row.strip()
                date_color = c.dateArray[test % 3]
                test += 1
            else:
                # time conversion to local time
                time = tt._convert(each_row[0].strip())

                home_team = each_row[1].strip()
                away_team = each_row[3].strip()

                try:
                    _temp = each_row[2].strip().split()
                    home_team_score = int(_temp[0])
                    away_team_score = int(_temp[2])
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

                except ValueError:  # if the result is 'home   ? - ?   away'
                    home_team_score = '?'
                    home_team_score = '?'
                    home_team_color = c.GREEN
                    away_team_color = c.GREEN
                    middle_live = each_row[2].strip()

                # if previous score is not equal to present score send notification to user
                if home_team_score != self.score_h[position] or away_team_score != self.score_a[position]:
                    send_alert('{}   {} - {}   {}'.format(
                        time, home_team, middle_live, away_team), self.key)
                    self.score_h[position] = home_team_score
                    self.score_a[position] = away_team_score

                print(' ' + date_color + ''.join(date.ljust(lmax[0])) + ''.join(time.ljust(lmax[1] + 2))\
                       + c.END + home_team_color + ''.join(home_team.ljust(lmax[2]+2)) + c.END\
                       + ''.join(middle_live.ljust(lmax[3]+2)) + away_team_color\
                       + ''.join(away_team.ljust(lmax[4])) + c.END)

        self.__print_pattern('-', total_width, c.BLUE)
        self.__print_pattern('-', total_width, c.BLUE)


    def display_table(self, tables):
        """Display the table of the league"""
        table = URL[self.key][0] + ' TABLE'
        league_position = 0
        _temp = lsprocess.get_longest_list([row[1] for row in tables])
        longest_length = int(_temp[0])
        ucl = 'Champions League'
        ucl_color = c.ORANGE
        ucl_qual = 'Champions League qualification'
        ucq_color = c.BLUE
        europa = 'Europa League'
        eup_color = c.PURPLE
        europa_qual = 'Europa League qualification'
        euq_color = c.CYAN
        rel = 'Relegation'; rel_color = c.RED

        self.__print_pattern('+', 75 + longest_length, c.BLUE)
        print('\t\t\t\t' + c.GREEN + table)
        self.__print_pattern('+', 75 + longest_length, c.BLUE)

        print(' LP' + '\t' + ''.join('Team Name'.ljust(longest_length))\
              + '\t'+'GP' + '\t' + 'W' + '\t' + 'D' + '\t' + 'L' + '\t' + 'GF'\
              + '\t' + 'GA' + '\t' + 'GD' + '\t' + 'Pts')

        self.__print_pattern('-', 75 + longest_length, c.BLUE)

        for first_row in tables[1::]:
            league_position += 1
            team_name = first_row[1]
            games_played = first_row[2]
            total_wins = first_row[3]
            total_draws = first_row[4]
            total_loses = first_row[5]
            goals_for = first_row[6]
            goals_against = first_row[7]
            goal_difference = first_row[8]
            total_points = first_row[9]

            row_color = c.GREEN
            if isinstance(first_row[0], list):
                if first_row[0][1] == ucl:
                    row_color = ucl_color
                elif first_row[0][1] == ucl_qual:
                    row_color = ucq_color
                elif first_row[0][1] == europa:
                    row_color = eup_color
                elif first_row[0][1] == europa_qual:
                    row_color = euq_color
                elif first_row[0][1] == rel:
                    row_color = rel_color

            else:
                pass

            print(row_color + ' ' + str(league_position) + '\t' + ''.join(team_name.ljust(longest_length))\
                  + '\t' + games_played + '\t' + total_wins + '\t' + total_draws + '\t' + total_loses\
                  + '\t' + goals_for + '\t' + goals_against + '\t' + goal_difference + '\t' + total_points + c.END)

        self.__print_pattern('+', 75+longest_length, c.BLUE)
        print(c.GRAY + ' LP = League Position \tGP = Games Played\tW = Wins \tD = Draws \tL = Lose \n GF = Goals For\t\tGA = Goal Against \tGD = Goal Differences')
        self.__print_pattern('-', 75 + longest_length, c.GREEN)
        print(' ' + ucl_color + ucl + '\t' + ucq_color + ucl_qual + '\t'\
            + eup_color + europa + '\n ' + euq_color + europa_qual + '\t' + rel_color + rel)
        self.__print_pattern('+', 75 + longest_length, c.BLUE)


    # characterToprint #no of character to print
    def __print_pattern(self, c2p, n, color):
        for i in range(n):
            print(color + c2p),
            sys.stdout.softspace = 0
        print(c.END)
