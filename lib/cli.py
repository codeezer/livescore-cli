#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Module to parse the command line parameters passed to the file.
    --help provides most of the description of the module. Try:
    >>> python cli.py --help
'''

import argparse
from .urls import details

supported_competition = list(details.get('competition').keys())
parser = argparse.ArgumentParser(description="A simple livescore tool.",
                                 epilog="Sample uses:\n "
                                 "python livescore.py --table bpl laliga")

parser.add_argument("-v", "--verbose",
                    help="Display verbose output",
                    action="store_true")
parser.add_argument("-t", "--table",
                    help="Display the League Table",
                    action="store_true")
parser.add_argument("-n", "--news",
                    help="Display the News",
                    action="store_true")
parser.add_argument("-s", "--score",
                    help="Display the Score",
                    action="store_true")
parser.add_argument("-ts", "--scorers",
                    help="Display the Top Scorers",
                    action="store_true")
parser.add_argument("competition",
                    help="The competition for which the details have to be displayed."
                    " Allowed values are ["+", ".join(supported_competition)+"]. "
                    "For multiple choices, separate each league name by a space.",
                    choices=supported_competition, nargs='+',
                    type=str.lower, metavar='COMPETITION')

args = parser.parse_args()
if args.verbose:
    print("Verbose Activated")
