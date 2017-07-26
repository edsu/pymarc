version = '3.1.7'

from setuptools import setup

install_requires = ['six>=1.9.0']
try:
    import xml.etree
except ImportError:
    install_requires.append('elementtree>=1.2.6')

import sys
if sys.version_info < (2 , 6):
    install_requires.append('simplejson>=1.7.3')
del sys

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup(
    name = 'pymarc',
    version = version,
    url = 'http://github.com/edsu/pymarc',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = ['pymarc'],
    install_requires = install_requires,
    description = 'read, write and modify MARC bibliographic data',
    classifiers = list(filter(None, classifiers.split('\n'))),
    test_suite = 'test',
)
