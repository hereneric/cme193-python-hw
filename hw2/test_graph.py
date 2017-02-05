import numpy as np
from graph import Graph, ERGraph

g1 = Graph([[0,1,1],[1,0,0],[1,0,0]])
g2 = Graph([[0,1,1],[1,0,1],[1,1,0]])
g1.add_node([1])
g2.add_node([1])
print g1.get_matrix()
print g2.get_matrix()
g3 = g1 + g2
print g3.laplacian()
print g3.laplacian_eig()
print np.linalg.eig(g3.laplacian())[1].T[0]
print g3.adjacency_eig()
print np.linalg.eig(g3.matrix)[1].T[0]
print ERGraph(10, 0.1)