UV_FLAGS ?= --inexact
UV_RUN ?= env VIRTUAL_ENV=.venv uv run $(UV_FLAGS)

all: format lint mypy test

fix: format-fix lint-fix

format:
	@$(UV_RUN) --group dev ruff format --check

format-fix:
	@$(UV_RUN) --group dev ruff format

lint:
	@$(UV_RUN) --group dev ruff check

lint-fix:
	@$(UV_RUN) --group dev ruff check --fix

mypy:
	@$(UV_RUN) --group dev mypy src/enochecker_core

build:
	@uv build

test:
	@test -z "$(shell ls tests 2>/dev/null)" || \
		$(UV_RUN) --group dev pytest -v

.PHONY: all fix format format-fix lint lint-fix mypy build test
