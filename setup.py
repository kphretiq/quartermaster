#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="quartermaster",
    version="0.4",
    description="Get fiscal quarter",
    long_description="trivial class to get quarter from a user-defined gregorian fiscal year.",
    author="pathetiq kphretiq",
    author_email="kphretiq@gmail.com",
    maintainer="pathetiq kphretiq",
    url="https://github.com/kphretiq/quartermaster",
    download_url="https://github.com/kphretiq/quartermaster",
    packages=["quartermaster", "tests"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        ]
     )

