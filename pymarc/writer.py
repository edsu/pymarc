import pymarc
from pymarc import Record, WriteNeedsRecord

try:
    import xml.etree.ElementTree as ET  # builtin in Python 2.5
except ImportError:
    import elementtree.ElementTree as ET

try:
    # the json module was included in the stdlib in python 2.6
    # http://docs.python.org/library/json.html
    import json
except ImportError:
    # simplejson 2.0.9 is available for python 2.4+
    # http://pypi.python.org/pypi/simplejson/2.0.9
    # simplejson 1.7.3 is available for python 2.3+
    # http://pypi.python.org/pypi/simplejson/1.7.3
    import simplejson as json


class Writer(object):

    def __init__(self, file_handle):
        self.file_handle = file_handle

    def write(self, record):
        if not isinstance(record, Record):
            raise WriteNeedsRecord

    def close(self, close_fh=True):
        """
        Closes the writer.

        If close_fh is False close will also close the underlying file handle
        that was passed in to the constructor. The default is True.
        """
        if close_fh:
            self.file_handle.close()
        self.file_handle = None


class JSONWriter(Writer):
    """
    A class for writing records as an array of MARC-in-JSON objects.

    IMPORTANT: You must the close a JSONWriter,
    otherwise you will not get valid JSON.

    Simple usage::

        >>> from pymarc import JSONWriter

        ### writing to a file
        >>> writer = JSONWriter(open('file.json','wt'))
        >>> writer.write(record)
        >>> writer.close()  # Important!

        ### writing to a string
        >>> string = StringIO()
        >>> writer = JSONWriter(string)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)  # Important!
        >>> print string
    """

    def __init__(self, file_handle):
        """
        You need to pass in a text file like object.
        """
        super(JSONWriter, self).__init__(file_handle)
        self.write_count = 0
        self.file_handle.write('[')

    def write(self, record):
        """
        Writes a record.
        """
        Writer.write(self, record)
        if self.write_count > 0:
            self.file_handle.write(',')
        json.dump(record.as_dict(), self.file_handle, separators=(',', ':'))
        self.write_count += 1

    def close(self, close_fh=True):
        """
        Closes the writer.

        If close_fh is False close will also close the underlying file
        handle that was passed in to the constructor. The default is True.
        """
        self.file_handle.write(']')
        Writer.close(self, close_fh)


class MARCWriter(Writer):
    """
    A class for writing MARC21 records in transmission format.

    Simple usage::

        >>> from pymarc import MARCWriter

        ### writing to a file
        >>> writer = MARCWriter(open('file.dat','wb'))
        >>> writer.write(record)
        >>> writer.close()

        ### writing to a string (Python 2 only)
        >>> string = StringIO()
        >>> writer = MARCWriter(string)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)
        >>> print string

        ### writing to memory (Python 3 only)
        >>> memory = BytesIO()
        >>> writer = MARCWriter(memory)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)
    """

    def __init__(self, file_handle):
        """
        You need to pass in a byte file like object.
        """
        super(MARCWriter, self).__init__(file_handle)

    def write(self, record):
        """
        Writes a record.
        """
        Writer.write(self, record)
        self.file_handle.write(record.as_marc())


class TextWriter(Writer):
    """
    A class for writing records in prettified text MARCMaker format.

    A blank line separates each record.

    Simple usage::

        >>> from pymarc import TextWriter

        ### writing to a file
        >>> writer = TextWriter(open('file.txt','wt'))
        >>> writer.write(record)
        >>> writer.close()

        ### writing to a string
        >>> string = StringIO()
        >>> writer = TextWriter(string)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)
        >>> print string
    """

    def __init__(self, file_handle):
        """
        You need to pass in a text file like object.
        """
        super(TextWriter, self).__init__(file_handle)
        self.write_count = 0

    def write(self, record):
        """
        Writes a record.
        """
        Writer.write(self, record)
        if self.write_count > 0:
            self.file_handle.write('\n')
        self.file_handle.write(str(record))
        self.write_count += 1


class XMLWriter(Writer):
    """
    A class for writing records as a MARCXML collection.

    IMPORTANT: You must the close an XMLWriter, otherwise you will not get
    a valid XML document.

    Simple usage::

        >>> from pymarc import XMLWriter

        ### writing to a file
        >>> writer = XMLWriter(open('file.xml','wb'))
        >>> writer.write(record)
        >>> writer.close()  # Important!

        ### writing to a string (Python 2 only)
        >>> string = StringIO()
        >>> writer = XMLWriter(string)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)  # Important!
        >>> print string

        ### writing to memory (Python 3 only)
        >>> memory = BytesIO()
        >>> writer = XMLWriter(memory)
        >>> writer.write(record)
        >>> writer.close(close_fh=False)  # Important!
    """

    def __init__(self, file_handle):
        """
        You need to pass in a binary file like object.
        """
        super(XMLWriter, self).__init__(file_handle)
        self.file_handle.write(
            b'<?xml version="1.0" encoding="UTF-8"?>')
        self.file_handle.write(
            b'<collection xmlns="http://www.loc.gov/MARC21/slim">')

    def write(self, record):
        """
        Writes a record.
        """
        Writer.write(self, record)
        node = pymarc.record_to_xml_node(record)
        self.file_handle.write(ET.tostring(node, encoding='utf-8'))

    def close(self, close_fh=True):
        """
        Closes the writer.

        If close_fh is False close will also close the underlying file handle
        that was passed in to the constructor. The default is True.
        """
        self.file_handle.write(b'</collection>')
        Writer.close(self, close_fh)
