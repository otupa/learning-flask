#!/bin/bash

echo "Acessando Ambiente Poetry"

echo "Verify pyproject.toml"
poetry check
echo

echo "Running Black"
find . -type f -name "*.py" | xargs poetry run black
echo

echo "Running Isort"
find . -type f -name "*.py" | xargs poetry run isort
echo

echo "Running Pylint"
find . -type f -name "*.py" | xargs poetry run pylint
echo

echo "Running Tests with Pylint"
poetry run pytest
echo

echo "Running Tests server flask"
poetry run python manage.py   