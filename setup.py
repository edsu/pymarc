# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
from sys import version_info

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
    version = '2.0',
    url = 'http://cheeseshop.python.org/pypi/pymarc',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = ['pymarc'],
    description = 'read, write and modify MARC bibliographic data',
    classifiers = filter(None, classifiers.split('\n')),
    test_suite = 'test',
)
