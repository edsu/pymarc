import unittest
import sys

from pymarc.field import Field

class FieldTest(unittest.TestCase):

    def setUp(self):
        self.field = Field(
            tag = '245',
            indicators = [ 0, 1 ],
            subfields = [
                'a', 'Huckleberry Finn: ',
                'b', 'An American Odyssey'
            ]
        )

        self.controlfield = Field(
            tag = '008',
            data = '831227m19799999nyu           ||| | ger  '
        )

        self.subjectfield = Field(
            tag = '650',
            indicators = [' ', '0'],
            subfields = [
                'a', 'Python (Computer program language)',
                'v', 'Poetry.'
            ]
        )

    def test_string(self):
        self.assertEqual(str(self.field),
            '=245  01$aHuckleberry Finn: $bAn American Odyssey')

    def test_controlfield_string(self):
        self.assertEqual(str(self.controlfield),
            r'=008  831227m19799999nyu\\\\\\\\\\\|||\|\ger\\')

    def test_indicators(self):
        self.assertEqual(self.field.indicator1, '0')
        self.assertEqual(self.field.indicator2, '1')

    def test_subfields_created(self):
        subfields = self.field.subfields
        self.assertEqual(len(subfields), 4)

    def test_subfield_short(self):
        self.assertEqual(self.field['a'], 'Huckleberry Finn: ')
        self.assertEqual(self.field['z'], None)

    def test_subfields(self):
        self.assertEqual(self.field.get_subfields('a'),
            ['Huckleberry Finn: '])
        self.assertEqual(self.subjectfield.get_subfields('a'),
            ['Python (Computer program language)'])

    def test_subfields_multi(self):
        self.assertEqual(self.field.get_subfields('a','b'),
            ['Huckleberry Finn: ', 'An American Odyssey' ])
        self.assertEqual(self.subjectfield.get_subfields('a','v'),
            ['Python (Computer program language)', 'Poetry.' ])

    def test_encode(self):
        self.field.as_marc(encoding='utf-8')

    def test_membership(self):
        self.assertTrue('a' in self.field)
        self.assertFalse('zzz' in self.field)

    def test_iterator(self):
        string = ""
        for subfield in self.field:
            string += subfield[0]
            string += subfield[1]
        self.assertEqual(string, 'aHuckleberry Finn: bAn American Odyssey')

    def test_value(self):
        self.assertEqual(self.field.value(),
            'Huckleberry Finn: An American Odyssey')
        self.assertEqual(self.controlfield.value(),
                '831227m19799999nyu           ||| | ger  ')

    def test_non_integer_tag(self):
        # make sure this doesn't throw an exception
        field = Field(tag='3 0', indicators=[0, 1], subfields=['a', 'foo'])

    def test_add_subfield(self):
        field = Field(tag='245', indicators=[0, 1], subfields=['a', 'foo'])
        field.add_subfield('a','bar')
        self.assertEqual(field.__str__(), '=245  01$afoo$abar')

    def test_delete_subfield(self):
        field = Field(tag='200', indicators=[0,1], subfields=['a','My Title', 'a', 'Kinda Bogus Anyhow'])
        self.assertEqual(field.delete_subfield('z'), None)
        self.assertEqual(field.delete_subfield('a'), 'My Title')
        self.assertEqual(field.delete_subfield('a'), 'Kinda Bogus Anyhow')
        self.assertTrue(len(field.subfields) == 0)

    def test_is_subject_field(self):
        self.assertEqual(self.subjectfield.is_subject_field(), True)
        self.assertEqual(self.field.is_subject_field(), False)

    def test_format_field(self):
        self.subjectfield.add_subfield('6', '880-4')
        self.assertEqual(self.subjectfield.format_field(),
            'Python (Computer program language) -- Poetry.')
        self.field.add_subfield('6', '880-1')
        self.assertEqual(self.field.format_field(),
            'Huckleberry Finn:  An American Odyssey')

    def test_tag_normalize(self):
        f = Field(tag='42', indicators=['', ''])
        self.assertEqual(f.tag, '042')

    def test_alphatag(self):
        f = Field(tag='CAT', indicators=[0, 1], subfields=['a', 'foo'])
        self.assertEqual(f.tag, 'CAT')
        self.assertEqual(f['a'], 'foo')
        self.assertEqual(f.is_control_field(), False)

    def test_setitem_no_key(self):
        try:
            self.field['h'] = 'error'
        except KeyError:
            pass
        except Exception:
            e = sys.exc_info()[1]
            self.fail('Unexpected exception thrown: %s' % e)
        else:
            self.fail('KeyError not thrown')

    def test_setitem_repeated_key(self):
        try:
            self.field.add_subfield('a','bar')
            self.field['a'] = 'error'
        except KeyError:
            pass
        except Exception:
            e = sys.exc_info()[1]
            self.fail('Unexpected exception thrown: %s' % e)
        else:
            self.fail('KeyError not thrown')

    def test_iter_over_controlfield(self):
        try:
            l = [subfield for subfield in self.controlfield]
        except AttributeError as e:
            self.fail('Error during iteration: %s' % e)

    def test_setitem(self):
        self.field['a'] = 'changed'
        self.assertEqual(self.field['a'], 'changed')

def suite():
    test_suite = unittest.makeSuite(FieldTest, 'test')
    return test_suite

if __name__ == "__main__":
    unittest.main()


