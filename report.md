# Phase 1 Scientific Report: Processor Architecture Impact on QAOA
## 1. What changed in the compiled circuits?
The logical QAOA ansatz assumes all-to-all connectivity. When transpiled:
* **Processor A:** The cycle graph cannot map natively to a linear topology. The transpiler inserts multiple SWAP operations.
* **Processor B:** The branching structure provides slightly more routing flexibility, resulting in different SWAP overheads.
## 2. Why did routing overhead differ?
Processor A's strict linear layout creates a bottleneck. Processor B's auxiliary qubits allow alternate routing paths.
## 3. How did noise degrade the cut?
Every SWAP gate decomposes into 3 CX gates. Processor A's higher SWAP count translates to a deeper circuit with more CX gates, degrading the final expectation value under depolarizing noise.
