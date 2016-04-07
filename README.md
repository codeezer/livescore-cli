<b>livescore-cli</b> - enjoy football scores live right from the linux terminal.

![Sample Run](http://i.imgur.com/yDR7Bxs.jpg)
    
## DEPENDENCIES
    
    1. BeautifulSoup (python-bs4)

    2. Requests (python-requests)
    

## INSTALLATION

    git clone https://github.com/codeezer/livescore-cli.git
  
    cd livescore-cli
    
    ./setup

    livescore -t bpl 


## Description

livescore-cli is a small commandline program to watch scores, tables and fixtures of football(soccer) from the commandline. It requires the python interpreter(2). It uses the data from the website livescore.com and some other websites. It is essentially built for the busy people that are passionate about football.

## Features

        1. Real Time Livescore
        2. Game Time in Local Time 
        3. League Table with division
        4. Top Scorer of each League
        5. Live Soccer News

## Soccer News *

![alt tag](http://i.imgur.com/P6d8Qgz.jpg)


##USAGE

    usage: livescore.py [-h] [-v] [-t] [-s] [-ts] LEAGUE [LEAGUE ...]
    
    A simple livescore tool. Currently works only for the Limited Leagues.
    
    positional arguments:
      LEAGUE          The league for which the details have to be displayed.
                                   Allowed values are [bundesliga, ligue1, seriea, bpl,
                                   portugal, laliga]. For multiple choices, separate each
                                   league name by a space.

    optional arguments:
      -h, --help      show this help message and exit
      -v, --verbose   Display verbose output
      -t, --table     Display the League Table
      -s, --score     Display the Score
      -ts, --scorers  Display the Top Scorers
    
    Sample uses: python livescore.py --table bpl laliga
                 python livescore.py -s bpl
                 python livescore.py -t -s -ts bpl laliga seriea

