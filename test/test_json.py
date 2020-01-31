# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

import json
import unittest

import pymarc


class JsonReaderTest(unittest.TestCase):
    def setUp(self):
        with open("test/test.json") as fh:
            self.in_json = json.load(fh, strict=False)

        with open("test/test.json") as fh:
            self.reader = pymarc.JSONReader(fh)

    def testRoundtrip(self):
        """Test from and to json.

        Tests that result of loading records from the test file
        produces objects deeply equal to the result of loading
        marc-in-json files directly
        """
        recs = list(self.reader)
        self.assertEqual(
            len(self.in_json), len(recs), "Incorrect number of records found"
        )
        for i, rec in enumerate(recs):
            deserialized = json.loads(rec.as_json(), strict=False)
            comp = self.in_json[i]
            self.assertEqual(comp, deserialized)

    def testOneRecord(self):
        """Tests case when in source json there is only 1 record not wrapped in list."""
        data = json.dumps(self.in_json[0])
        reader = pymarc.JSONReader(data)
        self.assertEqual([rec.as_dict() for rec in reader][0], self.in_json[0])


class JsonTest(unittest.TestCase):
    def setUp(self):
        self.reader = pymarc.MARCReader(open("test/test.dat", "rb"))
        self._record = pymarc.Record()
        field = pymarc.Field(
            tag="245", indicators=["1", "0"], subfields=["a", "Python", "c", "Guido"]
        )
        self._record.add_field(field)

    def test_as_dict_single(self):
        _expected = {
            "fields": [
                {
                    "245": {
                        "ind1": "1",
                        "ind2": "0",
                        "subfields": [{"a": "Python"}, {"c": "Guido"}],
                    }
                }
            ],
            "leader": "          22        4500",
        }
        self.assertEqual(_expected, self._record.as_dict())

    def test_as_json_types(self):
        rd = self._record.as_dict()
        self.assertTrue(isinstance(rd, dict))
        self.assertTrue(isinstance(rd["leader"], str))
        self.assertTrue(isinstance(rd["fields"], list))
        self.assertTrue(isinstance(rd["fields"][0], dict))
        self.assertTrue(isinstance(rd["fields"][0], dict))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["ind1"], str))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["ind2"], str))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["subfields"], list))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["subfields"][0], dict))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["subfields"][0]["a"], str))
        self.assertTrue(isinstance(rd["fields"][0]["245"]["subfields"][1]["c"], str))

    def test_as_json_simple(self):
        record = json.loads(self._record.as_json())

        self.assertTrue("leader" in record)
        self.assertEqual(record["leader"], "          22        4500")

        self.assertTrue("fields" in record)
        self.assertTrue("245" in record["fields"][0])
        self.assertEqual(
            record["fields"][0]["245"],
            {
                u"subfields": [{u"a": u"Python"}, {u"c": u"Guido"}],
                u"ind2": u"0",
                u"ind1": u"1",
            },
        )

    def test_as_json_multiple(self):
        for record in self.reader:
            self.assertEqual(dict, json.loads(record.as_json()).__class__)


class JsonParse(unittest.TestCase):
    def setUp(self):
        self.reader_dat = pymarc.MARCReader(open("test/one.dat", "rb"))
        self.parse_json = pymarc.parse_json_to_array(open("test/one.json"))

        self.batch_xml = pymarc.parse_xml_to_array(open("test/batch.xml"))
        self.batch_json = pymarc.parse_json_to_array(open("test/batch.json"))

    def testRoundtrip(self):
        recs = list(self.reader_dat)
        self.assertEqual(
            len(self.parse_json), len(recs), "Incorrect number of records found"
        )
        for from_dat, from_json in zip(recs, self.parse_json):
            self.assertEqual(from_dat.as_marc(), from_json.as_marc(), "Icorrect Record")

    def testParseJsonXml(self):
        self.assertEqual(
            len(self.batch_json),
            len(self.batch_xml),
            "Incorrect number of parse records found",
        )
        for from_dat, from_json in zip(self.batch_json, self.batch_xml):
            self.assertEqual(from_dat.as_marc(), from_json.as_marc(), "Icorrect Record")


def suite():
    test_suite = unittest.makeSuite(JsonTest, "test")
    return test_suite


if __name__ == "__main__":
    unittest.main()
