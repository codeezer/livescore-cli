import time
import re

'''
module to convert the given time in UTC to local device time
_convert() method takes a single time in string and returns the local time
convTimes() takes a list of time in string format and returns in local time
NOTE: any string not in the format "digits:digits" will be returned as is
USAGE: 
>>>convTimes(['19:45','18:15','5:45','512','FT'])
['01:00','00:00','11:30','512','FT']
'''

if time.daylight:
	offsetHour = time.altzone / 3600
else:
	offsetHour = time.timezone / 3600
hour = int(-offsetHour)
minute = int(-offsetHour * 60 % 60)

def _conv(time):
	if bool(re.match(r'[0-9]{1,2}:[0-9]{1,2}',time)):
		time = list(map(int,time.split(':')))
		time[1]+=minute
		time[0]+=hour
		if time[1]>59:
			time[1]-=60
			time[0]+=1
		elif time[1]<0:
			time[1]+=60
			time[0]-=1
		if time[0]<0:
			time[0]+=24
		elif time[0]>23:
			time[0]-=24
		time = _fix(str(time[0])) +":"+ _fix(str(time[1]))
	return time
			
def _fix(y):
	if len(y)==1:
		y = '0'+y
	return y

def convert(times):
	times = list(map(_conv, times))
	return times
