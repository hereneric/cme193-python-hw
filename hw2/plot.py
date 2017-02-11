"""
q2(1):algebraic connectivity simulation and plot
"""
import numpy as np
from graph import ERGraph
import matplotlib.pyplot as plt

def get_connectivity(n, p, repeat=1000):
	"""
	compute connectivity multiple times and take average
	"""
	results = []
	for i in xrange(repeat):
		graph = ERGraph(n, p)
		mat = graph.laplacian()
		results.append(get_matrix_conn(mat))
	return np.mean(results)

def get_matrix_conn(mat):
	"""
	return the second smallest eigenvalue
	"""
	eig_vals, _ = np.linalg.eig(mat)
	sort_vals = np.sort(eig_vals)
	return sort_vals[1]

# the number of nodes in the graph
n = 10
results = []
# probabilitys from 0 to 1, stepsize=0.05
probs = np.asarray(range(0, 101, 5)) / 100.0
for p in probs:
	results.append(get_connectivity(n, p))
plt.plot(probs, results)
plt.xlabel("Probability")
plt.ylabel("Average Connectivity")
plt.title("Average Connectivity V.S. Probability")
plt.show()