import unittest
from test import record
from test import field
from test import reader 
from test import encode
from test import writer

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(record.suite())
    test_suite.addTest(field.suite())
    test_suite.addTest(reader.suite())
    test_suite.addTest(encode.suite())
    test_suite.addTest(writer.suite())
    return test_suite

runner = unittest.TextTestRunner()
runner.run(suite())

