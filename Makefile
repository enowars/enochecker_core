UV_FLAGS ?= --inexact
UV_RUN ?= env VIRTUAL_ENV=.venv uv run $(UV_FLAGS)

all: format lint mypy

fix: format-fix lint-fix

format:
	@$(UV_RUN) --group format ruff format --check

format-fix:
	@$(UV_RUN) --group format ruff format

lint:
	@$(UV_RUN) --group lint ruff check

lint-fix:
	@$(UV_RUN) --group lint ruff check --fix

mypy:
	@$(UV_RUN) --group typing mypy src/enochecker_core

build:
	@uv build

.PHONY: all fix format format-fix lint lint-fix mypy build
