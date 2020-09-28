from collections import Counter
from string import ascii_letters

def count_words(sentence):
    a = ''
    for i in sentence:
        if i in set(ascii_letters + ' ' + '\'' + ',' + '	' + '_') or i in ('0','1', '2', '3', '4', '5', '6', '7', '8', '9'):
            a = a + i.replace(',',' ').replace('	',' ').replace('_',' ').lower()
    b = [i.replace('\'','') if i.startswith('\'') and i.endswith('\'') else i for i in a.split()]
    return dict(Counter(b))

print(count_words("go's,'go',go, Go, 1, 1, 1"))