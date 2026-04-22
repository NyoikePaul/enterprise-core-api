.PHONY: test lint scan

lint:
	ruff check .

test:
	pytest tests/

scan:
	bandit -r src/
	checkov -d .
