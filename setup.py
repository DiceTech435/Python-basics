# REUSE MY PACKAGES IN OTHER PROJECTS, MAKE IT DISTRIBUTABLE
from setuptools import setup, find_packages

setup(
    name="CustomFuncs",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
)

# The install it Locally with:
    # pip install -e .