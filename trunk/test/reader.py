import util
import unittest
import pymarc
import re

class MARCReaderFileTest( unittest.TestCase ):
    """
    Tests for the pymarc.MARCReader class which provides iterator
    based access to a MARC file.
    """ 

    def setUp( self ):
        self.reader = pymarc.MARCReader(file('test/test.dat'))

    def testIterator( self ):
        count = 0
        for record in self.reader:
            count += 1
        self.assertEquals(count, 10, 'found expected amt of MARC21 records')

    def testString( self ):
        ## basic test of stringification
        startsWithLeader = re.compile( "^LDR" )
        hasNumericTag = re.compile( "\n\d\d\d " )
        for record in self.reader:
            text = str(record)
            self.failUnless( startsWithLeader.search(text), 'got leader')
            self.failUnless(hasNumericTag.search(text), 'got a tag')

class MARCReaderStringTest(MARCReaderFileTest):

    def setUp(self):
        raw = file('test/test.dat').read()
        self.reader = pymarc.reader.MARCReader(raw)

    # inherit same tests from MARCReaderTestFile

def suite():
    fileSuite = unittest.makeSuite(MARCReaderFileTest, 'test')
    stringSuite = unittest.makeSuite(MARCReaderStringTest, 'test')
    suite = unittest.TestSuite((fileSuite, stringSuite))
    return suite

if __name__ == "__main__":
    unittest.main()
