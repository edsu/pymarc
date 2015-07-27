import sys
import unittest

import six
import pymarc

from os.path import getsize
from six.moves import cStringIO as StringIO


class XmlTest(unittest.TestCase):

    def test_map_xml(self):
        self.seen = 0
        def count(record):
            self.seen += 1
        pymarc.map_xml(count, 'test/batch.xml')
        self.assertEqual(2, self.seen)

    def test_multi_map_xml(self):
        self.seen = 0
        def count(record):
            self.seen += 1
        pymarc.map_xml(count, 'test/batch.xml', 'test/batch.xml')
        self.assertEqual(4, self.seen)

    def test_parse_to_array(self):
        records = pymarc.parse_xml_to_array('test/batch.xml')
        self.assertEqual(len(records), 2)

        # should've got two records
        self.assertEqual(type(records[0]), pymarc.Record)
        self.assertEqual(type(records[1]), pymarc.Record)

        # first record should have 18 fields
        record = records[0]
        self.assertEqual(len(record.get_fields()), 18)

        # check the content of a control field
        self.assertEqual(record['008'].data,
                         u'910926s1957    nyuuun              eng  ')

        # check a data field with subfields
        field = record['245']
        self.assertEqual(field.indicator1, '0')
        self.assertEqual(field.indicator2, '4')
        self.assertEqual(field['a'], u'The Great Ray Charles')
        self.assertEqual(field['h'], u'[sound recording].')

    def test_xml(self):
        # read in xml to a record
        record1 = pymarc.parse_xml_to_array('test/batch.xml')[0]
        # generate xml
        xml = pymarc.record_to_xml(record1)
        # parse generated xml
        record2 = pymarc.parse_xml_to_array(six.BytesIO(xml))[0]

        # compare original and resulting record
        self.assertEqual(record1.leader, record2.leader)

        field1 = record1.get_fields()
        field2 = record2.get_fields()
        self.assertEqual(len(field1), len(field2))

        pos = 0
        while pos < len(field1):
            self.assertEqual(field1[pos].tag, field2[pos].tag)
            if field1[pos].is_control_field():
                self.assertEqual(field1[pos].data, field2[pos].data)
            else:
                self.assertEqual(field1[pos].get_subfields(), field2[pos].get_subfields())
                self.assertEqual(field1[pos].indicators, field2[pos].indicators)
            pos += 1

    # this test stopped working when Record.as_marc started returning a
    # utf-8 encoded string, and Record.decode_marc started decoding utf-8

    def disabled_test_xml_quiet(self):
        """ Tests the 'quiet' parameter of the MARC8ToUnicode class,
            passed in via the pymarc.record_to_xml() method
        """
        outfile = 'test/dummy_stderr.txt'
        # truncate outfile in case someone's fiddled with it
        open(outfile, 'wb').close()
        # redirect stderr
        sys.stderr = open(outfile, 'wb')
        # reload pymarc so it picks up the new sys.stderr
        reload(pymarc)
        # get problematic record
        record = next(pymarc.reader.MARCReader(open('test/utf8_errors.dat', 'rb')))
        # record_to_xml() with quiet set to False should generate errors
        #   and write them to sys.stderr
        xml = pymarc.record_to_xml(record, quiet=False)
        # close dummy stderr so we can accurately get its size
        sys.stderr.close()
        # file size should be greater than 0
        self.assertNotEqual(getsize(outfile), 0)

        # truncate file again
        open(outfile, 'wb').close()
        # be sure its truncated
        self.assertEqual(getsize(outfile), 0)
        # redirect stderr again
        sys.stderr = open(outfile, 'wb')
        reload(pymarc)
        # record_to_xml() with quiet set to True should not generate errors
        xml = pymarc.record_to_xml(record, quiet=True)
        # close dummy stderr
        sys.stderr.close()
        # no errors should have been written
        self.assertEqual(getsize(outfile), 0)

    def test_strict(self):
        a = pymarc.parse_xml_to_array(open('test/batch.xml'), strict=True)
        self.assertEqual(len(a), 2)

    def test_xml_namespaces(self):
        """ Tests the 'namespace' parameter of the record_to_xml() method
        """
        # get a test record
        fh = open('test/test.dat', 'rb')
        record = next(pymarc.reader.MARCReader(fh))
        # record_to_xml() with quiet set to False should generate errors
        #   and write them to sys.stderr
        xml = pymarc.record_to_xml(record, namespace=False)
        # look for the xmlns in the written xml, should be -1
        self.assertNotIn(b'xmlns="http://www.loc.gov/MARC21/slim"', xml)

        # record_to_xml() with quiet set to True should not generate errors
        xml = pymarc.record_to_xml(record, namespace=True)
        # look for the xmlns in the written xml, should be >= 0
        self.assertIn(b'xmlns="http://www.loc.gov/MARC21/slim"', xml)

        fh.close()

    def test_bad_tag(self):
        a = pymarc.parse_xml_to_array(open('test/bad_tag.xml'))
        self.assertEqual(len(a), 1)

def suite():
    test_suite = unittest.makeSuite(XmlTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
