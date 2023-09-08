# tests/test_console.py
"""Tests for the console module."""
import click.testing
import pytest


from src.fictional_octo_guacamole import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0