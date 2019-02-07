# pandas-diff

This is a small tool to compare pandas dataframes.
It is tested under python3.7.

## Install

Setup a a virtual python environment:

    python3 -m venv .venv

Install requirements:

    .venv/bin/python -m pip install -U pip setuptools
    .venv/bin/pip install -r etc/requirements.txt

Install package requirements and the package itself:

    .venv/bin/python -m pip install -e .

For usage information, run:

    .venv/bin/compare_dataframes --help

## Tests

To run tests, you need the dev dependencies:

    .venv/bin/pip install -r etc/requirements_dev.txt

Run tests:

    .venv/bin/zope-testrunner --path . -s tests --color --shuffle
