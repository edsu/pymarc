# -*- coding: utf-8 -*-

import unittest
import pymarc

try:
    import json
except ImportError:
    import simplejson as json

class JsonTest(unittest.TestCase):

    def setUp(self):
        self.reader = pymarc.MARCReader(file('test/test.dat'))
        self._record = pymarc.Record()
        field = pymarc.Field(
            tag = '245',
            indicators = ['1', '0'],
            subfields = ['a', 'Python', 'c', 'Guido'])
        self._record.add_field(field)

    def test_as_dict_single(self):
        _expected = {
            'fields': {
                '245': {
                    'indicators': ['1', '0'],
                    'subfields': {'a': 'Python', 'c': 'Guido'}
                }
            },
            'leader': '          22        4500'
        }
        self.assertEqual(_expected, self._record.as_dict())

    def test_as_dict_multiple(self):
        for record in self.reader:
            self.assertTrue(dict, record.as_dict().__class__)
            self.assertTrue('fields' in record.as_dict())
            self.assertTrue('leader' in record.as_dict())

    def test_as_json_simple(self):
        self.assertTrue('leader' in json.loads(self._record.as_json()))
        self.assertTrue('fields' in json.loads(self._record.as_json()))
        self.assertTrue('245' in json.loads(self._record.as_json())['fields'])
        self.assertTrue('indicators' in json.loads(self._record.as_json())['fields']['245'])
        self.assertTrue('subfields' in json.loads(self._record.as_json())['fields']['245'])
        self.assertEquals(dict, json.loads(self._record.as_json())['fields']['245'].__class__)
        self.assertEquals(list, json.loads(self._record.as_json())['fields']['245']['indicators'].__class__)
        self.assertEquals(dict, json.loads(self._record.as_json())['fields']['245']['subfields'].__class__)

    def test_as_json_multiple(self):
        for record in self.reader:
            self.assertTrue(basestring in record.as_json().__class__.__bases__)
            self.assertEquals(dict, json.loads(record.as_json()).__class__)

def suite():
    test_suite = unittest.makeSuite(JsonTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()

