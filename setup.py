#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright:
#   2020 P. H. <github.com/perfide>
# License:
#   BSD-2-Clause (BSD 2-Clause "Simplified" License)
#   https://spdx.org/licenses/BSD-2-Clause.html

"""Configuration script for setuptools to install px-totp"""

import setuptools

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='px-totp',
    version='0.0.1',
    scripts=['px-totp'],
    author='P. H.',
    author_email='px-totp.perfide@safersignup.de',
    description='Time-based One-Time Password Generator',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/perfide/px-totp',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
)
