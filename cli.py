'''
Module to parse the command line parameters passed to the file.
do not know what might be used in --verbose.
--help provides most of the description of the module.Try:
>>>python3 cli.py --help
file contains a maintained list of supported leagues and a dictionary with their fetch URL
The required functions are yet to be linked. See the comments below.
'''

import argparse


supported_leagues = ['bpl', 'laliga', 'bundesliga', 'seriea', 'ligue1','portugal']
parser = argparse.ArgumentParser(description="A simple livescore tool. Currently works only for the Barclays Premier League")

parser.add_argument("-v","--verbose", help="Display verbose output", action="store_true")
parser.add_argument("-t","--table", help="Display the League Table", action = "store_true")
parser.add_argument("-f","--fixtures", help="Display the Fixtures", action = "store_true")
parser.add_argument("-s", "--score", help="Display the Score", action = "store_true")
parser.add_argument("-ts","--scorers", help="Display the Top Scorers", action = "store_true")
parser.add_argument("League", help="The league for which the details have to be displayed. Allowed values are ["+', '.join(supported_leagues)+']',choices = supported_leagues, nargs='+', type=str.lower)

args = parser.parse_args()
if args.verbose:
	print("Verbose Activated")
	
for k in args.League:
	'''
	#Code to load the table for given league
	#Can be done by a dictionary with leage names as keys and URL as values
	URL = {
			'bpl' : 'http://www.livescore.com/soccer/england/premier-league/',
			'laliga' : 'http://www.livescore.com/soccer/spain/primera-division/'
			'bundesliga' : 'http://www.livescore.com/soccer/germany/bundesliga/'
			'seriea' : 'http://www.livescore.com/soccer/italy/serie-a/'
			'ligue1' : 'http://www.livescore.com/soccer/france/ligue-1/'
			'portugal' : 'http://www.livescore.com/soccer/portugal/liga-sagres/'
	}
	'''
	#Code to fetch data from URL[k]
	if args.table:
		print("Displaying Table for {}".format(k.title()))
		#Add function to display table for the league k
	if args.fixtures:
		print("Displaying Fixtures for {}".format(k.title()))
		#Add function to display fixtures for the leage k
	if args.score:
		print("Displaying Scores for {}".format(k.title()))
		#Add function to display fixtures for the league k
	if args.scorers:
		print("Displaying Top Scorers for {}".format(k.title()))



