#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='{{ project_name }}',
    version='1.0',
    description="",
    author="Example Author",
    author_email='info@example.com',
    url='',
    packages=find_packages(),
    package_data={'{{ project_name }}': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
