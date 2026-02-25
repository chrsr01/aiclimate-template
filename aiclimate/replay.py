"""
aiclimate.replay.

-------------------
"""

from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING, Any

from aiclimate.utils import get_context_key, make_sure_path_exists

if TYPE_CHECKING:
    from pathlib import Path


def get_file_name(replay_dir: Path | str, template_name: str) -> str:
    """Get the name of file."""
    suffix = '.json' if not template_name.endswith('.json') else ''
    file_name = f'{template_name}{suffix}'
    return os.path.join(replay_dir, file_name)


def dump(replay_dir: Path | str, template_name: str, context: dict[str, Any]) -> None:
    """Write json data to file."""
    make_sure_path_exists(replay_dir)

    try:
        get_context_key(context)
    except ValueError as e:
        msg = 'Context is required to contain an aiclimate or cookiecutter key'
        raise ValueError(msg) from e

    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, 'w', encoding="utf-8") as outfile:
        json.dump(context, outfile, indent=2)


def load(replay_dir: Path | str, template_name: str) -> dict[str, Any]:
    """Read json data from file."""
    replay_file = get_file_name(replay_dir, template_name)

    with open(replay_file, encoding="utf-8") as infile:
        context: dict[str, Any] = json.load(infile)

    try:
        get_context_key(context)
    except ValueError as e:
        msg = 'Context is required to contain an aiclimate or cookiecutter key'
        raise ValueError(msg) from e

    return context
