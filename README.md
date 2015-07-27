```
 _ __  _   _ _ __ ___   __ _ _ __ ___
| '_ \| | | | '_ ` _ \ / _` | '__/ __|
| |_) | |_| | | | | | | (_| | | | (__
| .__/ \__, |_| |_| |_|\__,_|_|  \___|
|_|    |___/
```

[![Build Status](https://travis-ci.org/edsu/pymarc.svg)](http://travis-ci.org/edsu/pymarc)
[![Downloads](https://pypip.in/d/pymarc/badge.png)](http://pypi.org/pymarc)

pymarc is a python library for working with bibliographic data encoded in
[MARC21](http://en.wikipedia.org/wiki/MARC_standards). It should work under
python 2.x and 3.x. It provides an API for reading, writing and modifying
MARC records. It was mostly designed to be an emergency eject seat, for
getting your data assets out of MARC and into some kind of saner
representation. However over the years it has been used to create and
modify MARC records, since despite
[repeated calls](http://marc-must-die.info/index.php/Main_Page) for it to die
as a format, MARC seems to be living quite happily as a zombie.

Below are some common examples of how you might want to use pymarc. If
you run across an example that you think should be here please send a
pull request.

### Reading

Most often you will have some MARC data and will want to extract data
from it. Here's an example of reading a batch of records and printing out
the title. If you are curious this example uses the batch file
available here in pymarc repository:

```python
from pymarc import MARCReader
with open('test/marc.dat', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.title())
```
```
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
```

A `pymarc.Record` object has a few handy methods like `title` for getting at
bits of a bibliographic record, others include: `author`, `isbn`, `subjects`,
`location`, `notes`, `physicaldescription`, `publisher`, `pubyear`. But
really, to work with MARC data you need to understand the numeric field tags
and subfield codes that are used to designate various bits of information. There
is a lot more hiding in a MARC record than these methods provide access to.
For example the `title` method extracts the information from the `245` field,
subfields `a` and `b`. You can access `245a` like so:

```python
print(record['245']['a'])
```

Some fields like subjects can repeat. In cases like that you will want to use
`get_fields` to get all of them as `pmarc.Field` objects, which you can then
interact with further:

```python
for f in record.get_fields('650'):
    print(f)
```

If you are new to MARC fields [Understanding
MARC](http://www.loc.gov/marc/umb/) is a pretty good primer, and the [MARC 21
Formats](http://www.loc.gov/marc/marcdocz.html) page at the Library of Congress is a good reference once you understand the basics.

### Writing

Here's an example of creating a record and writing it out to a file.

```python
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
out = open('file.dat', 'wb')
out.write(record.as_marc())
out.close()
```

### Updating

Updating works the same way, you read it in, modify it, and then write it out
again:

```python
from pymarc import MARCReader
with open('test/marc.dat', 'rb') as fh:
    reader = MARCReader(fh)
    record = next(reader)
    record['245']['a'] = 'The Zombie Programmer'

out = open('file.dat', 'wb')
out.write(record.as_marc())
out.close()
```


### JSON and XML

If you find yourself using MARC data a fair bit, and distributing it, you may
make other developers a bit happier by using the JSON or XML serializations.
pymarc has support for both. The main benefit here is that the UTF8 character
encoding is used, rather than the frustratingly archaic MARC8 encoding. Also
they will be able to use JSON and XML tools to get at the data they want instead
of some crazy MARC processing library like, ahem, pymarc.

Installation
------------

You'll probably just want to use pip to install pymarc:

    pip install pymarc

If you'd like to download and install the latest source you'll need git:

    git clone git://github.com/edsu/pymarc.git

You'll also need [setuptools](https://pypi.python.org/pypi/setuptools#installation-instructions). Once you have the source and setuptools run the pymarc test
suite to make sure things are in order with the distribution:

    python setup.py test

And then install:

    python setup.py install

Support
-------

The pymarc developers encourage you to join the [pymarc Google Group](http://groups.google.com/group/pymarc) if you need help.  Also, please feel free to use [issue tracking](https://github.com/edsu/pymarc/issues) on Github to to submit feature requests or bug reports. If you've got an itch to scratch, please scratch it, and send merge requests on [Github](http://github.com/edsu/pymarc).

If you start working with MARC you may feel like you need moral support
in addition to technical support. The [#code4lib](irc://freenode.net/code4lib)
channel on [Freenode](http://freenode.net) is a good place for both.

Copyright
---------

Copyright (c) 2005-2014 Gabriel Farrell, Mark Matienzo, Geoffrey Spear, Ed Summers

License
-------

[BSD](http://www.opensource.org/licenses/bsd-license.php)
