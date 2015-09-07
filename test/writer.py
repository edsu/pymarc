import unittest
import pymarc
import os
import textwrap
from six import BytesIO, StringIO, u, binary_type

try:
    # the json module was included in the stdlib in python 2.6
    # http://docs.python.org/library/json.html
    import json
except ImportError:
    # simplejson 2.0.9 is available for python 2.4+
    # http://pypi.python.org/pypi/simplejson/2.0.9
    # simplejson 1.7.3 is available for python 2.3+
    # http://pypi.python.org/pypi/simplejson/1.7.3
    import simplejson as json


class JSONWriterTest(unittest.TestCase):

    def test_close_true(self):
        """
        If close_fh is true, then the file handle is also closed.
        """
        file_handle = StringIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.JSONWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

    def test_close_false(self):
        """
        If close_fh is false, then the file handle is NOT closed.
        """
        file_handle = StringIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.JSONWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close(close_fh=False)
        self.assertFalse(
            file_handle.closed,
            'The file handle should NOT close when the writer closes')

    def test_writing_0_records(self):
        expected = json.loads(r"""
            []
        """)
        file_handle = StringIO()
        try:
            writer = pymarc.JSONWriter(file_handle)
            writer.close(close_fh=False)
            actual = json.loads(file_handle.getvalue())
            self.assertEquals(actual, expected)
        finally:
            file_handle.close()

    def test_writing_empty_record(self):
        expected = json.loads(r"""
            [
                {
                    "leader" : "          22        4500",
                    "fields" : []
                }
            ]
        """)
        file_handle = StringIO()
        try:
            writer = pymarc.JSONWriter(file_handle)
            record = pymarc.Record()
            writer.write(record)
            writer.close(close_fh=False)
            actual = json.loads(file_handle.getvalue())
            self.assertEquals(actual, expected)
        finally:
            file_handle.close()

    def test_writing_1_record(self):
        expected = json.loads(r"""
            [
                {
                    "leader" : "          22        4500",
                    "fields" : [
                        {
                            "100": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "me" }
                                ]
                            }
                        },
                        {
                            "245": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "Foo /" },
                                    { "c": "by me." }
                                ]
                            }
                        }
                    ]
                }
            ]
        """)
        file_handle = StringIO()
        try:
            writer = pymarc.JSONWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            actual = json.loads(file_handle.getvalue())
            self.assertEquals(actual, expected)
        finally:
            file_handle.close()

    def test_writing_3_records(self):
        expected = json.loads(r"""
            [
                {
                    "leader" : "          22        4500",
                    "fields" : [
                        {
                            "008": "090227s2009    mau                 chi d"
                        },
                        {
                            "100": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "me" }
                                ]
                            }
                        },
                        {
                            "245": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "Foo /" },
                                    { "c": "by me." }
                                ]
                            }
                        }
                    ]
                },
                {
                    "leader" : "          22        4500",
                    "fields" : [
                        {
                            "100": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "me" }
                                ]
                            }
                        },
                        {
                            "245": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "Foo /" },
                                    { "c": "by me." }
                                ]
                            }
                        }
                    ]
                },
                {
                    "leader" : "          22        4500",
                    "fields" : [
                        {
                            "245": {
                                "ind1": "0",
                                "ind2": "0",
                                "subfields": [
                                    { "a": "Foo /" },
                                    { "c": "by me." }
                                ]
                            }
                        }
                    ]
                }
            ]
        """)
        file_handle = StringIO()
        try:
            writer = pymarc.JSONWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '008',
                    data=u('090227s2009    mau                 chi d')))
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            actual = json.loads(file_handle.getvalue())
            self.assertEquals(actual, expected)
        finally:
            file_handle.close()


class MARCWriterTest(unittest.TestCase):

    def test_write(self):

        # write a record off to a file
        file_handle = open('test/writer-test.dat', 'wb')
        writer = pymarc.MARCWriter(file_handle)
        record = pymarc.Record()
        field = pymarc.Field('245', ['0', '0'], ['a', 'foo'])
        record.add_field(field)
        writer.write(record)
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

        # read it back in
        reader = pymarc.MARCReader(open('test/writer-test.dat', 'rb'))
        r = next(reader)
        reader.close()

        # remove it
        os.remove('test/writer-test.dat')

    def test_close_true(self):
        """
        If close_fh is true, then the file handle is also closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.MARCWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

    def test_close_false(self):
        """
        If close_fh is false, then the file handle is NOT closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.MARCWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close(close_fh=False)
        self.assertFalse(
            file_handle.closed,
            'The file handle should NOT close when the writer closes')


class TextWriterTest(unittest.TestCase):

    def test_writing_0_records(self):
        file_handle = StringIO()
        try:
            writer = pymarc.TextWriter(file_handle)
            writer.close(close_fh=False)
            self.assertEqual(
                file_handle.getvalue(),
                '',
                'Nothing should be have been written to the file handle')
        finally:
            file_handle.close()

    def test_writing_1_record(self):
        expected = r"""
            =LDR            22        4500
            =100  00$ame
            =245  00$aFoo /$cby me.
        """
        expected = textwrap.dedent(expected[1:])
        file_handle = StringIO()
        try:
            writer = pymarc.TextWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_writing_3_records(self):
        expected = r"""
            =LDR            22        4500
            =008  090227s2009\\\\mau\\\\\\\\\\\\\\\\\chi\d
            =100  00$ame
            =245  00$aFoo /$cby me.

            =LDR            22        4500
            =100  00$ame
            =245  00$aFoo /$cby me.

            =LDR            22        4500
            =245  00$aFoo /$cby me.
        """
        expected = textwrap.dedent(expected[1:])
        file_handle = StringIO()
        try:
            writer = pymarc.TextWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '008',
                    data=u('090227s2009    mau                 chi d')))
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_writing_empty_record(self):
        expected = r"""
            =LDR            22        4500
        """
        expected = textwrap.dedent(expected[1:])
        file_handle = StringIO()
        try:
            writer = pymarc.TextWriter(file_handle)
            record = pymarc.Record()
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_close_true(self):
        """
        If close_fh is true, then the file handle is also closed.
        """
        file_handle = StringIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.TextWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

    def test_close_false(self):
        """
        If close_fh is false, then the file handle is NOT closed.
        """
        file_handle = StringIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.TextWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close(close_fh=False)
        self.assertFalse(
            file_handle.closed,
            'The file handle should NOT close when the writer closes')


class XMLWriterTest(unittest.TestCase):

    def test_writing_0_records(self):
        expected = r"""
            <?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            </collection>
        """
        expected = textwrap.dedent(expected[1:]).replace('\n', '')
        if str != binary_type:
            expected = expected.encode()
        file_handle = BytesIO()
        try:
            writer = pymarc.XMLWriter(file_handle)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_writing_empty_record(self):
        expected = r"""
            <?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
            <leader>          22        4500</leader>
            </record>
            </collection>
        """
        expected = textwrap.dedent(expected[1:]).replace('\n', '')
        if str != binary_type:
            expected = expected.encode()
        file_handle = BytesIO()
        try:
            writer = pymarc.XMLWriter(file_handle)
            record = pymarc.Record()
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_writing_1_record(self):
        expected = r"""
            <?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
            <leader>          22        4500</leader>
            <datafield ind1="0" ind2="0" tag="100">
            <subfield code="a">me</subfield>
            </datafield>
            <datafield ind1="0" ind2="0" tag="245">
            <subfield code="a">Foo /</subfield>
            <subfield code="c">by me.</subfield>
            </datafield>
            </record>
            </collection>
        """
        expected = textwrap.dedent(expected[1:]).replace('\n', '')
        if str != binary_type:
            expected = expected.encode()
        file_handle = BytesIO()
        try:
            writer = pymarc.XMLWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_writing_3_records(self):
        expected = r"""
            <?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
            <leader>          22        4500</leader>
            <controlfield tag="008">090227s2009    mau                 chi d</controlfield>
            <datafield ind1="0" ind2="0" tag="100">
            <subfield code="a">me</subfield>
            </datafield>
            <datafield ind1="0" ind2="0" tag="245">
            <subfield code="a">Foo /</subfield>
            <subfield code="c">by me.</subfield>
            </datafield>
            </record>
            <record>
            <leader>          22        4500</leader>
            <datafield ind1="0" ind2="0" tag="100">
            <subfield code="a">me</subfield>
            </datafield>
            <datafield ind1="0" ind2="0" tag="245">
            <subfield code="a">Foo /</subfield>
            <subfield code="c">by me.</subfield>
            </datafield>
            </record>
            <record>
            <leader>          22        4500</leader>
            <datafield ind1="0" ind2="0" tag="245">
            <subfield code="a">Foo /</subfield>
            <subfield code="c">by me.</subfield>
            </datafield>
            </record>
            </collection>
        """
        expected = textwrap.dedent(expected[1:]).replace('\n', '')
        if str != binary_type:
            expected = expected.encode()
        file_handle = BytesIO()
        try:
            writer = pymarc.XMLWriter(file_handle)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '008',
                    data=u('090227s2009    mau                 chi d')))
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field('100', ['0', '0'], ['a', u('me')]))
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            record = pymarc.Record()
            record.add_field(
                pymarc.Field(
                    '245',
                    ['0', '0'],
                    ['a', u('Foo /'), 'c', u('by me.')]))
            writer.write(record)
            writer.close(close_fh=False)
            self.assertEquals(file_handle.getvalue(), expected)
        finally:
            file_handle.close()

    def test_close_true(self):
        """
        If close_fh is true, then the file handle is also closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.XMLWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

    def test_close_false(self):
        """
        If close_fh is false, then the file handle is NOT closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.XMLWriter(file_handle)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close(close_fh=False)
        self.assertFalse(
            file_handle.closed,
            'The file handle should NOT close when the writer closes')


def suite():
    json_suite = unittest.makeSuite(JSONWriterTest, 'test')
    marc_suite = unittest.makeSuite(MARCWriterTest, 'test')
    text_suite = unittest.makeSuite(TextWriterTest, 'test')
    xml_suite = unittest.makeSuite(XMLWriterTest, 'test')
    test_suite = unittest.TestSuite((json_suite, marc_suite, text_suite, xml_suite))
    return test_suite

if __name__ == '__main__':
    unittest.main()
