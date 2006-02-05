import util
from pymarc import MARCReader, Record, Field
import unittest
import os

class Encode( unittest.TestCase ):

    def testEncodeDecode( self ):
        # get raw data from file 
        original = file( 'test/one.dat' ).read()
        # create a record object for the file
        reader = MARCReader(file('test/one.dat'))
        record = reader.next()
        # make sure original data is the same as 
        # the record encoded as MARC
        raw = record.asMARC21()
        self.assertEqual( original, raw )

def suite():
    suite = unittest.makeSuite( Encode, 'test' )
    return suite

if __name__ == "__main__":
    unittest.main()

