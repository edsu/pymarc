from unittest import TestCase, makeSuite

import os
import codecs
import logging

from six import unichr
from six import text_type, binary_type

from pymarc import marc8_to_unicode, Field, Record, MARCReader, MARCWriter

class MARC8Test(TestCase):

    def test_marc8_reader(self):
        with open('test/marc8.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=False)
            r = next(reader)
            self.assertEqual(type(r), Record)
            utitle = r['240']['a']
            self.assertEqual(type(utitle), binary_type)
            self.assertEqual(utitle, b'De la solitude \xe1a la communaut\xe2e.')

    def test_marc8_reader_to_unicode(self):
        with open('test/marc8.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True)
            r = next(reader)
            self.assertEqual(type(r), Record)
            utitle = r['240']['a']
            self.assertEqual(type(utitle), text_type)
            self.assertEqual(utitle, u'De la solitude \xe0 la communaut\xe9.')

    def test_marc8_reader_to_unicode_bad_eacc_sequence(self):
        with open('test/bad_eacc_encoding.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True, hide_utf8_warnings=True)
            try:
                r = next(reader)
                self.assertFalse("Was able to decode invalid MARC8")
            except UnicodeDecodeError:
                self.assertTrue("Caught UnicodeDecodeError as expected")

    def test_marc8_reader_to_unicode_bad_escape(self):
        with open('test/bad_marc8_escape.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True)
            r = next(reader)
            self.assertEqual(type(r), Record)
            upublisher = r['260']['b']
            self.assertEqual(type(upublisher), text_type)
            self.assertEqual(upublisher, u'La Soci\xe9t\x1b,')

    def test_marc8_to_unicode(self):
        marc8_file = open('test/test_marc8.txt', 'rb')
        utf8_file = open('test/test_utf8.txt', 'rb')
        count = 0

        while True:
            marc8 = marc8_file.readline().strip(b"\n")
            utf8 = utf8_file.readline().strip(b"\n")
            if marc8 == b'' or utf8 == b'':
                break
            count += 1
            self.assertEqual(marc8_to_unicode(marc8).encode('utf8'), utf8)

        self.assertEqual(count, 1515)
        marc8_file.close()
        utf8_file.close()

    def test_writing_unicode(self):
        record = Record()
        record.add_field(Field(245, ['1', '0'], ['a', unichr(0x1234)]))
        record.leader = '         a              '
        writer = MARCWriter(open('test/foo', 'wb'))
        writer.write(record)
        writer.close()

        reader = MARCReader(open('test/foo', 'rb'), to_unicode=True)
        record = next(reader)
        self.assertEqual(record['245']['a'], unichr(0x1234))
        reader.close()

        os.remove('test/foo')

    def test_reading_utf8_with_flag(self):
        with open('test/utf8_with_leader_flag.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=False)
            record = next(reader)
            self.assertEqual(type(record), Record)
            utitle = record['240']['a']
            self.assertEqual(type(utitle), binary_type)
            self.assertEqual(utitle,
                b'De la solitude a\xcc\x80 la communaute\xcc\x81.')

        with open('test/utf8_with_leader_flag.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True)
            record = next(reader)
            self.assertEqual(type(record), Record)
            utitle = record['240']['a']
            self.assertEqual(type(utitle), text_type)
            self.assertEqual(utitle, u'De la solitude a' + unichr(0x0300) +
                ' la communaute' + unichr(0x0301) + '.')

    def test_reading_utf8_without_flag(self):
        with open('test/utf8_without_leader_flag.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=False)
            record = next(reader)
            self.assertEqual(type(record), Record)
            utitle = record['240']['a']
            self.assertEqual(type(utitle), binary_type)
            self.assertEqual(utitle,
                b'De la solitude a\xcc\x80 la communaute\xcc\x81.')

        with open('test/utf8_without_leader_flag.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True, hide_utf8_warnings=True)
            record = next(reader)
            self.assertEqual(type(record), Record)
            utitle = record['240']['a']
            self.assertEqual(type(utitle), text_type)
            # unless you force utf-8 characters will get lost and
            # warnings will appear in the terminal
            self.assertEqual(utitle, 'De la solitude a   la communaute .')

        # force reading as utf-8
        with open('test/utf8_without_leader_flag.dat', 'rb') as fh:
            reader = MARCReader(fh, to_unicode=True, force_utf8=True,
                                hide_utf8_warnings=True)
            record = next(reader)
            self.assertEqual(type(record), Record)
            utitle = record['240']['a']
            self.assertEqual(type(utitle), text_type)
            self.assertEqual(utitle, u'De la solitude a' + unichr(0x0300) +
                ' la communaute' + unichr(0x0301) + '.')

    def test_record_create_force_utf8(self, force_utf8=True):
        r = Record(force_utf8=True)
        self.assertEqual(r.leader[9], 'a')

    def test_subscript_2(self):
        self.assertEqual(marc8_to_unicode(b'CO\x1bb2\x1bs is a gas'),
                         u'CO\u2082 is a gas')
        self.assertEqual(marc8_to_unicode(b'CO\x1bb2\x1bs'), u'CO\u2082')

    def test_eszett_euro(self):
        # MARC-8 mapping: Revised June 2004 to add the Eszett (M+C7) and the
        # Euro Sign (M+C8) to the MARC-8 set.
        self.assertEqual(marc8_to_unicode(b'ESZETT SYMBOL: \xc7 is U+00DF'),
                         u'ESZETT SYMBOL: \u00df is U+00DF')
        self.assertEqual(marc8_to_unicode(b'EURO SIGN: \xc8 is U+20AC'),
                         u'EURO SIGN: \u20ac is U+20AC')

    def test_alif(self):
        # MARC-8 mapping: Revised March 2005 to change the mapping from MARC-8
        # to Unicode for the Alif (M+2E) from U+02BE to U+02BC.
        self.assertEqual(marc8_to_unicode(b'ALIF: \xae is U+02BC'),
                         u'ALIF: \u02bc is U+02BC')

def suite():
    test_suite = makeSuite(MARC8Test, 'test')
    return test_suite
