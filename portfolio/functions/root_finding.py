def root(f, a, b):
    """
    Find the root of a polynomials
    """
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        print 'function evals have same sign'
    c = (a + b) / 2
    while abs(f(c)) < 10e-5:
        if f(c) < 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
    return c

print root(lambda x : x**2 - 2, 2.0, 0.0)