#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import re
from datetime import datetime, timedelta

'''
module to convert the given time in UTC to local device time
_convert() method takes a single time in string and returns the local time
convert() takes a list of time in string format and returns in local time
NOTE: any string not in the format "digits:digits" will be returned as is
USAGE:
>>>convert(['19:45','18:15','5:45','512','FT'])
['01:00','00:00','11:30','512','FT']

isgreat(time1,time2) takes two time strings such as "4:30" and "12"15"
and returns if the first time is greater than the second.
if time1>time2: return 1
if time2>time1: return -1
if time1==time2: return 0
NOTE: the function stalls if not in the above format
USAGE:
>>>isgreat("3:00","4:15")
-1
'''

# Input time already considers daylight savings
# if time.daylight:
#     offsetHour = time.altzone / 3600.0
# else:
#     offsetHour = time.timezone / 3600.0

offsetHour = time.timezone / 3600.0
hours = int(-offsetHour)
minutes = int(-offsetHour * 60 % 60)
delta = timedelta(hours=hours, minutes=minutes)


def _convert(time):
    try:
        t = datetime.strptime(time, '%H:%M')
        return (t+delta).strftime('%H:%M')
    except ValueError as e:
        return time

def _fix(y):
        if len(y) == 1:
                y = '0' + y
        return y


def convert(times):
        times = list(map(_convert, times))
        return times


def is_great(time1, time2):
        t1 = list(map(int, time1.split(':')))
        t2 = list(map(int, time2.split(':')))
        if t1[0] > t2[0]:
                return 1
        elif t2[0] > t1[0]:
                return -1
        else:
                if t1[1] > t2[1]:
                        return 1
                elif t2[1] > t1[1]:
                        return -1
                else:
                        return 0


def datetime_now():
    return time.strftime("%c")
