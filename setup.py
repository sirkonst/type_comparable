#!/usr/bin/env python

from datetime import datetime
from subprocess import check_output, STDOUT
from sys import stderr

from setuptools import setup

# -- versioning
major, minor, build, dev = 0, 0, 0, ''

try:
    build = check_output(
        ['git', 'rev-list', '--count', 'HEAD'], stderr=STDOUT
    ).strip().decode('utf-8')
except Exception as e:
    print(
        '[!] Can not get git revision version: {}'.format(e), file=stderr
    )

try:
    branch = check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stderr=STDOUT
    ).strip().decode('utf-8')
    print('branch=', branch)
    if branch != 'master':
        dev = 'dev{:%Y%m%d}'.format(datetime.utcnow().date())
except Exception as e:
    print(
        '[!] Can not get git branch: {}'.format(e), file=stderr
    )

if dev:
    version = '.'.join(map(str, [major, minor, build, dev]))
else:
    version = '.'.join(map(str, [major, minor, build]))


# -- setuping
setup(
    setup_requires=[
        'setuptools >= 30.4'
    ],
    version=version,
)
