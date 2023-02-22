from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mycli',
    version='0.1',
    packages=find_packages(include=['mycli', 'mycli.cmd', 'mycli.config', 'mycli.utils']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'w_terraformer = mycli.cli:main'
        ]
    }
)

print(find_packages())


