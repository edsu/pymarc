import unittest
import re
import urllib

import pymarc

class MARCReaderFileTest(unittest.TestCase):
    """
    Tests for the pymarc.MARCReader class which provides iterator
    based access to a MARC file.
    """ 

    def setUp(self):
        self.reader = pymarc.MARCReader(file('test/test.dat'))

    def test_iterator(self):
        count = 0
        for record in self.reader:
            count += 1
        self.assertEquals(count, 10, 
                'found expected number of MARC21 records')

    def test_map_records(self):
        self.count = 0
        def f(r):
            self.count += 1
        pymarc.map_records(f, file('test/test.dat'))
        self.assertEquals(self.count, 10, 'map_records appears to work')

    def test_multi_map_records(self):
        self.count = 0
        def f(r):
            self.count += 1
        pymarc.map_records(f, file('test/test.dat'), file('test/test.dat'))
        self.assertEquals(self.count, 20, 'map_records appears to work')

    def test_string(self):
        ## basic test of stringification
        starts_with_leader = re.compile('^=LDR')
        has_numeric_tag = re.compile('\n=\d\d\d ')
        for record in self.reader:
            text = str(record)
            self.failUnless(starts_with_leader.search(text), 'got leader')
            self.failUnless(has_numeric_tag.search(text), 'got a tag')

    def test_url(self):
        reader = pymarc.MARCReader(urllib.urlopen(
            'http://inkdroid.org/data/marc.dat'))
        record = reader.next()
        self.assertEqual(record['245']['a'], 'Python pocket reference /')

    def test_codecs(self):
        import codecs
        reader = pymarc.MARCReader(codecs.open('test/test.dat',
            encoding='utf-8'))
        record = reader.next()
        self.assertEqual(record['245']['a'], u'ActivePerl with ASP and ADO /')

class MARCReaderStringTest(MARCReaderFileTest):

    def setUp(self):
        raw = file('test/test.dat').read()
        self.reader = pymarc.reader.MARCReader(raw)

    # inherit same tests from MARCReaderTestFile

def suite():
    file_suite = unittest.makeSuite(MARCReaderFileTest, 'test')
    string_suite = unittest.makeSuite(MARCReaderStringTest, 'test')
    test_suite = unittest.TestSuite((file_suite, string_suite))
    return test_suite

if __name__ == '__main__':
    unittest.main()
