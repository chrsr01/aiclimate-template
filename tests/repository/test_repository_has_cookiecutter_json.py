"""Tests for `repository_has_template_config` function."""

import pytest

from aiclimate.repository import repository_has_template_config


def test_valid_repository() -> None:
    """Validate correct response if `cookiecutter.json` file exist."""
    assert repository_has_template_config('tests/fake-repo')


@pytest.mark.parametrize(
    'invalid_repository', (['tests/fake-repo-bad', 'tests/unknown-repo'])
)
def test_invalid_repository(invalid_repository) -> None:
    """Validate correct response if `cookiecutter.json` file not exist."""
    assert not repository_has_template_config(invalid_repository)
