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

    If you would like to have your Record object contain unicode strings
    use the to_unicode parameter:

        reader = MARCReader(file('file.dat'), to_unicode=True)

    This will decode from MARC-8 or UTF-8 depending on the value in the 
    MARC leader at position 9. 
    
    If you find yourself in the unfortunate position of having data that 
    is utf-8 encoded without the leader set appropriately you can use 
    the force_utf8 parameter:

        reader = MARCReader(file('file.dat'), to_unicode=True, force_utf8=True)

    """
    def __init__(self, marc_target, to_unicode=False, force_utf8=False):
        """
        The constructor to which you can pass either raw marc or a file-like
        object. Basically the argument you pass in should be raw MARC in 
        transmission format or an object that responds to read().
        """
        super(MARCReader, self).__init__()
        self.to_unicode = to_unicode
        self.force_utf8 = force_utf8
        if (hasattr(marc_target, "read") and callable(marc_target.read)):
            self.file_handle = marc_target
        else: 
            self.file_handle = StringIO(marc_target)

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
        record = Record(chunk, 
                        to_unicode=self.to_unicode,
                        force_utf8=self.force_utf8)
        return record 

def map_records(f, *files):
    """
    Applies a given function to each record in a batch. You can
    pass in multiple batches.

    >>> def print_title(r): 
    >>>     print r['245']
    >>> 
    >>> map_records(print_title, file('marc.dat'))
    """
    for file in files:
        map(f, MARCReader(file))

