INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)

.DEFAULT_GOAL := help

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  install     install packages and prepare environment"
	@echo "  clean       remove all temporary files"
	@echo "  lint        run the code linters"
	@echo "  test        run all the tests"
	@echo ""

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP) .coverage .mypy_cache .pytest_cache

lint: $(INSTALL_STAMP)
	$(POETRY) run isort --profile=black --lines-after-imports=2 ./
	$(POETRY) run black ./
	$(POETRY) run flake8 --ignore=W503,E501,E402,F401,F821 ./
	$(POETRY) run mypy ./ --ignore-missing-imports
	$(POETRY) run bandit -r ./ -s B101,B104

test: $(INSTALL_STAMP)
	$(POETRY) run pytest ./

.PHONY: help test lint clean install