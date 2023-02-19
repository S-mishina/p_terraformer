from setuptools import setup, find_packages
import subprocess
import platform

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="terraform-python-wrapper",
    version="0.0.1",
    author="S-mishina",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mycommand=terraformer-wrapper.cli:main'
        ]
    }
)
print(find_packages())
operation=platform.system()
subprocess.call(['bash', 'setup/setup.sh',"-e",operation])
