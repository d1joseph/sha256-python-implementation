#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='SHA256',
    version='0.1.0',
    description='Python Distribution Utilities',
    author='Dhiv Joseph',
    packages=find_packages(include=['app', 'sha256.*'])
)