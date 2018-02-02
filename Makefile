# interpreter version (ex.: 3.6) or use current
PYTHON := $(PYTHON)

all: test


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


.PHONY: clean_dist
clean_dist:
	if [ -d dist/ ]; then rm -rv dist/; fi;


.PHONY: build_dist
build_dist: clean_dist
	python setup.py sdist bdist_wheel


.PHONY: _check_dist
_check_dist:
	test -d dist/ || ( \
		echo -e "\n--> [!] run 'make build_dist' before!\n" && exit 1 \
	)


.PHONY: upload
upload: _check_dist
	twine upload --skip-existing dist/*
