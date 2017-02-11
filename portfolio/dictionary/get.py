from collections import *
"""
Dictionary get() exercise
"""

def histogram(l):
    table = {}
    for element in l:
        table[element] = table.get(element, 0) + 1
    return table

def histogram_counter(l):
    cnt = Counter()
    for element in l:
        cnt[element] += 1
    return cnt

print histogram([1,2,3,'a',1,'2','a'])
print histogram_counter([1,2,3,'a',1,'2','a'])