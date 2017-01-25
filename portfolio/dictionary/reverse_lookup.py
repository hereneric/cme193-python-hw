def reverse_lookup(dic, x):
    result = []
    for key, val in dic.iteritems():
        if val == x:
            result.append(key)
    return result

print reverse_lookup({'a':1, 'b':2, 'c':1}, 1)
