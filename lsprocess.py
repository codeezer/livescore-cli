import re

def pretty_array(rows,flag):
    contents = '\n'.join(map(lambda r: r.text, rows))
    
    
    
    if flag == 'scores':
        _contents = re.split('# ', contents)
        livescores = _contents[0]
        _livescores = re.split('\n',livescores)
        return [re.split('   |-', _livescores[i]) for i in range(len(_livescores))]
    
    elif flag == 'table':
        _contents = re.split('# ', contents)
        scoreTable = _contents[1]
        _scoreTable = re.split('\n',scoreTable)
        return [re.split('   ', _scoreTable[i]) for i in range(len(_scoreTable))]

    elif flag == 'scorers':
        _contents = re.split('     ',contents)
        return [re.split('   ', _contents[i]) for i in range(len(_contents))]
