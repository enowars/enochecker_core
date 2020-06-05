lint:
	python -m isort -c -rc enochecker_core/
	python -m black --line-length 160 --check enochecker_core/
	python -m flake8 --select F --per-file-ignores="__init__.py:F401" enochecker_core/
	python -m mypy enochecker_core/

format:
	python -m isort -rc enochecker_core/
	python -m black --line-length 160 enochecker_core/

test:
	pip install .
	python -m pytest
