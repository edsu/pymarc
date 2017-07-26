import os
import sys
import json

from six import Iterator
from six import BytesIO, StringIO

from pymarc import Record, Field
from pymarc.exceptions import RecordLengthInvalid

class Reader(Iterator):
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

        reader = MARCReader(file('file.dat'), to_unicode=True,
            force_utf8=True)

    If you find yourself in the unfortunate position of having data that is
    mostly utf-8 encoded but with a few non-utf-8 characters, you can also use
    the utf8_handling parameter, which takes the same values ('strict',
    'replace', and 'ignore') as the Python Unicode codecs (see
    http://docs.python.org/library/codecs.html for more info).

    """
    def __init__(self, marc_target, to_unicode=True, force_utf8=False,
        hide_utf8_warnings=False, utf8_handling='strict'):
        """
        The constructor to which you can pass either raw marc or a file-like
        object. Basically the argument you pass in should be raw MARC in
        transmission format or an object that responds to read().
        """
        super(MARCReader, self).__init__()
        self.to_unicode = to_unicode
        self.force_utf8 = force_utf8
        self.hide_utf8_warnings = hide_utf8_warnings
        self.utf8_handling = utf8_handling
        if (hasattr(marc_target, "read") and callable(marc_target.read)):
            self.file_handle = marc_target
        else:
            self.file_handle = BytesIO(marc_target)

    def close(self):
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None

    def __next__(self):
        """
        To support iteration.
        """
        first5 = self.file_handle.read(5)
        if not first5:
            raise StopIteration
        if len(first5) < 5:
            raise RecordLengthInvalid

        try:
            length = int(first5)
        except ValueError:
            raise RecordLengthInvalid

        chunk = self.file_handle.read(length - 5)
        chunk = first5 + chunk
        record = Record(chunk,
                        to_unicode=self.to_unicode,
                        force_utf8=self.force_utf8,
                        hide_utf8_warnings=self.hide_utf8_warnings,
                        utf8_handling=self.utf8_handling)
        return record

def map_records(f, *files):
    """
    Applies a given function to each record in a batch. You can
    pass in multiple batches.

    >>> def print_title(r):
    >>>     print(r['245'])
    >>>
    >>> map_records(print_title, file('marc.dat'))
    """
    for file in files:
        list(map(f, MARCReader(file)))

class JSONReader(Reader):
    def __init__(self,marc_target,encoding='utf-8',stream=False):
        self.encoding = encoding
        if hasattr(marc_target,'read') and callable(marc_target.read):
            self.file_handle = marc_target
        else:
            if os.path.exists(marc_target):
                self.file_handle = open(marc_target,'r')
            else:
                self.file_handle = StringIO(marc_target)
        if stream:
            sys.stderr.write("Streaming not yet implemented, your data will be loaded into memory\n")
        self.records =json.load(self.file_handle,strict=False)

    def __iter__(self):
        if hasattr(self.records,'__iter__') and not isinstance(self.records, dict):
        	self.iter = iter(self.records)
        else:
        	self.iter = iter([self.records])
        return self

    def __next__(self):
        jobj = next(self.iter)
        rec = Record()
        rec.leader = jobj['leader']
        for field in jobj['fields']:
            k,v = list(field.items())[0]
            if 'subfields' in v and hasattr(v,'update'):
                # flatten m-i-j dict to list in pymarc
                subfields = []
                for sub in v['subfields']:
                    for code,value in sub.items():
                        subfields.extend((code,value))
                fld = Field(tag=k,subfields=subfields,indicators=[v['ind1'], v['ind2']])
            else:
                fld = Field(tag=k,data=v)
            rec.add_field(fld)
        return rec

