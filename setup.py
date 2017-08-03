import os.path
import setuptools


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "DESCRIPTION.rst")) as f:
    long_description = f.read()

setuptools.setup(
    name="flake8-import-style", version="0.3.0",
    description="A flake8 plugin to ensure explicit module imports",
    long_description=long_description,
    packages=setuptools.find_packages(),
    author="Stefano Palazzo",
    author_email="stefano.palazzo@gmail.com",
    url="https://github.com/sfstpala/flake8-import-style",
    license="ISC",
    install_requires=[
        "setuptools",
    ],
    test_suite="flake8_import_style.tests",
    entry_points={
        "flake8.extension": [
            "I8 = flake8_import_style:I8",
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
