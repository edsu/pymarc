import unittest
from test import record
from test import field
from test import reader 
from test import encode
from test import writer
from test import marc8
from test import xml_test


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(record.suite())
    test_suite.addTest(field.suite())
    test_suite.addTest(reader.suite())
    test_suite.addTest(encode.suite())
    test_suite.addTest(writer.suite())
    test_suite.addTest(marc8.suite())
    test_suite.addTest(xml_test.suite())
    return test_suite

runner = unittest.TextTestRunner()
runner.run(suite())

