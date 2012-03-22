from unittest import TestCase, makeSuite

import os
import codecs

from pymarc import marc8_to_unicode, Field, Record, MARCReader, MARCWriter

class MARC8Test(TestCase):
    
    def test_marc8_reader(self):
        reader = MARCReader(file('test/marc8.dat'))
        r =  reader.next()
        self.assertEquals(type(r), Record)
        utitle = r['240']['a']
        self.assertEquals(type(utitle), str)
        self.assertEquals(utitle, 'De la solitude \xe1a la communaut\xe2e.')

    def test_marc8_reader_to_unicode(self):
        reader = MARCReader(file('test/marc8.dat'), to_unicode=True)
        r =  reader.next()
        self.assertEquals(type(r), Record)
        utitle = r['240']['a']
        self.assertEquals(type(utitle), unicode)
        self.assertEquals(utitle, u'De la solitude \xe0 la communaut\xe9.')
        
    def test_marc8_reader_to_unicode_bad_eacc_sequence(self):
        reader = MARCReader(file('test/bad_eacc_encoding.dat'), to_unicode=True, hide_utf8_warnings=True)
        try:
            r =  reader.next()
            self.assertFalse("Was able to decode invalid MARC8") 
        except UnicodeDecodeError:
            self.assertTrue("Caught UnicodeDecodeError as expected") 

    def test_marc8_reader_to_unicode_bad_escape(self):
        reader = MARCReader(file('test/bad_marc8_escape.dat'), to_unicode=True)
        r =  reader.next()
        self.assertEquals(type(r), Record)
        upublisher = r['260']['b']
        self.assertEquals(type(upublisher), unicode)
        self.assertEquals(upublisher, u'La Soci\xe9t\x1b,')

    def test_marc8_to_unicode(self):
        marc8_file = file('test/test_marc8.txt')
        utf8_file = file('test/test_utf8.txt')
        count = 0

        while True:
            marc8 = marc8_file.readline().strip("\n")
            utf8 = utf8_file.readline().strip("\n")
            if marc8 == '' or utf8 == '':
                break
            count += 1
            self.assertEquals(marc8_to_unicode(marc8).encode('utf8'), utf8)

        self.assertEquals(count, 1515)

    def test_writing_unicode(self):
        record = Record()
        record.add_field(Field(245, ['1', '0'], ['a', unichr(0x1234)]))
        record.leader = '         a              '
        writer = MARCWriter(open('test/foo', 'w'))
        writer.write(record)
        writer.close()

        reader = MARCReader(open('test/foo'), to_unicode=True)
        record = reader.next()
        self.assertEqual(record['245']['a'], unichr(0x1234))

        os.remove('test/foo')

    def test_reading_utf8_with_flag(self):
        reader = MARCReader(open('test/utf8_with_leader_flag.dat'))
        record = reader.next()
        self.assertEquals(type(record), Record)
        utitle = record['240']['a']
        self.assertEquals(type(utitle), str)
        self.assertEquals(utitle,
            'De la solitude a\xcc\x80 la communaute\xcc\x81.')

        reader = MARCReader(open('test/utf8_with_leader_flag.dat'), 
                            to_unicode=True)
        record = reader.next()
        self.assertEquals(type(record), Record)
        utitle = record['240']['a']
        self.assertEquals(type(utitle), unicode)
        self.assertEquals(utitle, u'De la solitude a' + unichr(0x0300) +
            ' la communaute' + unichr(0x0301) + '.')

    def test_reading_utf8_without_flag(self):
        reader = MARCReader(open('test/utf8_without_leader_flag.dat'))
        record = reader.next()
        self.assertEquals(type(record), Record)
        utitle = record['240']['a']
        self.assertEquals(type(utitle), str)
        self.assertEquals(utitle,
            'De la solitude a\xcc\x80 la communaute\xcc\x81.')

        reader = MARCReader(open('test/utf8_without_leader_flag.dat'), 
                            to_unicode=True, hide_utf8_warnings=True)
        record = reader.next()
        self.assertEquals(type(record), Record)
        utitle = record['240']['a']
        self.assertEquals(type(utitle), unicode)
        # unless you force utf-8 characters will get lost and
        # warnings will appear in the terminal
        self.assertEquals(utitle, 'De la solitude a   la communaute .')

        # force reading as utf-8
        reader = MARCReader(open('test/utf8_without_leader_flag.dat'), 
                            to_unicode=True, force_utf8=True,
                            hide_utf8_warnings=True)
        record = reader.next()
        self.assertEquals(type(record), Record)
        utitle = record['240']['a']
        self.assertEquals(type(utitle), unicode)
        self.assertEquals(utitle, u'De la solitude a' + unichr(0x0300) +
            ' la communaute' + unichr(0x0301) + '.')

    def test_record_create_force_utf8(self, force_utf8=True):
        r = Record(force_utf8=True)
        self.assertEqual(r.leader[9], 'a')

    def test_subscript_2(self):
        self.assertEqual(marc8_to_unicode('CO\x1bb2\x1bs is a gas'), u'CO\u2082 is a gas')
        self.assertEqual(marc8_to_unicode('CO\x1bb2\x1bs'), u'CO\u2082')

def suite():
    test_suite = makeSuite(MARC8Test, 'test')
    return test_suite 
