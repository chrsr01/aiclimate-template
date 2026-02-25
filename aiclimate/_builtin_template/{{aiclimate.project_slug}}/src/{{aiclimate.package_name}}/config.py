"""Configuration loading utilities."""

from __future__ import annotations

from pathlib import Path

import yaml


def load_config(config_path: str | Path = "configs/default.yaml") -> dict:
    """Load a YAML configuration file.

    :param config_path: Path to the YAML config file.
    :returns: Configuration dictionary.
    """
    config_path = Path(config_path)
    with open(config_path) as f:
        return yaml.safe_load(f)
