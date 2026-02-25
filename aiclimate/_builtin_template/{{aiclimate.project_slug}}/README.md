# {{ aiclimate.project_name }}

{{ aiclimate.project_description }}

## Setup

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

## Project Structure

```
├── configs/          # Experiment configuration files
├── data/
│   ├── raw/          # Original, immutable data
│   ├── processed/    # Cleaned and transformed data
│   └── external/     # Data from third-party sources
├── experiments/      # Experiment outputs and logs
├── models/           # Trained model checkpoints
├── notebooks/        # Jupyter notebooks for exploration
├── src/{{ aiclimate.package_name }}/
│   ├── config.py     # Configuration loading
│   ├── train.py      # Training entrypoint
│   ├── evaluate.py   # Evaluation entrypoint
│   └── predict.py    # Inference entrypoint
└── tests/            # Unit tests
```

## Usage

```bash
# Run training
uv run python -m {{ aiclimate.package_name }}.train

# Run evaluation
uv run python -m {{ aiclimate.package_name }}.evaluate

# Run tests
uv run pytest

# Lint code
uv run ruff check .
```
