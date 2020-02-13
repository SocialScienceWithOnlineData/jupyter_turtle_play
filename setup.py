#!/usr/bin/env python
### cribbed from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
from setuptools import setup, find_packages

setup(
    name='jupyter_turtle_play',
    version='0.1.0',
    url='https://github.com/SocialScienceWithOnlineData/jupyter_turtle_play.git',
    author='Seth Frey',
    author_email='sfrey@ucdavis.edu',
    description='Wrapper functions (around the "calysto" package) for easy turtle graphics in a jupyterhub environment',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        "calysto",
    ],
)
