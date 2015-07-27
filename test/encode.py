import unittest

from pymarc import MARCReader

class Encode(unittest.TestCase):

    def test_encode_decode(self):
        # get raw data from file
        with open('test/one.dat', 'rb') as fh:
            original = fh.read()

        # create a record object for the file
        with open('test/one.dat', 'rb') as fh:
            reader = MARCReader(fh)
            record = next(reader)
            # make sure original data is the same as
            # the record encoded as MARC
            raw = record.as_marc()
            self.assertEqual(original, raw)

    def test_encode_decode_alphatag(self):
        # get raw data from file containing non-numeric tags
        with open('test/alphatag.dat', 'rb') as fh:
            original = fh.read()

        # create a record object for the file
        with open('test/alphatag.dat', 'rb') as fh:
            reader = MARCReader(fh)
            record = next(reader)
            # make sure original data is the same as
            # the record encoded as MARC
            raw = record.as_marc()
            self.assertEqual(original, raw)

def suite():
    test_suite = unittest.makeSuite(Encode, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()

