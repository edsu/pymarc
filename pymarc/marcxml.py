"pymarc marcxml file."

import logging
from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces
import unicodedata

import six

try:
    import xml.etree.ElementTree as ET  # builtin in Python 2.5
except ImportError:
    import elementtree.ElementTree as ET

from pymarc import Record, Field, MARC8ToUnicode

XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
MARC_XML_NS = "http://www.loc.gov/MARC21/slim"
MARC_XML_SCHEMA = "http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"

class XmlHandler(ContentHandler):

    """
    You can subclass XmlHandler and add your own process_record
    method that'll be passed a pymarc.Record as it becomes
    available. This could be useful if you want to stream the
    records elsewhere (like to a rdbms) without having to store
    them all in memory.
    """
    def __init__(self, strict=False, normalize_form=None):
        self.records = []
        self._record = None
        self._field = None
        self._subfield_code = None
        self._text = []
        self._strict = strict
        self.normalize_form = normalize_form

    def startElementNS(self, name, qname, attrs):
        if self._strict and name[0] != MARC_XML_NS:
            return

        element = name[1]
        self._text = []

        if element == 'record':
            self._record = Record()
        elif element == 'controlfield':
            tag = attrs.getValue((None, u'tag'))
            self._field = Field(tag)
        elif element == 'datafield':
            tag = attrs.getValue((None, u'tag'))
            ind1 = attrs.get((None, u'ind1'), u' ')
            ind2 = attrs.get((None, u'ind2'), u' ')
            self._field = Field(tag, [ind1, ind2])
        elif element == 'subfield':
            self._subfield_code = attrs[(None, 'code')]

    def endElementNS(self, name, qname):
        if self._strict and name[0] != MARC_XML_NS:
            return

        element = name[1]
        if self.normalize_form is not None:
            text = unicodedata.normalize(self.normalize_form, u''.join(self._text))
        else:
            text = u''.join(self._text)

        if element == 'record':
            self.process_record(self._record)
            self._record = None
        elif element == 'leader':
            self._record.leader = text
        elif element == 'controlfield':
            self._field.data = text
            self._record.add_field(self._field)
            self._field = None
        elif element == 'datafield':
            self._record.add_field(self._field)
            self._field = None
        elif element == 'subfield':
            self._field.subfields.append(self._subfield_code)
            self._field.subfields.append(text)
            self._subfield_code = None

        self._text = []

    def characters(self, chars):
        self._text.append(chars)

    def process_record(self, record):
        self.records.append(record)

def parse_xml(xml_file, handler):
    """
    parse a file with a given subclass of xml.sax.handler.ContentHandler
    """
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setFeature(feature_namespaces, 1)
    parser.parse(xml_file)

def map_xml(function, *files):
    """
    map a function onto the file, so that for each record that is
    parsed the function will get called with the extracted record

    def do_it(r):
      print(r)

    map_xml(do_it, 'marc.xml')
    """
    handler = XmlHandler()
    handler.process_record = function
    for xml_file in files:
        parse_xml(xml_file, handler)

def parse_xml_to_array(xml_file, strict=False, normalize_form=None):
    """
    parse an xml file and return the records as an array. If you would
    like the parser to explicitly check the namespaces for the MARCSlim
    namespace use the strict=True option.
    Valid values for normalize_form are 'NFC', 'NFKC', 'NFD', and 'NFKD'. See
    unicodedata.normalize info.
    """
    handler = XmlHandler(strict, normalize_form)
    parse_xml(xml_file, handler)
    return handler.records

def record_to_xml(record, quiet=False, namespace=False):
    node = record_to_xml_node(record, quiet, namespace)
    return ET.tostring(node)

def record_to_xml_node(record, quiet=False, namespace=False):
    """
    converts a record object to a chunk of xml

    # include the marcxml namespace in the root tag (default: False)
    record_to_xml(record, namespace=True)
    """
    # helper for converting non-unicode data to unicode
    # TODO: maybe should set g0 and g1 appropriately using 066 $a and $b?
    marc8 = MARC8ToUnicode(quiet=quiet)
    def translate(data):
        if type(data) == six.text_type:
            return data
        else:
            return marc8.translate(data)

    root = ET.Element('record')
    if namespace:
        root.set('xmlns', MARC_XML_NS)
        root.set('xmlns:xsi', XSI_NS)
        root.set('xsi:schemaLocation', MARC_XML_SCHEMA)
    leader = ET.SubElement(root, 'leader')
    leader.text = record.leader
    for field in record:
        if field.is_control_field():
            control_field = ET.SubElement(root, 'controlfield')
            control_field.set('tag', field.tag)
            control_field.text = translate(field.data)
        else:
            data_field = ET.SubElement(root, 'datafield')
            data_field.set('tag', field.tag)
            data_field.set('ind1', field.indicators[0])
            data_field.set('ind2', field.indicators[1])
            for subfield in field:
                data_subfield = ET.SubElement(data_field, 'subfield')
                data_subfield.set('code', subfield[0])
                data_subfield.text = translate(subfield[1])

    return root
