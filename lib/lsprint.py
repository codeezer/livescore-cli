#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    modules containg all the layout configuration of printable data 
    scores : function containing layout info of scores
    table : function containing layout info of table 
'''

import lscolors as c
import subprocess
import tt, URL, sys
import lsprocess,os

def sendAlert(message,title=''):
    #subprocess.Popen(['notify-send',message])
    #return
    os.system('notify-send "'+title+'" "'+message+'"')
    return


def scores(scores,key):
    lmax = lsprocess.get_longest_list(scores)
    total_width = sum(lmax)+8; test = 3

    print_pattern('-',total_width,c.BLUE)
    print(c.TITLE+'\t\t '+URL.URL[key][0]+' SCORES '+c.END)
    print_pattern('-',total_width,c.BLUE)
    count = 0
    for each_row in scores:
        if isinstance(each_row,list) == False:
            date = each_row.strip()                 #extract date if 1D array
            date_color = c.dateArray[test%3]; test+=1
        else:
            time = tt._convert(each_row[0].strip()) #time conversion to local time
            
            home_team = each_row[1].strip()
            home_team_color = c.GREEN
            away_team = each_row[3].strip()
            away_team_color = c.GREEN
            
            
            try:
                
                _temp = each_row[2].strip().split() 
                home_team_score = int(_temp[0])
                away_team_score = int(_temp[2])


                middle_live = str(home_team_score) + ' - ' + str(away_team_score)
                
                if home_team_score > away_team_score:
                    away_team_color = c.RED
                    home_team_color = c.ORANGE
                else:
                    away_team_color = c.ORANGE
                    home_team_color = c.RED
            except:
                middle_live = each_row[2].strip()

            
            print(' '+date_color+''.join(date.ljust(lmax[0])) + ''.join(time.ljust(lmax[1]+2))  \
                    + c.END +home_team_color+''.join(home_team.ljust(lmax[2]+2))+c.END      	\
                    + ''.join(middle_live.ljust(lmax[3]+2)) + away_team_color               	\
                    + ''.join(away_team.ljust(lmax[4])) + c.END)
            
    print_pattern('-',total_width,c.BLUE)
    print_pattern('-',total_width,c.BLUE)



def table(tables,key):
    table = URL.URL[key][0]+' TABLE'
    league_position = 0
    _temp = lsprocess.get_longest_list([row[1] for row in tables])
    longest_length = int(_temp[0])
    ucl = 'Champions League';   ucl_color = c.ORANGE 
    ucl_qual = 'Champions League qualification';    ucq_color = c.GRAY
    europa = 'Europa League';   eup_color = c.BLUE
    europa_qual = 'Europa League qualification';    euq_color = c.GREEN
    rel = 'Relegation'; rel_color = c.RED

    print_pattern('+',75+longest_length,c.BLUE)
    print('\t\t\t\t'+c.GREEN+table)
    print_pattern('+',75+longest_length,c.BLUE)

    print(' LP'+'\t'+''.join('Team Name'.ljust(longest_length))    	\
            +'\t'+'GP'+'\t'+'W'+'\t'+'D'+'\t'+'L'+'\t'+'GF'+'\t'+'GA'   \
            +'\t'+'GD'+'\t'+'Pts')

    print_pattern('-',75+longest_length,c.BLUE)
    
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
        
        row_color = c.PURPLE
        if isinstance(first_row[0],list) == True:
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

        print(row_color+' '+str(league_position)+'\t'    				\
                +''.join(team_name.ljust(longest_length))		 	\
                +'\t'+games_played+'\t'+total_wins+'\t'+total_draws+'\t'     	\
                +total_loses+'\t'+goals_for+'\t'+goals_against+'\t'     	\
                +goal_difference+'\t'+total_points+c.END)

    print_pattern('+',75+longest_length,c.BLUE)
    print(c.GRAY+' LP = League Position \tGP = Games Played\tW = Wins \tD = Draws \tL = Lose \n GF = Goals For\t\tGA = Goal Against \tGD = Goal Differences')     
    print_pattern('-',75+longest_length,c.GREEN)
    print(' '+ucl_color+ucl+'\t'+ucq_color+ucl_qual+'\t'+eup_color+europa+'\n '+euq_color+europa_qual+'\t'+rel_color+rel)
    print_pattern('+',75+longest_length,c.BLUE)



def print_pattern(c2p,n,color): #characterToprint #no of character to print
    for i in range(n):
        print(color+c2p),
        sys.stdout.softspace=0
    print(c.END)
