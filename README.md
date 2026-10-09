# qff-2026-quantum-drift-PS-O1

**Team:** Quantum Drift
**Author:** ADABALA VEERA VENKATA RAMAKRISHNA
**Track:** Quantum Optimization
**Problem Statement:** PS-O1 (Max-Cut via QAOA)
**Event:** SRM University-AP Qiskit Fall Fest 2026 Flagship Hackathon

## Overview
This repository contains Phase 1 of the Geometry-Aware Quantum Cloud Challenge. We implement a parameterized Quantum Approximate Optimization Algorithm (QAOA) to solve the Max-Cut problem on a 5-node cycle graph. 

The core focus is benchmarking logical formulation against two distinct physical topologies:
* **Processor A**: 5-qubit linear baseline.
* **Processor B**: 7-qubit heavy-hex-inspired graph.

By observing transpiled depth, SWAP insertions, and noisy expectation values, this project demonstrates how hardware topology dictating qubit routing directly impacts the algorithmic success (approximation ratio) of QAOA.

## Execution Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Execute the full end-to-end pipeline via the Jupyter Notebook: `main.ipynb`
3. View the generated tables in `results/tables/` and figures in `results/figures/`.
