# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

"""From XML to MARC21 and back again."""

import unicodedata
from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces
import xml.etree.ElementTree as ET

from pymarc import Field, MARC8ToUnicode, Record


XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
MARC_XML_NS = "http://www.loc.gov/MARC21/slim"
MARC_XML_SCHEMA = "http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"


class XmlHandler(ContentHandler):
    """XML Handler.

    You can subclass XmlHandler and add your own process_record
    method that'll be passed a pymarc.Record as it becomes
    available. This could be useful if you want to stream the
    records elsewhere (like to a rdbms) without having to store
    them all in memory.
    """

    def __init__(self, strict=False, normalize_form=None):
        """Initialize XmlHandler.

        * `strict` will ignore elements not matching MARC_XML_NS.
        * see unicodedata.normalize for valid `normalize_form` values
        """
        self.records = []
        self._record = None
        self._field = None
        self._subfield_code = None
        self._text = []
        self._strict = strict
        self.normalize_form = normalize_form

    def startElementNS(self, name, qname, attrs):
        """Start element NS."""
        if self._strict and name[0] != MARC_XML_NS:
            return

        element = name[1]
        self._text = []

        if element == "record":
            self._record = Record()
        elif element == "controlfield":
            tag = attrs.getValue((None, u"tag"))
            self._field = Field(tag)
        elif element == "datafield":
            tag = attrs.getValue((None, u"tag"))
            ind1 = attrs.get((None, u"ind1"), u" ")
            ind2 = attrs.get((None, u"ind2"), u" ")
            self._field = Field(tag, [ind1, ind2])
        elif element == "subfield":
            self._subfield_code = attrs[(None, "code")]

    def endElementNS(self, name, qname):
        """End element NS."""
        if self._strict and name[0] != MARC_XML_NS:
            return

        element = name[1]
        if self.normalize_form is not None:
            text = unicodedata.normalize(self.normalize_form, u"".join(self._text))
        else:
            text = u"".join(self._text)

        if element == "record":
            self.process_record(self._record)
            self._record = None
        elif element == "leader":
            self._record.leader = text
        elif element == "controlfield":
            self._field.data = text
            self._record.add_field(self._field)
            self._field = None
        elif element == "datafield":
            self._record.add_field(self._field)
            self._field = None
        elif element == "subfield":
            self._field.subfields.append(self._subfield_code)
            self._field.subfields.append(text)
            self._subfield_code = None

        self._text = []

    def characters(self, chars):
        """Append `chars` to `_text`."""
        self._text.append(chars)

    def process_record(self, record):
        """Append `record` to `records`."""
        self.records.append(record)


def parse_xml(xml_file, handler):
    """Parse a file with a given subclass of xml.sax.handler.ContentHandler."""
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setFeature(feature_namespaces, 1)
    parser.parse(xml_file)


def map_xml(function, *files):
    """Map a function onto the file.

    So that for each record that is parsed the function will get called with the
    extracted record

    .. code-block:: python

        def do_it(r):
            print(r)

        map_xml(do_it, 'marc.xml')
    """
    handler = XmlHandler()
    handler.process_record = function
    for xml_file in files:
        parse_xml(xml_file, handler)


def parse_xml_to_array(xml_file, strict=False, normalize_form=None):
    """Parse an XML file and return the records as an array.

    Instead of passing in a file path you can also pass in an open file handle, or a file
    like object like StringIO. If you would like the parser to explicitly check the
    namespaces for the MARCSlim namespace use the strict=True option. Valid values for
    normalize_form are 'NFC', 'NFKC', 'NFD', and 'NFKD'. See
    unicodedata.normalize for more info on these.
    """
    handler = XmlHandler(strict, normalize_form)
    parse_xml(xml_file, handler)
    return handler.records


def record_to_xml(record, quiet=False, namespace=False):
    """From MARC to XML."""
    node = record_to_xml_node(record, quiet, namespace)
    return ET.tostring(node)


def record_to_xml_node(record, quiet=False, namespace=False):
    """Converts a record object to a chunk of XML.

    If you would like to include the marcxml namespace in the root tag set namespace to
    True.
    """
    # helper for converting non-unicode data to unicode
    # TODO: maybe should set g0 and g1 appropriately using 066 $a and $b?
    marc8 = MARC8ToUnicode(quiet=quiet)

    def translate(data):
        if type(data) == str:
            return data
        else:
            return marc8.translate(data)

    root = ET.Element("record")
    if namespace:
        root.set("xmlns", MARC_XML_NS)
        root.set("xmlns:xsi", XSI_NS)
        root.set("xsi:schemaLocation", MARC_XML_SCHEMA)
    leader = ET.SubElement(root, "leader")
    leader.text = str(record.leader)
    for field in record:
        if field.is_control_field():
            control_field = ET.SubElement(root, "controlfield")
            control_field.set("tag", field.tag)
            control_field.text = translate(field.data)
        else:
            data_field = ET.SubElement(root, "datafield")
            data_field.set("ind1", field.indicators[0])
            data_field.set("ind2", field.indicators[1])
            data_field.set("tag", field.tag)
            for subfield in field:
                data_subfield = ET.SubElement(data_field, "subfield")
                data_subfield.set("code", subfield[0])
                data_subfield.text = translate(subfield[1])

    return root
