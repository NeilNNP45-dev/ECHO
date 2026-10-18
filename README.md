# ECHO

ECHO is a modular Python lab for exploring reinforcement learning, agent behavior, reward design, exploration, learning, and adaptation through custom environments and measurable experiments.

## Project goals

- Explore reinforcement learning fundamentals.
- Implement a custom grid-world environment.
- Study tabular Q-learning.
- Investigate reward design and exploration strategies.
- Compare agent performance through measurable experiments.

## Planned technology

Python with `pygame`, `numpy`, `matplotlib`, and `pytest`.

## Project structure

- `echo/environments/` will contain the custom grid-world environment.
- `echo/agents/` will contain learning agents, starting with tabular Q-learning.
- `echo/experiments/` will coordinate experiment runs.
- `echo/analysis/` will contain metrics and performance analysis.
- `tests/` will hold environment and agent tests.
- The top-level `experiments/` directory is reserved for generated experiment outputs.
- `docs/` is reserved for project documentation.
- `main.py` will become the application entry point.

## Development roadmap

1. Build and test the grid-world environment.
2. Implement and test a tabular Q-learning agent.
3. Add experiment running, metrics, and performance analysis.

## Status

ECHO is in its initial setup stage. The environment, agent, experiment, and analysis features described above are planned and have not been implemented yet.

## Setup

Install the dependencies from the project root with:

```bash
python -m pip install -r requirements.txt
```

Then run the test suite with:

```bash
pytest
```

The application entry point and tests are placeholders at this stage; functionality will be added incrementally.
