# aiclimate

A CLI tool that scaffolds Python ML/data science projects for AI in climate and environmental sciences research.

Built by **AI for Climate and Environmental Sciences**.

## Quick Start

```bash
# Install with uv
uv tool install aiclimate

# Scaffold a new project (interactive)
aiclimate

# Or use with an external cookiecutter template
aiclimate gh:user/template
```

## What You Get

When you run `aiclimate`, you'll be prompted for project details and then a complete project is scaffolded:

```
my-climate-ai-project/
├── pyproject.toml          # uv-compatible, with ML + climate deps
├── justfile                # Task runner recipes
├── .python-version
├── .gitignore
├── README.md
├── .github/workflows/ci.yml
├── configs/
│   └── default.yaml        # Experiment configuration
├── data/
│   ├── raw/                # Original, immutable data
│   ├── processed/          # Cleaned and transformed data
│   └── external/           # Third-party data sources
├── experiments/            # Experiment outputs and logs
├── models/                 # Trained model checkpoints
├── notebooks/
│   └── 01_exploration.ipynb
├── src/<package_name>/
│   ├── __init__.py
│   ├── config.py           # Configuration loading
│   ├── train.py            # Training entrypoint
│   ├── evaluate.py         # Evaluation entrypoint
│   └── predict.py          # Inference entrypoint
└── tests/
    └── test_placeholder.py
```

## Template Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Human-readable project name | My Climate AI Project |
| `project_slug` | Directory name (auto-generated) | my-climate-ai-project |
| `package_name` | Python package name (auto-generated) | my_climate_ai_project |
| `project_description` | Short project description | ... |
| `author_name` | Your name | Your Name |
| `author_email` | Your email | ... |
| `python_version` | Python version | 3.12 |
| `ml_framework` | ML framework (pytorch/tensorflow/jax/none) | pytorch |
| `include_dvc` | Include DVC for data versioning | no |
| `license` | License type | MIT |

## Default Dependencies

Projects come pre-configured with common climate/environmental AI packages:

- **Data**: numpy, pandas, xarray, netCDF4, scipy
- **ML**: scikit-learn + your choice of pytorch/tensorflow/jax
- **Visualization**: matplotlib, seaborn
- **Utilities**: pyyaml, tqdm, loguru
- **Dev tools**: pytest, ruff, jupyter

## Backward Compatibility

aiclimate is built on the cookiecutter engine and can use any existing cookiecutter template:

```bash
aiclimate gh:audreyfeldroy/cookiecutter-pypackage
```

## Development

```bash
# Clone and install
git clone https://github.com/aiclimate/aiclimate.git
cd aiclimate
uv sync

# Run tests
just test-all

# Lint
just lint-check
```

## License

BSD-3-Clause
