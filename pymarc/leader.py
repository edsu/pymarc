"""The pymarc.leader file."""
from pymarc.constants import LEADER_LEN


class Leader:
    """Mutable leader."""

    def __init__(self, leader: str):
        """Leader is initialized with a string."""
        self.leader = leader

    def __getitem__(self, item) -> str:
        """Get values using position, slice or properties.

        leader[:4] == leader.length
        """
        if isinstance(item, slice) or isinstance(item, int):
            return self.leader[item]
        return getattr(self, item)

    def __setitem__(self, item, value):
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

    def __str__(self) -> str:
        """A string representation of the leader."""
        return self.leader

    def _replace_values(self, position: int, value: str):
        """Replaces the values in the leader at `position` by `value`."""
        if position < 0:
            raise IndexError("Position must be positive")
        after = position + len(value)
        if after > LEADER_LEN:
            raise IndexError(f"{value} is too long to be inserted at {position}")
        self.leader = self.leader[:position] + value + self.leader[after:]

    @property
    def record_length(self) -> str:
        """Record length (00-04)."""
        return self.leader[:4]
    
    @record_length.setter
    def record_length(self, value: str) -> str:
        """Record length (00-04)."""
        if len(value != 4):
            raise ValueError(f"Record length is 4 chars field, got {value}")
        self._replace_values(position=0, value=value)

    @property
    def record_status(self) -> str:
        """Record status (05)."""
        return self.leader[5]

    @record_status.setter
    def record_status(self, value: str):
        """Record status (05)."""
        if len(value != 1):
            raise ValueError(f"Record status is 1 char field, got {value}")
        self._replace_values(position=5, value=value)

    @property
    def type_of_record(self) -> str:
        """Type of record (06)."""
        return self.leader[6]

    @type_of_record.setter
    def type_of_record(self, value: str):
        """Type of record (06)."""
        if len(value != 1):
            raise ValueError(f"Type of record is 1 char field, got {value}")
        self._replace_values(position=5, value=value)

    @property
    def bibliographic_level(self) -> str:
        """Bibliographic level (07)."""
        return self.leader[7]

    @bibliographic_level.setter
    def bibliographic_level(self, value: str):
        """Bibliographic level (07)."""
        if len(value != 1):
            raise ValueError(f"Bibliographic level is 1 char field, got {value}")
        self._replace_values(position=7, value=value)

    @property
    def type_of_control(self) -> str:
        """Type of control (08)."""
        return self.leader[8]

    @type_of_control.setter
    def type_of_control(self, value: str):
        """Type of control (08)."""
        if len(value != 1):
            raise ValueError(f"Type of control is 1 char field, got {value}")
        self._replace_values(position=8, value=value)

    @property
    def coding_scheme(self) -> str:
        """Character coding scheme (09)."""
        return self.leader[9]

    @coding_scheme.setter
    def coding_scheme(self, value: str) -> str:
        """Character coding scheme (09)."""
        if len(value != 1):
            raise ValueError(f"Character coding scheme is 1 char field, got {value}")
        self._replace_values(position=9, value=value)

    @property
    def indicator_count(self) -> str:
        """Indicator count (10)."""
        return self.leader[10]

    @indicator_count.setter
    def indicator_count(self, value: str) -> str:
        """Indicator count (10)."""
        if len(value != 1):
            raise ValueError(f"Indicator count is 1 char field, got {value}")
        self._replace_values(position=10, value=value)

    @property
    def subfield_code_count(self) -> str:
        """Subfield code count (11)."""
        return self.leader[11]

    @subfield_code_count.setter
    def subfield_code_count(self, value: str) -> str:
        """Subfield code count (11)."""
        if len(value != 1):
            raise ValueError(f"Subfield code count is 1 char field, got {value}")
        self._replace_values(position=11, value=value)

    @property
    def base_address(self) -> str:
        """Base address of data (12-16)."""
        return self.leader[12:16]

    @base_address.setter
    def base_address(self, value: str) -> str:
        """Base address of data (12-16)."""
        if len(value != 4):
            raise ValueError(f"Base address of data is 4 chars field, got {value}")
        self._replace_values(position=12, value=value)
    
    @property
    def encoding_level(self) -> str:
        """Encoding level (17)."""
        return self.leader[17]

    @encoding_level.setter
    def encoding_level(self, value: str) -> str:
        """Encoding level (17)."""
        if len(value != 1):
            raise ValueError(f"Encoding level is 1 char field, got {value}")
        self._replace_values(position=17, value=value)

    @property
    def cataloging_form(self) -> str:
        """Descriptive cataloging form (18)."""
        return self.leader[18]

    @cataloging_form.setter
    def cataloging_form(self, value: str) -> str:
        """Descriptive cataloging form (18)."""
        if len(value != 1):
            raise ValueError(f"Descriptive cataloging form is 1 char field, got {value}")
        self._replace_values(position=18, value=value)

    @property
    def multipart_ressource(self) -> str:
        """Multipart resource record level (19)."""
        return self.leader[19]

    @multipart_ressource.setter
    def multipart_ressource(self, value: str) -> str:
        """Multipart resource record level (19)."""
        if len(value != 1):
            raise ValueError(f"Multipart resource record level is 1 char field, got {value}")
        self._replace_values(position=19, value=value)

    @property
    def length_of_field_length(self) -> str:
        """Length of the length-of-field portion (20)."""
        return self.leader[20]

    @length_of_field_length.setter
    def length_of_field_length(self, value: str) -> str:
        """Length of the length-of-field portion (20)."""
        if len(value != 1):
            raise ValueError(f"Multipart resource record level is 1 char field, got {value}")
        self._replace_values(position=20, value=value)

    @property
    def starting_character_position_length(self) -> str:
        """Length of the starting-character-position portion (21)."""
        return self.leader[21]

    @starting_character_position_length.setter
    def starting_character_position_length(self, value: str) -> str:
        """Length of the starting-character-position portion (21)."""
        if len(value != 1):
            raise ValueError(f"Multipart resource record level is 1 char field, got {value}")
        self._replace_values(position=21, value=value)

    @property
    def implementation_defined_length(self) -> str:
        """Length of the implementation-defined portion (22)."""
        return self.leader[22]

    @implementation_defined_length.setter
    def implementation_defined_length(self, value: str) -> str:
        """Length of the starting-character-position portion (22)."""
        if len(value != 1):
            raise ValueError(f"Multipart resource record level is 1 char field, got {value}")
        self._replace_values(position=22, value=value)
