import util
import unittest

from pymarc import Record, Field
from pymarc.exceptions import *

class RecordTest( unittest.TestCase ):

    def test_add_field( self ):
        record = Record()
        field = Field( 
            tag = '245', 
            indicators = [ '1', '0' ], 
            data = [ 'a', 'Python', 'c', 'Guido' ] )
        record.addField( field )
        self.failUnless( field in record.fields, msg='found field' )

    def test_quick_access( self ):
        record = Record() 
        title = Field( 
            tag = '245', 
            indicators = [ '1', '0' ],
            data = [ 'a', 'Python', 'c', 'Guido' ] )
        record.addField( title )
        self.assertEqual( record['245'], title, 'short access' )
        self.assertEqual( record['999'], None, 'short access with no field' )

    def test_field_not_found( self ):
        record = Record()
        self.assertEquals( len( record.fields ), 0 )

    def test_find( self ):
        record = Record() 
        subject1 = Field( 
            tag = '650', 
            indicators = [ '', '0' ], 
            data = [ 'a', 'Programming Language' ] )
        record.addField( subject1 )
        subject2 = Field( 
            tag = '650', 
            indicators = [ '', '0' ], 
            data = [ 'a', 'Object Oriented' ] )
        record.addField( subject2 )
        found = record.getFields( '650' )
        self.assertEqual( found[0], subject1, 'getFields() item 1' )
        self.assertEqual( found[0], subject1, 'getFields() item 2' )
        found = record.getFields()
        self.assertEqual(len(found), 2, 'getFields() with no tag')

    def test_multi_find( self ):
        record = Record() 
        subject1 = Field( 
            tag = '650', 
            indicators = [ '', '0' ], 
            data = [ 'a', 'Programming Language' ] )
        record.addField( subject1 )
        subject2 = Field( 
            tag = '651', 
            indicators = [ '', '0' ], 
            data = [ 'a', 'Object Oriented' ] )
        record.addField( subject2 )
        found = record.getFields( '650', '651' )
        self.assertEquals( len(found), 2 )

    def test_bad_leader( self ):
        record = Record()
        self.failUnlessRaises( RecordLeaderInvalid, 
            record.decodeMARC, 'foo' )

    def test_bad_base_ddress( self ):
        record = Record()
        self.failUnlessRaises( BaseAddressInvalid,
            record.decodeMARC, '00695cam  2200241Ia 45x00' )

    def test_title( self ):
        record = Record()
        self.assertEquals( record.title(), None )
        record.addField( Field( '245', [0,1], 
            subfields=[ 'a', "Foo :", 'b', 'bar' ] ) )
        self.assertEquals( record.title(), 'Foo :bar' )

        record = Record()
        record.addField( Field( '245', [0,1], 
            subfields=[ 'a', "Farghin" ] ) )
        self.assertEquals( record.title(), "Farghin" )

    def test_isbn( self ):
        record = Record()
        self.assertEquals( record.isbn(), None ) 
        record.addField( Field( '020', [0,1], subfields=['a', '123456789' ] ) )
        self.assertEquals( record.isbn(), '123456789' )


def suite():
    suite = unittest.makeSuite( RecordTest, 'test' )
    return suite 

if __name__ == "__main__":
    unittest.main()


