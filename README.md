# qff-2026-quantum-drift-PS-01

**Phase 1 Submission: PS-01: Max-Cut on a Graph**

**Team:** Quantum Drift
**Track:** Quantum Optimization
**Problem Statement:** PS-O1 (Max-Cut via QAOA)
**Event:** SRM University-AP Qiskit Fall Fest 2026 Flagship Hackathon

**Team Members:**
* **Ramakrishna Adabala** (Leader) - Rajamahendri Institute of Engineering & Technology
* **Asha Dharmani** - Rajamahendri Institute of Engineering & Technology
* **Nayomi G** - Rajamahendri Institute of Engineering & Technology
* **Gunda Saranya** - Rajamahendri Institute of Engineering & Technology
* **G Swathi** - Rajamahendri Institute of Engineering & Technology


## Overview
This repository contains Phase 1 of the Geometry-Aware Quantum Cloud Challenge. We implement a parameterized Quantum Approximate Optimization Algorithm (QAOA) to solve the Max-Cut problem on a 5-node cycle graph.

The core focus is benchmarking logical formulation against two distinct physical topologies as per the final official benchmark configuration:
* **Processor A**: 5-qubit linear baseline.
* **Processor B**: 9-qubit heavy-hex topology.

By observing transpiled depth, SWAP insertions, and noisy expectation values, this project demonstrates how hardware topology dictating qubit routing directly impacts the algorithmic success (approximation ratio) of QAOA.


## Execution Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Execute the full end-to-end pipeline via the Jupyter Notebook: `main.ipynb`
