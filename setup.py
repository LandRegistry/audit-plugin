#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='lraudit',
      version='0.1',
      description='Adds auditing to LR Flask apps',
      author='Land Registry',
      author_email='lr-dev@example.org',
      url='http://github.com/LandRegistry/audit-plugin',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      install_requires=[],
)
