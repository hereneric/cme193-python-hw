def filter(func, l):
    return [i for i in l if func(i)]

l = range(8)
print filter(lambda x: x % 2 == 0, l)
