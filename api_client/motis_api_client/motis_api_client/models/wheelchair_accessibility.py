from enum import Enum


class WheelchairAccessibility(str, Enum):
    ACCESSIBLE = "ACCESSIBLE"
    NOT_ACCESSIBLE = "NOT_ACCESSIBLE"

    def __str__(self) -> str:
        return str(self.value)
