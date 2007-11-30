from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces, \
  feature_namespace_prefixes
from pymarc import Record, Field

class XmlHandler(ContentHandler):
  """
  You can subclass XmlHandler and add your own process_record 
  method that'll be passed a pymarc.Record as it becomes 
  available. This could be useful if you want to stream the 
  records elsewhere (like to a rdbms) without having to store 
  them all in memory.
  """

  def __init__(self):
    self.records = []
    self._record = None
    self._field = None
    self._subfield_code = None
    self._text = []

  def startElementNS(self, name, qname, attrs):
    el = name[1]
    self._text = []

    if el == 'record':
      self._record = Record() 
    elif el == 'controlfield':
      tag = attrs.getValue((None, u'tag'))
      self._field = Field(tag)
    elif el == 'datafield':
      tag = attrs.getValue((None, u'tag'))
      ind1 = attrs.getValue((None, u'ind1'))
      ind2 = attrs.getValue((None, u'ind2'))
      self._field = Field(tag, [ind1, ind2])
    elif el == 'subfield':
      self._subfield_code = attrs[(None, 'code')]

  def endElementNS(self, name, qname):
    el = name[1]
    text = u''.join(self._text)

    if el == 'record':
      self.process_record(self._record)
      self._record = None
    elif el == 'leader':
      self._record.leader = text
    elif el == 'controlfield':
      self._field.data = text
      self._record.addField(self._field)
      self._field = None
    elif el == 'datafield':
      self._record.addField(self._field)
      self._field = None
    elif el == 'subfield':
      self._field.subfields.append(self._subfield_code)
      self._field.subfields.append(text)
      self._subfield_code = None

    self._text = []

  def characters(self, chars):
    self._text.append(chars)

  def process_record(self, record):
    self.records.append(record)

def parse_xml(file, handler):
  """
  parse a file with a given subclass of xml.sax.handler.ContentHandler
  """
  parser = make_parser()
  parser.setContentHandler(handler)
  parser.setFeature(feature_namespaces, 1)
  parser.parse(file)

def map_xml(f, *files):
  """
  map a function onto the file, so that for each record that is
  parsed the function f will get called with the extracted record

  def do_it(r):
    print r

  map_xml(do_it, 'marc.xml')
  """
  parser = make_parser()
  handler = XmlHandler()
  handler.process_record = f
  for file in files:
    parse_xml(file, handler)

def parse_xml_to_array(file):
  """
  parse an xml file and return the records as an array
  """
  handler = XmlHandler()
  parse_xml(file, handler)
  return handler.records

