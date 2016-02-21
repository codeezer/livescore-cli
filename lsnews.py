#!/usr/bin/env python
# -*- coding: utf-8 -*-

import URL,re
import lsweb
import lscolors
import json

def get_news():
    try:
        rows = lsweb.get_livescore(URL.goalUS,'news_box2')
        print('fetching soccer news from soccernews.com\n')
        contents = '\n'.join(map(lambda r: r.text, rows))
        news = re.split('\n',contents)
        with open('data.txt', 'w') as outfile:
            json.dump(news, outfile)
        return news

    except:
        with open('data.txt', 'r') as infile:
            news=json.load(infile)
        return news


def print_news(news):
    #temp
    #news=get_news();
    news_count = 1
    color_count = 1
    print(lscolors.ORANGE+'************************************************************************'+lscolors.END)
    for news_no in news:
        pcount = str(news_count)+'.'
        print(lscolors.colorArray[color_count]+''.join(pcount.ljust(5))+news_no)
        news_count = news_count + 1
        if color_count == 3:
            color_count = 0
        color_count = color_count + 1

    print(lscolors.ORANGE+'************************************************************************'+lscolors.END)

if __name__ == '__main__':
    print_news(get_news())
