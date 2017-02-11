class Rational:
    """
    Class of Rational Numbers
    Can do add, sub, mul, div, can compare
    """
    def __init__(self, p, q=1):
        g = self.gcd(p, q)
        self.p = p / g
        self.q = q / g

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def __add__(self, other):
        p = self.p * other.q + other.p * self.q
        q = self.q * other.q
        return Rational(p, q)

    def __neg__(self):
        return Rational(-self.p, self.q)

    def __sub__(self, other):
    	return self.__add__(-other)

    def __mul__(self, other):
        p = self.p * other.p
        q = self.q * other.q
        return Rational(p, q)

    def __div__(self, other):
        p = self.p * other.q
        q = self.q * other.p
        return Rational(p, q)

    def __eq__(self, other):
    	return self.p == other.p and self.q == other.q

    def __float__(self):
    	return 1.0 * self.p / self.q

    def __repr__(self):
        return str(self.p) + '/' + str(self.q)
