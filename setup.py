# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='todoist-capture',
    version='1.0.2',
    description='Capture tasks to your Inbox from command line',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Ege Güneş',
    author_email='egegunes@gmail.com',
    license="GPLv3",
    url='https://github.com/egegunes/todoist-capture',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['capture=capture.capture:run']
    }
)
