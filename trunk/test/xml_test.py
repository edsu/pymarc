from unittest import TestCase
from pymarc import map_xml, parse_xml_to_array, Record

class XmlTest(TestCase):

  def test_map_xml(self):
    self.seen = 0
    def count(r): self.seen += 1
    map_xml(count, 'test/batch.xml')
    self.assertEqual(2, self.seen)

  def test_parse_to_array(self):
    records = parse_xml_to_array('test/batch.xml')
    self.assertEqual(len(records), 2)

    # should've got two records
    self.assertEqual(type(records[0]), Record)
    self.assertEqual(type(records[1]), Record)
   
    # first record should have 18 fields
    r = records[0]
    self.assertEqual(len(r.getFields()), 18)
  
    # check the content of a control field
    self.assertEqual(r['008'].data, 
      u'910926s1957    nyuuun              eng  ')

    # check a data field with subfields
    f = r['245']
    self.assertEqual(f.indicator1, '0')
    self.assertEqual(f.indicator2, '4')
    self.assertEqual(f['a'], u'The Great Ray Charles')
    self.assertEqual(f['h'], u'[sound recording].')
     
