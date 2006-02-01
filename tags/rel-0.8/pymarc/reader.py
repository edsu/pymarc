from pymarc import Record, Field
from constants import END_OF_RECORD
from exceptions import *
from types import *
from cStringIO import StringIO

class Reader( object ):
    """
    A base class for all iterating readers in the pymarc package. 
    """
    def __iter__( self ):
        return self

class MARCReader( Reader ):
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

    def __init__(self, f):
        """
        The constructor which you can pass either raw marc or a file object.
        """
        if (type(f) == FileType): self.fh = f
        else: self.fh = StringIO(f)

    def next( self ):
        """
        To support iteration. 
        """
        first5 = self.fh.read( 5 )
        if not first5:
            raise StopIteration
        if len( first5 ) < 5:
            raise RecordLengthInvalid

        length = int( first5 )
        chunk = self.fh.read( length - 5 )
        chunk = first5 + chunk
        r = Record( chunk )
        return r 

