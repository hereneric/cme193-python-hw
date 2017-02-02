import numpy as np
from scipy.linalg import toeplitz

def compute(A, B, lamb):
	I = np.identity(B.shape[0])
	return A.dot((B - lamb*I))

n = 200
m = 500
A = np.random.randn(n,m)
B = toeplitz(np.random.randn(1,m))

print A + A
print A.dot(A.T)
print A.T.dot(A)
print A.dot(B)
print compute(A,B,1)