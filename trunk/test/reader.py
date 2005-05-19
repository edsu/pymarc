import util
import unittest
import pymarc
import re

class MARCReaderFilenameTest( unittest.TestCase ):
    """
    Tests for the pymarc.MARCReader class which provides iterator
    based access to a MARC file.
    """ 

    def setUp( self ):
        self.reader = pymarc.MARCReader( 'test/test.dat' )

    def testIterator( self ):
        count = 0
        for record in self.reader:
            count += 1
        self.assertEquals( count, 10, 'found expected amt of MARC21 records' )

    def testString( self ):
        ## basic test of stringification
        startsWithLeader = re.compile( "^LDR" )
        hasNumericTag = re.compile( "\n\d\d\d " )
        for record in self.reader:
            text = str( record )
            self.failUnless( startsWithLeader.search( text ), 'got leader' )
            self.failUnless( hasNumericTag.search( text ), 'got a tag' )

class MARCReaderFileTest( MARCReaderFilenameTest ):

    def setUp( self ):
        self.reader = pymarc.reader.MARCReader( file( 'test/test.dat' ) )

    # inherit same tests from MARCReaderTestFile

def suite():
    filenameSuite = unittest.makeSuite( MARCReaderFilenameTest, 'test' )
    fileSuite = unittest.makeSuite( MARCReaderFileTest, 'test' )
    suite = unittest.TestSuite( (filenameSuite, fileSuite ) )
    return suite

if __name__ == "__main__":
    unittest.main()
