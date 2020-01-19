# -*- coding: utf-8 -*-
import re
import unittest

import six

import pymarc


class MARCReaderBaseTest(object):
    def test_iterator(self):
        count = 0
        for record in self.reader:
            count += 1
        self.assertEqual(count, 10, "found expected number of MARC21 records")

    def test_string(self):
        # basic test of stringification
        starts_with_leader = re.compile("^=LDR")
        has_numeric_tag = re.compile(r"\n=\d\d\d ")
        for record in self.reader:
            text = str(record)
            self.assertTrue(starts_with_leader.search(text), "got leader")
            self.assertTrue(has_numeric_tag.search(text), "got a tag")


class MARCReaderFileTest(unittest.TestCase, MARCReaderBaseTest):
    """Tests MARCReader which provides iterator based access to a MARC file."""

    def setUp(self):
        self.reader = pymarc.MARCReader(open("test/test.dat", "rb"))

    def tearDown(self):
        if self.reader:
            self.reader.close()

    def test_map_records(self):
        self.count = 0

        def f(r):
            self.count += 1

        with open("test/test.dat", "rb") as fh:
            pymarc.map_records(f, fh)
            self.assertEqual(self.count, 10, "map_records appears to work")

    def test_multi_map_records(self):
        self.count = 0

        def f(r):
            self.count += 1

        fh1 = open("test/test.dat", "rb")
        fh2 = open("test/test.dat", "rb")
        pymarc.map_records(f, fh1, fh2)
        self.assertEqual(self.count, 20, "map_records appears to work")
        fh1.close()
        fh2.close()

    def disabled_test_codecs(self):
        import codecs

        with codecs.open("test/test.dat", encoding="utf-8") as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record["245"]["a"], u"ActivePerl with ASP and ADO /")

    def test_bad_subfield(self):
        with open("test/bad_subfield_code.dat", "rb") as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record["245"]["a"], u"ActivePerl with ASP and ADO /")

    def test_bad_indicator(self):
        with open("test/bad_indicator.dat", "rb") as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record["245"]["a"], "Aristocrats of color :")

    def test_regression_45(self):
        # https://github.com/edsu/pymarc/issues/45
        with open("test/regression45.dat", "rb") as fh:
            reader = pymarc.MARCReader(fh)
            record = next(reader)
            self.assertEqual(record["752"]["a"], "Russian Federation")
            self.assertEqual(record["752"]["b"], "Kostroma Oblast")
            self.assertEqual(record["752"]["d"], "Kostroma")

    def test_strict_mode(self):
        with self.assertRaises(pymarc.exceptions.BaseAddressInvalid), open(
            "test/bad_records.mrc", "rb"
        ) as fh:
            reader = pymarc.MARCReader(fh)
            for record in reader:
                self.assertIsNotNone(reader.current_chunk)

    # inherit same tests from MARCReaderBaseTest


class MARCReaderStringTest(unittest.TestCase, MARCReaderBaseTest):
    def setUp(self):
        fh = open("test/test.dat")
        raw = fh.read()
        fh.close()

        self.reader = pymarc.reader.MARCReader(six.b(raw))

    # inherit same tests from MARCReaderBaseTest


class MARCReaderFilePermissiveTest(unittest.TestCase):
    """Tests MARCReader which provides iterator based access in a permissive way."""

    def setUp(self):
        self.reader = pymarc.MARCReader(
            open("test/bad_records.mrc", "rb"), permissive=True
        )

    def tearDown(self):
        if self.reader:
            self.reader.close()

    def test_permissive_mode(self):
        """Test permissive mode.

        In bad_records.mrc we expect following records in the given order :

        * working record
        * BaseAddressInvalid (base_address (99937) >= len(marc))
        * BaseAddressNotFound (base_address (00000) <= 0)
        * RecordDirectoryInvalid (len(directory) % DIRECTORY_ENTRY_LEN != 0)
        * UnicodeDecodeError (directory with non ascii code (245ù0890000))
        * ValueError (base_address with literal (f0037))
        * last record should be ok
        """
        expected_exceptions = [
            None,
            pymarc.exceptions.BaseAddressInvalid,
            pymarc.exceptions.BaseAddressNotFound,
            pymarc.exceptions.RecordDirectoryInvalid,
            UnicodeDecodeError,
            ValueError,
            pymarc.exceptions.NoFieldsFound,
            None,
        ]
        for exception_type in expected_exceptions:
            record = next(self.reader)
            self.assertIsNotNone(self.reader.current_chunk)
            if exception_type is None:
                self.assertIsNotNone(record)
                self.assertIsNone(self.reader.current_exception)
                self.assertEqual(record["245"]["a"], "The pragmatic programmer : ")
                self.assertEqual(record["245"]["b"], "from journeyman to master /")
                self.assertEqual(record["245"]["c"], "Andrew Hunt, David Thomas.")
            else:
                self.assertIsNone(
                    record,
                    "expected parsing error with the following "
                    "exception %r" % exception_type,
                )
                self.assertTrue(
                    isinstance(self.reader.current_exception, exception_type),
                    "expected %r exception, "
                    "received: %r" % (exception_type, self.reader.current_exception),
                )


def suite():
    file_suite = unittest.makeSuite(MARCReaderFileTest, "test")
    string_suite = unittest.makeSuite(MARCReaderStringTest, "test")
    permissive_file_suite = unittest.makeSuite(MARCReaderFilePermissiveTest, "test")
    test_suite = unittest.TestSuite((file_suite, string_suite, permissive_file_suite))
    return test_suite


if __name__ == "__main__":
    unittest.main()
