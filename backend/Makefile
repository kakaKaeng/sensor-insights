img_uri := 579672773716.dkr.ecr.ap-southeast-1.amazonaws.com/kakakaeng/do-some-stuff:08062025

build:
	$$(aws ecr get-login --no-include-email --region ap-southeast-1)
	@uv export --no-hashes > .deployment/requirements.txt
	docker buildx build --platform linux/amd64 -f .deployment/Dockerfile -t $(img_uri) --push .


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
