import networkx as nx
from qiskit.quantum_info import SparsePauliOp

def generate_target_graph():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
    return G

def get_ising_hamiltonian(G):
    num_nodes = G.number_of_nodes()
    paulis = []
    coeffs = []
    for i, j in G.edges():
        p = ['I'] * num_nodes
        p[i] = 'Z'
        p[j] = 'Z'
        paulis.append("".join(p[::-1]))
        coeffs.append(0.5)
    offset = len(G.edges) / 2.0
    return SparsePauliOp(paulis, coeffs), offset

def solve_maxcut_brute_force(G):
    n = G.number_of_nodes()
    best_cost = 0
    best_bitstring = None
    for i in range(2**n):
        bitstring = format(i, f'0{n}b')
        cost = 0
        for u, v in G.edges():
            if bitstring[u] != bitstring[v]:
                cost += 1
        if cost > best_cost:
            best_cost = cost
            best_bitstring = bitstring
    return best_cost, best_bitstring
