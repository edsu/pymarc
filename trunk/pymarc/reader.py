from types import FileType
from cStringIO import StringIO

from pymarc import Record
from pymarc.exceptions import RecordLengthInvalid

class Reader(object):
    """
    A base class for all iterating readers in the pymarc package. 
    """
    def __iter__(self):
        return self

class MARCReader(Reader):
    """
    An iterator class for reading a file of MARC21 records. 

    Simple usage:

        from pymarc import MARCReader

        ## pass in a file object
        reader = MARCReader(file('file.dat'))
        for record in reader:
            ...

        ## pass in marc in transmission format 
        reader = MARCReader(rawmarc)
        for record in reader:
            ...
    """
    def __init__(self, raw_or_file_marc):
        """
        The constructor to which you can pass either raw marc or a file object.
        """
        super(MARCReader, self).__init__()
        if (type(raw_or_file_marc) == FileType): 
            self.file_handle = raw_or_file_marc
        else: 
            self.file_handle = StringIO(raw_or_file_marc)

    def next(self):
        """
        To support iteration. 
        """
        first5 = self.file_handle.read(5)
        if not first5:
            raise StopIteration
        if len(first5) < 5:
            raise RecordLengthInvalid

        length = int(first5)
        chunk = self.file_handle.read(length - 5)
        chunk = first5 + chunk
        record = Record(chunk)
        return record 
