#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""\
Setup file
"""

from distutils.core import setup

setup(
    name='tryalgo',
    version='1.3.0',
    description='Basic and advanced algorithms and datastructures',
    author='Jill-Jênn Vie and Christoph Dürr',
    author_email='christoph.durr@lip6.fr',
    license='MIT',
    url='https://jilljenn.github.io/tryalgo/',
    keywords='algorithms data-structures programming competition',
    packages=['tryalgo'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
