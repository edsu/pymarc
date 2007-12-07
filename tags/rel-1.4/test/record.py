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

    def test_bad_base_address( self ):
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
    
    def test_author( self ):
        record = Record()
        self.assertEquals( record.author(), None)
        record.addField( Field( '100', [1,0], subfields=['a', 'Bletch, Foobie,', 'd', '1979-1981.'] ) )
        self.assertEquals( record.author(), 'Bletch, Foobie, 1979-1981.')
        
        record = Record()
        record.addField( Field( '130', [0,' '], subfields=['a', 'Bible.', 'l', 'Python.'] ) )
        self.assertEquals( record.author(), None)

    def test_uniformtitle( self ):
        record = Record()
        self.assertEquals( record.uniformtitle(), None )
        record.addField( Field( '130', [0,' '], 
            subfields=[ 'a', "Tosefta.", 'l', "English.", 'f', "1977." ] ) )
        self.assertEquals( record.uniformtitle(), "Tosefta. English. 1977." )

        record = Record()
        record.addField( Field( '240', [1,4], 
            subfields=[ 'a', "The Pickwick papers.", 'l', "French." ] ) )
        self.assertEquals( record.uniformtitle(), "The Pickwick papers. French." )
    
    def test_subjects( self ):
        record = Record()
        r1 = '=630  0\\$aTosefta.$lEnglish.$f1977.'
        r2 = '=600  10$aLe Peu, Pepe.'
        shlist = [r1, r2]
        self.assertEquals( record.subjects(), [] )
        record.addField( Field( '630', [0,' '], 
            subfields=[ 'a', "Tosefta.", 'l', "English.", 'f', "1977." ] ) )
        record.addField( Field( '730', [0,' '], 
            subfields=[ 'a', "Tosefta.", 'l', "English.", 'f', "1977." ] ) )
        record.addField( Field( '600', [1,0], 
            subfields=[ 'a', "Le Peu, Pepe." ] ) )
        self.assertEquals( len( record.subjects() ), 2 )
        self.assertEquals( record.subjects()[0].__str__(), r1 )
        self.assertEquals( record.subjects()[1].__str__(), r2 )
        rshlist = [rsh.__str__() for rsh in record.subjects()]
        self.assertEquals( shlist, rshlist )
     
    def test_added_entries( self ):
        record = Record()
        ae1 = '=730  0\\$aTosefta.$lEnglish.$f1977.'
        ae2 = '=700  10$aLe Peu, Pepe.'
        aelist = [ae1, ae2]
        self.assertEquals( record.addedentries(), [] )
        record.addField( Field( '730', [0,' '], 
            subfields=[ 'a', "Tosefta.", 'l', "English.", 'f', "1977." ] ) )
        record.addField( Field( '700', [1,0], 
            subfields=[ 'a', "Le Peu, Pepe." ] ) )
        record.addField( Field( '245', [0,0],
            subfields=[ 'a', "Le Peu's Tosefa." ] ) )
        self.assertEquals( len( record.addedentries() ), 2 )
        self.assertEquals( record.addedentries()[0].__str__(), ae1 )
        self.assertEquals( record.addedentries()[1].__str__(), ae2 )
        raelist = [rae.__str__() for rae in record.addedentries()]
        self.assertEquals( aelist, raelist )

    def test_location( self ):
        record = Record()
        loc1 = '=852  \\\\$aAmerican Institute of Physics.$bNiels Bohr Library and Archives.$eCollege Park, MD'
        loc2 = '=852  01$aCtY$bMain$hLB201$i.M63'
        loclist = [loc1, loc2]
        self.assertEquals( record.location(), [] )
        record.addField( Field('040', [' ',' '],
            subfields=[ 'a', 'DLC', 'c', 'DLC' ] ) )
        record.addField( Field('852', [' ',' '],
            subfields=[ 'a', 'American Institute of Physics.',
                'b', 'Niels Bohr Library and Archives.',
                'e', 'College Park, MD' ] ) )
        record.addField( Field('852', [0,1],
            subfields=['a', 'CtY', 'b', 'Main', 'h', 'LB201', 'i', '.M63'] ) )
        self.assertEquals( len( record.location() ), 2 )
        self.assertEquals( record.location()[0].__str__(), loc1 )
        self.assertEquals( record.location()[1].__str__(), loc2 )
        rloclist = [rloc.__str__() for rloc in record.location()]
        self.assertEquals( loclist, rloclist )

def suite():
    suite = unittest.makeSuite( RecordTest, 'test' )
    return suite 

if __name__ == "__main__":
    unittest.main()


