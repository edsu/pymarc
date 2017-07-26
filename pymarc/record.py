import re
import six
import logging

from six import Iterator

from pymarc.exceptions import BaseAddressInvalid, RecordLeaderInvalid, \
        BaseAddressNotFound, RecordDirectoryInvalid, NoFieldsFound, \
        FieldNotFound
from pymarc.constants import LEADER_LEN, DIRECTORY_ENTRY_LEN, END_OF_RECORD
from pymarc.field import Field, SUBFIELD_INDICATOR, END_OF_FIELD, \
        map_marc8_field, RawField
from pymarc.marc8 import marc8_to_unicode

izip_longest = six.moves.zip_longest

try:
    # the json module was included in the stdlib in python 2.6
    # http://docs.python.org/library/json.html
    import json
except ImportError:
    # simplejson 2.0.9 is available for python 2.4+
    # http://pypi.python.org/pypi/simplejson/2.0.9
    # simplejson 1.7.3 is available for python 2.3+
    # http://pypi.python.org/pypi/simplejson/1.7.3
    import simplejson as json


isbn_regex = re.compile(r'([0-9\-xX]+)')

@six.python_2_unicode_compatible
class Record(Iterator):
    """
    A class for representing a MARC record. Each Record object is made up of
    multiple Field objects. You'll probably want to look at the docs for Field
    to see how to fully use a Record object.

    Basic usage:

        field = Field(
            tag = '245',
            indicators = ['0','1'],
            subfields = [
                'a', 'The pragmatic programmer : ',
                'b', 'from journeyman to master /',
                'c', 'Andrew Hunt, David Thomas.',
            ])

        record.add_field(field)

    Or creating a record from a chunk of MARC in transmission format:

        record = Record(data=chunk)

    Or getting a record as serialized MARC21.

        raw = record.as_marc()

    You'll normally want to use a MARCReader object to iterate through
    MARC records in a file.
    """

    def __init__(self, data='', to_unicode=True, force_utf8=False,
        hide_utf8_warnings=False, utf8_handling='strict',
        leader=' ' * LEADER_LEN):
        self.leader = leader[0:10] + '22' + leader[12:20] + '4500'
        self.fields = list()
        self.pos = 0
        self.force_utf8 = force_utf8
        if len(data) > 0:
            self.decode_marc(data, to_unicode=to_unicode,
                             force_utf8=force_utf8,
                             hide_utf8_warnings=hide_utf8_warnings,
                             utf8_handling=utf8_handling)
        elif force_utf8:
            self.leader = self.leader[0:9] + 'a' + self.leader[10:]

    def __str__(self):
        """
        In a string context a Record object will return a prettified version
        of the record in MARCMaker format. See the docstring for Field.__str__
        for more information.
        """
        # join is significantly faster than concatenation
        text_list = ['=LDR  %s' % self.leader]
        text_list.extend([six.text_type(field) for field in self.fields])
        text = '\n'.join(text_list) + '\n'
        return text

    def __getitem__(self, tag):
        """
        Allows a shorthand lookup by tag:

            record['245']

        """
        fields = self.get_fields(tag)
        if len(fields) > 0:
            return fields[0]
        return None

    def __contains__(self, tag):
        """
        Allows a shorthand test of tag membership:

            '245' in record

        """
        fields = self.get_fields(tag)
        return len(fields) > 0

    def __iter__(self):
        self.__pos = 0
        return self

    def __next__(self):
        if self.__pos >= len(self.fields):
            raise StopIteration
        self.__pos += 1
        return self.fields[self.__pos - 1]

    def add_field(self, *fields):
        """
        add_field() will add pymarc.Field objects to a Record object.
        Optionally you can pass in multiple fields.
        """
        self.fields.extend(fields)

    def add_grouped_field(self, *fields):
        """
        add_grouped_field() will add pymarc.Field objects to a Record object,
        attempting to maintain a loose numeric order per the MARC standard for
        "Organization of the record" (http://www.loc.gov/marc/96principl.html)
        Optionally you can pass in multiple fields.
        """
        for f in fields:
            if len(self.fields) == 0 or not f.tag.isdigit():
                self.fields.append(f)
                continue
            self._sort_fields(f, 'grouped')

    def add_ordered_field(self, *fields):
        """
        add_ordered_field() will add pymarc.Field objects to a Record object,
        attempting to maintain a strict numeric order.
        Optionally you can pass in multiple fields.
        """
        for f in fields:
            if len(self.fields) == 0 or not f.tag.isdigit():
                self.fields.append(f)
                continue
            self._sort_fields(f, 'ordered')

    def _sort_fields(self, field, mode):
        if mode == 'grouped':
            tag = int(field.tag[0])
        else:
            tag = int(field.tag)

        i, last_tag = 0, 0
        for selff in self.fields:
            i += 1
            if not selff.tag.isdigit():
                self.fields.insert(i - 1, field)
                break

            if mode == 'grouped':
                last_tag = int(selff.tag[0])
            else:
                last_tag = int(selff.tag)

            if last_tag > tag:
                self.fields.insert(i - 1, field)
                break
            if len(self.fields) == i:
                self.fields.append(field)
                break

    def remove_field(self, *fields):
        """
        remove_field() will remove one or more pymarc.Field objects from
        a Record object.
        """
        for f in fields:
            try:
                self.fields.remove(f)
            except ValueError:
                raise FieldNotFound

    def remove_fields(self, *tags):
        """
        Remove all the fields with the tags passed to the function:

            self.remove_fields('200', '899')

        will remove all the fields marked with tags '200' or '899'.
        """
        self.fields[:] = (field for field in self.fields if field.tag not in tags)

    def get_fields(self, *args):
        """
        When passed a tag ('245'), get_fields() will return a list of all the
        fields in a record with a given tag.

            title = record.get_fields('245')

        If no fields with the specified
        tag are found then an empty list is returned. If you are interested
        in more than one tag you can pass in a list:

            subjects = record.get_fields('600', '610', '650')

        If no tag is passed in to get_fields() a list of all the fields will be
        returned.
        """
        if (len(args) == 0):
            return self.fields

        return [f for f in self.fields if f.tag in args]

    def decode_marc(self, marc, to_unicode=True, force_utf8=False,
        hide_utf8_warnings=False, utf8_handling='strict'):
        """
        decode_marc() accepts a MARC record in transmission format as a
        a string argument, and will populate the object based on the data
        found. The Record constructor actually uses decode_marc() behind
        the scenes when you pass in a chunk of MARC data to it.

        """
        # extract record leader
        self.leader = marc[0:LEADER_LEN].decode('ascii')
        if len(self.leader) != LEADER_LEN:
            raise RecordLeaderInvalid

        if self.leader[9] == 'a' or self.force_utf8:
            encoding = 'utf-8'
        else:
            encoding = 'iso8859-1'

        # extract the byte offset where the record data starts
        base_address = int(marc[12:17])
        if base_address <= 0:
            raise BaseAddressNotFound
        if base_address >= len(marc):
            raise BaseAddressInvalid

        # extract directory, base_address-1 is used since the
        # director ends with an END_OF_FIELD byte
        directory = marc[LEADER_LEN:base_address-1].decode('ascii')

        # determine the number of fields in record
        if len(directory) % DIRECTORY_ENTRY_LEN != 0:
            raise RecordDirectoryInvalid
        field_total = len(directory) / DIRECTORY_ENTRY_LEN

        # add fields to our record using directory offsets
        field_count = 0
        while field_count < field_total:
            entry_start = field_count * DIRECTORY_ENTRY_LEN
            entry_end = entry_start + DIRECTORY_ENTRY_LEN
            entry = directory[entry_start:entry_end]
            entry_tag = entry[0:3]
            entry_length = int(entry[3:7])
            entry_offset = int(entry[7:12])
            entry_data = marc[base_address + entry_offset :
                base_address + entry_offset + entry_length - 1]

            # assume controlfields are numeric; replicates ruby-marc behavior
            if entry_tag < '010' and entry_tag.isdigit():
                if to_unicode:
                    field = Field(tag=entry_tag, data=entry_data.decode(encoding))
                else:
                    field = RawField(tag=entry_tag, data=entry_data)
            else:
                subfields = list()
                subs = entry_data.split(SUBFIELD_INDICATOR.encode('ascii'))

                # The MARC spec requires there to be two indicators in a
                # field. However experience in the wild has shown that
                # indicators are sometimes missing, and sometimes there
                # are too many. Rather than throwing an exception because
                # we can't find what we want and rejecting the field, or
                # barfing on the whole record we'll try to use what we can
                # find. This means missing indicators will be recorded as
                # blank spaces, and any more than 2 are dropped on the floor.

                first_indicator = second_indicator = ' '
                subs[0] = subs[0].decode('ascii')
                if len(subs[0]) == 0:
                    logging.warning("missing indicators: %s", entry_data)
                    first_indicator = second_indicator = ' '
                elif len(subs[0]) == 1:
                    logging.warning("only 1 indicator found: %s", entry_data)
                    first_indicator = subs[0][0]
                    second_indicator = ' '
                elif len(subs[0]) > 2:
                    logging.warning("more than 2 indicators found: %s", entry_data)
                    first_indicator = subs[0][0]
                    second_indicator = subs[0][1]
                else:
                    first_indicator = subs[0][0]
                    second_indicator = subs[0][1]

                for subfield in subs[1:]:
                    if len(subfield) == 0:
                        continue
                    code = subfield[0:1].decode('ascii')
                    data = subfield[1:]

                    if to_unicode:
                        if self.leader[9] == 'a' or force_utf8:
                            data = data.decode('utf-8', utf8_handling)
                        else:
                            data = marc8_to_unicode(data, hide_utf8_warnings)
                    subfields.append(code)
                    subfields.append(data)
                if to_unicode:
                    field = Field(
                        tag = entry_tag,
                        indicators = [first_indicator, second_indicator],
                        subfields = subfields,
                    )
                else:
                    field = RawField(
                        tag = entry_tag,
                        indicators = [first_indicator, second_indicator],
                        subfields = subfields,
                    )
            self.add_field(field)
            field_count += 1

        if field_count == 0:
            raise NoFieldsFound

    def as_marc(self):
        """
        returns the record serialized as MARC21
        """
        fields = b''
        directory = b''
        offset = 0

        # build the directory
        # each element of the directory includes the tag, the byte length of
        # the field and the offset from the base address where the field data
        # can be found
        if self.leader[9] == 'a' or self.force_utf8:
            encoding = 'utf-8'
        else:
            encoding = 'iso8859-1'

        for field in self.fields:
            field_data = field.as_marc(encoding=encoding)
            fields += field_data
            if field.tag.isdigit():
                directory += ('%03d' % int(field.tag)).encode(encoding)
            else:
                directory += ('%03s' % field.tag).encode(encoding)
            directory += ('%04d%05d' % (len(field_data), offset)).encode(encoding)

            offset += len(field_data)

        # directory ends with an end of field
        directory += END_OF_FIELD.encode(encoding)

        # field data ends with an end of record
        fields += END_OF_RECORD.encode(encoding)

        # the base address where the directory ends and the field data begins
        base_address = LEADER_LEN + len(directory)

        # figure out the length of the record
        record_length = base_address + len(fields)

        # update the leader with the current record length and base address
        # the lengths are fixed width and zero padded
        strleader = '%05d%s%05d%s' % \
            (record_length, self.leader[5:12], base_address, self.leader[17:])
        leader = strleader.encode(encoding)

        return leader + directory + fields

    # alias for backwards compatibility
    as_marc21 = as_marc

    def as_dict(self):
        """
        Turn a MARC record into a dictionary, which is used for ``as_json``.
        """
        record = {}
        record['leader'] = self.leader
        record['fields'] = []
        for field in self:
            if field.is_control_field():
                record['fields'].append({field.tag: field.data})
            else:
                fd = {}
                fd['subfields'] = []
                fd['ind1'] = field.indicator1
                fd['ind2'] = field.indicator2
                for tag, value in izip_longest(*[iter(field.subfields)] * 2):
                    fd['subfields'].append({tag: value})
                record['fields'].append({field.tag: fd})
        return record  # as dict

    def as_json(self, **kwargs):
        """
        Serialize a record as JSON according to
        http://dilettantes.code4lib.org/blog/2010/09/a-proposal-to-serialize-marc-in-json/
        """
        return json.dumps(self.as_dict(), **kwargs)

    def title(self):
        """
        Returns the title of the record (245 $a an $b).
        """
        try:
            title = self['245']['a']
        except TypeError:
            title = None
        if title:
            try:
                title += " " + self['245']['b']
            except TypeError:
                pass
        return title

    def isbn(self):
        """
        Returns the first ISBN in the record or None if one is not
        present. The returned ISBN will be all numeric, except for an
        x/X which may occur in the checksum position.  Dashes and
        extraneous information will be automatically removed. If you need
        this information you'll want to look directly at the 020 field,
        e.g. record['020']['a']
        """
        try:
            isbn_number = self['020']['a']
            match = isbn_regex.search(isbn_number)
            if match:
                return match.group(1).replace('-', '')
        except TypeError:
            # ISBN not set
            pass
        return None

    def author(self):
        if self['100']:
            return self['100'].format_field()
        elif self['110']:
            return self['110'].format_field()
        elif self['111']:
            return self['111'].format_field()
        return None

    def uniformtitle(self):
        if self['130']:
            return self['130'].format_field()
        elif self['240']:
            return self['240'].format_field()
        return None

    def series(self):
        """
        Note: 490 supersedes the 440 series statement which was both
        series statement and added entry. 8XX fields are added entries.
        """
        serieslist = self.get_fields('440', '490', '800', '810', '811', '830')
        return serieslist

    def subjects(self):
        """
        Note: Fields 690-699 are considered "local" added entry fields but
        occur with some frequency in OCLC and RLIN records.
        """
        subjlist = self.get_fields('600', '610', '611', '630', '648', '650',
            '651', '653', '654', '655', '656', '657', '658', '662', '690',
            '691', '696', '697', '698', '699')
        return subjlist

    def addedentries(self):
        """
        Note: Fields 790-799 are considered "local" added entry fields but
        occur with some frequency in OCLC and RLIN records.
        """
        aelist = self.get_fields('700', '710', '711', '720', '730', '740',
            '752', '753', '754', '790', '791', '792', '793', '796', '797',
            '798', '799')
        return aelist

    def location(self):
        loc = self.get_fields('852')
        return loc

    def notes(self):
        """
        Return all 5xx fields in an array.
        """
        notelist = self.get_fields('500', '501', '502', '504', '505',
            '506', '507', '508', '510', '511', '513', '514', '515',
            '516', '518', '520', '521', '522', '524', '525', '526',
            '530', '533', '534', '535', '536', '538', '540', '541',
            '544', '545', '546', '547', '550', '552', '555', '556',
            '561', '562', '563', '565', '567', '580', '581', '583',
            '584', '585', '586', '590', '591', '592', '593', '594',
            '595', '596', '597', '598', '599')
        return notelist

    def physicaldescription(self):
        """
        Return all 300 fields in an array
        """
        return self.get_fields('300')

    def publisher(self):
        """
        Note: 264 field with second indicator '1' indicates publisher.
        """
        for f in self.get_fields('260', '264'):
            if self['260']:
                return self['260']['b']
            if self['264'] and f.indicator2 == '1':
                return self['264']['b']

        return None

    def pubyear(self):
        for f in self.get_fields('260', '264'):
            if self['260']:
                return self['260']['c']
            if self['264'] and f.indicator2 == '1':
                return self['264']['c']

        return None

def map_marc8_record(r):
    r.fields = map(map_marc8_field, r.fields)
    l = list(r.leader)
    l[9] = 'a' # see http://www.loc.gov/marc/specifications/speccharucs.html
    r.leader = "".join(l)
    return r
