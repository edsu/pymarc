from pymarc import Record, Field
from constants import END_OF_RECORD
from exceptions import *
from types import *
import string

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

        ## pass in a filename
        reader = MARCReader( 'file.dat' )
        for record in reader:
            ...
    
        ## pass in a file object
        f = file( 'file.dat' );
        reader = MARCReader( f )
        for record in reader:
            ...
    
    """

    def __init__( self, f ):
        """
        The constructor which you can pass either the full path to a file
        you want to read, or a file object.
        """
        if ( type( f ) == FileType ): self.fh = f
        else: self.fh = file( f, 'r' )

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

