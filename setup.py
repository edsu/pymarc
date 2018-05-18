version = '3.1.10'

from setuptools import setup

install_requires = ['six>=1.9.0']
try:
    import xml.etree
except ImportError:
    install_requires.append('elementtree>=1.2.6')

import sys
if sys.version_info < (2 , 6):
    install_requires.append('simplejson>=1.7.3')

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Text Processing :: General
"""

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'pymarc',
    version = version,
    url = 'http://github.com/edsu/pymarc',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = ['pymarc'],
    install_requires = install_requires,
    description = 'Read, write and modify MARC bibliographic data',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = list(filter(None, classifiers.split('\n'))),
    test_suite = 'test',
)
