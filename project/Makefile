APP_PATH := restapi
.DEFAULT_GOAL := help

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  clean       remove all temporary files"
	@echo "  lint        run the code linters"
	@echo "  test        run all the tests"
	@echo "  run         run flask app"
	@echo ""

clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf .coverage .mypy_cache .pytest_cache

lint:
	poetry run isort --profile=black --lines-after-imports=2 ${APP_PATH}
	poetry run black ${APP_PATH}
	poetry run flake8 --ignore=W503,E501,E402,F401,F821 ${APP_PATH}
	poetry run mypy ${APP_PATH} --ignore-missing-imports
	poetry run bandit -r ${APP_PATH} -s B101,B104

test:
	poetry run pytest tests/

run:
	poetry run flask run

.PHONY: help test lint clean run