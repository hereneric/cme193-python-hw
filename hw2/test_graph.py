import numpy as np
from graph import Graph, ERGraph

def test_graph():
	"""
	unit test for Graph class and ERGraph class in graph.py
	"""
	g1 = Graph([[0,1,1],[1,0,0],[1,0,0]])
	g2 = Graph([[0,0,1],[0,0,1],[1,1,0]])
	g1.add_node([1])
	g2.add_node([])
	assert np.array_equal(g1.get_matrix(), np.asarray([
		[0.0, 1.0, 1.0, 0.0],
		[1.0, 0.0, 0.0, 1.0],
		[1.0, 0.0, 0.0, 0.0],
		[0.0, 1.0, 0.0, 0.0]
	]))
	assert np.array_equal(g2.get_matrix(), np.asarray([
		[0.0, 0.0, 1.0, 0.0],
		[0.0, 0.0, 1.0, 0.0],
		[1.0, 1.0, 0.0, 0.0],
		[0.0, 0.0, 0.0, 0.0]
	]))
	g3 = g1 + g2
	assert np.array_equal(g3.get_matrix(), np.asarray([
		[0.0, 1.0, 1.0, 0.0],
		[1.0, 0.0, 1.0, 1.0],
		[1.0, 1.0, 0.0, 0.0],
		[0.0, 1.0, 0.0, 0.0]
	]))
	assert np.array_equal(g3.laplacian(), np.asarray([
		[2.0, -1.0, -1.0, 0.0],
		[-1.0, 3.0, -1.0, -1.0],
		[-1.0, -1.0, 2.0, 0.0],
		[0.0, -1.0, 0.0, 1.0]
	]))

	laplacian_eig = g3.laplacian_eig(10e-6)
	laplacian_eig_true = np.linalg.eig(g3.laplacian())[1].T[0]
	assert np.allclose(
		laplacian_eig,
		laplacian_eig_true,
		rtol=10e-5
	) or np.allclose(
		-laplacian_eig,
		laplacian_eig_true,
		rtol=10e-5
	)
	adjacency_eig = g3.adjacency_eig(10e-6)
	adjacency_eig_true = np.linalg.eig(g3.matrix)[1].T[0]
	assert np.allclose(
		adjacency_eig,
		adjacency_eig_true,
		rtol=10e-5
	) or np.allclose(
		-adjacency_eig,
		adjacency_eig_true,
		rtol=10e-5
	)
	erg =  ERGraph(1000, 0.5)
	assert np.allclose(np.sum(erg.matrix), (1000 ** 2 - 1000) * 0.5, rtol=0.1)

test_graph()