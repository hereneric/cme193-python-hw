def eval_poly(x, l):
    return sum([x ** i * j for i,j in enumerate(l)])

x = 1
l = [1, 1, 2]
print eval_poly(x, l)
