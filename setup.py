#!/usr/bin/env python

from setuptools import setup
from versioning import version


setup(
    setup_requires=[
        'setuptools >= 30.4'
    ],
    version=version(0, 2),
)
