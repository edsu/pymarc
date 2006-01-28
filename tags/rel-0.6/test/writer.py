import util
import unittest
import pymarc
import re

class MARCWriterTest(unittest.TestCase):

    def testWrite(self):

        # write a record off to a file
        writer = pymarc.MARCWriter('test/writer-test.dat')
        record = pymarc.Record()
        field = pymarc.Field('245', ['0','0'], ['a', 'foo'])
        record.addField(field)
        writer.write(record)
        writer.close()

        # read it back in
        reader = pymarc.MARCReader('test/writer-test.dat')
        record = reader.next()

def suite():
    suite = unittest.makeSuite(MARCWriterTest, 'test')
    return suite

if __name__ == "__main__":
    unittest.main()
