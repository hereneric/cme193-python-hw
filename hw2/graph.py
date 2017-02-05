import numpy as np

def get_eig(mat, tol):
    b = np.random.randn(len(mat))
    prev_b = np.zeros(len(mat))
    while np.linalg.norm(b - prev_b, 2) >= tol:
        tmp = mat.dot(b)
        norm = np.linalg.norm(tmp, 2)
        prev_b = b
        b = tmp / norm
    return b

class Graph:
	def __init__(self, ad_matrix):
		if type(ad_matrix) is list:
			ad_matrix = np.asarray(ad_matrix)
		if ad_matrix.shape[0] != ad_matrix.shape[1]:
			raise "not a valid adjacent matrix"
		self.n = ad_matrix.shape[0]
		self.matrix = ad_matrix

	def add_edge(self, i, j):
		if i >= self.n or j >= self.n or i < 0 or j < 0:
			raise "node not in graph"
		self.matrix[i][j] = 1
		self.matrix[j][i] = 1

	def add_node(self, node_list=[]):
		col = np.zeros((self.n, 1))
		self.matrix = np.concatenate((self.matrix,col), axis=1)
		row = np.zeros((1, self.n + 1))
		self.matrix = np.concatenate((self.matrix,row), axis=0)
		self.n += 1
		for node in node_list:
			self.add_edge(self.n - 1, node)
		print "node added..."

	def __str__(self):
		return str(self.matrix)

	def get_matrix(self):
		return self.matrix

	def laplacian(self):
		degree_vec = np.sum(self.matrix, axis=1)
		degree = np.diag(degree_vec)
		la = degree - self.matrix
		return la

	def get_neighbors(self, vertices):
		neighbors = set()
		for node in vertices:
			for i in xrange(self.n):
				if self.matrix[node][i] == 1:
					neighbors.add(i)
		return neighbors

	def __add__(self, other):
		if other.n != self.n:
			raise "cannot add two graphs with different vertices"
		self.matrix = np.ceil((self.matrix + other.matrix) / 2)
		return Graph(self.matrix)

	def laplacian_eig(self):
		return get_eig(self.laplacian(), 10e-5)

	def adjacency_eig(self):
		return get_eig(self.matrix, 10e-5)

class ERGraph(Graph):
	def __init__(self, n, p):
		mat = np.zeros((n, n))
		for i in xrange(n):
			for j in xrange(i):
				if np.random.rand() <= p:
					mat[i][j] = 1
					mat[j][i] = 1
		Graph.__init__(self, mat)

g1 = Graph([[0,1,1],[1,0,0],[1,0,0]])
g2 = Graph([[0,1,1],[1,0,1],[1,1,0]])
g1.add_node([1])
g2.add_node([1])
print g1.get_matrix()
print g2.get_matrix()
g3 = g1 + g2
# print g3.get_matrix()
# print g1.get_neighbors({1,2})
print g3.laplacian()
print g3.laplacian_eig()
print np.linalg.eig(g3.laplacian())
print g3.adjacency_eig()
print np.linalg.eig(g3.matrix)

print ERGraph(10, 0.1)