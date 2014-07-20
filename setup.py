#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup


setup(
    name='wasipaid',
    url='https://github.com/miracle2k/wasipaid-python',
    version='0.1',
    license='BSD',
    author=u'Michael Elsdörfer',
    author_email='michael@elsdoerfer.com',
    description=
        'wasipaid command line client & library',
    py_modules=['wasipaid'],
    install_requires=['click>=2.4', 'requests>=2.0.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points="""[console_scripts]\rwasipaid = wasipaid:cli\n""",
)
