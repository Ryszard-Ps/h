# -*- coding: utf-8 -*-
"""
xlsx_data.

-----
Separate data to objects
-----
And Easy to Setup
`````````````````
And run it:
.. code:: bash
    $ pip install git+https://github.com/Ryszard-Ps/xlsx_data.git

"""

from codecs import open
from os import path

from setuptools import find_packages, setup
from xlsx_data.version import version

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='xlsx_data',
    version=version,
    description='Separate data to objects',
    long_description=long_description,
    url='https://github.com/Ryszard-Ps/xlsx_data.git',
    author='Ricardo Pascual',
    author_email='ricardopascual.developer@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status ::  5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public Licence v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(exclude=['docs', 'tests']),
)
