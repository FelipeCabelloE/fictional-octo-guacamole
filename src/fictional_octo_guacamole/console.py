# src/fictional_octo_guacamole/console.py
import textwrap

import click
import requests

from . import private_vars, wikipedia


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=private_vars.__version__)
def main():
    """The hypermodern Python project."""
    data = wikipedia.random_page()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))