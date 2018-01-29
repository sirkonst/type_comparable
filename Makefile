# interpreter version (ex.: 3.6) or use current
PYTHON := $(PYTHON)

all: build_dist


.PHONY: install
install:
	pip install --no-cache-dir .


.PHONY: install_dev
install_dev:
	pip install --no-cache-dir --editable .[develop]


.PHONY: test
test:
	if [ -z "$(PYTHON)" ]; then \
	    tox --recreate --skip-missing-interpreters; \
	else \
	    tox --recreate -e py$(PYTHON); \
	fi;
