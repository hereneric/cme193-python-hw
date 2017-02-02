import numpy as np

n = 200
C = np.random.rand(n,n)
p = 0.8
C = (C < p) * 1.0
largest_sin = np.linalg.norm(C, 2)
print largest_sin
print 'We find that n * p approximately equals largest singular value'