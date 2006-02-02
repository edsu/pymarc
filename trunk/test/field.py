import util
import unittest
from pymarc.record import Record, Field

class FieldTest( unittest.TestCase ):

    def setUp( self ):
        self.field = Field( 
            tag = '245', 
            indicators = [ 0, 1 ], 
            subfields = [ 
                'a', 'Huckleberry Finn: ', 
                'b', 'An American Odyssey'
            ]
         )

    def testString( self ):
        self.assertEquals( str(self.field), 
            '245 01 $aHuckleberry Finn: $bAn American Odyssey')

    def testIndicators( self ):
        assert self.field.indicator1 is 0
        self.assertEqual( self.field.indicator2, 1 ) 
        
    def testSubfieldsCreated( self ):
        subfields = self.field.subfields
        self.assertEqual( len( subfields ), 4 )

    def testSubfieldShort( self ):
        self.assertEqual( self.field['a'], 'Huckleberry Finn: ' )
        self.assertEqual( self.field['z'], None )

    def testSubfields( self ):
        self.assertEqual( self.field.getSubfields( 'a' ), 
            ['Huckleberry Finn: '] )

    def testSubfieldsMulti( self ):
        self.assertEqual( self.field.getSubfields( 'a','b' ), 
            ['Huckleberry Finn: ', 'An American Odyssey' ] )

    def testEncode( self ):
        self.field.asMARC21()

    def testIterator( self ):
        string = ""
        for subfield in self.field:
            string += subfield[0]
            string += subfield[1]
        self.assertEquals( string, "aHuckleberry Finn: bAn American Odyssey" )

    def testValue( self ):
        self.assertEquals( self.field.value(), 
            'Huckleberry Finn: An American Odyssey' )
        controlField = Field( tag='001', data='foobar' )
        self.assertEquals( controlField.value(), "foobar" )

    def testNonIntegerTag( self ):
        # make sure this doesn't throw an exception
        f = Field( tag="3 0", indicators=[0,1], subfields=['a', 'foo'] )

    def testAddSubfield( self ):
        f = Field( tag="245", indicators=[0,1], subfields=['a', 'foo'] )
        f.addSubfield('a','bar')
        self.assertEquals( f.__str__(), '245 01 $afoo$abar')

def suite():
    suite = unittest.makeSuite( FieldTest, 'test' )
    return suite

if __name__ == "__main__":
    unittest.main()


