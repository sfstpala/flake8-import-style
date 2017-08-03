python ?= python3.6
package = flake8_import_style

all: $(package).egg-info
$(package).egg-info: setup.py requirements-dev.txt bin/pip
	bin/pip install -r requirements-dev.txt && touch $@
bin/pip: bin/python
	bin/python -m pip install -I pip wheel
bin/python:
	$(python) -m venv .

test: all
	bin/coverage run setup.py test
	bin/coverage html
	bin/coverage report --fail-under=100
	bin/flake8 setup.py $(package)
	bin/check-manifest
	bin/python setup.py check -mrs
	bin/pip list --outdated

clean:
	rm -rf *.egg-info $(shell find $(package) -name "__pycache__")
	rm -rf *.pyc $(shell find $(package) -name "*.pyc")
	rm -rf bin lib lib64 include pip-selfcheck.json pyvenv.cfg
	rm -rf share build dist .tox .coverage htmlcov
