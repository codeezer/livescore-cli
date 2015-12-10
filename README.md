<b>livescore-cli</b> - enjoy football scores live right from the linux terminal.

![alt tag](https://raw.githubusercontent.com/codeezer/livescore-cli/master/graphics/score.jpg)

    : Work on Progress 
    
    currently only livescore of BPL (Barclays Premier League) is available

## INSTALLATION (Linux - Ubuntu)

![alt tag](https://raw.githubusercontent.com/codeezer/livescore-cli/master/graphics/livescore-cli.gif)

    sudo apt-get install python3 python3-bs4 
  
    git clone https://github.com/codeezer/livescore-cli.git
  
    cd livescore-cli
  
    python3 livescore.py
Or
    python livescore.py



## Description

livescore-cli is a small commandline program to watch scores, tables and fixtures of football(soccer) from the commandline. It requires the python interpreter(2 or 3). It uses the data from the website livescore.com and some other websites. It is essentially built for the busy people that are passionate about football.
    
##USAGE

    usage: livescore.py [-h] [-v] [-t] [-s] [-ts] LEAGUE [LEAGUE ...]
    
    A simple livescore tool. Currently works only for the Barclays Premier League
    
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
    
    Sample uses: python3 livescore.py --table bpl laliga
                 python3 livescore.py -t -s -ts bpl laliga seriea







