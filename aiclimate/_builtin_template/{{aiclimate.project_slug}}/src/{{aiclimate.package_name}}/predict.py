"""Inference entrypoint."""

from __future__ import annotations

from loguru import logger

from {{ aiclimate.package_name }}.config import load_config


def main() -> None:
    """Run inference pipeline."""
    config = load_config()
    logger.info("Starting inference with config: {}", config)

    # TODO: Implement your inference pipeline here
    # 1. Load trained model from models/
    # 2. Load input data
    # 3. Generate predictions
    # 4. Save outputs

    logger.info("Inference complete.")


if __name__ == "__main__":
    main()
