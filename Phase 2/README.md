# QFF 2026 Phase 2 — PS-O1

**Team:** Quantum Drifters

**Problem statement:** PS-O1, weighted six-vertex Max-Cut
**Processor D SHA-256:** `8b88e1f5ced09531fe674cc48731162fdbf7db72b915bf4e44be5e608116a1e8`

## Overview

`main.ipynb` loads the locked graph from `data/instance.json`, verifies the QUBO and exact optimum, optimizes p=1 QAOA with five fixed starts, evaluates Processor B and the frozen Processor D in ideal/noisy simulation, records Processor A's capacity limit, runs the required Bell checks, and regenerates result tables and figures. The official organizer module `qff_phase2.py` is unchanged.

## Results (4096 shots; random baseline r=0.614, P_opt=0.031)

| Processor | Condition | Executable | Best cut | r | r_best | P_opt |
|---|---|---:|---:|---:|---:|---:|
| A | ideal | no (6 needed; 5 available) | — | — | — | — |
| A | noisy | no (6 needed; 5 available) | — | — | — | — |
| B | ideal | yes | 22.0 | 0.7118 | 1.0000 | 0.0730 |
| B | noisy | yes | 22.0 | 0.7015 | 1.0000 | 0.0698 |
| D | ideal | yes | 22.0 | 0.7066 | 1.0000 | 0.0696 |
| D | noisy | yes | 22.0 | 0.6975 | 1.0000 | 0.0642 |

See `report.md`, `results/tables/`, and `results/figures/` for full analysis and artifacts.

## Reproduce

Python 3.10–3.12:

```bash
python -m venv opt-env
source opt-env/bin/activate
pip install -r requirements.txt
jupyter nbconvert --execute --to notebook main.ipynb
```

On Windows, activate with `opt-env\Scripts\activate`.

## AI-use disclosure

GitHub Copilot (AI assistant using Copilot SDK in VS Code) was used to help draft and validate notebook code, visualizations, and documentation. The team is responsible for checking the locked inputs, organizer utilities, and all reported results.
