#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests,re
import colors as c

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
    scores = 'BPL SCORES'
    COLOR2 = c.GREEN
    COLOR3 = c.GREEN
    print(c.BLUE+'------------------------------------------------------------')
    print('\t\t\t'+c.GREEN+scores)
    print(c.BLUE+'------------------------------------------------------------'+c.END)
    
    for i in range(len(x)-1):
    	piss = [p.strip() for p in x[i]]
    	
    	if int(piss[2]) > int(piss[3]):
            COLOR2 = c.RED
            COLOR3 = c.CYAN
    	elif int(piss[2]) < int(piss[3]):
            COLOR3 = c.RED
            COLOR2 = c.CYAN
	else:
	    COLOR2 = c.GREEN
	    COLOR3 = c.GREEN
        
        print(piss[0]+'\t'+COLOR2+''.join(piss[1].ljust(16))+'\t'+piss[2]+c.END+' - '+COLOR3+piss[3]+'\t'+piss[4]+c.END)
        
    print(c.BLUE+'------------------------------------------------------------')


def main():
    url = 'http://www.livescore.com/soccer/england/premier-league/'
    rows = get_livescore(url)
    print_scores(_process(rows,'scores'))




if __name__ == '__main__':
    main()
