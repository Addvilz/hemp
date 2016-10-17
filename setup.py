#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='Hemp',
    version="0.0.7",
    description='Tools for Fabric',
    long_description=readme,
    author='Addvilz',
    author_email='mrtreinis@gmail.com',
    url='https://github.com/Addvilz/hemp',
    download_url='https://github.com/Addvilz/hemp',
    license='Apache 2.0',
    platforms='UNIX',
    packages=find_packages(),
    install_requires=[
        "fabric>=1.12",
        "pyyaml>=3.12"
    ],
    entry_points={
        'console_scripts': [
            'hemp = hemp.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ],
)
