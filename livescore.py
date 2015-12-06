#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests, re, os, argparse
import colors as c
import subprocess, time


def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        return True
    else:
        return False

def sendAlert(message):
    subprocess.Popen(['notify-send',message])
    return


def get_livescore(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    _rows = soup.find_all(class_='row-gray')
    return _rows


def _process(rows,flag):
    contents = '\n'.join(map(lambda r: r.text, rows))
    _contents = re.split('# ', contents)
    livescores = _contents[0]
    _livescores = re.split('\n',livescores)
    scoreTable = _contents[1]
    _scoreTable = re.split('\n',scoreTable)
    if flag == 'scores':
        return [re.split('   |-', _livescores[i]) for i in range(len(_livescores))]
    else:
        return [re.split('   ', _scoreTable[i]) for i in range(len(_scoreTable))]


score1 = [0]*110
score2 = [0]*110

def print_scores(x):
    _message = []
    alert = []
    scores = 'BPL SCORES'        
    print(c.BLUE+'\n------------------------------------------------------------')
    print('\t\t\t'+c.GREEN+scores)
    print(c.BLUE+'------------------------------------------------------------'+c.END)

    for i in range(len(x)-1):
        piss = [p.strip() for p in x[i]]
        COLOR2 = c.GREEN
        COLOR3 = c.GREEN
        try:
            if int(piss[2]) != int(score1[i]) or int(piss[3]) != int(score2[i]) :
                sendAlert(piss[0]+'   '+piss[1]+' '+piss[2]+' - '+piss[3]+' '+piss[4])
                score1[i]=piss[2]
                score2[i]=piss[3]
            
            if int(piss[2]) > int(piss[3]):
                COLOR2 = c.ORANGE
                COLOR3 = c.RED
            
            elif int(piss[2]) < int(piss[3]):
                COLOR3 = c.ORANGE
                COLOR2 = c.RED
           
            else:
                COLOR2 = c.CYAN
                COLOR3 = c.CYAN
                
        except:
            _message.append(c.ORANGE+piss[1]+c.END+' vs '+c.ORANGE+piss[4]+c.END+' match has not started yet')
        
        score1.append(piss[2])
        score2.append(piss[3])
        print(piss[0]+'\t'+COLOR2+''.join(piss[1].ljust(16))+'\t'+piss[2]+c.END+' - '+COLOR3+piss[3]+'\t'+piss[4]+c.END)

    print(c.BLUE+'------------------------------------------------------------')
    print(c.RED+'\n******************************************************************'+c.END)
    for msz in _message:
        print(msz)
    print(c.RED+'******************************************************************'+c.END)




def print_table(x):
    table = 'BPL TABLE'        
    tables = []
    _table = []
    a = re.compile("\s+(?![a-zA-Z]+)")
    print(c.BLUE+'\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\t\t\t\t\t'+c.GREEN+table)
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    for i in range(1,len(x)):
        #print(lala[i])
        temp = re.split('  ',x[i][1])
        tables.append(temp[1])

    for each_row in tables:
        _table.append(a.split(each_row))

    position = 1

    print(' LP'+'\t'+''.join('Club Name'.ljust(16))+'\t'+'GP'+'\t'+'W'+'\t'+'D'+'\t'+'L'+'\t'+'GF'+'\t'+'GA'+'\t'+'GD'+'\t'+'Pts')
    print(c.BLUE+'-----------------------------------------------------------------------------------------------'+c.END)
    for print_row in _table:
        if int(position) <= 3:
            color = c.ORANGE
        elif int(position) >= 18:
            color = c.RED
        elif int(position) == 4:
            color = c.GREEN
        else:
            color = c.PURPLE
        print(color+'|'+str(position)+'|'+'\t'+''.join(print_row[0].ljust(16))+'\t'+str(print_row[1])+'\t'+str(print_row[2])+'\t'+str(print_row[3])+'\t'+str(print_row[4])+'\t'+str(print_row[5])+'\t'+str(print_row[6])+'\t'+str(print_row[7])+'\t'+str(print_row[8]))
        position += 1
        
    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)
    print(c.GRAY+'LP = League Position \tGP = Games Played \tW = Wins \tD = Draws \tL = Lose \nGF = Goals For \t\tGA = Goal Against \tGD = Goal Differences')

    print(c.BLUE+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+c.END)



def main():
    
    url = 'http://www.livescore.com/soccer/england/premier-league/'
    pingTest = 'livescore.com'
    while True:
        try:
            if check_ping(pingTest) == True:
                os.system('clear')
                print(' ... Fetching scores from http://www.livescore.com ... ')
                rows = get_livescore(url)
                print_scores(_process(rows,'scores'))
                print_table(_process(rows,'table'))
            
            else:
                print("Check Your Internet Connection , It looks like you're out of internet.")

            time.sleep(15)
        
        except KeyboardInterrupt:
            break

        except:
            print('Unexpected Error')
            
if __name__ == '__main__':
    main()
