from pymarc import Record, Field, WriteNeedsRecord, NoActiveFile
from types import *
from cStringIO import StringIO

class Writer( object ):
    
    def write( self ):
        pass

class MARCWriter( Writer ):
    """
    A class for writing MARC21 records in transmission format.

    Simple usage:

        from pymarc import MARCWriter

        ## pass in a file
        writer = MARCWriter(file('file.dat','w'))
        writer.write(record)
   
        ## use StringIO if you want to write to a string
        string = StringIO()
        writer = MARCWriter(string)
        writer.write(record)
        print string
    """

    def __init__(self, f):
        """
        You need to pass in a file like object.
        """
        self.fh = f

    def write(self, record):
        """
        Writes a record.
        """
        if type(record) != Record:
            raise WriteNeedsRecord
        self.fh.write(record.asMARC21())

    def close( self ):
        """
        Closes the file.
        """
        self.fh.close()
        self.fh = None

