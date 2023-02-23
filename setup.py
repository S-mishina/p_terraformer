from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import platform
import logging

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='p_terraformer',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'p_terraformer = p_terraformer.cli:main'
        ]
}
)
