# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

"""The pymarc.leader file."""
from pymarc.constants import LEADER_LEN
from pymarc.exceptions import BadLeaderValue, RecordLeaderInvalid


class Leader(object):
    """Mutable leader.

    A class to manipulate a `Record`'s leader.

    You can use the properties (`status`, `bibliographic_level`, etc.) or their
    slices/index equivalent (`leader[5]`, `leader[7]`, etc.) to read and write
    values.

    See `LoC's documentation
    <https://www.loc.gov/marc/bibliographic/bdleader.html>`_
    for more infos about those fields.

    .. code-block:: python

        leader = Leader("00475cas a2200169 i 4500")
        leader[0:4]  # returns "00475"
        leader.status  # returns "c"
        leader.status = "a"  # sets the status to "a"
        leader[5] # returns the status "a"
        leader[5] = "b" # sets the status to "b"
        str(leader)  # "00475bas a2200169 i 4500"

    Usually the leader is accessed through the `leader` property of a record.

    .. code-block:: python

        from pymarc import MARCReader
        with open('test/marc.dat', 'rb') as fh:
            reader = MARCReader(fh)
            for record in reader:
                print(record.leader)

    When creating/updating a `Record` please note that `record_length` and
    `base_address` will only be generated in the marc21 output of
    :func:`record.as_marc() <pymarc.record.Record.as_marc>`
    """

    def __init__(self, leader):
        # type: (str)
        """Leader is initialized with a string."""
        if len(leader) != LEADER_LEN:
            raise RecordLeaderInvalid
        self.leader = leader

    def __getitem__(self, item):
        # type: (str) -> str
        """Get values using position, slice or properties.

        leader[:4] == leader.length
        """
        if isinstance(item, slice) or isinstance(item, int):
            return self.leader[item]
        return getattr(self, item)

    def __setitem__(self, item, value):
        # type: (str, str) -> str
        """Set values using position, slice or properties.

        leader[5] = "a"
        leader[0:4] = "0000"
        leader.status = "a"
        """
        if isinstance(item, slice):
            self._replace_values(position=item.start, value=value)
        elif isinstance(item, int):
            self._replace_values(position=item, value=value)
        else:
            setattr(self, item, value)

    def __str__(self):
        # type: () -> str
        """A string representation of the leader."""
        return self.leader

    def _replace_values(self, position, value):
        # type: (int, str) -> str
        """Replaces the values in the leader at `position` by `value`."""
        if position < 0:
            raise IndexError("Position must be positive")
        after = position + len(value)
        if after > LEADER_LEN:
            raise BadLeaderValue(
                "%s is too long to be inserted at %d" % (value, position)
            )
        self.leader = self.leader[:position] + value + self.leader[after:]

    @property
    def record_length(self):
        # type: () -> str
        """Record length (00-04)."""
        return self.leader[:5]

    @record_length.setter
    def record_length(self, value):
        # type: (str) -> str
        """Record length (00-04)."""
        if len(value) != 5:
            raise BadLeaderValue("Record length is 4 chars field, got %s" % value)
        self._replace_values(position=0, value=value)

    @property
    def record_status(self):
        # type: () -> str
        """Record status (05)."""
        return self.leader[5]

    @record_status.setter
    def record_status(self, value):
        # type: (str) -> str
        """Record status (05)."""
        if len(value) != 1:
            raise BadLeaderValue("Record status is 1 char field, got %s" % value)
        self._replace_values(position=5, value=value)

    @property
    def type_of_record(self):
        # type: () -> str
        """Type of record (06)."""
        return self.leader[6]

    @type_of_record.setter
    def type_of_record(self, value):
        # type: (str) -> str
        """Type of record (06)."""
        if len(value) != 1:
            raise BadLeaderValue("Type of record is 1 char field, got %s" % value)
        self._replace_values(position=6, value=value)

    @property
    def bibliographic_level(self):
        # type: () -> str
        """Bibliographic level (07)."""
        return self.leader[7]

    @bibliographic_level.setter
    def bibliographic_level(self, value):
        # type: (str) -> str
        """Bibliographic level (07)."""
        if len(value) != 1:
            raise BadLeaderValue("Bibliographic level is 1 char field, got %s" % value)
        self._replace_values(position=7, value=value)

    @property
    def type_of_control(self):
        # type: () -> str
        """Type of control (08)."""
        return self.leader[8]

    @type_of_control.setter
    def type_of_control(self, value):
        # type: (str) -> str
        """Type of control (08)."""
        if len(value) != 1:
            raise BadLeaderValue("Type of control is 1 char field, got %s" % value)
        self._replace_values(position=8, value=value)

    @property
    def coding_scheme(self):
        # type: () -> str
        """Character coding scheme (09)."""
        return self.leader[9]

    @coding_scheme.setter
    def coding_scheme(self, value):
        # type: (str) -> str
        """Character coding scheme (09)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Character coding scheme is 1 char field, got %s" % value
            )
        self._replace_values(position=9, value=value)

    @property
    def indicator_count(self):
        # type: () -> str
        """Indicator count (10)."""
        return self.leader[10]

    @indicator_count.setter
    def indicator_count(self, value):
        # type: (str) -> str
        """Indicator count (10)."""
        if len(value) != 1:
            raise BadLeaderValue("Indicator count is 1 char field, got %s" % value)
        self._replace_values(position=10, value=value)

    @property
    def subfield_code_count(self):
        # type: () -> str
        """Subfield code count (11)."""
        return self.leader[11]

    @subfield_code_count.setter
    def subfield_code_count(self, value):
        # type: (str) -> str
        """Subfield code count (11)."""
        if len(value) != 1:
            raise BadLeaderValue("Subfield code count is 1 char field, got %s" % value)
        self._replace_values(position=11, value=value)

    @property
    def base_address(self):
        # type: () -> str
        """Base address of data (12-16)."""
        return self.leader[12:17]

    @base_address.setter
    def base_address(self, value):
        # type: (str) -> str
        """Base address of data (12-16)."""
        if len(value) != 5:
            raise BadLeaderValue(
                "Base address of data is 4 chars field, got %s" % value
            )
        self._replace_values(position=12, value=value)

    @property
    def encoding_level(self):
        # type: () -> str
        """Encoding level (17)."""
        return self.leader[17]

    @encoding_level.setter
    def encoding_level(self, value):
        # type: (str) -> str
        """Encoding level (17)."""
        if len(value) != 1:
            raise BadLeaderValue("Encoding level is 1 char field, got %s" % value)
        self._replace_values(position=17, value=value)

    @property
    def cataloging_form(self):
        # type: () -> str
        """Descriptive cataloging form (18)."""
        return self.leader[18]

    @cataloging_form.setter
    def cataloging_form(self, value):
        # type: (str) -> str
        """Descriptive cataloging form (18)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Descriptive cataloging form is 1 char field, got %s" % value
            )
        self._replace_values(position=18, value=value)

    @property
    def multipart_ressource(self):
        # type: () -> str
        """Multipart resource record level (19)."""
        return self.leader[19]

    @multipart_ressource.setter
    def multipart_ressource(self, value):
        # type: (str) -> str
        """Multipart resource record level (19)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Multipart resource record level is 1 char field, got %s" % value
            )
        self._replace_values(position=19, value=value)

    @property
    def length_of_field_length(self):
        # type: () -> str
        """Length of the length-of-field portion (20)."""
        return self.leader[20]

    @length_of_field_length.setter
    def length_of_field_length(self, value):
        # type: (str) -> str
        """Length of the length-of-field portion (20)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Length of the length-of-field portion is 1 char field, got %s" % value
            )
        self._replace_values(position=20, value=value)

    @property
    def starting_character_position_length(self):
        # type: () -> str
        """Length of the starting-character-position portion (21)."""
        return self.leader[21]

    @starting_character_position_length.setter
    def starting_character_position_length(self, value):
        # type: (str) -> str
        """Length of the starting-character-position portion (21)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Length of the starting-character-position portion is 1 char field, got %s"
                % value
            )
        self._replace_values(position=21, value=value)

    @property
    def implementation_defined_length(self):
        # type: () -> str
        """Length of the implementation-defined portion (22)."""
        return self.leader[22]

    @implementation_defined_length.setter
    def implementation_defined_length(self, value):
        # type: (str) -> str
        """Length of the starting-character-position portion (22)."""
        if len(value) != 1:
            raise BadLeaderValue(
                "Length of the implementation-defined portion is 1 char field, got %s"
                % value
            )
        self._replace_values(position=22, value=value)
