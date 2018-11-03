# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='todoist-capture',
    version='0.1.0',
    description='Capture tasks to your Inbox from command line',
    long_description=readme,
    author='Ege Güneş',
    author_email='egegunes@gmail.com',
    url='https://github.com/egegunes/todoist-capture',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['capture=capture.capture:run']
    }
)
