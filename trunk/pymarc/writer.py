from pymarc import Record, Field, WriteNeedsRecord, NoActiveFile
from types import *
import string

class Writer( object ):
    
    def write( self ):
        pass

class MARCWriter( Writer ):
    """
    A class for writing MARC21 records in transmission format.

    Simple usage:

        from pymarc import MARCWriter

        ## pass in a filename
        writer = MARCWriter( 'file.dat' )
        writer.write( record )
    
        ## pass in a file object
        f = file( 'file.dat' );
        writer = MARCWriter( f )
        writer.write( record )
    """

    def __init__( self, f ):
        """
        The constructor which you can pass either the full path to a file
        you want to write to, or a file object.
        """
        if ( type( f ) == FileType ): self.fh = f
        else: self.fh = file( f, 'w' )

    def write( self, record ):
        if type( record ) != Record:
            raise WriteNeedsRecord
        if type( self.fh ) != file:
            raise NoActiveFile
        self.fh.write( record.encodeMARC() )

    def close( self ):
        self.fh.close()
        self.fh = None

