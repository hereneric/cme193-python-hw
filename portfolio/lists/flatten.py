def flatten(l):
    result = []
    for element in l:
        if type(element) != list:
            result.append(element)
        else:
            result.extend(flatten(element))
    return result

l = [[1, [2]], [3, 4]]
print flatten(l)
