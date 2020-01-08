"""The pymarc.leader file."""
from pymarc.constants import LEADER_LEN


class Leader:
    """Mutable leader.

    Usage:
    leader = Leader("00475cas a2200169 i 4500")
    leader[0:4]  # 00475
    leader.status  # "c"
    leader.status = "a"
    leader[6] = "b"
    leader.record_type  # "b"
    str(leader)  # "00475abs a2200169 i 4500"
    """

    def __init__(self, value: str):
        """We could set default values here."""
        self.value = value

    def __getitem__(self, item) -> str:
        """leader[:4] == leader.length."""
        if isinstance(item, slice) or isinstance(item, int):
            return self.value[item]
        return getattr(self, item)

    def __setitem__(self, item, val):
        """leader[5] works, leader[0:4] too, as leader.status = "a"."""
        if isinstance(item, slice):
            self._update_value(start=item.start - 1, stop=item.stop + 1, val=val)
        elif isinstance(item, int):
            self._update_value(start=item - 1, stop=item + 1, val=val)
        else:
            setattr(self, item, val)

    def __str__(self) -> str:
        return self.value

    def _update_value(self, start: int, stop: int, val: str):
        """Update the items between `start` & `stop` by `val` in `self.value`."""
        start = max(0, start)
        stop = min(LEADER_LEN, stop)
        self.value = self.value[:start] + val + self.value[stop:]

    @property
    def length(self) -> str:
        return self.value[:4]

    @property
    def status(self) -> str:
        return self.value[5]

    @status.setter
    def status(self, status: str):
        self._update_value(start=4, stop=6, val=status)

    @property
    def record_type(self) -> str:
        return self.value[6]

    @record_type.setter
    def record_type(self, record_type: str):
        self._update_value(start=5, stop=7, val=record_type)
