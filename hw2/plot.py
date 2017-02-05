import numpy as np
from graph import ERGraph
import matplotlib.pyplot as plt

def get_connectivity(n, p, repeat=1000):
	results = []
	for i in xrange(repeat):
		graph = ERGraph(n, p)
		mat = graph.laplacian()
		results.append(get_matrix_conn(mat))
	return np.mean(results)

def get_matrix_conn(mat):
	eig_vals, _ = np.linalg.eig(mat)
	sort_vals = np.sort(eig_vals)
	return sort_vals[1]

n = 10
results = []
probs = np.asarray(range(0, 101, 5)) / 100.0
for p in probs:
	results.append(get_connectivity(n, p))
plt.plot(probs, results)
plt.xlabel("Probability")
plt.ylabel("Average Connectivity")
plt.title("Average Connectivity V.S. Probability")
plt.show()