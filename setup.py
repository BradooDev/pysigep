#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from codecs import open
from setuptools import setup, find_packages

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'pysigep',
                            '__version__.py')

about = {}
with open(version_path, 'r') as f:
    exec (f.read(), about)

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r') as history_file:
    history = history_file.read()

requirements = [
    'lxml==3.7.3',
    'requests==2.13.0',
    'Pillow==4.1.0',
    'Jinja2==2.9.6',
    'zeep',
]

test_requirements = [
    'coveralls',
    'flake8',
]

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Natural Language :: Portuguese',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: 2",
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    url=about['__url__'],
    download_url=about['__download_url__'],
    packages=find_packages(include=['pysigep']),
    package_dir={'pysigep': 'pysigep'},
    include_package_data=True,
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    keywords='correios sigep sigepweb frete rastreamento development api',
    classifiers=classifiers,
    platforms=['any'],
    test_suite='tests',
    tests_require=test_requirements,
)
