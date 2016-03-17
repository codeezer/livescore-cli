#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
    modules containg all the layout configuration of printable data 
    scores : function containing layout info of scores
    table : function containing layout info of table 
'''

import lscolors as c
import re, subprocess
import tt, URL, sys
import lsprocess

def sendAlert(message):
    subprocess.Popen(['notify-send',message])
    return
    

def scores1(scores,key):
    lmax = lsprocess.get_longest_list(scores)
    total_width = sum(lmax)+8; test = 3

    print_pattern('-',total_width,c.BLUE)
    print(c.TITLE+'\t\t '+URL.URL[key][0]+' SCORES '+c.END)
    print_pattern('-',total_width,c.BLUE)
    
    for each_row in scores:
        if isinstance(each_row,list) == False:
            date = each_row.strip()
            date_color = c.dateArray[test%3]; test+=1
        else:
            time = tt._convert(each_row[0].strip())
            home_team = each_row[1].strip()
            home_team_color = c.GREEN
            away_team = each_row[3].strip()
            away_team_color = c.GREEN
            try:
                _temp = each_row[2].strip().split() 
                home_team_score = int(_temp(0))
                away_team_score = int(_temp(2))
                middle_live = home_team_score + ' - ' + away_team_score

                if home_team_score > away_team_score:
                    away_team_color = c.RED
                    home_team_color = c.ORANGE
                else:
                    away_team_color = c.ORANGE
                    home_team_color = c.RED
            except:
                middle_live = each_row[2].strip()

            print(' '+date_color+''.join(date.ljust(lmax[0])) + ''.join(time.ljust(lmax[1]+2))  \
                    + c.END +home_team_color+''.join(home_team.ljust(lmax[2]+2))+c.END      \
                    + ''.join(middle_live.ljust(lmax[3]+2)) + away_team_color               \
                    + ''.join(away_team.ljust(lmax[4])) + c.END)

    print_pattern('-',total_width,c.BLUE)
    print_pattern('-',total_width,c.BLUE)
    guiscore.livescore(scores[2])




def table(x,key):
    table = URL.URL[key][0]+' TABLE'
    
    ucl_ = URL.URL[key][3]
    ucl_qual = URL.URL[key][4]
    europa_ = URL.URL[key][5]
    europa_qual = URL.URL[key][6]
    rel_qual = URL.URL[key][7]
    rel_ = URL.URL[key][8]

    tables = []
    _table = []
    print(c.BLUE+'\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\t\t\t\t'+c.GREEN+table)
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    for i in range(1,len(x)):
        temp = re.split('  ',x[i][1])
        tables.append(temp[1])

    for each_row in tables:
        _table.append(lsprocess.regSplit(each_row))

    position = 1

    longest_length = 15
    shortest_length = 10
    
    for data in _table:
        m = len(data[0])
        if m > longest_length:
            longest_length = m
    
    space = longest_length

    print(' LP'+'\t'+''.join('Club Name'.ljust(space))+'\t'+'GP'+'\t'+'W'+'\t'+'D'+'\t'+'L'+'\t'+'GF'+'\t'+'GA'+'\t'+'GD'+'\t'+'Pts')
    print(c.BLUE+'---------------------------------------------------------------------------------------------------'+c.END)
    for print_row in _table:
        if int(position) <= ucl_:
            color = c.ORANGE
        elif int(position) > len(_table)-rel_:
            color = c.RED
        elif ucl_ < int(position) <= ucl_ + ucl_qual:
            color = c.GREEN
        elif ucl_ + ucl_qual < int(position) <= ucl_ + ucl_qual + europa_:
            color = c.END
        else:
            color = c.PURPLE
#After issue,interim solution of issue 
        if len(print_row) > 10:
            print_row[0] = print_row[0]+" "+print_row[1]
            print_row[1] = print_row[2]
            print_row[2] = print_row[3]
            print_row[3] = print_row[4]
            print_row[4] = print_row[5]
            print_row[5] = print_row[6]
            print_row[6] = print_row[7]
            print_row[7] = print_row[8]
            print_row[8] = print_row[9]
#------------------------------------------------------------
        print(color+'|'+str(position)+'|'+'\t'+''.join(print_row[0].ljust(space))+'\t'+str(print_row[1])+'\t'+str(print_row[2])+'\t'+str(print_row[3])+'\t'+str(print_row[4])+'\t'+str(print_row[5])+'\t'+str(print_row[6])+'\t'+str(print_row[7])+'\t'+str(print_row[8]))
        position += 1
        
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    print(c.GRAY+'LP = League Position \tGP = Games Played \tW = Wins \tD = Draws \tL = Lose \nGF = Goals For \t\tGA = Goal Against \tGD = Goal Differences')

    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)





def scorers(x,key):
    scorers = URL.URL[key][0]+' TOP SCORER'
    print(c.ORANGE+'\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\t\t\t'+c.GREEN+scorers)
    print(c.ORANGE+'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    longest_length1 = 15
    longest_length2 = 15
    for data in x[1:]:
        dataa = [p.strip() for p in data]
        mx1 = len(dataa[1])
        mx2 = len(dataa[2])
        if mx1 > longest_length1:
            longest_length1 = mx1
        if mx2 > longest_length2:
            longest_length2 = mx2

    space1 = longest_length1
    space2 = longest_length2
    print('|'+'SN'+'|'+'\t'+''.join('Players Name'.ljust(space1))+'\t'+''.join('Club'.ljust(space2))+'\t'+'Goals')
    print(c.ORANGE+'------------------------------------------------------------------------------'+c.END)
    for data in x[1:]:
        dataa = [p.strip() for p in data]
        print(c.CYAN+'|'+dataa[0]+'|'+'\t'+''.join(dataa[1].ljust(space1))+'\t'+''.join(dataa[2].ljust(space2))+'\t'+dataa[3]+c.END)
    
    print(c.ORANGE+'\n******************************************************************************'+c.END)
    print(c.ORANGE+'------------------------------------------------------------------------------')




def print_pattern(c2p,n,color): #characterToprint #no of character to print
    for i in range(n):
        print(color+c2p),
        sys.stdout.softspace=0
    print(c.END)

