"""Evaluation entrypoint."""

from __future__ import annotations

from loguru import logger

from {{ aiclimate.package_name }}.config import load_config


def main() -> None:
    """Run evaluation pipeline."""
    config = load_config()
    logger.info("Starting evaluation with config: {}", config)

    # TODO: Implement your evaluation pipeline here
    # 1. Load trained model from models/
    # 2. Load test data
    # 3. Compute metrics
    # 4. Save results to experiments/

    logger.info("Evaluation complete.")


if __name__ == "__main__":
    main()
