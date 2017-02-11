"""
zip and unzip using zip()
"""

def coordinate(list_x, list_y):
    return zip(list_x, list_y)

def un_zip(l):
    return [list(t) for t in zip(*l)]
print coordinate([1,1,1], [2,2,3])
print un_zip(coordinate([1,1,1],[2,2,3]))
