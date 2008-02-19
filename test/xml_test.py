from unittest import TestCase
from cStringIO import StringIO

from pymarc import map_xml, parse_xml_to_array, record_to_xml, Record

class XmlTest(TestCase):

    def test_map_xml(self):
        self.seen = 0
        def count(record): 
            self.seen += 1
        map_xml(count, 'test/batch.xml')
        self.assertEqual(2, self.seen)

    def test_multi_map_xml(self):
        self.seen = 0
        def count(record): 
            self.seen += 1
        map_xml(count, 'test/batch.xml', 'test/batch.xml')
        self.assertEqual(4, self.seen)

    def test_parse_to_array(self):
        records = parse_xml_to_array('test/batch.xml')
        self.assertEqual(len(records), 2)

        # should've got two records
        self.assertEqual(type(records[0]), Record)
        self.assertEqual(type(records[1]), Record)
       
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
        record1 = parse_xml_to_array('test/batch.xml')[0]
        # generate xml
        xml = record_to_xml(record1)
        # parse generated xml 
        record2 = parse_xml_to_array(StringIO(xml))[0]

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

