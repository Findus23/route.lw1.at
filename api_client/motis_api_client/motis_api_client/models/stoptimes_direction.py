from enum import Enum


class StoptimesDirection(str, Enum):
    EARLIER = "EARLIER"
    LATER = "LATER"

    def __str__(self) -> str:
        return str(self.value)
