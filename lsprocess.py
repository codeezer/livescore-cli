import re

def pretty_array(rows,flag):
    contents = '\n'.join(map(lambda r: r.text, rows))
    _contents = re.split('# ', contents)
    
    livescores = _contents[0]
    _livescores = re.split('\n',livescores)
    
    scoreTable = _contents[1]
    _scoreTable = re.split('\n',scoreTable)
    
    if flag == 'scores':
        return [re.split('   |-', _livescores[i]) for i in range(len(_livescores))]
    else:
        return [re.split('   ', _scoreTable[i]) for i in range(len(_scoreTable))]
