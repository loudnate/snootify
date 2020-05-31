from enum import IntEnum
from typing import Optional


class SessionStatus(IntEnum):
    AWAKE = 1
    ASLEEP = 2
    SOOTHING = 3

    @classmethod
    def from_str(cls, s: str) -> Optional:
        s = s.lower()
        if s == 'awake' or s == '1':
            return cls.AWAKE
        if s == 'asleep' or s == '2':
            return cls.ASLEEP
        if s == 'soothing' or s == '3':
            return cls.SOOTHING
        return None

    def __str__(self):
        if self == self.AWAKE:
            return "Awake"
        elif self == self.ASLEEP:
            return "Asleep"
        elif self == self.SOOTHING:
            return "Soothing"
        return super.__str__()
