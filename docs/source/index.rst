.. pymarc documentation master file, created by
   sphinx-quickstart on Thu Jul 21 10:24:11 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pymarc
======

Release v\ |version|

Pymarc is a python library for working with bibliographic data encoded in MARC21.

It should work under python 2.x and 3.x. It provides an API for reading, writing
and modifying MARC records. It was mostly designed to be an emergency
eject seat, for getting your data assets out of MARC and into some kind
of saner representation. However over the years it has been used to
create and modify MARC records, since despite `repeated calls`_ for it to die as a
format, MARC seems to be living quite happily as a zombie.

Below are some common examples of how you might want to use pymarc. If
you run across an example that you think should be here please send a
pull request.

.. _repeated calls: https://web.archive.org/web/20170731163019/http://www.marc-must-die.info/index.php/Main_Page

Reading
~~~~~~~

Most often you will have some MARC data and will want to extract data
from it. Here's an example of reading a batch of records and printing
out the title. If you are curious this example uses the batch file
available here in pymarc repository:

.. code-block:: python

    from pymarc import MARCReader

    with open('test/marc.dat', 'rb') as fh:
        reader = MARCReader(fh)
        for record in reader:
            print(record.title())

    The pragmatic programmer : from journeyman to master /
    Programming Python /
    Learning Python /
    Python cookbook /
    Python programming for the absolute beginner /
    Web programming : techniques for integrating Python, Linux, Apache, and MySQL /
    Python programming on Win32 /
    Python programming : an introduction to computer science /
    Python Web programming /
    Core python programming /
    Python and Tkinter programming /
    Game programming with Python, Lua, and Ruby /
    Python programming patterns /
    Python programming with the Java class libraries : a tutorial for building Web
    and Enterprise applications /
    Learn to program using Python : a tutorial for hobbyists, self-starters, and all
    who want to learn the art of computer programming /
    Programming with Python /
    BSD Sockets programming from a multi-language perspective /
    Design patterns : elements of reusable object-oriented software /
    Introduction to algorithms /
    ANSI Common Lisp /

A pymarc.Record object has a few handy methods like title for
getting at bits of a bibliographic record, others include: author,
isbn, subjects, location, notes,
physicaldescription, publisher, pubyear. But really, to work
with MARC data you need to understand the numeric field tags and
subfield codes that are used to designate various bits of information.
There is a lot more hiding in a MARC record than these methods provide
access to. For example the title method extracts the information
from the 245 field, subfields a and b. You can access
245a like so:

.. code-block:: python

    print(record['245']['a'])

Some fields like subjects can repeat. In cases like that you will want
to use get_fields to get all of them as pymarc.Field objects,
which you can then interact with further:

.. code-block:: python

    for f in record.get_fields('650'):
        print(f)

If you are new to MARC fields Understanding
MARC (http://www.loc.gov/marc/umb/) is a pretty good primer, and the
MARC 21 Formats (http://www.loc.gov/marc/marcdocz.html) page at the
Library of Congress is a good reference once you understand the basics.

Writing
~~~~~~~

Here's an example of creating a record and writing it out to a file.

.. code-block:: python

    from pymarc import Record, Field

    record = Record()
    record.add_field(
        Field(
            tag = '245',
            indicators = ['0','1'],
            subfields = [
                'a', 'The pragmatic programmer : ',
                'b', 'from journeyman to master /',
                'c', 'Andrew Hunt, David Thomas.'
            ]))
    with open('file.dat', 'wb') as out:
        out.write(record.as_marc())

Updating
~~~~~~~~

Updating works the same way, you read it in, modify it, and then write
it out again:

.. code-block:: python

    from pymarc import MARCReader

    with open('test/marc.dat', 'rb') as fh:
       reader = MARCReader(fh)
       record = next(reader)
       record['245']['a'] = 'The Zombie Programmer'
    with open('file.dat', 'wb') as out:
       out.write(record.as_marc())

JSON and XML
~~~~~~~~~~~~

If you find yourself using MARC data a fair bit, and distributing it,
you may make other developers a bit happier by using the JSON or XML
serializations. pymarc has support for both. The main benefit here is
that the UTF8 character encoding is used, rather than the frustratingly
archaic MARC8 encoding. Also they will be able to use JSON and XML tools
to get at the data they want instead of some crazy MARC processing
library like, ahem, pymarc.


API Docs
========

Reader
~~~~~~

.. automodule:: pymarc.reader
    :members:
    :undoc-members:
    :show-inheritance:

Record
~~~~~~

.. automodule:: pymarc.record
    :members:
    :undoc-members:
    :show-inheritance:

Writer
~~~~~~

.. automodule:: pymarc.writer
    :members:
    :undoc-members:
    :show-inheritance:

Field
-----

.. automodule:: pymarc.field
    :members:
    :undoc-members:
    :show-inheritance:

Exceptions
~~~~~~~~~~

.. automodule:: pymarc.exceptions
    :members:
    :undoc-members:
    :show-inheritance:

MarcXML
~~~~~~~

.. automodule:: pymarc.marcxml
    :members:
    :undoc-members:
    :show-inheritance:

Constants
~~~~~~~~~

.. automodule:: pymarc.constants
    :members:
    :undoc-members:
    :show-inheritance:

MARC-8
~~~~~~

.. automodule:: pymarc.marc8
    :members:
    :undoc-members:
    :show-inheritance:

MARC-8 mapping
~~~~~~~~~~~~~~

.. automodule:: pymarc.marc8_mapping
    :members:
    :undoc-members:
    :show-inheritance:

Leader
------

.. automodule:: pymarc.leader
    :members:
    :undoc-members:
    :show-inheritance:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
