def my_max1(x, y):
    if x > y:
        return x
    else:
        return y

def my_max2(x, y):
    if x > y:
        return x
    return y

print my_max1(1, 2), my_max2(1, 2)
print my_max1(1, 1), my_max2(1, 1)
print my_max1(2, 1), my_max2(2, 1)
