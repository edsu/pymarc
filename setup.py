version = '3.1.13'

from setuptools import setup

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
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
    install_requires = ['six>=1.9.0',],
    description = 'Read, write and modify MARC bibliographic data',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = list(filter(None, classifiers.split('\n'))),
    test_suite = 'test',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
)
