#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
    modules containg all the layout configuration of printable data 
    scores : function containing layout info of scores
    table : function containing layout info of table 
'''

import lscolors as c
import re, subprocess
import tt, URL

def sendAlert(message):
    subprocess.Popen(['notify-send',message])
    return
    
    
score1 = [0]*110
score2 = [0]*110

def scores(x,key):
    _message = []
    alert = []
    scores = URL.URL[key][0]+' SCORES'        
    print(c.BLUE+'\n------------------------------------------------------------')
    print('\t\t'+c.GREEN+scores)
    print(c.BLUE+'------------------------------------------------------------'+c.END)

    
    for i in range(len(x)-1):
        ''' 
            piss variabe contains the score layout like 
            piss[0] = Time / Status
            piss[1] = Team1
            piss[2] = Score1
            piss[3] = Score2
            piss[4] = Team2
            
            i.e. 20:00 Everton   1 - 2   Crystal Palace
        '''
        piss = [p.strip() for p in x[i]] #striping strings i.e. ' 3 ' -> '3' or '44 ' -> '44'
        piss[0] = tt._convert(piss[0])
        COLOR2 = c.GREEN
        COLOR3 = c.GREEN
        try:
            #if score is different than previous score then send alert
            if int(piss[2]) != int(score1[i]) or int(piss[3]) != int(score2[i]) :
                sendAlert(piss[0]+'   '+piss[1]+' '+piss[2]+' - '+piss[3]+' '+piss[4])
                score1[i]=piss[2]
                score2[i]=piss[3]
            
            #tE show loser team with red color and winner with orange and draw with cyan
            if int(piss[2]) > int(piss[3]): 
                COLOR2 = c.ORANGE
                COLOR3 = c.RED
            
            elif int(piss[2]) < int(piss[3]):
                COLOR3 = c.ORANGE
                COLOR2 = c.RED
           
            else:
                COLOR2 = c.CYAN
                COLOR3 = c.CYAN
            
            if piss[0] == 'FT':
                _message.append(c.ORANGE+piss[1]+c.END+' vs '+c.ORANGE+piss[4]+c.END+' match has been completed')
        #if conversion to int fails i.e. '?' instead of numbers then match hasnt started yet :)
        except:
            _message.append(c.ORANGE+piss[1]+c.END+' vs '+c.ORANGE+piss[4]+c.END+' match has not started yet')
        
        score1.append(piss[2])
        score2.append(piss[3])
        print(piss[0]+'\t'+COLOR2+''.join(piss[1].ljust(16))+'\t'+piss[2]+c.END+' - '+COLOR3+piss[3]+'\t'+piss[4]+c.END)

    print(c.BLUE+'------------------------------------------------------------')
    print(c.CYAN+'\n******************************************************************'+c.END)
    for msz in _message:
        print(msz)
    print(c.CYAN+'******************************************************************'+c.END)







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
    a = re.compile("\s+(?![a-zA-Z]+)")
    print(c.BLUE+'\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\t\t\t\t'+c.GREEN+table)
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    for i in range(1,len(x)):
        temp = re.split('  ',x[i][1])
        tables.append(temp[1])

    for each_row in tables:
        _table.append(a.split(each_row))

    position = 1

    longest_length = 15
    shortest_length = 10
    
    for data in _table:
        m = len(data[0])
        if m > longest_length:
            longest_length = m
    
    space = longest_length

    print(' LP'+'\t'+''.join('Club Name'.ljust(space))+'\t'+'GP'+'\t'+'W'+'\t'+'D'+'\t'+'L'+'\t'+'GF'+'\t'+'GA'+'\t'+'GD'+'\t'+'Pts')
    print(c.BLUE+'-----------------------------------------------------------------------------------------------'+c.END)
    for print_row in _table:
        if int(position) <= ucl_:
            color = c.ORANGE
        elif int(position) >= len(_table)-rel_:
            color = c.RED
        elif int(position) == 4:
            color = c.GREEN
        elif int(position) == 5:
            color = c.END
        else:
            color = c.PURPLE
        print(color+'|'+str(position)+'|'+'\t'+''.join(print_row[0].ljust(space))+'\t'+str(print_row[1])+'\t'+str(print_row[2])+'\t'+str(print_row[3])+'\t'+str(print_row[4])+'\t'+str(print_row[5])+'\t'+str(print_row[6])+'\t'+str(print_row[7])+'\t'+str(print_row[8]))
        position += 1
        
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    print(c.GRAY+'LP = League Position \tGP = Games Played \tW = Wins \tD = Draws \tL = Lose \nGF = Goals For \t\tGA = Goal Against \tGD = Goal Differences')

    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)





def scorers(x,key):
    scorers = URL.URL[key][0]+'BPL TOP SCORER'
    print(c.BLUE+'\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print('\t\t\t'+c.GREEN+scorers)
    print(c.BLUE+'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'+c.END)
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
    print(c.BLUE+'--------------------------------------------------------------'+c.END)
    for data in x[1:]:
        dataa = [p.strip() for p in data]
        print('|'+dataa[0]+'|'+'\t'+''.join(dataa[1].ljust(space1))+'\t'+''.join(dataa[2].ljust(space2))+'\t'+dataa[3])
    
    print(c.BLUE+'\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'+c.END)
    print('\n'+c.BLUE+'------------------------------------------------------------')

