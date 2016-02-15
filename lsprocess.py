import re


#---Init Code block solely for splitting a single row of table---#

#List the clubs whose name includes numbers
ClubsWithNum = ["Schalke 04", "Hannover 96", "Mainz 05"]
reg = []
#Join the list to a single string
club_pattern = "("+"|".join(ClubsWithNum)+")"
reg.append(club_pattern)
#For all other club names with spaces . or - in between
text = "((?:[A-Za-z.-]+\s)+)"
reg.append(text)
#Split by the remaining spaces
reg.append("\s")
#Merge into a huge regex string
split_pattern = "|".join(reg)
regex = re.compile(split_pattern)

#----End split Init---#

#Function to split the rows using the above regex
#Inputs a string, Returns a list
def regSplit(row):
	b = regex.split(row)
	#Remove any none elements
	c = [x for x in b if x]
	return c


def pretty_array(rows,flag):
    contents = '\n'.join(map(lambda r: r.text, rows))
    
    
    
    if flag == 'scores':
        _contents = re.split('# ', contents)
        livescores = _contents[0]
        _livescores = re.split('\n',livescores)
        return [re.split('   | - ', _livescores[i]) for i in range(len(_livescores))]
    
    elif flag == 'table':
        _contents = re.split('# ', contents)
        scoreTable = _contents[1]
        _scoreTable = re.split('\n',scoreTable)
        return [re.split('   ', _scoreTable[i]) for i in range(len(_scoreTable))]

    elif flag == 'scorers':
        _contents = re.split('     ',contents)
        return [re.split('   ', _contents[i]) for i in range(len(_contents))]
