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

def process_table(rows):
	contents = '\n'.join(map(lambda r: r.text, rows))
	_contents = re.split('# ', contents)
	livescores = _contents[0]
	_livescores = re.split('\n',livescores)
	scoreTable = _contents[1]
	_scoreTable = re.split('\n',scoreTable)
	return [re.split('   |-', _livescores[i]) for i in range(len(_livescores))]
	
def print_table(x):
	table = 'BPL TABLE'
	
	print(c.BLUE+'------------------------------------------------------------')
	print('\t\t\t'+c.GREEN+table)
	print(c.BLUE+'------------------------------------------------------------'+c.GREEN)
    
	for i in range(len(x)-1):
		piss = [p.strip() for p in x[i]]
		print(piss[0]+'\t'+''.join(piss[1].ljust(16))+'\t'+piss[2]+' - '+piss[3]+'\t'+piss[4])
        
	print(c.BLUE+'------------------------------------------------------------')
    
def main():
	url = 'http://www.livescore.com/soccer/england/premier-league/'
	rows = get_livescore(url)
	print_table(process_table(rows))

if __name__ == '__main__':
    main()
