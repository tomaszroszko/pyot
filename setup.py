#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages
from pyot import __version__

setup(name="pyot",
    version=__version__,
    description="Opentopic library for python",
    license="MIT",
    author="Tomasz Roszko",
    author_email="tomaszroszko@gmail.com",
    url="https://github.com/tomaszroszko/pyot",
    packages=find_packages(),
    keywords="opentopic library",
    zip_safe=True,
    install_requires=(
        "requests==2.2.1",
    ),
)