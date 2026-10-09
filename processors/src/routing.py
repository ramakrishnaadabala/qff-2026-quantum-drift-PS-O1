import json
from qiskit import transpile
from qiskit.transpiler import CouplingMap

def load_processor_spec(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def transpile_circuit(logical_circuit, processor_spec, seed=42):
    cmap = CouplingMap(processor_spec["coupling_map"])
    basis_gates = processor_spec["basis_gates"]
    transpiled = transpile(logical_circuit, coupling_map=cmap, basis_gates=basis_gates, optimization_level=1, seed_transpiler=seed)
    return transpiled
