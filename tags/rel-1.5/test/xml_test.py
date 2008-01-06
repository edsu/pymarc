from unittest import TestCase
from pymarc import map_xml, parse_xml_to_array, record_to_xml, Record
from cStringIO import StringIO

class XmlTest(TestCase):

  def test_map_xml(self):
    self.seen = 0
    def count(r): self.seen += 1
    map_xml(count, 'test/batch.xml')
    self.assertEqual(2, self.seen)

  def test_multi_map_xml(self):
    self.seen = 0
    def count(r): self.seen += 1
    map_xml(count, 'test/batch.xml', 'test/batch.xml')
    self.assertEqual(4, self.seen)

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

  def test_xml(self):
    # read in xml to a record
    r1 = parse_xml_to_array('test/batch.xml')[0]
    # generate xml
    xml = record_to_xml(r1)
    # parse generated xml 
    r2 = parse_xml_to_array(StringIO(xml))[0]

    # compare original and resulting record
    self.assertEqual(r1.leader, r2.leader)

    f1 = r1.getFields()
    f2 = r2.getFields()
    self.assertEqual(len(f1), len(f2))

    pos = 0
    while pos < len(f1):
      self.assertEqual(f1[pos].tag, f2[pos].tag)
      if f1[pos].isControlField():
        self.assertEqual(f1[pos].data, f2[pos].data)
      else:
        self.assertEqual(f1[pos].getSubfields(), f2[pos].getSubfields())
        self.assertEqual(f1[pos].indicators, f2[pos].indicators)
      pos += 1

