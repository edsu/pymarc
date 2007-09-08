from pymarc import marc8_to_unicode
from unittest import TestCase

class MARC8Test(TestCase):

  def test_marc8_to_unicode(self):
    marc8_file = file('test/test_marc8.txt')
    utf8_file = file('test/test_utf8.txt')
    count = 0

    while True:
      marc8 = marc8_file.readline().strip("\n")
      utf8 = utf8_file.readline().strip("\n")
      if marc8 == '' or utf8 == '':
        break
      count += 1
      self.assertEquals(marc8_to_unicode(marc8).encode('utf8'), utf8)

    self.assertEquals(count, 1514)

