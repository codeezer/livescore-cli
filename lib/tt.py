#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re

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

if time.daylight:
    offsetHour = time.altzone / 3600.0
else:
    offsetHour = time.timezone / 3600.0

hour = int(-offsetHour)
minute = int(-offsetHour * 60 % 60)


def _convert(time):
    if bool(re.match(r'[0-9]{1,2}:[0-9]{1,2}', time)):
        time = list(map(int, time.split(':')))
        time[1] += minute
        time[0] += hour
        if time[1] > 59:
            time[1] -= 60
            time[0] += 1
        elif time[1] < 0:
            time[1] += 60
            time[0] -= 1
        if time[0] < 0:
            time[0] += 24
        elif time[0] > 23:
            time[0] -= 24
            time = _fix(str(time[0])) + ":" + _fix(str(time[1]))
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
