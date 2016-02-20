#!/usr/bin/env python
# -*- coding: utf-8 -*-

import URL,re
import lsweb
import lscolors

def get_news():
    rows = lsweb.get_livescore(URL.goalUS,'news_box2')
    print('fetching soccer news from soccernews.com\n')
    contents = '\n'.join(map(lambda r: r.text, rows))
    news = re.split('\n',contents)
    news_count = 1
    color_count = 1
    for news_no in news:
        pcount = str(news_count)+'>>'
        print(lscolors.colorArray[color_count]+''.join(pcount.ljust(6))+news_no)
        news_count = news_count + 1
        if color_count == 3:
            color_count = 1
        color_count = color_count + 1
    print('\n')


if __name__ == '__main__':
    get_news() 
