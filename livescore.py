#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests,re
import colors as c
import subprocess
import time,os

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
        return False


def print_scores(x):
    
    COLOR2 = c.GREEN
    COLOR3 = c.GREEN
    scores = 'BPL SCORES'
    
    print(c.BLUE+'------------------------------------------------------------')
    print('\t\t\t'+c.GREEN+scores)
    print(c.BLUE+'------------------------------------------------------------'+c.END)
    for i in range(len(x)-1):
    	piss = [p.strip() for p in x[i]]
    	
    	if int(piss[2]) > int(piss[3]):
            COLOR2 = c.ORANGE
            COLOR3 = c.RED
    	elif int(piss[2]) < int(piss[3]):
            COLOR3 = c.ORANGE
            COLOR2 = c.RED
	else:
	    COLOR2 = c.CYAN
	    COLOR3 = c.CYAN
        
        print(piss[0]+'\t'+COLOR2+''.join(piss[1].ljust(16))+'\t'+piss[2]+c.END+' - '+COLOR3+piss[3]+'\t'+piss[4]+c.END)
    
    print(c.BLUE+'------------------------------------------------------------')


def main():
    
    url = 'http://www.livescore.com/soccer/england/premier-league/'
    
    while True:
        try:
            print('...fetching scores from livescore...')
            rows = get_livescore(url)
	    os.system('clear')
            print_scores(_process(rows,'scores'))
            
            time.sleep(10)

        except KeyboardInterrupt:
            break

        




if __name__ == '__main__':
    main()
