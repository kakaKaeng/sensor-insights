check:
	IS_TESTING=True uv run mypy .
	@uv run ruff format --check

test:
	IS_TESTING=True uv run pytest

format:
	@uv run ruff check --fix
	@uv run ruff format

run-local:
	@uv run manage.py runserver 0.0.0.0:8000
