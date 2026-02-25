"""pytest fixtures which are globally available throughout the suite."""

import os
import shutil
from pathlib import Path
from typing import TypedDict

import pytest

from aiclimate import utils
from aiclimate.config import DEFAULT_CONFIG

USER_CONFIG = """
templates_dir: '{templates_dir}'
replay_dir: '{replay_dir}'
"""


@pytest.fixture(autouse=True)
def isolated_filesystem(monkeypatch, tmp_path) -> None:
    """Ensure filesystem isolation, set the user home to a tmp_path."""
    root_path = tmp_path.joinpath("home")
    root_path.mkdir()
    templates_dir = root_path.joinpath(".aiclimate_templates/")
    replay_dir = root_path.joinpath(".aiclimate_replay/")
    monkeypatch.setitem(DEFAULT_CONFIG, 'templates_dir', str(templates_dir))
    monkeypatch.setitem(DEFAULT_CONFIG, 'replay_dir', str(replay_dir))

    monkeypatch.setenv("HOME", str(root_path))
    monkeypatch.setenv("USERPROFILE", str(root_path))


def backup_dir(original_dir, backup_dir) -> bool:
    """Generate backup directory based on original directory."""
    # If the default original_dir is pre-existing, move it to a temp location
    if not os.path.isdir(original_dir):
        return False

    # Remove existing stale backups before backing up.
    if os.path.isdir(backup_dir):
        utils.rmtree(backup_dir)

    shutil.copytree(original_dir, backup_dir)
    return True


def restore_backup_dir(original_dir, backup_dir, original_dir_found) -> None:
    """Restore default contents."""
    original_dir_is_dir = os.path.isdir(original_dir)
    if original_dir_found:
        # Delete original_dir if a backup exists
        if original_dir_is_dir and os.path.isdir(backup_dir):
            utils.rmtree(original_dir)
    else:
        # Delete the created original_dir.
        # There's no backup because it never existed
        if original_dir_is_dir:
            utils.rmtree(original_dir)

    # Restore the user's default original_dir contents
    if os.path.isdir(backup_dir):
        shutil.copytree(backup_dir, original_dir)
    if os.path.isdir(original_dir):
        utils.rmtree(backup_dir)


@pytest.fixture(scope='function')
def clean_system(request) -> None:
    """Fixture. Simulates a clean system with no configured or cloned cookiecutters.

    It runs code which can be regarded as setup code as known from a unittest
    TestCase. Additionally it defines a local function referring to values
    which have been stored to local variables in the setup such as the location
    of the cookiecutters on disk. This function is registered as a teardown
    hook with `request.addfinalizer` at the very end of the fixture. Pytest
    runs the named hook as soon as the fixture is out of scope, when the test
    finished to put it another way.

    During setup:

    * Back up the `~/.aiclimaterc` config file to `~/.aiclimaterc.backup`
    * Back up the `~/.aiclimate_templates/` dir to `~/.aiclimate_templates.backup/`
    * Back up the `~/.aiclimate_replay/` dir to
      `~/.aiclimate_replay.backup/`
    * Starts off a test case with no pre-existing `~/.aiclimaterc` or
      `~/.aiclimate_templates/` or `~/.aiclimate_replay/`

    During teardown:

    * Delete `~/.aiclimate_templates/` only if a backup is present at
      `~/.aiclimate_templates.backup/`
    * Delete `~/.aiclimate_replay/` only if a backup is present at
      `~/.aiclimate_replay.backup/`
    * Restore the `~/.aiclimaterc` config file from
      `~/.aiclimaterc.backup`
    * Restore the `~/.aiclimate_templates/` dir from `~/.aiclimate_templates.backup/`
    * Restore the `~/.aiclimate_replay/` dir from
      `~/.aiclimate_replay.backup/`

    """
    # If ~/.aiclimaterc is pre-existing, move it to a temp location
    user_config_path = os.path.expanduser('~/.aiclimaterc')
    user_config_path_backup = os.path.expanduser('~/.aiclimaterc.backup')
    if os.path.exists(user_config_path):
        user_config_found = True
        shutil.copy(user_config_path, user_config_path_backup)
        os.remove(user_config_path)
    else:
        user_config_found = False

    # If the default templates_dir is pre-existing, move it to a
    # temp location
    templates_dir = os.path.expanduser('~/.aiclimate_templates')
    templates_dir_backup = os.path.expanduser('~/.aiclimate_templates.backup')
    templates_dir_found = backup_dir(templates_dir, templates_dir_backup)

    # If the default aiclimate_replay_dir is pre-existing, move it to a
    # temp location
    aiclimate_replay_dir = os.path.expanduser('~/.aiclimate_replay')
    aiclimate_replay_dir_backup = os.path.expanduser('~/.aiclimate_replay.backup')
    aiclimate_replay_dir_found = backup_dir(
        aiclimate_replay_dir, aiclimate_replay_dir_backup
    )

    def restore_backup() -> None:
        # If it existed, restore ~/.aiclimaterc
        # We never write to ~/.aiclimaterc, so this logic is simpler.
        if user_config_found and os.path.exists(user_config_path_backup):
            shutil.copy(user_config_path_backup, user_config_path)
            os.remove(user_config_path_backup)

        # Carefully delete the created ~/.aiclimate_templates dir only in certain
        # conditions.
        restore_backup_dir(
            templates_dir, templates_dir_backup, templates_dir_found
        )

        # Carefully delete the created ~/.aiclimate_replay dir only in
        # certain conditions.
        restore_backup_dir(
            aiclimate_replay_dir,
            aiclimate_replay_dir_backup,
            aiclimate_replay_dir_found,
        )

    request.addfinalizer(restore_backup)


@pytest.fixture(scope='session')
def user_dir(tmp_path_factory):
    """Fixture that simulates the user's home directory."""
    return tmp_path_factory.mktemp('user_dir')


class UserConfigData(TypedDict):
    templates_dir: str
    replay_dir: str


@pytest.fixture(scope='session')
def user_config_data(user_dir) -> UserConfigData:
    """Fixture that creates 2 Cookiecutter user config dirs.

     It will create it in the user's home directory.

    * `templates_dir`
    * `aiclimate_replay`

    :returns: Dict with name of both user config dirs
    """
    templates_dir = user_dir.joinpath('templates')
    templates_dir.mkdir()
    replay_dir = user_dir.joinpath('aiclimate_replay')
    replay_dir.mkdir()
    return {
        'templates_dir': str(templates_dir),
        'replay_dir': str(replay_dir),
    }


@pytest.fixture(scope='session')
def user_config_file(user_dir, user_config_data) -> str:
    """Fixture that creates a config file called `config`.

     It will create it in the user's home directory, with YAML from
     `user_config_data`.

    :param user_dir: Simulated user's home directory
    :param user_config_data: Dict of config values
    :returns: String of path to config file
    """
    config_file = user_dir.joinpath('config')

    config_text = USER_CONFIG.format(**user_config_data)
    config_file.write_text(config_text)
    return str(config_file)


@pytest.fixture
def output_dir(tmp_path) -> str:
    """Fixture to prepare test output directory."""
    output_path = tmp_path.joinpath("output")
    output_path.mkdir()
    return str(output_path)


@pytest.fixture
def clone_dir(tmp_path: Path) -> Path:
    """Simulate creation of a directory called `clone_dir` inside of `tmp_path`. \
    Returns a str to said directory."""
    clone_dir = tmp_path.joinpath("clone_dir")
    clone_dir.mkdir()
    return clone_dir
