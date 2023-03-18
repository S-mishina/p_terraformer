# setup.py
from setuptools import setup, find_packages

URL = 'https://github.com/S-mishina/p_terraformer'
AUTHOR = 'S-mishina'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    author=AUTHOR,
    url=URL,
    name='p_terraformer',
    version='0.2',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'p_terraformer = p_terraformer.cli:main'
        ]
}
)
