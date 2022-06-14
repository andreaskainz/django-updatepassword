#!/bin/env python3
from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='django-updatepassword',
    version=version,
    description='Provides a custom updatepassword management command',
    author='Andreas Kainz',
    url='https://github.com/andreaskainz/django-updatepassword',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
)
