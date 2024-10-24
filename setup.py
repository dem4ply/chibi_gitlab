#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'chibi>=0.14.0', 'chibi-requests>=1.0.0' ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="libreria para hacer llamadas al api de gitlab",
    entry_points={
        'console_scripts': [
            'chibi_gitlab=chibi_gitlab.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_gitlab',
    name='chibi_gitlab',
    packages=find_packages(include=['chibi_gitlab', 'chibi_gitlab.*']),
    url='https://github.com/dem4ply/chibi_gitlab',
    version='0.0.1',
    zip_safe=False,
)