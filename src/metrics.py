def extract_circuit_metrics(transpiled_circuit):
    ops = transpiled_circuit.count_ops()
    cx_count = ops.get('cx', 0)
    return {
        "depth": transpiled_circuit.depth(),
        "total_gates": sum(ops.values()),
        "two_qubit_gates": cx_count,
        "physical_qubits_used": transpiled_circuit.num_qubits
    }

def calculate_approximation_ratio(measured_energy, max_cut_value, offset):
    cut_expectation = offset - measured_energy
    return cut_expectation / max_cut_value
