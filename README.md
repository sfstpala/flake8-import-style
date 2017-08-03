# flake8-import-style

[![Build](https://img.shields.io/travis/sfstpala/flake8-import-style.svg?style=flat-square)](https://travis-ci.org/sfstpala/flake8-import-style)
[![Coverage](https://img.shields.io/coveralls/sfstpala/flake8-import-style.svg?style=flat-square)](https://coveralls.io/r/sfstpala/flake8-import-style)
[![PyPI](https://img.shields.io/pypi/v/flake8-import-style.svg?style=flat-square)](https://pypi.python.org/pypi/flake8-import-style)

A [flake8](http://flake8.pycqa.org/en/latest/) plugin to ensure explicit module imports.

    pip install flake8_import_style
    flake8 *.py

Errors (enabled by default):

 - `I801 use 'import ...' instead of 'from ... import ...'`

Tested with Python 2.7, 3.4, 3.5, and 3.6.

Type `make test` or `tox` to run the test suite in a virtual environment.
