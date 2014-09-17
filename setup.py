#!/usr/bin/env python
from setuptools import setup, find_packages


__version__ = '0.1'


setup(
    name='watchmbed',
    version=__version__,
    url='http://anthony.land',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        watchmbed=watchmbed.watcher:watch_directory
    """
)
