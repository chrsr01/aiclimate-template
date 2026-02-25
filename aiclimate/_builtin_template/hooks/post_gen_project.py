#!/usr/bin/env python
"""Post-generation hook: initialize git repo and run uv sync."""

import subprocess
import sys


def main():
    """Initialize git and install dependencies."""
    # Initialize git repository
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial scaffold from aiclimate"],
            check=True,
            capture_output=True,
        )
        print("[aiclimate] Git repository initialized.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[aiclimate] Git not available, skipping repo initialization.")

    # Install dependencies with uv
    try:
        subprocess.run(["uv", "sync"], check=True)
        print("[aiclimate] Dependencies installed with uv.")
    except FileNotFoundError:
        print("[aiclimate] uv not found. Run 'uv sync' to install dependencies.")
    except subprocess.CalledProcessError:
        print("[aiclimate] uv sync failed. Run 'uv sync' manually to install dependencies.")


if __name__ == "__main__":
    main()
