from qiskit.circuit.library import QAOAAnsatz

def build_qaoa_circuit(hamiltonian, p=2):
    qaoa = QAOAAnsatz(hamiltonian, reps=p)
    return qaoa.decompose()
