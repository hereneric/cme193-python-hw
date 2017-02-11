import numpy as np

def _get_eig(mat, tol):
	"""
	q1(8):compute dominant eigenvector by power iteration
	"""
	b = np.random.randn(len(mat))
	prev_b = np.zeros(len(mat))
	# power iteration
	while np.linalg.norm(b - prev_b, 2) >= tol:
		tmp = mat.dot(b)
		norm = np.linalg.norm(tmp, 2)
		prev_b = b
		b = tmp / norm
	return b

class Graph:
	def __init__(self, ad_matrix):
		"""
		q1(1):initialize the graph with an adjacency matrix
		"""
		if type(ad_matrix) is list:
			ad_matrix = np.asarray(ad_matrix)
		if ad_matrix.shape[0] != ad_matrix.shape[1]:
			raise "not a valid adjacency matrix"
		self.n = ad_matrix.shape[0]
		self.matrix = ad_matrix

	def add_edge(self, i, j):
		"""
		q1(2):add an edge between node i and node j
		"""
		try:
			self.matrix[i][j] = 1
			self.matrix[j][i] = 1
		except IndexError:
			print "please use valid indices"

	def add_node(self, node_list=[]):
		"""
		q1(3):add a node and a list nodes it connect to
		"""
		col = np.zeros((self.n, 1))
		self.matrix = np.concatenate((self.matrix,col), axis=1)
		row = np.zeros((1, self.n + 1))
		self.matrix = np.concatenate((self.matrix,row), axis=0)
		self.n += 1
		for node in node_list:
			self.add_edge(self.n - 1, node)

	def __str__(self):
		return str(self.matrix)

	def get_matrix(self):
		"""
		q1(4):return the adjacency matrix
		"""
		return self.matrix

	def laplacian(self):
		"""
		q1(5):return the laplacian matrix of the graph
		"""
		degree_vec = np.sum(self.matrix, axis=1)
		degree = np.diag(degree_vec)
		la = degree - self.matrix
		return la

	def get_neighbors(self, vertices):
		"""
		q1(6):return the neighborhood of a set of vertices
		"""
		neighbors = set()
		for node in vertices:
			for i in xrange(self.n):
				if self.matrix[node][i] == 1:
					neighbors.add(i)
		return neighbors

	def __add__(self, other):
		"""
		q1(7):add two graphs
		"""
		if other.n != self.n:
			raise "cannot add two graphs with different vertices"
		self.matrix = np.ceil((self.matrix + other.matrix) / 2)
		return Graph(self.matrix)

	def laplacian_eig(self, tol):
		"""
		q1(9):return the dominant eigenvector of laplacian matrix
		"""
		return _get_eig(self.laplacian(), tol)

	def adjacency_eig(self, tol):
		"""
		q1(9):return the dominant eigenvector of adjacency matrix
		"""
		return _get_eig(self.matrix, tol)

class ERGraph(Graph):
	"""
	q1(10):ERGraph is Erdos-Renyi graph, extends Graph
	"""
	def __init__(self, n, p):
		mat = np.zeros((n, n))
		for i in xrange(n):
			for j in xrange(i):
				if np.random.rand() <= p:
					mat[i][j] = 1
					mat[j][i] = 1
		Graph.__init__(self, mat)