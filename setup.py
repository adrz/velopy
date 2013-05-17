#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages
from velopy import __version__

setup(name="velopy",
      version=__version__,
      description="JCDecaux library for python",
      license="MIT",
      author="Adrien",
      author_email="",
      url="http://github.com/",
      packages = find_packages(),
      keywords= "JCDecaux API",
      zip_safe = True)
