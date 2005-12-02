import unittest
import test.record
import test.field
import test.reader 
import test.encode
import test.writer

def suite():
    suite = unittest.TestSuite()
    suite.addTest( test.record.suite() )
    suite.addTest( test.field.suite() )
    suite.addTest( test.reader.suite() )
    suite.addTest( test.encode.suite() )
    suite.addTest( test.writer.suite() )
    return suite

runner = unittest.TextTestRunner()
runner.run( suite() )

