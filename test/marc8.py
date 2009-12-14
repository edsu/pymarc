from unittest import TestCase, makeSuite
import codecs

from pymarc import marc8_to_unicode, Field, Record, MARCReader, MARCWriter

class MARC8Test(TestCase):
    
    def test_marc8_reader(self):
        marc8_file = file('test/marc8.dat')
        reader = MARCReader(marc8_file)
        self.assertEquals(type(reader.next()), Record)

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

    def test_unicode(self):
        record = Record()
        record.add_field(Field(245, ['1', '0'], ['a', unichr(0x1234)]))
        writer = MARCWriter(open('test/foo', 'w'))
        writer.write(record)
        writer.close()

        reader = MARCReader(open('test/foo'))
        record = reader.next()
        self.assertEqual(record['245']['a'], unichr(0x1234))

def suite():
    test_suite = makeSuite(MARC8Test, 'test')
    return test_suite 
