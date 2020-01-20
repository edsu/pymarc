# This file is part of pymarc. It is subject to the license terms in the
# LICENSE file found in the top-level directory of this distribution and at
# https://opensource.org/licenses/BSD-2-Clause. pymarc may be copied, modified,
# propagated, or distributed according to the terms contained in the LICENSE
# file.

"""Leader tests."""
import random
import string
import unittest

from pymarc.exceptions import BadLeaderValue, RecordLeaderInvalid
from pymarc.leader import Leader

LEADER = "00475casaa2200169 ib4500"

FIELDS = [
    ("record_length", slice(0, 5), "00475"),
    ("record_status", 5, "c"),
    ("type_of_record", 6, "a"),
    ("bibliographic_level", 7, "s"),
    ("type_of_control", 8, "a"),
    ("coding_scheme", 9, "a"),
    ("indicator_count", 10, "2"),
    ("subfield_code_count", 11, "2"),
    ("base_address", slice(12, 17), "00169"),
    ("encoding_level", 17, " "),
    ("cataloging_form", 18, "i"),
    ("multipart_ressource", 19, "b"),
    ("length_of_field_length", 20, "4"),
    ("starting_character_position_length", 21, "5"),
    ("implementation_defined_length", 22, "0"),
]


def random_string(length):
    """Random string to fill a field."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class LeaderTest(unittest.TestCase):
    """LeaderTest."""

    def test_leader_invalid_length(self):
        self.assertRaises(RecordLeaderInvalid, Leader, LEADER[:-1])

    def test_leader_value(self):
        leader = Leader(LEADER)
        self.assertEqual(leader.leader, LEADER)

    def test_str(self):
        leader = Leader(LEADER)
        self.assertEqual(str(leader), LEADER)

    def test_add(self):
        leader = Leader(LEADER)
        new_leader = leader[0:9] + "b" + leader[10:]
        self.assertEqual(new_leader, "00475casab2200169 ib4500")

    def test_getters(self):
        leader = Leader(LEADER)
        for field, index, expected in FIELDS:
            self.assertEqual(getattr(leader, field), leader[index])
            self.assertEqual(expected, leader[index])

    def test_setters(self):
        leader = Leader(LEADER)
        for field, index, expected in FIELDS:
            value = random_string(len(expected))
            leader[index] = value
            self.assertEqual(getattr(leader, field), value)
            value = random_string(len(expected))
            setattr(leader, field, value)
            self.assertEqual(leader[index], value)

    def test_setters_errors(self):
        leader = Leader(LEADER)
        for field, index, expected in FIELDS:
            value = random_string(len(expected) + 1)
            with self.assertRaises(BadLeaderValue):
                setattr(leader, field, value)


def suite():
    test_suite = unittest.makeSuite(LeaderTest, "test")
    return test_suite


if __name__ == "__main__":
    unittest.main()
