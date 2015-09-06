import re
import unittest

import six
import pymarc

from six.moves.urllib.request import urlopen

class MARCReaderFileTest(unittest.TestCase):
    """
    Tests for the pymarc.MARCReader class which provides iterator
    based access to a MARC file.
    """

    def setUp(self):
        self.reader = pymarc.MARCReader(open('test/test.dat', 'rb'))

    def tearDown(self):
        if self.reader:
            self.reader.close()

    def test_iterator(self):
        count = 0
        for record in self.reader:
            count += 1
        self.assertEqual(count, 10,
                'found expected number of MARC21 records')

    def test_map_records(self):
        self.count = 0
        def f(r):
            self.count += 1
        with open('test/test.dat', 'rb') as fh:
            pymarc.map_records(f, fh)
            self.assertEqual(self.count, 10, 'map_records appears to work')

    def test_multi_map_records(self):
        self.count = 0
        def f(r):
            self.count += 1
        fh1 = open('test/test.dat', 'rb')
        fh2 = open('test/test.dat', 'rb')
        pymarc.map_records(f, fh1, fh2)
        self.assertEqual(self.count, 20, 'map_records appears to work')
        fh1.close()
        fh2.close()

    def test_string(self):
        ## basic test of stringification
        starts_with_leader = re.compile('^=LDR')
        has_numeric_tag = re.compile('\n=\d\d\d ')
        for record in self.reader:
            text = str(record)
            self.assertTrue(starts_with_leader.search(text), 'got leader')
            self.assertTrue(has_numeric_tag.search(text), 'got a tag')

    def disabled_test_codecs(self):
        import codecs
        with codecs.open('test/test.dat', encoding='utf-8') as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record['245']['a'], u'ActivePerl with ASP and ADO /')

    def test_bad_indicator(self):
        with open('test/bad_indicator.dat', 'rb') as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record['245']['a'], 'Aristocrats of color :')

    def test_regression_45(self):
        # https://github.com/edsu/pymarc/issues/45
        with open('test/regression45.dat', 'rb') as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record['752']['a'], 'Russian Federation')
            self.assertEqual(record['752']['b'], 'Kostroma Oblast')
            self.assertEqual(record['752']['d'], 'Kostroma')


class MARCReaderStringTest(MARCReaderFileTest):

    def setUp(self):
        fh = open('test/test.dat')
        raw = fh.read()
        fh.close()

        self.reader = pymarc.reader.MARCReader(six.b(raw))

    # inherit same tests from MARCReaderTestFile

def suite():
    file_suite = unittest.makeSuite(MARCReaderFileTest, 'test')
    string_suite = unittest.makeSuite(MARCReaderStringTest, 'test')
    test_suite = unittest.TestSuite((file_suite, string_suite))
    return test_suite

if __name__ == '__main__':
    unittest.main()
