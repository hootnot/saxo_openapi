#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

requirements = map(str.strip, open("requirements.txt").readlines())

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Feite Brekeveld",
    author_email='f.brekeveld@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="SAXO Bank OpenAPI REST-API access",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='saxo_openapi',
    name='saxo_openapi',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hootnot/saxo_openapi',
    version='0.4.1',
    zip_safe=False,
)
