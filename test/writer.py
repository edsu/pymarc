import unittest
import pymarc
import os

class MARCWriterTest(unittest.TestCase):

    def test_write(self):

        # write a record off to a file
        writer = pymarc.MARCWriter(open('test/writer-test.dat', 'wb'))
        record = pymarc.Record()
        field = pymarc.Field('245', ['0', '0'], ['a', 'foo'])
        record.add_field(field)
        writer.write(record)
        writer.close()

        # read it back in
        reader = pymarc.MARCReader(open('test/writer-test.dat', 'rb'))
        r = next(reader)
        reader.close()

        # remove it
        os.remove('test/writer-test.dat')

def suite():
    test_suite = unittest.makeSuite(MARCWriterTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
