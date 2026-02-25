"""Allow aiclimate to be executable through `python -m aiclimate`."""

from aiclimate.cli import main

if __name__ == "__main__":
    main(prog_name="aiclimate")
