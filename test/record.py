import unittest

from pymarc.reader import MARCReader
from pymarc.record import Record
from pymarc.field import Field
from pymarc.exceptions import BaseAddressInvalid, RecordLeaderInvalid, \
        FieldNotFound

class RecordTest(unittest.TestCase):

    def test_add_field(self):
        record = Record()
        field = Field(
            tag = '245',
            indicators = ['1', '0'],
            subfields = ['a', 'Python', 'c', 'Guido'])
        record.add_field(field)
        self.assertTrue(field in record.fields, msg='found field')

    def test_remove_field(self):
        record = Record()
        field = Field(
            tag = '245',
            indicators = ['1', '0'],
            subfields = ['a', 'Python', 'c', 'Guido'])
        record.add_field(field)
        self.assertEqual(record['245']['a'], 'Python')

        # try removing a field that exists
        record.remove_field(field)
        self.assertEqual(record['245'], None)

        # try removing a field that doesn't exist
        field = Field('001', data='abcd1234')
        self.assertRaises(FieldNotFound, record.remove_field, field)

    def test_quick_access(self):
        record = Record()
        title = Field(
            tag = '245',
            indicators = ['1', '0'],
            subfields = ['a', 'Python', 'c', 'Guido'])
        record.add_field(title)
        self.assertEqual(record['245'], title, 'short access')
        self.assertEqual(record['999'], None, 'short access with no field')

    def test_membership(self):
        record = Record()
        title = Field(
            tag = '245',
            indicators = ['1', '0'],
            subfields = ['a', 'Python', 'c', 'Guido'])
        record.add_field(title)
        self.assertTrue('245' in record)
        self.assertFalse('999' in record)

    def test_field_not_found(self):
        record = Record()
        self.assertEqual(len(record.fields), 0)

    def test_find(self):
        record = Record()
        subject1 = Field(
            tag = '650',
            indicators = ['', '0'],
            subfields = ['a', 'Programming Language'])
        record.add_field(subject1)
        subject2 = Field(
            tag = '650',
            indicators = ['', '0'],
            subfields = ['a', 'Object Oriented'])
        record.add_field(subject2)
        found = record.get_fields('650')
        self.assertEqual(found[0], subject1, 'get_fields() item 1')
        self.assertEqual(found[0], subject1, 'get_fields() item 2')
        found = record.get_fields()
        self.assertEqual(len(found), 2, 'get_fields() with no tag')

    def test_multi_find(self):
        record = Record()
        subject1 = Field(
            tag = '650',
            indicators = ['', '0'],
            subfields = ['a', 'Programming Language'])
        record.add_field(subject1)
        subject2 = Field(
            tag = '651',
            indicators = ['', '0'],
            subfields = ['a', 'Object Oriented'])
        record.add_field(subject2)
        found = record.get_fields('650', '651')
        self.assertEqual(len(found), 2)

    def test_bad_leader(self):
        record = Record()
        self.assertRaises(RecordLeaderInvalid, record.decode_marc, b'foo')

    def test_bad_base_address(self):
        record = Record()
        self.assertRaises(BaseAddressInvalid, record.decode_marc, b'00695cam  2200241Ia 45x00')

    def test_title(self):
        record = Record()
        self.assertEqual(record.title(), None)
        record.add_field(Field('245', [0, 1],
            subfields=['a', 'Foo :', 'b', 'bar']))
        self.assertEqual(record.title(), 'Foo : bar')

        record = Record()
        record.add_field(Field('245', [0, 1],
            subfields=['a', "Farghin"]))
        self.assertEqual(record.title(), "Farghin")

    def test_isbn(self):
        record = Record()
        self.assertEqual(record.isbn(), None)
        record.add_field(Field('020', [0, 1], subfields=['a', '9781416566113']))
        self.assertEqual(record.isbn(), '9781416566113')

        record = Record()
        record.add_field(Field('020', [0, 1], subfields=['a', '978-1416566113']))
        self.assertEqual(record.isbn(), '9781416566113')

        record = Record()
        record.add_field(Field('020', [0, 1], subfields=['a', 'ISBN-978-1416566113']))
        self.assertEqual(record.isbn(), '9781416566113')

        record = Record()
        record.add_field(Field('020', [' ', ' '], subfields=['a', '0456789012 (reel 1)']))
        self.assertEqual(record.isbn(), '0456789012')

        record = Record()
        record.add_field(Field('020', [' ', ' '], subfields=['a', '006073132X']))
        self.assertEqual(record.isbn(), '006073132X')

    def test_multiple_isbn(self):
        with open('test/multi_isbn.dat', 'rb') as fh:
            reader = MARCReader(fh)
            record = next(reader)
            self.assertEqual(record.isbn(), '0914378287')

    def test_author(self):
        record = Record()
        self.assertEqual(record.author(), None)
        record.add_field(Field('100', [1, 0],
            subfields=['a', 'Bletch, Foobie,', 'd', '1979-1981.']))
        self.assertEqual(record.author(), 'Bletch, Foobie, 1979-1981.')

        record = Record()
        record.add_field(Field('130', [0, ' '],
            subfields=['a', 'Bible.', 'l', 'Python.']))
        self.assertEqual(record.author(), None)

    def test_uniformtitle(self):
        record = Record()
        self.assertEqual(record.uniformtitle(), None)
        record.add_field(Field('130', [0, ' '],
            subfields=['a', "Tosefta.", 'l', "English.", 'f', "1977."]))
        self.assertEqual(record.uniformtitle(), "Tosefta. English. 1977.")

        record = Record()
        record.add_field(Field('240', [1, 4],
            subfields=['a', "The Pickwick papers.", 'l', "French."]))
        self.assertEqual(record.uniformtitle(),
                "The Pickwick papers. French.")

    def test_subjects(self):
        record = Record()
        subject1 = '=630  0\\$aTosefta.$lEnglish.$f1977.'
        subject2 = '=600  10$aLe Peu, Pepe.'
        shlist = [subject1, subject2]
        self.assertEqual(record.subjects(), [])
        record.add_field(Field('630', [0, ' '],
            subfields=['a', "Tosefta.", 'l', "English.", 'f', "1977."]))
        record.add_field(Field('730', [0, ' '],
            subfields=['a', "Tosefta.", 'l', "English.", 'f', "1977."]))
        record.add_field(Field('600', [1, 0],
            subfields=['a', "Le Peu, Pepe."]))
        self.assertEqual(len(record.subjects()), 2)
        self.assertEqual(record.subjects()[0].__str__(), subject1)
        self.assertEqual(record.subjects()[1].__str__(), subject2)
        rshlist = [rsh.__str__() for rsh in record.subjects()]
        self.assertEqual(shlist, rshlist)

    def test_added_entries(self):
        record = Record()
        ae1 = '=730  0\\$aTosefta.$lEnglish.$f1977.'
        ae2 = '=700  10$aLe Peu, Pepe.'
        aelist = [ae1, ae2]
        self.assertEqual(record.addedentries(), [])
        record.add_field(Field('730', [0, ' '],
            subfields=['a', "Tosefta.", 'l', "English.", 'f', "1977."]))
        record.add_field(Field('700', [1, 0],
            subfields=['a', "Le Peu, Pepe."]))
        record.add_field(Field('245', [0, 0],
            subfields=['a', "Le Peu's Tosefa."]))
        self.assertEqual(len(record.addedentries()), 2)
        self.assertEqual(record.addedentries()[0].__str__(), ae1)
        self.assertEqual(record.addedentries()[1].__str__(), ae2)
        raelist = [rae.__str__() for rae in record.addedentries()]
        self.assertEqual(aelist, raelist)

    def test_physicaldescription(self):
        record = Record()
        pd1 = '=300  \\$a1 photographic print :$bgelatin silver ;$c10 x 56 in.'
        pd2 = '=300  \\$aFOO$bBAR$cBAZ'
        pdlist = [pd1, pd2]
        self.assertEqual(record.physicaldescription(), [])
        record.add_field(Field('300', ['\\', ''],
            subfields=['a', '1 photographic print :',
                       'b', 'gelatin silver ;',
                       'c', '10 x 56 in.']))
        record.add_field(Field('300', ['\\', ''],
            subfields=['a', 'FOO',
                       'b', 'BAR',
                       'c', 'BAZ']))
        self.assertEqual(len(record.physicaldescription()), 2)
        self.assertEqual(record.physicaldescription()[0].__str__(), pd1)
        self.assertEqual(record.physicaldescription()[1].__str__(), pd2)
        rpdlist = [rpd.__str__() for rpd in record.physicaldescription()]
        self.assertEqual(pdlist, rpdlist)

    def test_location(self):
        record = Record()
        loc1 = '=852  \\\\$aAmerican Institute of Physics.$bNiels Bohr Library and Archives.$eCollege Park, MD'
        loc2 = '=852  01$aCtY$bMain$hLB201$i.M63'
        loclist = [loc1, loc2]
        self.assertEqual(record.location(), [])
        record.add_field(Field('040', [' ', ' '],
            subfields=['a', 'DLC', 'c', 'DLC']))
        record.add_field(Field('852', [' ', ' '],
            subfields=['a', 'American Institute of Physics.',
                'b', 'Niels Bohr Library and Archives.',
                'e', 'College Park, MD']))
        record.add_field(Field('852', [0, 1],
            subfields=['a', 'CtY', 'b', 'Main', 'h', 'LB201', 'i', '.M63']))
        self.assertEqual(len(record.location()), 2)
        self.assertEqual(record.location()[0].__str__(), loc1)
        self.assertEqual(record.location()[1].__str__(), loc2)
        rloclist = [rloc.__str__() for rloc in record.location()]
        self.assertEqual(loclist, rloclist)

    def test_notes(self):
        record = Record()
        self.assertEqual(record.notes(), [])
        record.add_field(Field('500', [' ', ' '],
            subfields=['a', "Recast in bronze from artist's plaster original of 1903."]))
        self.assertEqual(record.notes()[0].format_field(), "Recast in bronze from artist's plaster original of 1903.")

    def test_publisher(self):
        record = Record()
        self.assertEqual(record.publisher(), None)
        record.add_field(Field('260', [' ', ' '],
            subfields=['a', 'Paris :', 'b', 'Gauthier-Villars ;', 'a', 'Chicago :', 'b', 'University of Chicago Press,', 'c', '1955.']))
        self.assertEqual(record.publisher(), 'Gauthier-Villars ;')

        record = Record()
        self.assertEqual(record.publisher(), None)
        record.add_field(Field('264', [' ', '1'],
            subfields=['a', 'London :', 'b', 'Penguin,', 'c', '1961.']))
        self.assertEqual(record.publisher(), 'Penguin,')

    def test_pubyear(self):
        record = Record()
        self.assertEqual(record.pubyear(), None)
        record.add_field(Field('260', [' ', ' '],
            subfields=['a', 'Paris :', 'b', 'Gauthier-Villars ;', 'a', 'Chicago :', 'b', 'University of Chicago Press,', 'c', '1955.']))
        self.assertEqual(record.pubyear(), '1955.')

        record = Record()
        self.assertEqual(record.pubyear(), None)
        record.add_field(Field('264', [' ', '1'],
            subfields=['a', 'London :', 'b', 'Penguin,', 'c', '1961.']))
        self.assertEqual(record.pubyear(), '1961.')

    def test_alphatag(self):
        record = Record()
        record.add_field(Field('CAT', [' ', ' '], subfields=['a', 'foo']))
        record.add_field(Field('CAT', [' ', ' '], subfields=['b', 'bar']))
        fields = record.get_fields('CAT')
        self.assertEqual(len(fields), 2)
        self.assertEqual(fields[0]['a'], 'foo')
        self.assertEqual(fields[1]['b'], 'bar')
        self.assertEqual(record['CAT']['a'], 'foo')

    def test_copy(self):
        from copy import deepcopy
        with open('test/one.dat', 'rb') as fh:
            r1 = next(MARCReader(fh))
            r2 = deepcopy(r1)
            r1.add_field(Field('999', [' ', ' '], subfields=['a', 'foo']))
            r2.add_field(Field('999', [' ', ' '], subfields=['a', 'bar']))
            self.assertEqual(r1['999']['a'], 'foo')
            self.assertEqual(r2['999']['a'], 'bar')

    def test_as_marc_with_explicit_leader(self):
        """
        Test setting an explicit leader.
        as_marc() should use the whole leader as set.
        """
        record = Record()
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','1'],
                subfields = ['a', 'The pragmatic programmer']))
        record.leader = '00067     2200037   4500'
        leader_not_touched = record.leader
        transmission_format = record.as_marc()
        leader_touched = record.leader
        self.assertTrue(leader_not_touched==leader_touched)

    def test_remove_fields(self):
        with open('test/testunimarc.dat', 'rb') as fh:
            record = Record(fh.read(), force_utf8=True)
        self.assertTrue(len(record.get_fields('899'))!=0)
        self.assertTrue(len(record.get_fields('702'))!=0)
        record.remove_fields('899', '702')
        self.assertTrue(len(record.get_fields('899'))==0)
        self.assertTrue(len(record.get_fields('702'))==0)

    def test_as_marc_consistency(self):
        record = Record()
        leadertype = type(record.leader)
        record.as_marc()
        self.assertEqual(leadertype, type(record.leader))

    def test_init_with_no_leader(self):
        """
        Test creating a Record object with no leader argument.
        """
        record = Record()
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','1'],
                subfields = ['a', 'The pragmatic programmer']))
        transmission_format = record.as_marc()
        transmission_format_leader = transmission_format[0:24]
        self.assertEqual(
            transmission_format_leader,
            b'00067     2200037   4500')

    def test_init_with_no_leader_but_with_force_utf8(self):
        """
        Test creating a Record object with no leader argument
        but with the force_utf8 argument being True.
        """
        record = Record(force_utf8 = True)
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','1'],
                subfields = ['a', 'The pragmatic programmer']))
        transmission_format = record.as_marc()
        transmission_format_leader = transmission_format[0:24]
        self.assertEqual(
            transmission_format_leader,
            b'00067    a2200037   4500')

    def test_init_with_leader(self):
        """
        Test creating a Record with a leader argument.
        """
        record = Record(leader='abcdefghijklmnopqrstuvwx')
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','1'],
                subfields = ['a', 'The pragmatic programmer']))
        transmission_format = record.as_marc()
        transmission_format_leader = transmission_format[0:24]
        self.assertEqual(
            transmission_format_leader,
            b'00067fghij2200037rst4500')

    def test_init_with_leader_and_force_utf8(self):
        """
        Test creating a Record  with a leader argument
        and with the force_ut8 argument being True.
        """
        record = Record(
            leader = 'abcdefghijklmnopqrstuvwx',
            force_utf8 = True)
        record.add_field(
            Field(
                tag = '245',
                indicators = ['0','1'],
                subfields = ['a', 'The pragmatic programmer']))
        transmission_format = record.as_marc()
        transmission_format_leader = transmission_format[0:24]
        self.assertEqual(
            transmission_format_leader,
            b'00067fghia2200037rst4500')

def suite():
    test_suite = unittest.makeSuite(RecordTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()

