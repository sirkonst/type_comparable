all: build_dist


.PHONY: install
install:
	pip install --no-cache-dir .


.PHONY: install_dev
install_dev:
	pip install --no-cache-dir --editable .[develop]


.PHONY: test
test:
	pytest --cov tests/
