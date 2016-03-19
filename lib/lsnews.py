#!/usr/bin/env python
# -*- coding: utf-8 -*-

import URL,re
import lsweb, lsprocess
import lscolors, lsprint
import json,tt

def get_news(uri=URL.goalUS,sclass='news_box2'):
    try:
        rows = lsweb.get_livescore(uri,sclass)
        print('fetching soccer news from goal.com\n')
        print('(Last Updated at '+lscolors.ORANGE+tt.datetime_now()+lscolors.END+')')
        a_dict = {'datetime': tt.datetime_now()}
        contents = '\n'.join(map(lambda r: r.text, rows))
        news = re.split('\n',contents)
        fw = open('data.json', 'w')
        newsstr = json.dumps(news, indent=4)
        fw.write('{"news":')
        fw.write(newsstr)   
        fw.write('}')
        fw.close()
        with open('data.json') as f:
            data = json.load(f)
        data.update(a_dict)
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return news

    except:
        fr = open('data.json').read()
        read = json.loads(fr)
        datetime = read['datetime']
        print("(Last Updated at "+lscolors.ORANGE+datetime+lscolors.END+')')
        return read['news']



def print_news(news):
    width = lsprocess.find_longest_no(news)
    news_count = 1
    color_count = 1
    lsprint.print_pattern('*',width+6,lscolors.ORANGE)
    for news_no in news:
        pcount = str(news_count)+'.'
        print(lscolors.colorArray[color_count]+''.join(pcount.ljust(5))+news_no)
        #lsprint.sendAlert(news_no)
        news_count = news_count + 1
        if color_count == 3:
            color_count = 0
        color_count = color_count + 1
    lsprint.print_pattern('*',width+6,lscolors.ORANGE)
    lsprint.print_pattern('*',width+6,lscolors.ORANGE)


if __name__ == '__main__':
    print_news(get_news())
