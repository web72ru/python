import re

def reg(text, pravilo, flagi=''):
    if flagi:
        return re.findall(r''+'(?' + flagi + ')' + pravilo, text)
    else:
        return re.findall(r'' + pravilo, text)