import unittest
import pymarc
import os
from six import BytesIO


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

    def test_own_file_handle_true(self):
        """
        If a MARCWriter is created with own_file_handle = True, then when the
        MARCWriter is closed the file handle is also closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.MARCWriter(file_handle, own_file_handle = True)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertTrue(
            file_handle.closed,
            'The file handle should close when the writer closes')

    def test_own_file_handle_false(self):
        """
        If a MARCWriter is created with own_file_handle = False, then when the
        MARCWriter is closed the file handle is NOT also closed.
        """
        file_handle = BytesIO()
        self.assertFalse(
            file_handle.closed,
            'The file handle should be open')
        writer = pymarc.MARCWriter(file_handle, own_file_handle = False)
        self.assertFalse(
            file_handle.closed,
            'The file handle should still be open')
        writer.close()
        self.assertFalse(
            file_handle.closed,
            'The file handle should NOT close when the writer closes')

def suite():
    test_suite = unittest.makeSuite(MARCWriterTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
