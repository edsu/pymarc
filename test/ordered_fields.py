import unittest
import pymarc
import os

class OrderedFieldsTest(unittest.TestCase):

    def test_add_ordered_fields(self):

        record = pymarc.Record()
        for tag in ('999', '888', '111', 'abc', '666', '988', '998'):
            field = pymarc.Field(tag, ['0', '0'], ['a', 'foo'])
            record.add_ordered_field(field)

        # ensure all numeric fields are in strict order
        ordered = True
        last_tag = 0;
        for field in record:
            if not field.tag.isdigit():
                continue
            curr_tag = int(field.tag)
            if last_tag > curr_tag:
                ordered = False
            last_tag = curr_tag

        self.assertTrue(ordered, "Fields are not strictly ordered numerically")

    def test_add_grouped_fields(self):
        record = pymarc.Record()
        for tag in ('999', '888', '111', 'abc', '666', '988', '998'):
            field = pymarc.Field(tag, ['0', '0'], ['a', 'foo'])
            record.add_grouped_field(field)

        # ensure all numeric fields are in grouped order
        grouped = list()
        for field in record:
            if not field.tag.isdigit():
                continue
            grouped.append(field.tag)

        exp = ['111', '666', '888', '999', '988', '998']

        self.assertEqual(grouped, exp, "Fields are not grouped numerically")

def suite():
    test_suite = unittest.makeSuite(OrderedFieldsTest, 'test')
    return test_suite

if __name__ == '__main__':
    unittest.main()
