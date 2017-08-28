#! /usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__version__ = '0.4.0'

setup(
    author           = 'Christian Heitman',
    author_email     = 'cnheitman@fundacionsadosky.org.ar',
    description      = 'A multiplatform open source Binary Analysis and Reverse engineering Framework',
    download_url     = 'https://github.com/programa-stic/barf-project/tarball/v' + __version__,
    install_requires = [
        'capstone>=3.0.5rc2',
        'networkx',
        'pefile',
        'pydot',
        'pyelftools',
        'pygments',
        'pyparsing',
    ],
    license          = 'BSD 2-Clause',
    name             = 'barf',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Security',
        'Topic :: Software Development :: Disassemblers',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages         = find_packages(exclude=['tests', 'tests.*']),
    url              = 'http://github.com/programa-stic/barf-project',
    scripts          = [
        'scripts/barf-install-solvers.sh',
        'tools/cfg/BARFcfg',
        'tools/cg/BARFcg',
        'tools/gadgets/BARFgadgets',
    ],
    version          = __version__,
    zip_safe         = False
)
