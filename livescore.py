#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests, re, os
import colors as c
import subprocess, time

score1 = [0]*110
score2 = [0]*110

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


def print_scores(x):
    _message = [[]]
    COLOR2 = c.GREEN
    COLOR3 = c.GREEN
    scores = 'BPL SCORES'        
    print(c.BLUE+'\n------------------------------------------------------------')
    print('\t\t\t'+c.GREEN+scores)
    print(c.BLUE+'------------------------------------------------------------'+c.END)

    for i in range(len(x)-1):
        piss = [p.strip() for p in x[i]]
        try:
            if int(piss[2]) == int(score1[i]) or int(piss[3]) == int(score2[i]) :
                sendAlert(piss[0]+'   '+piss[1]+' '+piss[2]+' - '+piss[3]+' '+piss[4])
            
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
            _message.append(c.ORANGE+piss[1]+c.END+' vs '+c.ORANGE+piss[4]+c.END+' match is not started yet')
        
        score1.append(piss[2])
        score2.append(piss[3])
        print(piss[0]+'\t'+COLOR2+''.join(piss[1].ljust(16))+'\t'+piss[2]+c.END+' - '+COLOR3+piss[3]+'\t'+piss[4]+c.END)
    
    for msz in _message:
        if msz == '':
            return True        
        else:
            print(msz)
    print(c.BLUE+'------------------------------------------------------------')
    

def main():
    
    url = 'http://www.livescore.com/soccer/england/premier-league/'

    while True:
        try:
            os.system('clear')
            print(' ... Fetching scores from http://www.livescore.com ... ')
            rows = get_livescore(url)
            print_scores(_process(rows,'scores'))
            time.sleep(15)
            
        except KeyboardInterrupt:
            break

        

if __name__ == '__main__':
    main()
