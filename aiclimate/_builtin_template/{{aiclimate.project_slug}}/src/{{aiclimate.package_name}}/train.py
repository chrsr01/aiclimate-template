"""Training entrypoint."""

from __future__ import annotations

from loguru import logger

from {{ aiclimate.package_name }}.config import load_config


def main() -> None:
    """Run training pipeline."""
    config = load_config()
    logger.info("Starting training with config: {}", config)

    # TODO: Implement your training pipeline here
    # 1. Load data
    # 2. Preprocess
    # 3. Train model
    # 4. Save model to models/

    logger.info("Training complete.")


if __name__ == "__main__":
    main()
